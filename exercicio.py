from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

base_url = "https://shopee.com.br"
requisicao = Request(base_url + "/api/v4/pages/get_category_tree", headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
# variável original: requisicao = Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})

url = urlopen(requisicao)
bs = BeautifulSoup(url, 'html.parser')
bs_json = json.loads("".join(bs.contents))

for categoria in bs_json["data"]["category_list"]:
       nome_categoria = categoria["display_name"]
       id_cat = categoria["catid"]
       
       endpoint = f'{base_url}/{nome_categoria.replace(" ", "-")}-cat.{id_cat}'
       print(endpoint)
       indexador = Request(endpoint)
       url = urlopen(indexador)
       print(url)
    
# https://shopee.com.br/Fragr%C3%A2ncia-da-Casa-e-Aromaterapia-cat.11060114
