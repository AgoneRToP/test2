# class kitob:
#     def __init__(self, nomi, mual, narx, nash):
#         self.nomi = nomi
#         self.mual = mual
#         self.narx = narx
#         self.nash = nash

#     def __str__(self):
#         return f"""
# Kitob nomi: {self.nomi}
# Kitob mualliflari: {self.mual}
# Kitob narxi: {self.narx}
# Kitob nashriyoti: {self.nash}
# """
    
# lst = []

# for i in range(5):
#     lst.append(kitob(input("Kitob nomi: "), input("Kitob mualliflari: "), int(input("Kitob narxi: ")), input("Kitob nashriyoti: ")))

# for i in lst:
#     if i.nash[0].lower() in "abcdefgh":
#         print(i)



# class kompyuter:
#     def __init__(self, nomi, rami, narx, prot):
#         self.nomi = nomi
#         self.rami = rami
#         self.narx = narx
#         self.prot = prot

#     def __str__(self):
#         return f"""
# Kompyuter nomi: {self.nomi}
# Kompyuter RAMi: {self.rami}
# Kompyuter narxi: {self.narx}
# Kompyuter protsessor: {self.prot}
# """
    
# lst = []

# for i in range(4):
#     lst.append(kompyuter(input("Kompyuter nomi: "), int(input("Kompyuter RAMi: ")), int(input("Kompyuter narxi: ")), input("Kompyuter protsessor: ")))

# for i in lst:
#     if 4 < i.rami < 16:
#         print(i)



# class easy:
#     def __init__(self, nomi, nick, mail, prof):
#         self.nomi = nomi
#         self.nick = nick
#         self.mail = mail
#         self.prof = prof
    
#     def info(self):
#         print(f"""
# Foydalanuvchi: {self.nick}
# Ismi: {self.nomi}
# Email: {self.mail}
# Kasb: {self.prof}
# """)
        
# lst = [easy("Lola", "LOLLY", "LOL@university.edu", "Model"),
#        easy("Edward", "Eddy", "CoolEd@gmail.com", "Maker"),
#        easy("Banner", "!HULK!", "NotSheHulk@state.uz", "Model")]

# for i in range(len(lst)):
#     print(lst[i].info())