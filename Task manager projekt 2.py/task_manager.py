import mysql.connector
from mysql.connector import Error

def pripojeni_db(test=False):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Norbinka28.',
            database='task_manager_test' if test else 'task_manager'
        )
        if conn.is_connected():
            print("Připojeno k databázi")
            return conn
    except Error as e:
        print(f"Chyba připojení k databázi: {e}")
        return None

def vytvoreni_tabulky():
    conn = pripojeni_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ukoly (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nazev VARCHAR(255) NOT NULL,
            popis TEXT NOT NULL,
            stav ENUM('nezahájeno', 'probíhá', 'hotovo') DEFAULT 'nezahájeno',
            datum_vytvoreni DATETIME
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def pridat_ukol(conn, nazev, popis):
    if not nazev or not popis.strip():
        raise ValueError("Název a popis nesmí být prázdné.")
    cursor = conn.cursor()
    sql = "INSERT INTO ukoly (nazev, popis, stav, datum_vytvoreni) VALUES (%s, %s, %s, NOW())"
    cursor.execute(sql, (nazev, popis, 'nezahájeno'))
    conn.commit()
    cursor.close()
    
    

def zobrazit_ukoly(conn):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nazev, popis, stav FROM ukoly WHERE stav IN ('nezahájeno', 'probíhá')"
    )
    rows = cursor.fetchall()
    cursor.close()
    return rows

def aktualizovat_ukol(conn, id_ukolu, novy_stav):
    if novy_stav not in ['probíhá', 'hotovo']:
        raise ValueError("Neplatný stav úkolu.")
    cursor = conn.cursor()
    cursor.execute("UPDATE ukoly SET stav = %s WHERE id = %s", (novy_stav, id_ukolu))
    if cursor.rowcount == 0:
        raise ValueError("Úkol s tímto ID neexistuje.")
    conn.commit()
    cursor.close()

def odstranit_ukol(conn, id_ukolu=None):
    cursor = conn.cursor()

    if id_ukolu is None:
        
        cursor.execute("SELECT id, nazev FROM ukoly")
        ukoly = cursor.fetchall()

        if not ukoly:
            print("Žádné úkoly k odstranění.")
            return

        print("Seznam úkolů:")
        for id_, nazev in ukoly:
            print(f"{id_} - {nazev}")

        try:
            id_ukolu = int(input("Zadej ID úkolu ke smazání: "))
        except ValueError:
            print("Neplatné ID.")
            return

    
    cursor.execute("DELETE FROM ukoly WHERE id = %s", (id_ukolu,))
    conn.commit()

    if cursor.rowcount == 0:
        raise ValueError("Úkol s tímto ID neexistuje.")

    cursor.close()


def hlavni_menu():
    vytvoreni_tabulky()
    conn = pripojeni_db()

    while True:
        print("\n--- Task Manager ---")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Aktualizovat úkol")
        print("4. Odstranit úkol")
        print("5. Ukončit")
        volba = input("Vyber možnost: ")

        if volba == "1":
            nazev = input("Zadej název úkolu: ")
            popis = input("Zadej popis úkolu: ")
            try:
                pridat_ukol(conn, nazev, popis)
                print("Úkol přidán.")
            except ValueError as e:
                print(e)

        elif volba == "2":
            ukoly = zobrazit_ukoly(conn)
            if not ukoly:
                print("Seznam úkolů je prázdný.")
            else:
                for u in ukoly:
                    print(f"{u[0]} | {u[1]} | {u[2]} | {u[3]}")

        elif volba == "3":
            ukoly = zobrazit_ukoly(conn)
            for u in ukoly:
                print(f"{u[0]}: {u[1]} ({u[3]})")
            try:
                id_ukolu = int(input("Zadej ID úkolu k aktualizaci: "))
                novy_stav = input("Zadej nový stav (probíhá/hotovo): ")
                aktualizovat_ukol(conn, id_ukolu, novy_stav)
                print("Stav úkolu byl aktualizován.")
            except ValueError as e:
                print(e)

        elif volba == "4":
            ukoly = zobrazit_ukoly(conn)
            for u in ukoly:
                print(f"{u[0]}: {u[1]}")
            try:
                id_ukolu = int(input("Zadej ID úkolu ke smazání: "))
                odstranit_ukol(conn, id_ukolu)
                print("Úkol byl odstraněn.")
            except ValueError as e:
                print(e)

        elif volba == "5":
            print("Program ukončen.")
            break
        else:
            print("Neplatná volba, zkus znovu.")

    conn.close()

if __name__ == "__main__":
    hlavni_menu()
