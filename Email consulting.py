import requests
from bs4 import BeautifulSoup

def search_illicit_services(email):
    url = f"https://search.illicit.services/records?emails={email}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Realize o scraping dos resultados conforme necessário
    # Neste exemplo, estamos apenas pegando o conteúdo da página
    results = str(soup)
    
    return results

def save_results_to_file(results, filename):
    with open(filename, 'w') as file:
        file.write(results)
    
    print(f"Os resultados foram salvos no arquivo {filename}.")

# Exemplo de uso
email = input("Digite o endereço de e-mail: ")
filename = "resultados.txt"

search_results = search_illicit_services(email)
save_results_to_file(search_results, filename)
