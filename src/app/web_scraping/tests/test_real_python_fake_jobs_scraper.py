from scraping.fake_jobs_scraper import RealPythonFakeJobsScraper

# Write a test for the RealPythonFakeJobsScraper class based on the commented main below
def test_real_python_fake_jobs_scraper():
    scraper = RealPythonFakeJobsScraper()

    response = scraper.fetch_page()

    if not response:
        assert False, "# Failed to fetch the page. Try Again"

    postings = scraper.extract_job_postings(response)

    if len(postings) == 0:
        assert False, "# No data scraped"

    result = scraper.save_to_csv(postings)

    if result:
        assert True
    else:
        assert False, "# Something went wrong. Try again"

# def main():
#     scraper = FakeJobsScraper()

#     response = scraper.fetch_page()

#     if not response:
#         print("# Failed to fetch the page. Try Again")
#         return

#     postings = scraper.extract_job_postings(response)

#     if len(postings) == 0:
#         print("# No data scraped")
#         return

#     result = scraper.save_to_csv(postings)

#     if result:
#         print(f"# Successfully saved to: {scraper.data_file}")
#     else:
#         print("# Something went wrong. Try again")
