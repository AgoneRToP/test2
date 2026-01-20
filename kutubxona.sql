CREATE TABLE genre(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL UNIQUE);

INSERT INTO genre(name) VALUES("Badiiy"), ("Ilmiy"), ("Horror");

CREATE TABLE author(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL UNIQUE);
INSERT INTO author(name) VALUES("Alisher Navoiy"),("Oybek"),("Zulfiya"),("Pushkin");

CREATE TABLE book(id INT AUTO_INCREMENT PRIMARY KEY, 
                    name VARCHAR(50) NOT NULL,
                    price REAL,
                    sold SMALLINT,
                    genre_id INT,
                    author_id INT,
                    FOREIGN KEY (genre_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (author_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE);

INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("1984", 72000, 85, 1, 4);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Harry Potter", 200000, 50, 3, 1);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Garov", 12000, 140, 2, 3);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Sariq Devni minib", 80000, 150, 2, 2);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Ming bir kecha", 2000, 5, 1, 1);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Hamsa", 7000, 3, 1, 3);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Islom olami", 2000, 2000, 2, 1);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Zolotoy Braslet", 45000, 1000, 3, 1);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Yapon Zobiti", 78000, 4, 3, 3);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Voyna i Mir", 7200, 5, 2, 4);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Zolushka", 79000, 2, 1, 1);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Oppog'oy", 700, 5, 3, 3);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Ne Tupi", 80000, 77, 2, 2);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("MEN", 720, 85, 1, 1);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("O'tgan KUnlar", 2000, 85, 1, 2);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Temur Tuzuklari", 22000, 85, 3, 4);
INSERT INTO book(name, price, sold, genre_id, author_id) VALUES("Boy bo'lish sirlari", 2000, 85, 2, 4);



select * From book as b
    inner join author as a
    on b.author_id = a.id;
+----+---------------------+--------+------+----------+-----------+----+----------------+
| id | name                | price  | sold | genre_id | author_id | id | name           |
+----+---------------------+--------+------+----------+-----------+----+----------------+
|  2 | Harry Potter        | 200000 |   50 |        3 |         1 |  1 | Alisher Navoiy |
|  5 | Ming bir kecha      |   2000 |    5 |        1 |         1 |  1 | Alisher Navoiy |
|  7 | Islom olami         |   2000 | 2000 |        2 |         1 |  1 | Alisher Navoiy |
|  8 | Zolotoy Braslet     |  45000 | 1000 |        3 |         1 |  1 | Alisher Navoiy |
| 11 | Zolushka            |  79000 |    2 |        1 |         1 |  1 | Alisher Navoiy |
| 14 | MEN                 |    720 |   85 |        1 |         1 |  1 | Alisher Navoiy |
|  4 | Sariq Devni minib   |  80000 |  150 |        2 |         2 |  2 | Oybek          |
| 13 | Ne Tupi             |  80000 |   77 |        2 |         2 |  2 | Oybek          |
| 15 | O'tgan KUnlar       |   2000 |   85 |        1 |         2 |  2 | Oybek          |
|  1 | 1984                |  72000 |   85 |        1 |         4 |  4 | Pushkin        |
| 10 | Voyna i Mir         |   7200 |    5 |        2 |         4 |  4 | Pushkin        |
| 16 | Temur Tuzuklari     |  22000 |   85 |        3 |         4 |  4 | Pushkin        |
| 17 | Boy bo'lish sirlari |   2000 |   85 |        2 |         4 |  4 | Pushkin        |
|  3 | Garov               |  12000 |  140 |        2 |         3 |  3 | Zulfiya        |
|  6 | Hamsa               |   7000 |    3 |        1 |         3 |  3 | Zulfiya        |
|  9 | Yapon Zobiti        |  78000 |    4 |        3 |         3 |  3 | Zulfiya        |
| 12 | Oppog'oy            |    700 |    5 |        3 |         3 |  3 | Zulfiya        |
+----+---------------------+--------+------+----------+-----------+----+----------------+




SELECT a.name, JSON_ARRAYAGG(b.name), COUNT(*) AS miqdor FROM book AS b
JOIN author AS a
ON a.id = b.author_id
GROUP BY a.id;

+----------------+-----------------------------------------------------------------------------------------+--------+
| name           | JSON_ARRAYAGG(b.name)                                                                   | miqdor |
+----------------+-----------------------------------------------------------------------------------------+--------+
| Alisher Navoiy | ["Harry Potter", "Ming bir kecha", "Islom olami", "Zolotoy Braslet", "Zolushka", "MEN"] |      6 |
| Oybek          | ["Sariq Devni minib", "Ne Tupi", "O'tgan KUnlar"]                                       |      3 |
| Zulfiya        | ["Garov", "Hamsa", "Yapon Zobiti", "Oppog'oy"]                                          |      4 |
| Pushkin        | ["1984", "Voyna i Mir", "Temur Tuzuklari", "Boy bo'lish sirlari"]                       |      4 |
+----------------+-----------------------------------------------------------------------------------------+--------+


select * From book as b
    inner join author as a
    on b.author_id = a.id
    inner join genre as g
    on g.id = b.genre_id;
+----+---------------------+--------+------+----------+-----------+----+----------------+----+--------+
| id | name                | price  | sold | genre_id | author_id | id | name           | id | name   |
+----+---------------------+--------+------+----------+-----------+----+----------------+----+--------+
|  2 | Harry Potter        | 200000 |   50 |        3 |         1 |  1 | Alisher Navoiy |  3 | Horror |
|  5 | Ming bir kecha      |   2000 |    5 |        1 |         1 |  1 | Alisher Navoiy |  1 | Badiiy |
|  7 | Islom olami         |   2000 | 2000 |        2 |         1 |  1 | Alisher Navoiy |  2 | Ilmiy  |
|  8 | Zolotoy Braslet     |  45000 | 1000 |        3 |         1 |  1 | Alisher Navoiy |  3 | Horror |
| 11 | Zolushka            |  79000 |    2 |        1 |         1 |  1 | Alisher Navoiy |  1 | Badiiy |
| 14 | MEN                 |    720 |   85 |        1 |         1 |  1 | Alisher Navoiy |  1 | Badiiy |
|  4 | Sariq Devni minib   |  80000 |  150 |        2 |         2 |  2 | Oybek          |  2 | Ilmiy  |
| 13 | Ne Tupi             |  80000 |   77 |        2 |         2 |  2 | Oybek          |  2 | Ilmiy  |
| 15 | O'tgan KUnlar       |   2000 |   85 |        1 |         2 |  2 | Oybek          |  1 | Badiiy |
|  1 | 1984                |  72000 |   85 |        1 |         4 |  4 | Pushkin        |  1 | Badiiy |
| 10 | Voyna i Mir         |   7200 |    5 |        2 |         4 |  4 | Pushkin        |  2 | Ilmiy  |
| 16 | Temur Tuzuklari     |  22000 |   85 |        3 |         4 |  4 | Pushkin        |  3 | Horror |
| 17 | Boy bo'lish sirlari |   2000 |   85 |        2 |         4 |  4 | Pushkin        |  2 | Ilmiy  |
|  3 | Garov               |  12000 |  140 |        2 |         3 |  3 | Zulfiya        |  2 | Ilmiy  |
|  6 | Hamsa               |   7000 |    3 |        1 |         3 |  3 | Zulfiya        |  1 | Badiiy |
|  9 | Yapon Zobiti        |  78000 |    4 |        3 |         3 |  3 | Zulfiya        |  3 | Horror |
| 12 | Oppog'oy            |    700 |    5 |        3 |         3 |  3 | Zulfiya        |  3 | Horror |
+----+---------------------+--------+------+----------+-----------+----+----------------+----+--------+

SELECT DISTINCT g.name AS genre
FROM genre g
JOIN book b ON g.id = b.genre_id
JOIN author a ON b.author_id = a.id
WHERE a.name = 'Alisher Navoiy';

SELECT a.name,
       GROUP_CONCAT(DISTINCT g.name) AS janrlar
FROM author a
JOIN book b ON a.id = b.author_id
JOIN genre g ON b.genre_id = g.id
GROUP BY a.name;

SELECT a.name,
       g.name AS genre,
       COUNT(b.id) AS kitob_soni
FROM author a
JOIN book b ON a.id = b.author_id
JOIN genre g ON b.genre_id = g.id
GROUP BY a.name, g.name;

SELECT g.name AS genre,
       COUNT(b.id) AS jami_kitoblar
FROM genre g
JOIN book b ON g.id = b.genre_id
GROUP BY g.name
ORDER BY jami_kitoblar DESC
LIMIT 1;

SELECT a.name,
       g.name AS genre,
       COUNT(b.id) AS soni
FROM author a
JOIN book b ON a.id = b.author_id
JOIN genre g ON b.genre_id = g.id
GROUP BY a.name, g.name
HAVING soni = (
    SELECT MAX(cnt)
    FROM (
        SELECT author_id, genre_id, COUNT(*) AS cnt
        FROM book
        GROUP BY author_id, genre_id
    ) sub
    WHERE sub.author_id = a.id
);

SELECT a.name,
       SUM(b.sold) AS jami_sotuv
FROM author a
JOIN book b ON a.id = b.author_id
GROUP BY a.name
ORDER BY jami_sotuv DESC
LIMIT 1;

