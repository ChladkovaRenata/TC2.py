import pytest
import mysql.connector
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from task_manager import pripojeni_db


def test_pripojeni_k_databazi():
    """Test připojení k databázi a kontrola tabulek"""
    conn = pripojeni_db(test=False)
    assert conn is not None, "Nepodařilo se připojit k databázi"

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tabulky = cursor.fetchall()
    print("Připojení OK")
    print("Tabulky:", tabulky)

    cursor.close()
    conn.close()

    
    assert any("ukoly" in t for t in tabulky), "Tabulka 'ukoly' nebyla nalezena"