import bs4
import requests
import sys
import time

OUTFILE = 'data/quotes.txt'
BASE_URL = 'https://www.goodreads.com/author/quotes/'
QUOTE_ID = sys.argv[1]
SLEEP_SECONDS = 3


def process_node(node):
    stripped = node.text.strip()
    first_line = stripped.split("\n")[0]
    without_quotes = first_line[1:-1]
    return without_quotes

def scrape():
    page = 1
    while True:
        print('Starting page ' + str(page))
        url = BASE_URL + QUOTE_ID
        if page > 1:
            url += '?page=' + str(page)
        resp = requests.get(url)
        resp.raise_for_status()
        soup = bs4.BeautifulSoup(resp.content, 'html.parser')

        nodes = soup.find_all('div', class_='quoteText')
        if not len(nodes):
            break
        quotes = map(process_node, nodes)
        with open(OUTFILE, "a") as f:
            f.write("\n" + "\n".join(quotes))
        page += 1

if __name__ == '__main__':
    scrape()
