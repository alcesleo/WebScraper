import requests
import re
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin
from locallyproduced.models import Producer

class Scraper(object):

    def __init__(self):

        # define URL:s
        self.base_url = 'http://vhost3.lnu.se:20080/~1dv449/scrape/'
        self.login_url = self.base_url + 'check.php'
        self.product_url = self.base_url + 'secure/producenter.php'

        # log in
        credentials = {'username': 'admin', 'password': 'admin'}
        self.session = self.get_logged_in_session(credentials)

    def get_logged_in_session(self, login_data):
        """Returns requests session-object"""

        # log in
        s = requests.session()
        s.post(self.login_url, data=login_data)
        return s

    def empty_database(self):
        """Delete all rows in db"""
        Producer.objects.all().delete()

    def scrape(self):

        # clear the table
        self.empty_database()

        # get and parse the table portion of the page
        response = self.session.get(self.product_url)
        # TODO: Fix encoding, should probably be set to utf-8 once the head-tag is in place
        soup = BeautifulSoup(response.text.encode('latin-1', 'ignore'), parse_only=SoupStrainer('table'))

        # remove the annoying thead
        soup.table.thead.extract()

        # parse each row
        for row in soup.find_all('tr'):
            self.parse_row(row)

    def parse_row(self, row):

        producer = Producer()

        # link is in first td
        link = row.td.a

        # get the name
        producer.name = link.string.strip()

        # href
        if link.has_attr('href'):
            href = link['href']

            # get the id
            match = re.search('producer_(\d.)', href)
            if match:
                print int(match.group(1))
                producer.producer_id = int(match.group(1))
            else:
                producer.producer_id = -1

            # go to details page
            self.parse_details_page(href)

        producer.save()


    def parse_details_page(self, href):
        # get full link
        link = urljoin(self.product_url, href)
        print(link)
