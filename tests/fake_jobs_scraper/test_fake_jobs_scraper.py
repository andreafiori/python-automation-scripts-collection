import pytest
import csv
import requests

from app.fake_jobs_scraper.fake_jobs_scraper import FakeJobsScraper
from unittest.mock import Mock, patch
from pathlib import Path

class TestFakeJobsScraper:
    """Unit tests for FakeJobsScraper class."""

    @pytest.fixture
    def scraper(self):
        return FakeJobsScraper()

    @pytest.fixture
    def sample_html(self):
        return """
        <div class="column is-half">
            <h2 class="title is-5"><a href="https://realpython.github.io/fake-jobs/1.html">Senior Python Developer</a></h2>
            <h3 class="subtitle is-6 company">Tech Corp</h3>
            <p class="location">New York, NY</p>
        </div>
        <div class="column is-half">
            <h2 class="title is-5"><a href="https://realpython.github.io/fake-jobs/2.html">Data Scientist</a></h2>
            <h3 class="subtitle is-6 company">Data Inc</h3>
            <p class="location">London, UK</p>
        </div>
        """

    def test_init_attributes(self, scraper):
        """Test that scraper initializes with correct default attributes."""
        assert scraper.data_dir == Path("data")
        assert scraper.data_file == Path("data") / "postings.csv"
        assert scraper.posting_container_class == "column is-half"
        assert scraper.posting_href_start == "https://realpython.github.io/fake-jobs/"

    def test_save_to_csv_success(self, scraper, tmp_path):
        """Test successful CSV saving."""
        scraper.data_file = tmp_path / "postings.csv"

        postings = [
            {"title": "Test Job", "company": "Test Corp", "location": "Test City", "url": "test-url"}
        ]

        result = scraper.save_to_csv(postings)
        assert result is True

        # Verify CSV was created and contains expected data
        with open(tmp_path / "postings.csv", "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            assert len(rows) == 1
            assert rows[0]["title"] == "Test Job"

    # TODO fix test: mocker fixture not defined
    # def test_save_to_csv_failure(self, scraper, mocker):
    #     """Test CSV saving handles write errors gracefully."""
    #     mocker.patch("builtins.open", side_effect=IOError("Write failed"))

    #     postings = [{"title": "Test Job"}]
    #     result = scraper.save_to_csv(postings)
    #     assert result is False

    @patch("requests.get")
    def test_fetch_page_success(self, mock_get, scraper):
        """Test successful page fetch."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "html content"
        mock_get.return_value = mock_response

        result = scraper.fetch_page()
        assert result == "html content"
        mock_get.assert_called_once_with(scraper.posting_href_start)

    @patch("requests.get")
    def test_fetch_page_failure(self, mock_get, scraper):
        """Test page fetch handles HTTP errors."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        result = scraper.fetch_page()
        assert result is None  # Just verify return value
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_fetch_page_request_exception(self, mock_get, scraper):
        """Test page fetch handles request exceptions."""
        mock_get.side_effect = requests.exceptions.RequestException("Connection failed")

        result = scraper.fetch_page()
        assert result is None

    def test_extract_job_postings_valid_html(self, scraper, sample_html):
        """Test extraction from valid HTML with complete job postings."""
        postings = scraper.extract_job_postings(sample_html)

        assert len(postings) == 2
        assert postings[0]["title"] == "Senior Python Developer"
        assert postings[0]["company"] == "Tech Corp"
        assert postings[0]["location"] == "New York, NY"
        assert postings[0]["url"] == "https://realpython.github.io/fake-jobs/1.html"

        assert postings[1]["title"] == "Data Scientist"
        assert postings[1]["company"] == "Data Inc"
        assert postings[1]["location"] == "London, UK"

    def test_extract_job_postings_missing_elements(self, scraper):
        """Test extraction handles missing HTML elements gracefully."""
        html = """
        <div class="column is-half">
            <h2 class="title is-5">Only Title</h2>
        </div>
        """

        postings = scraper.extract_job_postings(html)
        assert len(postings) == 1
        assert postings[0]["title"] == "Only Title"
        assert postings[0]["company"] == "N/A"
        assert postings[0]["location"] == "N/A"
        assert postings[0]["url"] == "N/A"

    def test_extract_job_postings_no_postings(self, scraper):
        """Test extraction returns empty list when no postings found."""
        html = "<html><body>No job postings here</body></html>"
        postings = scraper.extract_job_postings(html)
        assert postings == []

    def test_extract_job_postings_invalid_href(self, scraper):
        """Test extraction handles links that don't match href pattern."""
        html = """
        <div class="column is-half">
            <h2 class="title is-5"><a href="invalid-url">Test Job</a></h2>
            <h3 class="subtitle is-6 company">Test Corp</h3>
            <p class="location">Test City</p>
        </div>
        """

        postings = scraper.extract_job_postings(html)
        assert postings[0]["url"] == "N/A"
