from typing import List
from .config import YOUTUBE_CHANNELS #takip etmek istediğim yt kanal id leri var 
from .scrapers.youtube import YouTubeScraper, ChannelVideo
from .scrapers.openai import OpenAIScraper, OpenAIArticle #daha önce yazılan scrapers sınıfları
from .scrapers.anthropic import AnthropicScraper, AnthropicArticle #her biri kaynakalrdan veri çekiyor
from .database.repository import Repository #database e veri kaydetmeyi yapan sınıf


def run_scrapers(hours: int = 24) -> dict:   #son 24 saati al
    youtube_scraper = YouTubeScraper()  #her scraper için birer bje yarat
    openai_scraper = OpenAIScraper() #bu objelerin içinde get_latest_videos
    anthropic_scraper = AnthropicScraper() #get_articles gibi metotlar var
    repo = Repository() #repo veritabanı bağlantısı
    
    youtube_videos = []   # daha sonrafonk çıktısında döndürülecek ChannelVideo nesnelerinin listesi
    video_dicts = []  #db e göndermek için her videonun sözlük formatında (json gibi) tutulduğu liste
    for channel_id in YOUTUBE_CHANNELS:
        videos = youtube_scraper.get_latest_videos(channel_id, hours=hours)
        youtube_videos.extend(videos)
        video_dicts.extend([
            {
                "video_id": v.video_id,
                "title": v.title,
                "url": v.url,
                "channel_id": channel_id,
                "published_at": v.published_at,
                "description": v.description,
                "transcript": v.transcript
            }
            for v in videos
        ])
    
    openai_articles = openai_scraper.get_articles(hours=hours)
    anthropic_articles = anthropic_scraper.get_articles(hours=hours)
    
    if video_dicts:
        repo.bulk_create_youtube_videos(video_dicts) # db e hızla çoklu kayıt ekler
    
    if openai_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in openai_articles
        ]
        repo.bulk_create_openai_articles(article_dicts)
    
    if anthropic_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in anthropic_articles
        ]
        repo.bulk_create_anthropic_articles(article_dicts)
    
    return {
        "youtube": youtube_videos,
        "openai": openai_articles,
        "anthropic": anthropic_articles,
    }


if __name__ == "__main__":
    results = run_scrapers(hours=24)
    print(f"YouTube videos: {len(results['youtube'])}")
    print(f"OpenAI articles: {len(results['openai'])}")
    print(f"Anthropic articles: {len(results['anthropic'])}")

"""
YOUTUBE_CHANNELS içinde 2 kanal var: ["UCaaa", "UCbbb"].

Fonksiyon çağrıldığında:

YouTubeScraper her iki kanalı tarar, örneğin toplam 5 video bulur.

video_dicts içine 5 tane dict eklenir.

repo.bulk_create_youtube_videos(video_dicts) ile bu 5 video veritabanına eklenir.

OpenAI scraper 3 makale bulur → kaydedilir.

Anthropic scraper 2 makale bulur → kaydedilir.

Fonksiyon çıktı olarak bu üç listeyi geri verir.

"""