pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

#Vylepšený Task Manager (MySQL + Python + Pytest)

Tento projekt je jednoduchý správce úkolů, který pracuje s MySQL databází a umožňuje provádět operace: Přidat, Zobrazit, Aktualizovat a Odstranit úkol.



Požadavky

Než projekt spustíš, ujisti se, že máš nainstalované:

- Python 3.10 nebo novější
- MySQL Server (např. přes XAMPP nebo MySQL Workbench)
- Knihovny: `mysql-connector-python`, `pytest`



Instalace závislostí


pip install mysql-connector-python pytest


Spuštění programu jsou 2 varianty:
1. python main.py
2. Nebo jít na task_manager.py a dát Run Python File

Spuštění testů
V kořenovém adresáři projektu spusť:
pytest

Zobrazit detailní výstup (s printy a více informacemi)
pytest -v

Spuštění konkrétního testovacího souboru např.
pytest task_manager.py




Automatizované testy
Testy ověřují funkce:

Přidání úkolu
Aktualizace úkolu
Odstranění úkolu
Každá funkce má:
Pozitivní test (platný vstup)
Negativní test (neplatný vstup)

🔹 Příprava testovací databáze
V MySQL spusť následující:
Hlavní DB: 

CREATE DATABASE IF NOT EXISTS task_manager_test;

USE task_manager_test;

CREATE TABLE IF NOT EXISTS ukoly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(255) NOT NULL,
    popis TEXT NOT NULL,
    stav ENUM('nezahájeno', 'probíhá', 'hotovo') NOT NULL DEFAULT 'nezahájeno',
    datum_vytvoreni DATETIME
);

Testovací DB:

CREATE DATABASE IF NOT EXISTS test_task_manager;
USE test_task_manager;

CREATE TABLE IF NOT EXISTS ukoly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(255) NOT NULL,
    popis TEXT NOT NULL,
    stav ENUM('nezahájeno', 'probíhá', 'hotovo') NOT NULL DEFAULT 'nezahájeno',
    datum_vytvoreni DATETIME
);



Struktura projektu:

📦 Task Manager Projekt
├── __pycache__
├── .pytest_cache
    └── v
├── main.py
├── task_manager.py
├── test_task_manager/
├── test_task_manager.py
└── README.md
