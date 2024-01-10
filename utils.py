import os
import json
import requests
from bs4 import BeautifulSoup 
from constants import BASE_URL, HEADERS, JSON_FILE_PATH

def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, "html.parser")

def scrape_page(url, headers):
    soup = get_soup(url, headers)
    items = soup.find_all("div", class_="bx_catalog_item gtm-impression-product")
    
    results = []
    for item in items:
        name = item.find("h4", class_="bx_catalog_item_title_text").text
        articul = item.find("div", class_="bx_catalog_item_scu_code").get("text", "")
        try:
            price = item.find("span", class_="current_price").contents[0][:-2].replace(" ", "")
        except AttributeError:
            price = "Out of stock"
        memory_size = name.split(", ")[1].replace(" ", "")[:-2] + " Гб"
        
        smartphone = {
            "name": name, 
            "articul": articul, 
            "price": price, 
            "memory-size": memory_size
        }
        
        if price != "Out of stock":
            results.append(smartphone)

    return results

def scrape_smartphones(base_url, headers):
    soup = get_soup(base_url, headers)
    page_last = int(soup.find("div", class_="bx-pagination-container row").find_all("li")[-2].find("span").text)

    smartphones = []
    for i in range(1, page_last + 1):
        url = f"{base_url}/?PAGEN_1={i}"
        smartphones.extend(scrape_page(url, headers))

    return smartphones


def get_smartphones():

    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        smartphones_data = scrape_smartphones(BASE_URL, HEADERS)
        with open(JSON_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(smartphones_data, f, ensure_ascii=False)
        return smartphones_data