from dotenv import load_dotenv
import os
import httpx
from bs4 import BeautifulSoup
import mysql.connector

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")

conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

cursor = conn.cursor()

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
        guardar_producto(brand, name, price)
    except Exception as e:
        print(e)


def guardar_producto(brand, name, price):
    sql = "INSERT INTO products (brand, name, price) VALUES (%s, %s, %s)"
    val = (brand, name, price)
    cursor.execute(sql, val)
    conn.commit()


def main():
    response = httpx.get(url, headers=headers)
    response_html = response.text

    soup = BeautifulSoup(response_html, "html.parser")
    products = soup.find_all("div", class_="s-productthumbbox")
    for product in products:
        extract_product_data(product)


if __name__ == "__main__":
    main()


cursor.close()
conn.close()
