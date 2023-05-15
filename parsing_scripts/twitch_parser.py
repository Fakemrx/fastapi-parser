"""Parsing script for twitch pages."""
from bs4 import BeautifulSoup
from requests import get


def parse_page():
    """Parsing function, gets url and returns founded streams from web-page."""
    url = "https://www.twitch.tv/"
    request = get(url, timeout=10)
    soup = BeautifulSoup(request.text, "html.parser")
    print(soup)
    streams_response_dict = {}
    return streams_response_dict


parse_page()
