from random import *
inimesed = ["A", "B", "C", "D", "E"]
palgad = [1200,2500,750,395,1200]
def sisesta_andmed(i, p):
    """Добавление юзера в список, а также зарплата
    """
    N = 1
    for n in range(N):
        inimene = input("Введите имя: ")
        i.append(inimene)
        palk=int(input("Введите зарплату: "))
        p.append(palk )
    return i,p
def andmed_ekranile(i, p):
    """Показать список людей и зарплат
    """
    N=len(i)
    for n in range(N):
        print(f"{i[n]} - {p[n]}")
def kustutamine(i, p):
    """Удаляет имя и зарплату человека из списка
    """
    nimi=input("Введите имя человека, которого нужно удалить: ")
    n=i.count(nimi)
    abi_list=[]
    if n > 0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(f"{t}.{i[e]} - {p[e]}")
        j=int(input("Порядковый номер человека: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def maksimum(i, p):
    """Выводит макимальную зарплату юзера из списка на экран
    """
    max_palk = palgad[0] 
    kellel = inimesed[0]
    for p in palgad:
        if p > max_palk:
            max_palk = p
            i = palgad.index(max_palk)
            kellel = inimesed[i]
    print(f"Максимальную зарплату - {max_palk} получает - {kellel}")
def minimum(i, p):
    """Выводит минимальную зарплату юзера из списка на экран
    """
    min_palk = palgad[0]
    kellel = inimesed[0]
    for p in palgad:
        if p < min_palk:
            min_palk = p
            i = palgad.index(min_palk)
            kellel = inimesed[i]
    print(f"Минимальную зарплату - {min_palk} получает - {kellel}.")
def koik_palk(i, p):
    """Складывает все зарплаты и выводит на экран
    """
    summa=sum(palgad)
    print("Зарплаты всех сотрудников -", summa)
def koik_del(i, p):
    """Очищает список
    """
    delit=int(input("Хотите очистить список?\n1 - Да\n2 - Нет"))
    if delit == 1:
        palgad = []
        inimesed = []
    elif delit == 2:
        print("Выход")
    else:
        ValueError
def modulizm(i, p):
    """Проверяет есть ли пользователь по поиску имени в списке
    """
    imya=str(input("Введите имя человека которого хотите найти в списке"))
    if imya in (inimesed):
        print (imya)
    elif imya not in (inimesed):
        vvod=int(input("Данного имени нет в списке, хотите добавить юзера?\n1-Da\n2-Net"))
        if vvod == 1:
            sisesta_andmed(i, p)
        elif vvod == 2:
            return
        else:
            ValueError
