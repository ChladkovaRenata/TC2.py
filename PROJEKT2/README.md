# 📝 Task Manager – Projekt 2 (ENGETO)

Tento projekt je jednoduchý správce úkolů s využitím Pythonu a MySQL databáze.

## 📁 Struktura složek

projekt2/
│
├── .env                  # Konfigurační soubor s citlivými údaji (např. přihlašovací údaje do DB, ignorováno Gitem)
├── .gitignore            # Seznam souborů/složek, které Git ignoruje (např. .env, __pycache__)
├── init_db.py            # Skript pro inicializaci databáze (vytvoření tabulek atd.)
├── requirements.txt      # Seznam Python knihoven, které je potřeba nainstalovat
├── README.md             # Dokumentace projektu, základní info a instrukce
├── task_manager.py       # Hlavní modul s funkcemi pro správu úkolů (přidání, aktualizace, odstranění)
│
└── tests/                # Složka s testy
    ├── __pycache__/      # Cache Python kompilovaných souborů (ignorováno Gitem)
    ├── test_db_connection.py  # Testy pro připojení k databázi
    └── test_task_manager.py   # Testy funkcí pro správu úkolů


---

## ⚙️ Požadavky

- Python 3.13+
- `mysql-connector-python`
- `pytest`

Nainstaluj závislosti pomocí:

```bash
pip install -r requirements.txt

🛠️ Inicializace databáze
Ověření připojení k databázi/Spusť skript, který vytvoří databázi a tabulku automaticky:
python init_db.py


✅ Spuštění testů

Spuštění všech testů:
pytest -s

Spuštění konkrétního testu podle jména např.:
pytest -k "test_pridat_ukol_pozitivni" -s
pytest -k "test_pridat_ukol_negativni" -s
pytest -k "test_aktualizovat_ukol_pozitivni" -s
pytest -k "test_aktualizovat_ukol_negativni" -s
pytest -k "test_odstranit_ukol_pozitivni" -s
pytest -k "test_odstranit_ukol_negativni" -s

Spuštění testů z konkrétního souboru:
pytest tests/test_task_manager.py -s
pytest tests/test_db_connection.py -s


spušpětí hlavniho menu
python task_manager.py

Nebo otevřít složku task_manazer.py a spustit pomocí Run

📄 Popis funkcí
pridat_ukol(conn, nazev, popis) – přidá úkol

aktualizovat_ukol(conn, id, novy_stav) – změní stav úkolu

odstranit_ukol(conn, id) – smaže úkol

📚 Uživatelské příkazy v kódu
MySQL příkazy:

Test: 
CREATE DATABASE IF NOT EXISTS USE test_task_manager;
SHOW DATABASES;
USE test_task_manager;
SELECT * FROM ukoly;
SHOW TABLES

CREATE TABLE IF NOT EXISTS ukoly (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nazev VARCHAR(255) NOT NULL,
  popis TEXT NOT NULL,
  stav ENUM('nezahájeno', 'probíhá', 'hotovo') NOT NULL DEFAULT 'nezahájeno',
  datum_vytvoreni DATETIME DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;
DESCRIBE ukoly;

Hlavní:
CREATE DATABASE IF NOT EXISTS task_manager;
SHOW DATABASES;
USE task_manager;
SELECT * FROM ukoly;
SHOW TABLES;

CREATE TABLE IF NOT EXISTS ukoly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(255) NOT NULL,
    popis TEXT NOT NULL,
    stav ENUM('nezahájeno', 'probíhá', 'hotovo') NOT NULL DEFAULT 'nezahájeno',
    datum_vytvoreni DATETIME
);
SELECT DATABASE();
DESCRIBE ukoly;


Python funkce pro práci s úkoly:
pridat_ukol(conn, "Název", "Popis")
aktualizovat_ukol(conn, id_ukolu, "hotovo")
odstranit_ukol(conn, id_ukolu)


🧪 Doporučení pro testování
V test_task_manager.py je použit pytest.fixture, který:
smaže všechna data před a po každém testu

Testy kontrolují:
přidání úkolu (pozitivní i negativní scénáře)
aktualizaci úkolu
odstranění úkolu

💡 Poznámky
Při prvním spuštění databáze ověř, že běží MySQL server a máš správné přihlašovací údaje v init_db.py.

Skript init_db.py lze spouštět opakovaně – nevytvoří duplikáty.

🧑‍💻 Autor
Projekt vytvořen v rámci studia ENGETO – Python Akademie.



