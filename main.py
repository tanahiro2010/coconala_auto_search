import requests
from bs4 import BeautifulSoup

def main():
    url = "https://coconala.com/requests?recruiting=true"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })

    if not response.ok:
        raise requests.exceptions.ConnectionError
    try:
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        raise e

    demand_card_elements = soup.select(".c-searchItemWrapper.c-searchItemWrapper-hoverShadow")
    if not demand_card_elements:
        raise ValueError("Could not find the demands card element.")

    for demand_card in demand_card_elements:
        link_element = demand_card.select_one("a.c-searchItem_detailLink")
        if not link_element:
            continue
        link = link_element.get("href")
        info_box = demand_card.select_one(".c-itemInfo")
        if not info_box:
            continue




    return

if __name__ == "__main__":
    main()