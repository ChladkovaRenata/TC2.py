CREATE DATABASE IF NOT EXISTS test_task_manager;
SHOW DATABASES;
USE test_task_manager;
SELECT * FROM ukoly;
SHOW TABLES;

CREATE TABLE IF NOT EXISTS ukoly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(255) NOT NULL,
    popis TEXT NOT NULL,
    stav ENUM('nezahájeno', 'probíhá', 'hotovo') NOT NULL DEFAULT 'nezahájeno',
    datum_vytvoreni DATETIME
);
SELECT DATABASE();
DESCRIBE ukoly;