import sys
import logging
import re

from scraper import Scraper
from storage import Persistor
from myparser import Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SCRAPPED_FILE = 'scrapped_data.txt'
TABLE_FORMAT_FILE = 'data.csv'


def gather():
    logger.info("gather")
    storage = Persistor(SCRAPPED_FILE)

    scrapper = Scraper(storage)
    scrapper.scrape()


def parse():

    logger.info("parse")
    storage = Persistor(SCRAPPED_FILE)
    parser = Parser()

    raw_data = storage.read_raw_data()

    ind_start = raw_data.find('table class=\"wikitable sortable\"')
    raw_data = raw_data[ind_start:]
    ind_end = raw_data.find('</table>')
    raw_data = raw_data[:ind_end + len('</table>')]

    all_rows = re.findall('<tr[^^]*?</tr>', raw_data)

    parsed_files = [parser.parse_object(raw) for raw in all_rows]
    storage.save_csv(parsed_files, TABLE_FORMAT_FILE)


def stats():
    logger.info("stats")

    # to do

    # Your code here
    # Load pandas DataFrame and print to stdout different statistics about the data.
    # Try to think about the data and use as different methods applicable to DataFrames.
    # Ask yourself what would you like to know about this data (most frequent word, average price, e.t.c.)


if __name__ == '__main__':

    logger.info("Work started")

    if sys.argv[1] == 'gather':
        gather()

    elif sys.argv[1] == 'parse':
        parse()

    elif sys.argv[1] == 'stats':
        stats()

    logger.info("work ended")