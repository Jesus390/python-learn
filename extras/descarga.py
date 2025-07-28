import requests

class Descarga:
    def descargar(self, url:str) -> str:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException as e:
            raise(f"ErrorDescarga: {e}")

if __name__ == "__main__":
    url = "https://www.example.com"
    descarga = Descarga()
    texto = descarga.descargar(url)
    print(texto)
