import requests
import json

# Konfigurasi proxy Burp Suite
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

# Data registrasi
register_data = {
    'username': 'siklunting',
    'password': 'Gu3st@ccess',
    'email': 'contoh@email.com'
}

# Kirim permintaan registrasi
register_url = 'http://167.172.75.216/register'
headers = {'Content-Type': 'application/json'}
response = requests.post(register_url, data=json.dumps(register_data), headers=headers, proxies=proxies)

# Periksa respons
if response.status_code == 200:
    print('Registrasi berhasil')
else:
    print('Registrasi gagal')
    print(response.text)