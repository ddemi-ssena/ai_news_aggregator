import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

#VERİTABANINA BAĞLANMA DOSYASI
#VERİTABANINA GİDEN KAPI GİBİ, KAPIYI AÇMAK İÇİN USERNAME, PASSWORD, HOST,PORT GEREK

def get_database_url() -> str:
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "ai_news_aggregator")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(get_database_url()) #ENGİNE MOTORU SQL KOMUTLARINI VERİTABANINA GÖNDERİYOR.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    return SessionLocal()
    #Bu, veritabanına bağlanıp işlem yapmanı sağlayan oturum → session yaratıyor.