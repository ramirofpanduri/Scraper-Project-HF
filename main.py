import httpx
from bs4 import BeautifulSoup

url = "https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"

}


def extract_product_data(product):
    try:
        name = product.find("span", class_="productdescriptionname").text
        brand = product.find("span", class_="productdescriptionbrand").text
        price = product.find(
            "span", class_="CurrencySizeLarge curprice").text.strip()
        print(f"brand: {brand} Name: {name} Price: {price}")
    except Exception as e:
        print(e)


def main():
    response = httpx.get(url, headers=headers)
    print(response.text)
    response_html = response.text

    soup = BeautifulSoup(response_html, "html.parser")
    products = soup.find_all("div", class_="s-productthumbbox")
    for product in products:
        extract_product_data(product)


if __name__ == "__main__":
    main()
