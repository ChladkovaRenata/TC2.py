import pytest
import mysql.connector
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from task_manager import pridat_ukol, aktualizovat_ukol, odstranit_ukol

from init_db import inicializuj_databazi, inicializuj_tabulku

def test_pridat_ukol():
    pass

inicializuj_databazi()
inicializuj_tabulku()
print("Databáze a tabulka připraveny.")

_connection_logged = False

def pripojeni_test_db():
    global _connection_logged
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Norbinka28.',
        database='test_task_manager'
    )
    if not _connection_logged:
        print("Připojeno k databázi")
        print(conn.is_connected())
        _connection_logged = True
    return conn

@pytest.fixture(autouse=True)
def cleanup():
    # vyčistí tabulku před testem
    conn = pripojeni_test_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ukoly")
    conn.commit()
    cursor.close()
    conn.close()
    yield
    # vyčistí tabulku po testu
    conn = pripojeni_test_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ukoly")
    conn.commit()
    cursor.close()
    conn.close()

def test_pridat_ukol_pozitivni():
    conn = pripojeni_test_db()
    pridat_ukol(conn, "Test úkol", "Popis test úkolu")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE nazev = %s", ("Test úkol",))
    pocet = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    assert pocet == 1

def test_pridat_ukol_negativni():
    conn = pripojeni_test_db()
    with pytest.raises(ValueError):
        pridat_ukol(conn, "", "Popis")
    conn.close()

def test_aktualizovat_ukol_pozitivni():
    conn = pripojeni_test_db()
    pridat_ukol(conn, "Aktualizuj mě", "Popis")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM ukoly WHERE nazev = %s", ("Aktualizuj mě",))
    id_ukolu = cursor.fetchone()[0]
    cursor.close()
    aktualizovat_ukol(conn, id_ukolu, "hotovo")
    cursor = conn.cursor()
    cursor.execute("SELECT stav FROM ukoly WHERE id = %s", (id_ukolu,))
    stav = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    assert stav == "hotovo"

def test_aktualizovat_ukol_negativni():
    conn = pripojeni_test_db()
    with pytest.raises(ValueError):
        aktualizovat_ukol(conn, 9999, "hotovo")
    with pytest.raises(ValueError):
        aktualizovat_ukol(conn, 1, "špatný_stav")
    conn.close()

def test_odstranit_ukol_pozitivni():
    conn = pripojeni_test_db()
    pridat_ukol(conn, "Smazat mě", "Popis")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM ukoly WHERE nazev = %s", ("Smazat mě",))
    id_ukolu = cursor.fetchone()[0]
    cursor.close()
    odstranit_ukol(conn, id_ukolu)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ukoly WHERE id = %s", (id_ukolu,))
    pocet = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    assert pocet == 0

def test_odstranit_ukol_negativni():
    conn = pripojeni_test_db()
    with pytest.raises(ValueError):
        odstranit_ukol(conn, 9999)
    conn.close()