
MYSQL GROUP BY UYGA VAZIFA (JOIN ISHTIROK ETMAYDI)

Jadval: sales
Ustunlar:
id, product_name, category, price, quantity, sale_date

--------------------------------------------------
JADVAL YARATISH
--------------------------------------------------
CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT,
    quantity INT,
    sale_date DATE
);

--------------------------------------------------
MA'LUMOTLAR (20 ta INSERT)
--------------------------------------------------
INSERT INTO sales VALUES (1, 'Laptop', 'Electronics', 800, 2, '2025-01-01');
INSERT INTO sales VALUES (2, 'Phone', 'Electronics', 600, 3, '2025-01-01');
INSERT INTO sales VALUES (3, 'TV', 'Electronics', 900, 1, '2025-01-02');
INSERT INTO sales VALUES (4, 'Headphones', 'Electronics', 150, 5, '2025-01-03');

INSERT INTO sales VALUES (5, 'Table', 'Furniture', 300, 1, '2025-01-01');
INSERT INTO sales VALUES (6, 'Chair', 'Furniture', 100, 4, '2025-01-02');
INSERT INTO sales VALUES (7, 'Sofa', 'Furniture', 1200, 1, '2025-01-03');
INSERT INTO sales VALUES (8, 'Bed', 'Furniture', 900, 1, '2025-01-04');

INSERT INTO sales VALUES (9, 'T-shirt', 'Clothing', 40, 6, '2025-01-01');
INSERT INTO sales VALUES (10, 'Jeans', 'Clothing', 70, 3, '2025-01-02');
INSERT INTO sales VALUES (11, 'Jacket', 'Clothing', 120, 2, '2025-01-03');
INSERT INTO sales VALUES (12, 'Shoes', 'Clothing', 90, 4, '2025-01-04');

INSERT INTO sales VALUES (13, 'Apple', 'Food', 2, 20, '2025-01-01');
INSERT INTO sales VALUES (14, 'Bread', 'Food', 3, 15, '2025-01-02');
INSERT INTO sales VALUES (15, 'Milk', 'Food', 4, 10, '2025-01-03');
INSERT INTO sales VALUES (16, 'Cheese', 'Food', 8, 5, '2025-01-04');

INSERT INTO sales VALUES (17, 'Notebook', 'Stationery', 5, 10, '2025-01-01');
INSERT INTO sales VALUES (18, 'Pen', 'Stationery', 2, 25, '2025-01-02');
INSERT INTO sales VALUES (19, 'Marker', 'Stationery', 4, 12, '2025-01-03');
INSERT INTO sales VALUES (20, 'Folder', 'Stationery', 6, 8, '2025-01-04');

--------------------------------------------------
MASALALAR (TOP 10)
--------------------------------------------------

1. Har bir kategoriya bo'yicha nechta mahsulot sotilganini toping.
2. Har bir kategoriya bo'yicha jami sotuv summasini chiqaring.
3. Har bir kategoriya bo'yicha o'rtacha narxni hisoblang.
4. Har bir kun bo'yicha jami tushumni toping.
5. Faqat Electronics kategoriyasidagi mahsulotlar bo'yicha umumiy tushumni hisoblang.
6. Jami sotuv summasi 2000 dan katta bo'lgan kategoriyalarni chiqaring.
7. O'rtacha narxi 100 dan yuqori bo'lgan kategoriyalarni toping.
8. 2025-01-01 sanasida nechta mahsulot sotilganini aniqlang.
9. Eng ko'p miqdorda (quantity) sotilgan kategoriyani toping.
10. 3 martadan ko'p sotilgan (quantity > 3) mahsulotlar bo'yicha kategoriyalar kesimida jami tushumni chiqaring.

ESLATMA:
- JOIN ishlatilmaydi
- WHERE - guruhlashdan oldin
- HAVING - guruhlashdan keyin
- GROUP BY agregat funksiyalar bilan ishlatiladi

----------------------------------------------------

SELECT category, SUM(quantity) AS total_products_sold
FROM sales
GROUP BY category;

SELECT category, SUM(price * quantity) AS total_sales_amount
FROM sales
GROUP BY category;

SELECT category, AVG(price) AS average_price
FROM sales
GROUP BY category;

SELECT sale_date, SUM(price * quantity) AS daily_revenue
FROM sales
GROUP BY sale_date;

SELECT SUM(price * quantity) AS electronics_total_revenue
FROM sales
WHERE category = 'Electronics';

SELECT category, SUM(price * quantity) AS total_sales_amount
FROM sales
GROUP BY category
HAVING total_sales_amount > 2000;

SELECT category, AVG(price) AS average_price
FROM sales
GROUP BY category
HAVING average_price > 100;

SELECT SUM(quantity) AS total_products_sold_on_2025_01_01
FROM sales
WHERE sale_date = '2025-01-01';

SELECT category, SUM(quantity) AS total_quantity_sold
FROM sales
GROUP BY category
ORDER BY total_quantity_sold DESC
LIMIT 1;

SELECT category, SUM(price * quantity) AS total_revenue
FROM sales
WHERE quantity > 3
GROUP BY category;