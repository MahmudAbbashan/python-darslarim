# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:47:26 2021

@author: Abbos
"""

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
# qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

# def malumot_baza(ism, familya, t_yil, t_joy, pochta='', tel=''):
#     yosh = 2021
#     baza = {'ism':ism,
#             'familya':familya,
#             'yosh':yosh-t_yil,
#             't_yil':t_yil,
#             't_joy':t_joy,
#             'pochta':'pochtasi',
#             'tel':'teli',}
#     return baza
# baza=[]

# while True:
#      print("\nQuyidagi ma'lumotlarni kiriting",end='')
#      ism=input("Ismingiz: ")
#      familya=input("Familyangiz: ")
#      t_yil=int(input("Tug'ilgan yilingiz: "))
#      t_joy=input("Tug'ilgan joyingiz: ")
#      pochta=input("Elektron manzilingiz: ")
#      tel=input("Telefon raqamingiz: ")
     
#      baza.append(malumot_baza(ism, familya, t_yil, t_joy, pochta, tel))
     
#      javob = input("Yana avto qo'shasizmi? (yes/no): ")    
#      if javob=='no':        
#          break
    

# def eng_katta_son_chiqar():
#     a=input("Son kiriting: ")
#     b=input("Son kiriting: ")
#     c=input("Son kiriting: ")
#     if a>b and a>c:
#         print(f"Eng katta son {a}")
#     elif b>a and b>c:
#         print(f"Eng katta son {b}")
#     else:
#         print(f"Eng katta son {c}")
# eng_katta_son_chiqar()



def aylana_radius_hisobla(aylana='' ,diametr='', perimetr='', yuzi=''):
    r = {'aylana':aylana,'diametr':diametr,'perimetr':perimetr,'yuzi':yuzi}
    aylana = int(input("Aylananing radiusini kiriting: "))
    diametr = int(2*aylana)
    perimetr = int(2*3.14*aylana)
    yuzi = int(3.14*(aylana*2))
    baza=[]
    baza.append(aylana_radius_hisobla(aylana, diametr, perimetr, yuzi))
    
    return baza
    
aylana_radius_hisobla()
    

















