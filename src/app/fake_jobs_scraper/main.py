from app.fake_jobs_scraper.fake_jobs_scraper import FakeJobsScraper

def main():
    scraper = FakeJobsScraper()

    response = scraper.fetch_page()

    if not response:
        print("# Failed to fetch the page. Try Again")
        return

    postings = scraper.extract_job_postings(response)

    if len(postings) == 0:
        print("# No data scraped")
        return

    result = scraper.save_to_csv(postings)

    if result:
        print(f"# Successfully saved to: {scraper.data_file}")
    else:
        print("# Something went wrong. Try again")

# if __name__ == "__main__":
#     main()