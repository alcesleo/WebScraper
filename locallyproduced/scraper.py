import requests
from bs4 import BeautifulSoup

class Scraper(object):

    # Define vars
    base_url = 'http://vhost3.lnu.se:20080/~1dv449/scrape/'
    login_url = base_url + 'check.php'
    product_url = base_url + 'secure/producenter.php'

    login_data = {
        'username': 'admin',
        'password': 'admin'
    }

    def get_logged_in_session(self):
        """Returns requests session-object"""

        # Log in
        s = requests.session()
        s.post(self.login_url, data=self.login_data)
        return s

    def scrape(self):

        s = self.get_logged_in_session()

        # Scrape
        response = s.get(self.product_url)
        soup = BeautifulSoup(response.text)
        soup.encode('utf-8')
        links = ''
        for link in soup.find_all('a'):
            print(link)


# Test
s = Scraper()
s.scrape()
