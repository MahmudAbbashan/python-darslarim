# ismlar = ['Abbos', 'Izzat', 'Sasha', 'Dilmurod', 'MIrsodiq']
# for ism in ismlar:
#         print(f"Salom {ism}")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# sonlar = list(range(11,100,2))
# for son in sonlar:
#      print(son**3)
# odamlar_soni = int(input(f"Nechta odam bilan suhbat qurdingiz>>> "))
# odamlar = []
# # print("Yaxshi ko'rgan kinolaringizni yozing:")
# for odam in range (odamlar_soni):
#     odamlar.append(input(f"{odam+1}-odam nomi yozing: "))
# print(f"siz gaplashgan odam soni {len(odamlar)} ta ")
# print(odamlar)


# avtolar = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto != 'gm':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

# ism = input("Ismingizni yozing\n>>>>")
# if ism.lower() == 'admin':
#         print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#         print(f"Xush kelibsiz {ism.title()}")

# son_1 = int(input("birinchi sonni kiriting>> "))
# son_2 = int(input("ikkinchi sonni kiriting>> "))
# if son_1 == son_2:
#     print("Sonlar teng ekan")
# else: print("Sonlar teng emas")

# son = int(input("Istalgan sonni kiriting>>"))
# if son>0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

# import math
# son = int(input("Son kiriting>>>>"))
# if son > 0:
#     print(math.sqrt(son))
# else: print("Musbat son kiriting!!!")


son = int(input("Son kiriting>>>"))
if son%2:
    print("Bu son juft emas")
else: 
    print("Rahmat")


# yosh = int(input("Yoshingizni kiriting>>>"))
# if yosh <4 or yosh >60:
#     narh = 0
# elif yosh<18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Sizga kirish {narh} so'm")

# a = float(input("Birinchi sonni kiriting>>>"))
# b = float(input("Ikkinchi sonni kiriting>>>"))
# if a<b:
#     print(f"{a}<{b}")
# else:
#     print(f"{a}>{b}")

# mahsulotlar = ['olma', 'olcha','banan','kivi','anor','shaftoli','anjir','uzum', 'nok', 'xurma', 'behi']
# savat = []

# for meva in range(5):
#         savat.append(input(f"Savatga {meva+1} mahsulotni qo'shing:  "))
# if savat:
#         for meva in savat:
#             if meva in mahsulotlar:
#                 print(f"Do'konimizda {meva} bor")
#             else:
#                 print(f"Kechirasiz, do'konimzda {meva} yo'q")
# else:
#     print("Savatchangiz bo'sh")

# mahsulotlar = ['olma', 'olcha','banan','kivi','anor','shaftoli','anjir','uzum', 'nok', 'xurma', 'behi']
# savat = []
# bor_mahsulot= []
# mavjud_emas = []
# for meva in range(5):
#         savat.append(input(f"Savatga {meva+1} mahsulotni qo'shing:  "))
# if savat:
#         for meva in savat:
#             if meva in mahsulotlar:
#                 bor_mahsulot.append(meva)
#             else:
#                 mavjud_emas.append(meva)
# print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for narsa in mavjud_emas:
#     print(narsa)
# # else:
#     print("Savatchangiz bo'sh")
        
# foydalanuvchi = input("Yangi login kiriting:  ")
# foydalanuvchilar = ['anvar', 'abbos','izzat','dilmurod','sasha']
# # if foydalanuvchi:
#      # for ism in foydalanuvchi:
# if foydalanuvchi.lower() in foydalanuvchilar:
#     print("Login band, boshqa login tanlang!")
# else:
#     print("Xush kelibsiz!!!")

# son =int(input("Istalgan butun sonni kiriting: "))
# for n in range(2,11):
#         if not (son%n):
#             print(f"{son} soni {n}ga qoldiqsiz bo'linadi")


























