import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None


def extract_meta(soup, property_name, default=None):
    meta_tag = soup.find('meta', property=property_name) or soup.find('meta', attrs={'name': property_name})
    return meta_tag['content'] if meta_tag else default


def scrape_og_data(url):
    html_content = fetch_html(url)
    if html_content is None:
        return 'No title', 'No description', '', 'website'

    soup = BeautifulSoup(html_content, 'html.parser')

    title = extract_meta(soup, 'og:title', soup.title.string if soup.title else 'No title')
    description = extract_meta(soup, 'og:description', 'No description')
    image = extract_meta(soup, 'og:image', '')
    link_type = extract_meta(soup, 'og:type', 'website')

    return title, description, image, link_type
