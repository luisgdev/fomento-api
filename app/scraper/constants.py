""" Constants for scraper module """

BASE_URL: str = "https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"
UF_YEAR_LIMIT: int = 2013
UF_DATE_RANGE_MSG: str = "UF values are available between 2013 and {this_year}"

INVALID_URL: str = "URL is not valid."
HTTP_ERROR: str = "HTTP Error: {code} - {reason}."

# Bs4 parser
HTML_PARSER: str = "html.parser"
ALL_MONTHS_TABLE_ID: str = "table_export"
