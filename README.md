📐 Math Service CLI
 
Un microserviciu în linia de comandă (CLI) scris în Python, care oferă operații matematice simple și salvează fiecare cerere într-o bază de date locală (SQLite). Aplicația respectă o arhitectură modulară (MVCS), este testabilă și extensibilă.
 
✅ Funcționalitate implementată
 
- `pow`: ridică un număr la o putere dată
- `factorial`: calculează factorialul unui număr natural
- `fibonacci`: returnează al n-lea număr din seria Fibonacci
 
Toate calculele:
- sunt validate cu `Pydantic`
- sunt cache-uite în memorie (dict-based caching)
- sunt salvate în SQLite împreună cu inputul, rezultatul și timestamp-ul
 
🚀 Cum se rulează
 
1. Instalează dependințele:
   pip install -r requirements.txt
 
2. Rulează una din comenzile CLI:
 
   python cli.py pow --x 2 --y 3         # → Rezultat: 8.0
   python cli.py factorial --n 5         # → Rezultat: 120
   python cli.py fibonacci --n 6         # → Rezultat: 8
 
🧩 Structura aplicației
 
math_service_cli/
│
├── app/
│   ├── cli.py               # CLI commands (click)
│   ├── controller.py        # Orchestrare: CLI ↔ servicii ↔ cache/DB
│   ├── models.py            # Validare input/output (Pydantic)
│   ├── cache.py             # Caching simplu în memorie
│   ├── database.py          # Persistență în SQLite
│   ├── services/
│   │   └── math_service.py  # Funcții matematice pure
│   └── worker.py            # (Opțional) execuție async/threaded
│
├── tests/                   # Teste unitare + CLI
├── cli.py                   # Entry point (invocă CLI-ul)
├── requirements.txt         # Dependențe Python
├── README.md                # Documentația aplicației
└── .flake8                  # Configurație linting
 
🔧 Tehnologii și librării folosite
 
- Click – CLI modern și ușor de extins
- Pydantic – validare și serializare dată
- SQLite3 – persistare ușoară locală (built-in în Python)
- flake8 – stil și calitate cod
- pytest – testare unitare/funcționale
 
🧪 Testare
 
Pentru rularea testelor:
pytest tests/
 
🧼 Linting
 
Pentru verificarea calității codului:
flake8 .
 
🌱 Extensibilitate
 
Structura este modulară și permite:
- adăugarea de noi operații (`gcd`, `sqrt`, etc.)
- rulare în thread/async via `worker.py`
- comenzi noi în CLI (`history`, `export`, etc.)
- migrare ușoară spre un API web (`FastAPI`, `Flask`)
 

---
## 👥 Contribuții pe membri

**Cristian-Valentin Alexa  – Logica matematică & CLI**
- Implementare funcții matematice (`pow_func`, `factorial`, `fibonacci`) în `app/services/math_service.py`
- CLI cu Click în `app/cli.py` și `cli.py` (entrypoint)
- Teste unitare pentru funcții în `tests/test_math.py`

**Dragos-Ionut Talaba – Cache, DB & Models**
- Modele Pydantic pentru request/response (`app/models.py`)
- Cache dict-based (`app/cache.py`)
- Persistență SQLite (`app/database.py`)
- Teste cache în `tests/test_cache.py`

**Gabriel Firisar  – Controller, Integrare, Calitate & Frontend**
- Orchestrare controller (`app/controller.py`)
- Integrare CLI ↔ controller ↔ servicii ↔ cache/DB
- Teste CLI cu Click (`tests/test_cli.py`)
- README, .flake8, linting
- Frontend React (implementat ulterior):
  - UI modern cu branding Endava
  - Integrare cu API Flask
  - Design responsive, gradient, temă custom

---
 
 
