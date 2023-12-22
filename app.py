import concurrent.futures
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)


def crawl_webpage(root_url, max_depth):
    visited = set()
    result = []

    def crawl(url, depth):
        # Base cases: stop crawling if depth exceeds the limit or if URL has been visited
        if depth > max_depth or url in visited:
            return

        visited.add(url)  # Mark the current URL as visited

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error crawling {url}: {e}")
            return

        result.append(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)  # Extract all anchor links from the page

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Use multithreading to crawl links concurrently
            futures = [executor.submit(crawl, urljoin(url, link['href']), depth + 1) for link in links]

            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error in crawling thread: {e}")

    crawl(root_url, 0)  # Start crawling from the root URL
    return result


# Flask route for the web application
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        root_url = request.form['url']
        max_depth = int(request.form['depth'])
        links = crawl_webpage(root_url, max_depth)
        return render_template('index.html', links=links)

    return render_template('index.html', links=[])


if __name__ == "__main__":
    app.run(debug=True)
