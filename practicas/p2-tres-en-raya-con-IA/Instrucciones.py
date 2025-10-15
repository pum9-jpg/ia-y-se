import requests
import json

# URL del endpoint
url = "https://api.llm7.io/v1/chat/completions"

# Tu API Key (reemplaza con la tuya)
api_key = "TU_API_KEY_AQUI"

# Cabeceras (Headers)
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Cuerpo (Body) de la solicitud
data = {
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "jugare en la (1,1), ahora tu cual jugarias?"
        }
    ],
    "max_tokens": 1000,
    "temperature": 0.7
}

# Enviamos la solicitud POST
response = requests.post(url, headers=headers, json=data)

# Mostramos el resultado
if response.status_code == 200:
    result = response.json()
    # Normalmente el texto generado está en result["choices"][0]["message"]["content"]
    print("Respuesta del modelo:")
    print(result["choices"][0]["message"]["content"])
else:
    print(f"Error {response.status_code}: {response.text}")