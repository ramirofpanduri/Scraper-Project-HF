import httpx
from bs4 import BeautifulSoup

url = "https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"

}


def main():
    response = httpx.get(url, headers=headers)
    print(response.text)
    response_html = response.text

    soup = BeautifulSoup(response_html, "html.parser")


if __name__ == "__main__":
    main()
