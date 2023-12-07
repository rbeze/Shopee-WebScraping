# from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup

base_url = "https://shopee.com.br/api/v4/pages/get_category_tree"
requisicao = requests.get(base_url, headers={'User-Agent': 'Mozilla/5.0'})
# requisicao = Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
# url = urlopen(requisicao)
# bs = BeautifulSoup(url, 'json.parser')

print(requisicao)