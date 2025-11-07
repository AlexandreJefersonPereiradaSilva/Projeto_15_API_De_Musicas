import requests
from datetime import datetime
import textwrap



def buscar_artista(nome_artista):

    url = f"https://www.theaudiodb.com/api/v1/json/2/search.php?s={nome_artista}"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()  
        dados = resposta.json()

      
        if dados["artists"] is None:
            return None
        else:
            return dados["artists"][0]
    except requests.exceptions.RequestException as erro:
        print(f"\n  Houve um erro com a conexão com a API: {erro}")
        return None

def exibir_informacoes(artista):

    nome = artista.get("strArtist", "Não disponível!")
    genero = artista.get("strGenre", "Não disponível!")
    pais = artista.get("strCountry", "Não disponível!")
    inicio = artista.get("intFormedYear", "Não disponível!")
    bio_pt = artista.get("strBiographyPT") or "Biografia em português está disponível!"
    site = artista.get("strWebsite") or "Nenhum site disponível!"
    estilo = artista.get("strStyle") or "Não informado!"
    data_consulta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("\n informações do artista ")
    print("=" * 60)
    print(f"Nome: {nome}")
    print(f"Estilo: {estilo}")
    print(f"Gênero: {genero}")
    print(f"País: {pais}")
    print(f"Início da carreira: {inicio}")
    print(f"Site: {site}")
    print(f" Consulta realizada em: {data_consulta}")
    print("-" * 30)

    print(" Biografia:")
    print(textwrap.fill(bio_pt, width=80))
    print("=" * 60)




print("PyTune - Buscar Músicas com API!")
print("=" * 50)
print("Pesquise informações sobre qualquer artista musical!")
print("Exemplo: Queen, Michael Jackson, Anitta, Coldplay...")
print("=" * 60)

