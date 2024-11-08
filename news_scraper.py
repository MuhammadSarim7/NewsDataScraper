import requests
from bs4 import BeautifulSoup
from datetime import datetime


def fetch_news(news_url="https://arynews.tv/"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(news_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.find_all("article"):
        title = item.find("h2").text if item.find("h2") else "No Title"
        date = item.find("time").text if item.find("time") else None
        summary = item.find("p").text if item.find("p") else "No Summary"
        try:
            publication_date = datetime.strptime(
                date, "%Y-%m-%d") if date else None
        except ValueError:
            publication_date = None
        articles.append({
            "title": title,
            "date": publication_date,
            "summary": summary
        })

    return articles
