""" Tests constants module """

import os

# Assets directory
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# Assets for testing purposes
CONTENT_ON_WEBPAGE: str = os.path.join(ASSETS_DIR, "uf_2020.html")
CONTENT_NOT_AVAILABLE: str = os.path.join(ASSETS_DIR, "no_content.html")
