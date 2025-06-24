from task_manager import pripojeni_db

conn = pripojeni_db(test=False)
if conn:
    print("Připojení OK")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    print("Tabulky:", cursor.fetchall())
    cursor.close()
    conn.close()
else:
    print("Nepodařilo se připojit.")