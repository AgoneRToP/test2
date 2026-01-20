CREATE TABLE Talaba (id int, ism varchar(50), yosh smallint, baho real);

INSERT INTO Talaba VALUES
    (1, "Trevor", 47, 89);
    (2, "Michal", 44, 95);
    (3, "Franklin", 28, 90);
    (4, "Lamar", 27, 81);
    (5, "Tech", 41, 101);
    (6, "Lara", 24, 79);
    (7, "Vaas", 31, 60);
    (8, "Afton", 72, 68);
    (9, "Kitty", 99, 77);
    (10, "So In", 18, 85);

SELECT * FROM Talaba;

SELECT * FROM Talaba WHERE baho BETWEEN 90 and 101 ORDER BY ism;

SELECT * FROM Talaba WHERE baho BETWEEN 70 and 90 ORDER BY ism;

SELECT * FROM Talaba WHERE baho BETWEEN 60 and 70 ORDER BY ism;

CREATE TABLE Milliy_Taomlar (id int, taom_nomi varchar(50), taom_masaliqlari TEXT);

INSERT INTO Milliy_Taomlar VALUES
    (1, "PotatoMina", "Kartoshka va Mina");
    (2, "BloodyMary", "Tomat, Vodka va Blood");
    (3, "Energetics", "Yellow-Snow va Batareya");
    (4, "Palov", "Guruch va Bla-Bla");
    (5, "Sushi", "Balu, Guruch va Bla-Bla");
    (6, "Limonad", "Limon va H2O");
    (7, "Cola", "Shakar, KoKoS va Hasharotlar");
    (8, "Hot-Dog", "It va Non");
    (9, "Ice-Tea", "Muz va Choy");
    (10, "Tovuq", "Tuxum");

SELECT * FROM Milliy_Taomlar;

SELECT * FROM Milliy_Taomlar WHERE taom_nomi LIKE "%A";

SELECT * FROM Milliy_Taomlar WHERE taom_masaliqlari LIKE "%Guruch%";

CREATE TABLE PC (brand varchar(50), model varchar(50), cpu varchar(50), frequency real, ram int, os varchar(50), price real);

INSERT INTO PC (brand, model, cpu, frequency, ram, os, price) VALUES

('Apple',  'MacBook Air',  'Intel Core i5', 1.8,  8,  'macOS',        1200),
('Apple',  'MacBook Pro',  'Intel Core i7', 2.3, 16,  'macOS',        2200),
('Apple',  'MacBook Pro',  'Intel Core i7', 2.6, 16,  'macOS',        2400),
('Apple',  'MacBook Air',  'Apple M1',      3.2,  8,  'macOS',        1800),

('ASUS',   'ZenBook',      'Intel Core i7', 2.5, 16,  'Windows 11',   1500),
('ASUS',   'ZenBook',      'Intel Core i5', 2.0,  8,  'Windows 10',    900),
('ASUS',   'VivoBook',     'AMD Ryzen 5',   3.6,  8,  'Windows 11',    850),
('ASUS',   'ROG',          'Intel Core i7', 3.9, 16,  'Windows 11',   2500),

('Dell',   'XPS 13',       'Intel Core i7', 2.8, 16,  'Windows 11',   1800),
('Dell',   'Inspiron',     'Intel Core i5', 2.4,  8,  'Windows 10',    700),
('Dell',   'Inspiron',     'AMD Ryzen 5',   3.5,  8,  'Ubuntu 20.04',  650),
('Dell',   'Latitude',     'Intel Core i7', 2.6, 16,  'Windows 11',   1600),

('HP',     'Pavilion',     'Intel Core i5', 2.3,  8,  'Windows 10',    600),
('HP',     'EliteBook',    'Intel Core i7', 2.9, 16,  'Windows 11',   1400),
('HP',     'ProBook',      'AMD Ryzen 5',   3.7,  8,  'Windows 11',    750),
('HP',     'Pavilion',     'Intel Core i5', 2.1,  4,  'Ubuntu 20.04',  500),

('Lenovo', 'ThinkPad',     'Intel Core i7', 2.8, 16,  'Windows 11',   1700),
('Lenovo', 'ThinkPad',     'Intel Core i5', 2.4,  8,  'Windows 10',    800),
('Lenovo', 'IdeaPad',      'AMD Ryzen 5',   3.6,  8,  'Windows 11',    700),
('Lenovo', 'IdeaPad',      'Intel Core i7', 2.9, 16,  'Windows 11',   1300);

SELECT * FROM PC WHERE price = (SELECT MAX(price) FROM PC);

SELECT * FROM PC WHERE price = (SELECT MIN(price) FROM PC);

SELECT frequency FROM PC WHERE price BETWEEN 400 AND 1000 AND cpu LIKE '%Intel%';

SELECT COUNT(*) AS apple_count FROM PC WHERE brand = 'Apple';

SELECT * FROM PC WHERE brand = 'ASUS' AND os LIKE '%Windows%' AND ram <> 8 ORDER BY price ASC;