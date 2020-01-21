import bs4
import requests
import sys
import time

OUTFILE = 'data/quotes.txt'
URLS = [
    'https://www.brainyquote.com/authors/mark-cuban-quotes/',
    'https://www.brainyquote.com/authors/steve-jobs-quotes',
    'https://www.brainyquote.com/authors/elon-musk-quotes',
    'https://www.brainyquote.com/authors/simon-sinek-quotes',
    'https://www.brainyquote.com/profession/quotes-by-businessmen',
    'https://www.brainyquote.com/authors/jeff-bezos-quotes',
    'https://www.brainyquote.com/authors/richard-branson-quotes',
    'https://www.brainyquote.com/authors/jack-ma-quotes',
    'https://www.brainyquote.com/authors/tim-cook-quotes',
    'https://www.brainyquote.com/authors/j-p-morgan-quotes',
    'https://www.brainyquote.com/authors/henry-ford-quotes',
    'https://www.brainyquote.com/search_results?q=entrepreneur',
    'https://www.brainyquote.com/topics/entrepreneurship-quotes',
    'https://www.brainyquote.com/topics/entrepreneurial-spirit-quotes',
    'https://www.brainyquote.com/search_results?q=billionaire',
    'https://www.brainyquote.com/search_results?q=wealthy',
    'https://www.brainyquote.com/search_results?q=business'
]
SLEEP_SECONDS = 3

def process_node(node):
    stripped = node.text.strip()
    first_line = stripped.split("\n")[0].strip().strip('"')
    return first_line

def scrape(urls):
    quotes = []
    for url in urls:
        resp = requests.get(url)

        resp.raise_for_status()
        soup = bs4.BeautifulSoup(resp.content, 'html.parser')

        nodes = soup.find_all('a', class_='b-qt')
        if not len(nodes):
            break
        pg_quotes = map(process_node, nodes)
        quotes += list(pg_quotes)
        print("Processed url:", url)
        time.sleep(SLEEP_SECONDS)

    with open(OUTFILE, "a") as f:
        f.write("\n" + "\n".join(quotes))

if __name__ == '__main__':
    scrape(URLS)
