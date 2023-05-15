"""Parsing script for lamoda pages."""
from bs4 import BeautifulSoup
from requests import get


def parse_page(url):
    """Parsing function, gets url and returns founded clothes from web-page."""
    # https://www.lamoda.by/c/477/clothes-muzhskaya-odezhda/
    request = get(url, timeout=10)
    soup = BeautifulSoup(request.text, "html.parser")
    clothes_response_dict = {}
    clothes = soup.find_all("a", class_="x-product-card__link x-product-card__hit-area")
    for item in clothes:
        info_dict = {}
        item_link = "https://lamoda.by" + item["href"]
        info_dict["brand"] = item.find(
            "div", class_="x-product-card-description__brand-name"
        ).text
        info_dict["name"] = item.find(
            "div", class_="x-product-card-description__product-name"
        ).text
        item_old_price = item.find(
            "span", class_="x-product-card-description__price-old"
        )
        item_new_price = item.find(
            "span", class_="x-product-card-description__price-new"
        )
        item_single_price = item.find(
            "span", class_="x-product-card-description__price-single"
        )
        if item_old_price:
            info_dict["old_price"] = float(item_old_price.text.replace(" ", ""))
            info_dict["price"] = float(item_new_price.text[:-3].replace(" ", ""))
        elif item_single_price:
            info_dict["price"] = float(item_single_price.text[:-3].replace(" ", ""))
        clothes_response_dict[item_link] = info_dict
    return clothes_response_dict
