from random import *
from module1 import *
import keyboard
inimesed = ["A", "B", "C", "D", "E"]
palgad = [1200,2500,750,395,1200]

while 1:
    valik=input("e -Показать данные \nk - Удаление\nmax - Максимальная зарплата\nmin - Минимальня зарплата\ns - Добавить юзера\nkoik - Все зарплаты сотрудников вместе\ndel - Очистить список зарплат и сотрудников\nsrch - poisk")
    if valik.lower() == "e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower() == "k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower() == "max":
        maksimum(inimesed, palgad)
    elif valik.lower() == "min":
        minimum(inimesed, palgad)
    elif valik.lower() == "s":
        sisesta_andmed(inimesed, palgad)
    elif valik.lower() == "koik":
        koik_palk(inimesed, palgad)
    elif valik.lower() == "del":
        koik_del(inimesed, palgad)
    elif valik.lower() == "srch":
        modulizm(inimesed, palgad)
    else:
        break
