from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

base_url = "https://shopee.com.br/api/v4/pages/get_category_tree"
requisicao = Request(base_url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
# variável original: requisicao = Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})

url = urlopen(requisicao)
bs = BeautifulSoup(url, 'html.parser')
bs_json = json.loads("".join(bs.contents))

print(bs_json)