import requests
import beautifulsoup

# Define vars
base_url = 'http://vhost3.lnu.se:20080/~1dv449/scrape/'
login_url = base_url + 'check.php'
product_url = base_url + 'secure/producenter.php'

login_data = {
    'username': 'admin',
    'password': 'admin'
}

# Log in
s = requests.session()
s.post(login_url, data=login_data)

# Scrape
r = s.get(product_url)
print(r.text)
