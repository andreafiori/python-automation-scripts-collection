import csv
import requests

from pathlib import Path
from bs4 import BeautifulSoup

"""
Real Python's Fake Jobs Scraper
"""
class FakeJobsScraper:

    def __init__(self):
        self.data_dir = Path("data")
        self.data_file = self.data_dir / "postings.csv"
        self.posting_container_class = "column is-half"
        self.posting_title_class = "title is-5"
        self.posting_company_class = "subtitle is-6 company"
        self.posting_location_class = "location"
        self.posting_href_start = "https://realpython.github.io/fake-jobs/"

    def save_to_csv(self, postings):
        """Saves list of dicts to a CSV file."""
        self.data_dir.mkdir(parents=True, exist_ok=True)

        try:
            with open(self.data_file, mode="w", newline="") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["title", "company", "location", "url"]
                )

                writer.writeheader()

                for posting in postings:
                    writer.writerow(
                        {
                            "title": posting.get("title", ""),
                            "company": posting.get("company", ""),
                            "location": posting.get("location", ""),
                            "url": posting.get("url", ""),
                        }
                    )
                return True
        except Exception as e:
            # print(f"# Error: {e}")
            return False

    def fetch_page(self):
        """Fetches and returns the webpage as a string."""
        url = self.posting_href_start

        try:
            response = requests.get(url)

            if response.status_code == 200:
                return response.text
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # print(f"# Error: {e}")
            return None

    def extract_job_postings(self, response):
        """Scrapes data from webpage and returns list of dicts."""
        soup = BeautifulSoup(response, "html.parser")
        postings = []
        posting_boxes = soup.find_all("div", class_=self.posting_container_class)
        for box in posting_boxes:
            box_title = box.find("h2", class_=self.posting_title_class)
            box_company = box.find("h3", class_=self.posting_company_class)
            box_location = box.find("p", class_=self.posting_location_class)
            box_link = box.find(
                "a",
                href=(lambda h: h and h.startswith(self.posting_href_start),),
            )

            posting = {
                "title": box_title.get_text(strip=True) if box_title else "N/A",
                "company": box_company.get_text(strip=True) if box_company else "N/A",
                "location": box_location.get_text(strip=True) if box_location else "N/A",
                "url": box_link.get("href") if box_link else "N/A",
            }
            postings.append(posting)
        return postings