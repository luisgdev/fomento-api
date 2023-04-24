""" Scraper module """

from datetime import date, datetime
from typing import Optional

import requests
import validators
from bs4 import BeautifulSoup
from requests import Response

from app.scraper.constants import (
    ALL_MONTHS_TABLE_ID,
    BASE_URL,
    HTML_PARSER,
    HTTP_ERROR,
    INVALID_URL,
    UF_DATE_RANGE_MSG,
    UF_YEAR_LIMIT,
)


class ScraperException(Exception):
    """
    Specific exception for scraper module.
    """


def _format_date(date_: str) -> date:
    """
    Validate date input and return a `date` object.
    :param date_: Given date (str).
    :return: Date object (datetime.date)
    :raises ValueError: If date is out of range or is not ISO format.
    """
    result = date.fromisoformat(date_)
    today = datetime.now()
    if result.year in range(UF_YEAR_LIMIT, today.year + 1):
        return result
    raise ValueError(UF_DATE_RANGE_MSG.format(this_year=today.year))


def _get_webpage(year: int) -> str:
    """
    Returns the web page for a given year.
    \f
    :param year: Year as YYYY (int).
    :return: Webpage HTML content (str).
    :raises ScraperException: If status code is not OK.
    """
    url: str = BASE_URL.format(year=year)
    if not validators.url(value=url):
        raise ScraperException(INVALID_URL)
    res: Response = requests.get(url=url, timeout=30)
    if res.status_code == 200:
        return res.text
    raise ScraperException(HTTP_ERROR.format(code=res.status_code, reason=res.reason))


def get_uf(iso_date: str, html_page: Optional[str] = None) -> str:
    """
    Returns the UF value for a given date.
    \f
    :param html_page: HTMl content of the source, for testing (str).
    :param iso_date: Date in ISO format (str).
    :return: UF value (str).
    """
    date_: date = _format_date(date_=iso_date)
    web_content = html_page if html_page else _get_webpage(year=date_.year)
    soup = BeautifulSoup(web_content, HTML_PARSER)
    # Find the "all months" table by its id.
    table = soup.find(id=ALL_MONTHS_TABLE_ID)
    # Let's extract the rows from the `tbody`.
    rows = tuple(row for row in table.tbody)
    # Remove jump lines and parse values by index.
    months = tuple(filter(lambda x: x != "\n", rows))[date_.day - 1]
    value = tuple(filter(lambda x: x != "\n", months))[date_.month]
    return value.text


if __name__ == "__main__":
    pass
