import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Načti .env soubor
load_dotenv()

def inicializuj_databazi():
    """Vytvoří testovací databázi, pokud neexistuje."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD"),
        )
        if conn.is_connected():
            print("✅ Připojeno k MySQL serveru.")

        cursor = conn.cursor()
        cursor.execute("""
            CREATE DATABASE IF NOT EXISTS test_task_manager
            CHARACTER SET utf8mb4 COLLATE utf8mb4_czech_ci;
        """)
        print("✅ Databáze 'test_task_manager' připravena.")

    except Error as e:
        print(f"❌ Chyba při vytváření databáze: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def inicializuj_tabulku():
    """Znovu vytvoří tabulku 'ukoly' (vždy čistou, ID od 1)."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD"),
            database='test_task_manager'
        )
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS ukoly;")

        cursor.execute("""
            CREATE TABLE ukoly (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nazev VARCHAR(255) NOT NULL,
                popis TEXT NOT NULL,
                stav ENUM('nezahájeno', 'probíhá', 'hotovo')
                     NOT NULL DEFAULT 'nezahájeno',
                datum_vytvoreni TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB AUTO_INCREMENT=1;
        """)
        conn.commit()
        print("✅ Tabulka 'ukoly' byla vytvořena znovu (ID začíná od 1).")

    except Error as e:
        print(f"❌ Chyba při vytváření tabulky: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    inicializuj_databazi()
    inicializuj_tabulku()
    print("✅ Databáze a tabulka byly úspěšně inicializovány.")