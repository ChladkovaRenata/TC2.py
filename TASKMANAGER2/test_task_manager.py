import pytest
import mysql.connector
from task_manager import pripojeni_db

# Pomocné funkce
def clear_test_data():
    conn = pripojeni_db(test=True)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ukoly")
    conn.commit()
    cursor.close()
    conn.close()
    

@pytest.fixture(autouse=True)
def setup_teardown():
    clear_test_data()
    yield
    clear_test_data()

# Přidání úkolu
def test_pridat_ukol_pozitivní():
    conn = pripojeni_db(test=True)
    cursor = conn.cursor()
    nazev = ""
    popis = ""
    cursor.execute("SELECT COUNT(*) FROM ukoly")
    count_before = cursor.fetchone()[0]
    cursor.execute("INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)", (nazev, popis))
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM ukoly")
    count_after = cursor.fetchone()[0]
    assert count_after == count_before + 1, "Úkol byl přidán i s prázdnými hodnotami"
    cursor.close()
    conn.close()

def test_pridat_ukol_negativni():
    conn = pripojeni_db(test=True)
    cursor = conn.cursor()
    with pytest.raises(mysql.connector.errors.IntegrityError):
        cursor.execute("INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)", (None, "Popis"))
        conn.commit()
    cursor.close()
    conn.close()

# Aktualizace úkolu
def test_aktualizovat_ukol_pozitivni():
    conn = pripojeni_db(test=True)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)", ("Aktualizuj", "Test"))
    conn.commit()
    cursor.execute("UPDATE ukoly SET stav = 'Hotovo' WHERE nazev = %s", ("Aktualizuj",))
    conn.commit()
    cursor.execute("SELECT stav FROM ukoly WHERE nazev = %s", ("Aktualizuj",))
    stav = cursor.fetchone()[0]
    assert stav == "hotovo"
    cursor.close()
    conn.close()

def test_aktualizovat_ukol_negativni():
    conn = pripojeni_db(test=True)
    cursor = conn.cursor()
    cursor.execute("UPDATE ukoly SET stav = 'Hotovo' WHERE id = -999")
    conn.commit()
    assert cursor.rowcount == 0
    cursor.close()
    conn.close()

# Odstranění úkolu
def test_odstranit_ukol_pozitivni():
    conn = pripojeni_db(test=True)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)", ("Smazat mě", "Test"))
    conn.commit()
    cursor.execute("DELETE FROM ukoly WHERE nazev = %s", ("Smazat mě",))
    conn.commit()
    cursor.execute("SELECT * FROM ukoly WHERE nazev = %s", ("Smazat mě",))
    assert cursor.fetchone() is None
    cursor.close()
    conn.close()

def test_odstranit_ukol_negativni():
    conn = pripojeni_db(test=True)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ukoly WHERE id = -1")
    conn.commit()
    assert cursor.rowcount == 0
    cursor.close()
    conn.close()