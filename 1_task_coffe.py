# Кафе, в котором на сейчас Х кофейных зерен, Х молока, Х взбитых сливок
# Приходит посетитель, говорит о своих препочтениях. Бариста вводит их в программу
# Программа выдает что можно приготовить исходя из доступных ингридиентов и предпочтений посетителя

# Норма расхода на напиток
esp = [1,0,0]
kap = [1,3,0]
mac = [2,1,0]
ven = [1,0,2]
lat = [1,2,1]
kon = [1,0,1]

# Ввод входных параметров для работы бариста
z = int(input('Сколько есть зерен '))
m = int(input('Сколько есть молока '))
s = int(input('Сколько есть сливок '))
ing = [z,m,s]

# Функция сравнения списков
def sravni (a,b):
    res=0
    for i in range(3):
        if a[i]>b[i]:
            res=res-1
        else:
            res=res+1
    return res

# Определение доступных напитков
dostupno = []
if sravni(esp,ing)==3:
    dostupno.append('esp')
if sravni(kap,ing)==3:
    dostupno.append('kap')
if sravni(mac,ing)==3:
    dostupno.append('mac')
if sravni(ven,ing)==3:
    dostupno.append('ven')
if sravni(lat,ing)==3:
    dostupno.append('lat')
if sravni(kon,ing)==3:
    dostupno.append('kon')

# Ввод предпочтений посетителя
want = input('Введите предпочтения посетителя через запятую ')
want_list = want.split(',')

# Сопоставление доступного и предпочтений
def choose (w,d):
    your_choose=[]
    for i in w:
        if i in d:
            your_choose.append(i)
    return your_choose

result = choose(want_list,dostupno)

# Печать результата
if result == []:
    print('Сейчас ничего приготовить не можем ')
else:
    print (f'Мы можем приготовить для вас {result}')