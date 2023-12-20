from urllib import request, parse
from bs4 import BeautifulSoup
import json


base_url = "https://shopee.com.br"
requisicao = request.Request(base_url + "/api/v4/pages/get_category_tree", headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
# variável original: requisicao = request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})

url = request.urlopen(requisicao)
bs = BeautifulSoup(url, 'html.parser')
bs_json = json.loads("".join(bs.contents))
#print(bs_json)
#print(type(bs_json))

def normalizar_url(url):
    parsed_url = parse.urlparse(url)
    
    # Obter o caminho da URL
    path = parsed_url.path

    # Codificar o caminho para lidar com caracteres especiais
    path_encoded = parse.quote(path, safe='')

    # Recriar a URL com o caminho codificado
    normalized_url = f"{parsed_url.scheme}{parsed_url.netloc}{path_encoded}"

    return normalized_url

for categoria in bs_json["data"]["category_list"]:
       nome_categoria = categoria["display_name"]
       id_cat = categoria["catid"]
       endpoint = f'{base_url}/{nome_categoria.replace(" ", "-")}-cat.{id_cat}'#.encode('UTF-8')
       try:
       #print(type(endpoint))
              indexador = request.Request(endpoint)
              url = request.urlopen(indexador)
              #print(endpoint)
       except:
              nome_categoria = normalizar_url(nome_categoria)
              endpoint = f'{base_url}/{nome_categoria.replace(" ", "-")}-cat.{id_cat}'#.encode('UTF-8')
              #print(endpoint)
              try:
                     indexador = request.Request(endpoint)
                     url = request.urlopen(indexador)
                     bs = BeautifulSoup(url, 'html.parser')
                     print(bs)
              except:
                     print(endpoint)
    
# https://shopee.com.br/Fragr%C3%A2ncia-da-Casa-e-Aromaterapia-cat.11060114
