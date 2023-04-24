""" Test utils module """


def get_asset(filename: str) -> str:
    """
    Get webpage sample for tests.
    :param filename: File name (str).
    :return: Webpage content (str).
    """
    content: str
    with open(filename, "r", encoding="utf-8") as _file:
        content = _file.read()
    return content
