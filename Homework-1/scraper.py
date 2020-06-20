import logging
import requests


logger = logging.getLogger(__name__)


class Scraper:

    def __init__(self, storage):
        self.storage = storage

    def scrape(self):
        url = 'https://en.wikipedia.org/wiki/World_Happiness_Report'
        response = requests.get(url)

        if not response.ok:
            logger.error(response.text)

        else:
            data = response.text
            self.storage.save_raw_data(data)