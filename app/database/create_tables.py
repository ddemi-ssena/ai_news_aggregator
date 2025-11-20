import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.database.models import Base
from app.database.connection import engine

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    #models.py içinde tanımlanan tüm tabloları veritabanında oluştur.
    print("Tables created successfully")
    #Docker’daki Postgres containerına bağlanır
    #Tabloları oluşturur
    #DBeaver’da anında görünür
    #Docker container loglarında tablo oluşturma mesajları görülür
