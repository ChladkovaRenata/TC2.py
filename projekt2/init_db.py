import mysql.connector

def inicializuj_databazi():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Norbinka28.'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_task_manager")
    cursor.close()
    conn.close()

def inicializuj_tabulku():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Norbinka28.',
        database='test_task_manager'
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ukoly (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nazev VARCHAR(255) NOT NULL,
            popis TEXT NOT NULL,
            stav ENUM('nezahájeno', 'probíhá', 'hotovo') NOT NULL DEFAULT 'nezahájeno',
            datum_vytvoreni TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    inicializuj_databazi()
    inicializuj_tabulku()
    print("Databáze a tabulka byly úspěšně vytvořeny.")