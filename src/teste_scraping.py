import requests

url = "https://remoteok.com/api"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
print(f"Status: {response.status_code}\n")

dados = response.json()
print(f"Total de itens recebidos: {len(dados)}\n")

print("--- Item 0 (aviso legal, nao e vaga) ---")
print(dados[0])

print("\n--- Item 1 (primeira vaga de verdade) ---")
print(dados[1])