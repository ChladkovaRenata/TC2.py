from task_manager import pripojeni_db, vytvoreni_tabulky
from task_manager import pridat_ukol, zobrazit_ukoly, aktualizovat_ukol, odstranit_ukol

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
