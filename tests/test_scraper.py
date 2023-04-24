""" Tests for scraper module """

import pytest
from utils import get_asset
from utils.constants import CONTENT_NOT_AVAILABLE, CONTENT_ON_WEBPAGE

from app import scraper


@pytest.mark.parametrize(
    ("iso_date", "result"),
    (
        # Valid dates returning successful values.
        ("2020-01-01", "28.310,86"),
        ("2020-02-01", "28.339,17"),
        ("2020-03-01", "28.469,54"),
        ("2020-04-01", "28.601,15"),
        ("2020-05-01", "28.693,59"),
        ("2020-06-01", "28.716,52"),
        ("2020-07-01", "28.695,46"),
        ("2020-08-01", "28.666,51"),
        ("2020-09-01", "28.680,37"),
        ("2020-10-01", "28.708,80"),
    ),
)
def test_get_uf_success(iso_date: str, result: str) -> None:
    """
    Test scraper.get_uf function works successfully.
    :param iso_date: Date in ISO format (str).
    :param result: UF value (str).
    :return: None
    """
    assert (
        scraper.get_uf(iso_date=iso_date, html_page=get_asset(CONTENT_ON_WEBPAGE))
        == result
    )


@pytest.mark.parametrize(
    ("iso_date", "exception", "content"),
    (
        # Wrong date format raises ValueError.
        ("220-01-01", ValueError, CONTENT_ON_WEBPAGE),
        ("2020-01-00", ValueError, CONTENT_ON_WEBPAGE),
        ("2020-02-30", ValueError, CONTENT_ON_WEBPAGE),
        ("2020-15-01", ValueError, CONTENT_ON_WEBPAGE),
        # Also If year is older than 2013 or greater than present year.
        ("2012-12-12", ValueError, CONTENT_ON_WEBPAGE),
        ("2042-12-12", ValueError, CONTENT_ON_WEBPAGE),
        # If the website, for some reason, doesn't show the desired info,
        # then the parser will raise an AttributeError.
        ("2020-01-01", AttributeError, CONTENT_NOT_AVAILABLE),
        ("2020-10-10", AttributeError, CONTENT_NOT_AVAILABLE),
        ("2020-11-11", AttributeError, CONTENT_NOT_AVAILABLE),
        ("2020-12-12", AttributeError, CONTENT_NOT_AVAILABLE),
    ),
)
def test_get_uf_fails(iso_date: str, exception: Exception, content: str) -> None:
    """
    Test scraper.get_uf function raises exceptions.
    :param iso_date: Date in ISO format (str).
    :param exception: Expected exception (Exception).
    :return: None
    """
    with pytest.raises(exception):
        assert scraper.get_uf(iso_date=iso_date, html_page=get_asset(content))
