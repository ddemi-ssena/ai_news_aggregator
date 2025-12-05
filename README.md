📘 AI News Aggregator — README

AI dünyasındaki gelişmeleri otomatik olarak toplayan, özetleyen, kişiselleştiren ve sıralayan tam otomatik bir haber toplama sistemi.
YouTube, OpenAI Blog ve Anthropic Blog kaynaklarını tarar, içerikleri özetler, kişisel profile göre önem sırasına koyar ve veritabanına kaydeder.

🚀 Proje Özeti

Bu proje, çeşitli yapay zekâ haber kaynaklarını otomatik şekilde takip eden ve içeriği kullanıcı profilinize göre zeka destekli özetleyen ve sıralayan bir AI News Aggregator aracıdır.

Sistem üç ana aşamada çalışır:

Scraper modülleri → YouTube videolarını, OpenAI Blog yazılarını ve Anthropic gönderilerini çeker.

DigestAgent → Bu içerikleri kısa ve etkili bir özet haline getirir.

CuratorAgent → Kullanıcının ilgi alanlarına göre haberleri puanlayıp sıralar.

Runner & Daily Runner → Tüm sistemi tek komutla otomatik olarak çalıştırır.

📂 Proje Yapısı
ai_new_aggregator/
│
├── app/
│   ├── agents/
│   │   ├── digest_agent.py
│   │   └── curator_agent.py
│   │
│   ├── services/
│   │   ├── fetch_openai_news.py
│   │   ├── fetch_anthropic_news.py
│   │   ├── fetch_youtube_videos.py
│   │   └── process_youtube_transcripts.py
│   │
│   ├── runner.py
│   ├── daily_runner.py
│   ├── config.py
│   └── profiles.py
│
├── data/
│   └── database.db
│
└── README.md

🧠 Kullanılan Yapay Zekâ Bileşenleri
1️⃣ DigestAgent — İçerik Özetleme

Model: gpt-4o-mini

Görevi:

İçeriği okuyup kısa başlık + 2–3 cümlelik özet üretmek

Pazarlama dili olmayan, teknik ve sade özetler üretmek

Sınıf: DigestAgent.generate_digest()

2️⃣ CuratorAgent — Kişiye Özel Sıralama

Model: gpt-4.1

Görevi:

Kullanıcı profilini okuyup makaleleri önem düzeyine göre puanlamak

Her içerik için:

relevance_score (0–10)

rank (1 = en ilgili)

reasoning (neden böyle sıraladı?)

Kullanıcı ilgi alanları:

LLMs
RAG
MLOps
AI Infrastructure
Practical AI
Research breakthroughs


Yapı:

profiles.py içine kullanıcı profili oluşturuluyor

Profil → CuratorAgent → sıralama

3️⃣ Services (Scrapers)

Her biri farklı bir kaynağı tarar:

Dosya	Kaynak	Çıktı
fetch_openai_news.py	OpenAI Blog	title + content
fetch_anthropic_news.py	Anthropic Blog	title + content
fetch_youtube_videos.py	YouTube API	video_id + title
process_youtube_transcripts.py	YouTube transcript API	tam metin transcript
4️⃣ Runner & Daily Runner
Dosya	Görev
runner.py	Manuel çalıştırma → Scraper + Digest + Curation
daily_runner.py	Günlük otomatik toplama (cron job / task scheduler için)
⚙️ Kurulum
1 — Depoyu klonla
git clone ...
cd ai_new_aggregator

2 — Sanal ortam oluştur
python -m venv venv
.\venv\Scripts\activate

3 — Gereksinimleri kur
pip install -r requirements.txt

4 — .env dosyasını ayarla
OPENAI_API_KEY=YOUR_KEY_HERE
YOUTUBE_API_KEY=YOUR_KEY_HERE

▶️ Çalıştırma
Manuel çalıştırma
python -m app.runner


Çıktı örneği:

YouTube videos: 1
OpenAI articles: 2
Anthropic articles: 0

Günlük otomatik çalıştırma
python -m app.daily_runner

📘 Bu projeyi yaparken takip edilen tutorial

Bu proje oluşturulurken ana ilham kaynağı şu tutorialdır:

"Building an AI News Aggregator with Python + OpenAI Responses API"

👉 Takip Ettiğim Proje - YT Kanalı

[[https://www.youtube.com/watch?v=YH93zJqIrEM](https://go.datalumina.com/MszdmaM)](https://go.datalumina.com/MszdmaM)
Dave EBBELAAR

Tutorial’dan alınan ana fikirler:

OpenAI Responses API ile structured output

Pydantic modelleri ile güvenli veri çıkarımı

Multi-agent mimarisi (digest agent + curator agent)

Runner tabanlı pipeline yaklaşımı

Haberleri kişiye özel sıralama

Bu repo ise tutorial üzerine çok daha gelişmiş bir mimari ekleyerek oluşturuldu:

Agents klasörü

Services klasörü

User Profile

Ranking sistemi

Transcript işleme

Daily automation

🔮 İleri Geliştirmeler

İstersen şu özellikleri ekleyebiliriz:

🔔 Telegram / Discord bildirim botu

📱 Mobil uygulama için API (FastAPI)

⭐ Favori haberler sistemi

📊 Dashboard (Streamlit)

📬 Yardım

Herhangi bir noktada takıldığında:

👉 Bana kodu, hata mesajını veya klasör yapısını gönder — birlikte çözelim!
