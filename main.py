from gatherers.news_scraper import fetch_news
from utils.file_manager import save_data

def main():
    print("📰 Gathering news headlines...")
    data = fetch_news()
    path = save_data(data)
    print(f"✅ Saved {len(data)} headlines to: {path}")

if __name__ == "__main__":
    main()
