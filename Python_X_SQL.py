import pymysql

# class MySQL:
#     def __init__(self):
#         self.ConnectDB()
#         self.CreateDB()
#         self.CreateCompany()

#     def ConnectDB(self):
#         self.db = pymysql.connect(
#             host = 'localhost',
#             user = 'root',
#             password = '1234'
#         )
#         self.c = self.db.cursor()

#     def CreateDB(self):
#         self.c.execute("CREATE DATABASE IF NOT EXISTS aa2;")
#         self.c.execute("USE aa2")

#     def CreateCompany(self):
#         self.c.execute("""CREATE TABLE IF NOT EXISTS Company (
#                             name VARCHAR(100),
#                             location VARCHAR(100),
#                             capital BIGINT,
#                             employees_count INT,
#                             establishedAt INT,
#                             monthly_expenses INT
#                             )""")
    
#     def InsertCompany(self):
#         self.c.execute(f"""INSERT INTO Company (name, location, capital, employees_count, establishedAt, monthly_expenses)
#                             VALUES 
#                             ('Artel', 'Tashkent', 500000000, 15000, 2011, 2000000),
#                             ('Korzinka', 'Tashkent', 300000000, 5000, 1996, 1200000),
#                             ('Bukhara Gold', 'Bukhara', 150000000, 200, 2018, 500000),
#                             ('Samarkand Tea', 'Samarkand', 250000000, 450, 2005, 800000),
#                             ('Navoi Industry', 'Navoi', 900000000, 20000, 1992, 5000000)
#                             """)
#         self.db.commit()

#     def First(self):
#         self.c.execute(f'''SELECT * FROM Company 
#                             ORDER BY name ASC 
#                             ''')
#         return self.c.fetchall()
    
#     def Second(self):
#         self.c.execute(f'''SELECT * FROM Company 
#                             ORDER BY capital DESC
#                             ''')
#         return self.c.fetchall()
    
#     def Third(self):
#         self.c.execute(f'''SELECT * FROM Company 
#                             ORDER BY employees_count ASC 
#                             LIMIT 1''')
#         return self.c.fetchall()

#     def Forth(self):
#         self.c.execute(f'''SELECT * FROM Company 
#                             WHERE location = "Tashkent"
#                             ''')
#         return self.c.fetchall()

#     def Fifth(self):
#         self.c.execute(f'''SELECT location, COUNT(*) as company_count
#                             FROM Company 
#                             GROUP BY location
#                             ''')
#         return self.c.fetchall()

#     def Sixth(self):
#         self.c.execute(f'''SELECT name, 
#                                 (2026 - establishedAt) * 12 * monthly_expenses AS total_expenses_till_now 
#                             FROM Company
#                             ''')
#         return self.c.fetchall()

# dbm = MySQL()

# ## dbm.InsertCompany()

# for i in dbm.First():
#     print(i)

# print("==================")

# for i in dbm.Second():
#     print(i)

# print("==================")

# for i in dbm.Third():
#     print(i)

# print("==================")

# for i in dbm.Forth():
#     print(i)

# print("==================")

# for i in dbm.Fifth():
#     print(i)

# print("==================")

# for i in dbm.Sixth():
#     print(i)



class RestoranDB:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
        )
        self.c = self.db.cursor()
        self.CreateDB()
        self.CreateTB()

    def CreateDB(self):
        self.c.execute("CREATE DATABASE IF NOT EXISTS aa3;")
        self.c.execute("USE aa3")

    def CreateTB(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS Restoranlar (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100),
                        address VARCHAR(150),
                        maxFoodPrice INT,
                        minFoodPrice INT,
                        employeesCount INT,
                        experience INT
                            )""")
    
    def InsertTB(self):
        self.c.execute(f"""INSERT INTO Restoranlar (name, address, maxFoodPrice, minFoodPrice, employeesCount, experience)
                        VALUES 
                        ('Maroqand', 'Toshkent', 150000, 45000, 25, 10),
                        ('Minor', 'Samarqand', 80000, 25000, 15, 5),
                        ('Milliy Taomlar', 'Fargona', 120000, 30000, 40, 12),
                        ('Mazali', 'Xiva', 95000, 20000, 10, 3),
                        ('Rayhon', 'Toshkent', 110000, 35000, 100, 15),
                        ('Manzara', 'Bo`stonliq', 300000, 80000, 50, 8),
                        ('Osh Markazi', 'Toshkent', 60000, 25000, 60, 20),
                        ('Movarounnahr', 'Buxoro', 200000, 55000, 30, 7),
                        ('Sezam', 'Namangan', 85000, 22000, 18, 4),
                        ('Mir', 'Andijon', 50000, 15000, 8, 2)
                       """)
        self.db.commit()

    def task_1(self):
        self.c.execute("""SELECT * FROM Restoranlar 
                   WHERE name LIKE 'M%r'
                   ORDER BY maxFoodPrice ASC""")
        return self.c.fetchall()

    def task_2(self):
        self.c.execute("""SELECT name FROM Restoranlar 
                   ORDER BY minFoodPrice ASC 
                   LIMIT 3""")
        return self.c.fetchall()

    def task_3(self):
        self.c.execute("""SELECT name, maxFoodPrice FROM Restoranlar 
                   ORDER BY experience DESC, maxFoodPrice DESC 
                   LIMIT 4""")
        return self.c.fetchall()

rest = RestoranDB()

# rest.InsertTB()

for i in rest.task_1():
    print(i)

print("==================")

for i in rest.task_2():
    print(i)

print("==================")

for i in rest.task_3():
    print(i)
