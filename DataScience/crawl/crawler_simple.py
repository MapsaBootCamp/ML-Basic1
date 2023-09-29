import requests
from bs4 import BeautifulSoup

url = "https://bootcamp.mapsahr.com/bootcamps/"
headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

r = requests.get(url, headers=headers)
bs = BeautifulSoup(r.content, "html.parser")

camps_data = bs.find_all(
    "div", class_="jet-listing-grid__item")

# print(len(camps_data))
# print(camps_data[0].find(
#     "a", class_="jet-listing-dynamic-link__link").span.get_text())

for item in camps_data:
    # item.find("span").get_text().strip()
    # elementor-widget-container
    print(item.find(
        "a", class_="jet-listing-dynamic-link__link").span.get_text())
    print(item.find("div", class_="jet-listing-dynamic-field__content").get_text())
