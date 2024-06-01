import requests
import json

# Data login
login_data = {
    'username': 'kluntingisreal',
    'password': 'Pr0j3ctX@zY'
}

# URL endpoint login
login_url = 'http://167.172.75.216/login'
headers = {'Content-Type': 'application/json'}

# Kirim permintaan login
session = requests.Session()
response = session.post(login_url, data=json.dumps(login_data), headers=headers)

# Periksa apakah login berhasil
if response.status_code == 200:
    print('Login berhasil')
    # Tampilkan cookie sesi
    cookies = session.cookies.get_dict()
    print('Cookies:', cookies)
else:
    print('Login gagal')
    print(response.text)
    
# Gunakan cookie sesi untuk mengakses endpoint lain
login_url = 'http://167.172.75.216/login'
response = session.get(login_url)


# Gunakan cookie sesi untuk mengakses endpoint lain
dashboard_url = 'http://167.172.75.216/dashboard'
response = session.get(dashboard_url)

# Periksa respons dari akses dashboard
if response.status_code == 200:
    print('Akses dashboard berhasil')
    print(response.text)
else:
    print('Akses dashboard gagal')
    print(response.text)
