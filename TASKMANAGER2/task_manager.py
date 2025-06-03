import mysql.connector
from mysql.connector import Error
import pytest

# Připojení k databázi
def pripojeni_db(test=False):
    try:
        task_manager = 'task_manager_test' if test else 'task_manager'
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Norbinka28.', 
            database=task_manager
        )
        return conn
    except Error as e:
        print("Chyba při připojení k databázi:", e)
        return None
# Přidání úkolu
def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if nazev and popis:
            conn = pripojeni_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)", (nazev, popis))
                conn.commit()
                conn.close()
                print("Úkol byl přidán.")
            break
        else:
            print("Chyba: Název i popis musí být vyplněny.")

# Zobrazení všech úkolů
def zobrazit_ukoly():
    print("\nSeznam úkolů:")
    conn = pripojeni_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nazev, popis, stav FROM ukoly")
        ukoly = cursor.fetchall()
        if not ukoly:
            print("Seznam úkolů je prázdný.")
        else:
            for u in ukoly:
                print(f"{u[0]}. {u[1]} - {u[2]} [{u[3]}]")
        conn.close()

# Aktualizace stavu úkolu
def aktualizovat_ukol():
    conn = pripojeni_db()
    if not conn:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT id, nazev, stav FROM ukoly")
    ukoly = cursor.fetchall()
    if not ukoly:
        print("Žádné úkoly k aktualizaci.")
        conn.close()
        return

    print("\nÚkoly k aktualizaci:")
    for u in ukoly:
        print(f"{u[0]}. {u[1]} [{u[2]}]")

    try:
        id_ukolu = int(input("Zadejte ID úkolu k aktualizaci: "))
    except ValueError:
        print("Chyba: Zadejte platné číslo.")
        conn.close()
        return

    cursor.execute("SELECT id FROM ukoly WHERE id = %s", (id_ukolu,))
    if cursor.fetchone() is None:
        print("Chyba: Úkol s tímto ID neexistuje.")
        conn.close()
        return

    novy_stav = input("Zadejte nový stav (Probíhá / Hotovo): ").capitalize()
    if novy_stav not in ["Probíhá", "Hotovo"]:
        print("Neplatný stav. Povolené hodnoty jsou: Probíhá, Hotovo.")
    else:
        cursor.execute("UPDATE ukoly SET stav = %s WHERE id = %s", (novy_stav, id_ukolu))
        conn.commit()
        print("Stav úkolu byl aktualizován.")
    conn.close()


# Odstranění úkolu
def odstranit_ukol():
    conn = pripojeni_db()
    if not conn:
        return

    zobrazit_ukoly()
    try:
        id_ukolu = int(input("Zadejte ID úkolu, který chcete odstranit: "))
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM ukoly WHERE id = %s", (id_ukolu,))
        if cursor.fetchone() is None:
            print("Chyba: Úkol s tímto ID neexistuje.")
        else:
            cursor.execute("DELETE FROM ukoly WHERE id = %s", (id_ukolu,))
            conn.commit()
            print("Úkol byl odstraněn.")
    except ValueError:
        print("Chyba: Zadejte platné číslo.")
    finally:
        conn.close()

# Hlavní menu
def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1 - Přidat nový úkol")
        print("2 - Zobrazit všechny úkoly")
        print("3 - Aktualizovat úkol")
        print("4 - Odstranit úkol")
        print("5 - Konec programu")

        volba = input("Vyberte možnost (1-5): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            aktualizovat_ukol()
        elif volba == "4":
            odstranit_ukol()
        elif volba == "5":
            print("Konec programu.")
            break
        else:
            print("Chyba: Neplatná volba. Zkuste to znovu.")

# Spuštění
if __name__ == "__main__":
    hlavni_menu()