from cgitb import text
from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.manulifeim.com.my/funds/quick-daily-price-list.html').text
soup = BeautifulSoup(html_text, 'lxml')
fund_detail = soup.find(
    'div', class_='/funds/quick-daily-price-list/_jcr_content/root/responsivegrid_641029165/responsivegrid/funds_listing_780824366.funds.featured.html')
print(fund_detail)
