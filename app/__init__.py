""" Main module """

from fastapi import FastAPI

from app import scraper

app = FastAPI()

# pylint: disable=broad-exception-caught


@app.get("/")
def index() -> dict:
    """
    Index route.
    :return: Response (dict).
    """
    return {"message": "Check documentation here -> /docs"}


@app.get("/uf/{date}")
def get_uf(date: str) -> dict:
    """
    Get value for a given date
    :param date: Given date (str).
    :return: Response, uf value or error details (dict).
    """
    try:
        value: str = scraper.get_uf(iso_date=date)
        return {"value": value}
    except AttributeError:
        return {"error": "Content was not found."}
    except (ValueError, Exception) as ex:
        return {"error": ex.args}
