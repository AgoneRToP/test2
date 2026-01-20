CREATE TABLE courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    Instructor VARCHAR(100) NOT NULL,
    DurationHr DECIMAL(4,1) NOT NULL,
    Price DECIMAL(8,2) DEFAULT 0,
    Rating DECIMAL(2,1) DEFAULT 0,
    Enrolled INT DEFAULT 0
);

INSERT INTO courses (Title, Instructor, DurationHr, Price, Rating, Enrolled) VALUES

('Python asoslari', 'Muhammad Narzullaev', 45.5, 500000.00, 4.9, 1200),
('SQL ma''lumotlar bazasi', 'Elena Volkova', 30.0, 450000.00, 4.7, 850),
('Frontend: React JS', 'Sardorbek Shokirov', 60.5, 800000.00, 4.8, 450),
('Grafik dizayn: Photoshop', 'Lola Azizova', 25.0, 350000.00, 4.5, 320),
('IELTS 7.0 Intensive', 'Sardorbek Shokirov', 120.0, 1200000.00, 4.9, 1500),
('Java Backend development', 'Muhammad Hasanov', 90.0, 1000000.00, 4.6, 210),
('SMM va Target reklama', 'Lola Azizova', 15.5, 300000.00, 4.4, 670),
('Excel: Noldan professionalgacha', 'Sardorbek Shokirov', 12.0, 0, 4.8, 2100),
('Mobil dasturlash: Flutter', 'Sardorbek Shokirov', 55.0, 950000.00, 4.7, 180),
('Node.js va Express', 'Muhammad Narzullaev', 40.0, 700000.00, 4.6, 340),
('Rus tili: So''zlashuv', 'Elena Volkova', 48.0, 400000.00, 4.5, 890),
('Kiberxavfsizlik asoslari', 'Lola Azizova', 35.5, 0, 4.9, 150);

