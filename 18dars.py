# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:19:14 2021

@author: Abbos
"""

# # Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# # Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# buyurtma = []
# n=1
# while True:
#     savol=f"{n}-mahsulot nomini kiriting: "
#     mahsulot=input(savol)
#     buyurtma.append(mahsulot)
#     javob= input('Yana mahsulot qo\'shasizmi? ha/yo\'q ')
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# # print("Mahsulotlar ro'txati")
# # for nom in buyurtma:
# #     print(nom.title())
    

# # e-bozor uchun mahsulotlar va ularning narhlari lug'atini
# # shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga 
# # bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.


# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot=input("Mahsulot nomini kiriting: ")
#     narh=input(f"{mahsulot.title()}ning narhini kiriting: " )
#     mahsulotlar[mahsulot]=int(narh)
    
#     javob= input('Yana mahsulot qo\'shasizmi? ha/yo\'q ')
#     if javob == 'ha':
#         continue
#     else:
#         break
# # print("Mahsulotlar ro'yxati:")
# # for mahsulot, narh in mahsulotlar.items():
# #     print(f"{mahsulot.title()} {narh} so'm")
    
# print("Bizda bor: ")   
# for info in buyurtma:   
#     if info not in mahsulotlar.keys():
#         print(f"{info.title()} mahsuloti bizda mavjud emas")
#     else:
#         print(f"{info.title()} {mahsulotlar[info]} so'm ") 