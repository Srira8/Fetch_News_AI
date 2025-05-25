from bs4 import BeautifulSoup
from config import HEADERS, NEWS_SOURCES
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def fetch_news():
    headlines = []

    # Set up Selenium with headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    for source, url in NEWS_SOURCES.items():
        print(f"🌐 Fetching: {source} - {url}")
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        
        if source == 'cnn':
            items = soup.select('h1#maincontent, span.container__headline-text, h3.card-title')
            
        elif source == 'bbc':
            items = soup.select('h3.gs-c-promo-heading__title')



        count = 0
        seen = set()
        for item in items:
            text = item.get_text(strip=True)
            if text and text not in seen:
                seen.add(text)
                headlines.append({'source': source, 'headline': text})
                count += 1

        print(f"✅ {count} headlines collected from {source}")

    driver.quit()
    return headlines

