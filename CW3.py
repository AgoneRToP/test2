# # class Student:
# #     def __init__(self, name: str, student_id: str):
# #         self.name = name
# #         self.student_id = student_id
# #         self.__grades = []

# #     def add_grade(self, grade: float):
# #         if 0 <= grade <= 100:
# #             self.__grades.append(grade)
# #         else:
# #             raise ValueError("Grade must be between 0 and 100")

# #     def get_average_grade(self) -> float:
# #         if not self.__grades:
# #             return 0.0
# #         return sum(self.__grades) / len(self.__grades)

# #     def get_grades(self) -> list:
# #         return self.__grades.copy()

# #     def __str__(self) -> str:
# #         return f"Student Name: {self.name}, ID: {self.student_id}, Average Grade: {self.get_average_grade():.2f}"


# # if __name__ == "__main__":
# #     student1 = Student("Alice", "S12345")
# #     student1.add_grade(90)
# #     student1.add_grade(85)
# #     student1.add_grade(78)

# #     print(student1)
# #     print("All grades:", student1.get_grades())




# class Playlist:
#     def __init__(self, owner: str) -> None:
#         self.owner = owner
#         self.tracks: list[tuple[str, str]] = []

#     def add_track(self, title: str, artist: str) -> None:
#         """Qo'shiqni (title, artist) ko'rinishida ro'yxat oxiriga qo'shadi."""
#         self.tracks.append((title, artist))

#     def remove_last(self) -> tuple[str, str] | None:
#         """Oxirgi qo'shiqni o'chiradi va qaytaradi. Bo'sh bo'lsa None qaytaradi."""
#         if not self.tracks:
#             return None
#         return self.tracks.pop()

#     def total_tracks(self) -> int:
#         """Jami qo'shiqlar sonini qaytaradi."""
#         return len(self.tracks)

#     def unique_tracks(self) -> list[tuple[str, str]]:
#         """Takroriy qo'shiqlarni olib tashlab, noyob ro'yxatni qaytaradi."""
#         seen = set()
#         unique_list = []
#         for track in self.tracks:
#             if track not in seen:
#                 unique_list.append(track)
#                 seen.add(track)
#         return unique_list

#     def search_by_title(self, title: str) -> list[tuple[str, str]]:
#         """Berilgan nomdagi qo'shiqlarni topadi."""
#         return [track for track in self.tracks if track[0] == title]

#     def filter_by_artist(self, artist: str) -> list[tuple[str, str]]:
#         """Faqat berilgan ijrochiga tegishli qo'shiqlarni qaytaradi."""
#         return [track for track in self.tracks if track[1] == artist]

# if __name__ == "__main__":
#     pl = Playlist("Muhammad")

#     print(pl.total_tracks())                      

#     pl.add_track("Yomg'irlar", "Shahzoda")
#     pl.add_track("Gulim", "Yulduz Usmonova")
#     pl.add_track("Yomg'irlar", "Shahzoda")
#     pl.add_track("Xayr edi", "Lola")
#     pl.add_track("Kel", "Ulug'bek Rahmatullayev")

#     print(pl.total_tracks())                      

#     print(pl.unique_tracks())                     

#     print(pl.remove_last())                       

#     print(pl.total_tracks())

#     print(pl.search_by_title("Yomg'irlar"))       

#     print(pl.filter_by_artist("Yulduz Usmonova")) 



class Employee:
    def __init__(self, name: str, employee_id: str, hourly_rate: float = 15.0) -> None:
        self.name = name
        self.employee_id = employee_id
        self.__working_hours: list[int] = []
        self.hourly_rate = hourly_rate

    def log_hours(self, hour: int) -> bool:
        """Kunlik ishlagan soatlarni ro'yxatga qo'shadi (0-24 oralig'ida)."""
        if 0 <= hour <= 24:
            self.__working_hours.append(hour)
            return True
        return False

    def total_hours(self) -> int:
        """Barcha kunlik ishlagan soatlarning yig'indisini qaytaradi."""
        return sum(self.__working_hours)

    def calculate_salary(self) -> float:
        """Umumiy soatlar va soatlik stavka asosida maoshni hisoblaydi."""
        return self.total_hours() * self.hourly_rate

    def reset_hours(self) -> None:
        """Ishlangan soatlar ro'yxatini tozalaydi."""
        self.__working_hours = []

if __name__ == "__main__":
    employee = Employee("Javlon", "E101", hourly_rate=20.0)

    print(employee.log_hours(8))   	
    print(employee.log_hours(9))   	
    print(employee.log_hours(10))  	
    print(employee.log_hours(25))  	

    print(employee.total_hours())       	
    print(employee.calculate_salary())  	

    employee.reset_hours()
    print(employee.total_hours())       	
    print(employee.calculate_salary())  	