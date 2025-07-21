from app.cli import cli
from app.databases import init_db

if __name__ == "__main__":
    init_db()  # 👈 creează tabelele dacă nu există
    cli()
