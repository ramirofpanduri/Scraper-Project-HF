# House Of Fraser Scraper

Scraper made to extract product data from House of Fraser.

## Description

This scraper uses BeautifulSoup and httpx to extract the price, brand, and name of the products from the clothing shop "House of Fraser" and saves them into a MySQL table called `products`.

## Installation

It is necessary to create a virtual environment for the scraper to work. Pipenv was used, so it is highly recommended.

```bash
# Clone the repository
git clone https://github.com/user/Scraper-Project-HF.git
cd Scraper-Project-HF

# Install dependencies using Pipenv
pipenv install

# Activate the virtual environment
pipenv shell
