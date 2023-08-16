import requests
from bs4 import BeautifulSoup
import os


def getFiles(url) -> bool:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    linhas_impar = soup.find_all("tr", class_="linhaimpar")

    if not os.path.exists("tmp"):
        os.mkdir("tmp")

    for linha in linhas_impar:
        if not "Baixar" in linha.text:
            continue

        link = linha.find("a")["href"]

        pdf_url = f"https://diario.jt.jus.br/cadernos/{link}"
        file_name = os.path.join("tmp", link.split("/")[-1])

        with requests.get(pdf_url, stream=True) as pdf_response:
            pdf_response.raise_for_status()

            with open(file_name, "wb") as pdf_file:
                for chunk in pdf_response.iter_content(chunk_size=8192):
                    pdf_file.write(chunk)

        print(f"Download concluído: {file_name}")

    return True
