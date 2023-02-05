# Шифр Цезаря
# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром Цезаря и возвращает его. 
# Шифр Цезаря заменяет каждую букву в тексте на букву, которая стоит в алфавите на Х позиций назад.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то сдивгаем на 3
# Все символы, кроме русских букв должны остаться неизменными. 
# Маленькие буквы должны превращаться в маленькие, большие — в большие.

# Алфавит (маленький, большой)
a = 'а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ы,ь,э,ю,я'
alf_small = list(a.split(','))
alf_big = [i.title() for i in alf_small]
alf_small_rev = list(alf_small.__reversed__())
alf_big_rev = list(alf_big.__reversed__())

# Ввод текста пользователем
text = input('Введите текст для шифрования ')
shift = input('Введите шифт (=на сколько позиций нужно сдвинуть букву при шифровании) ')


# Функция шифрования Цезаря
def cezar (text, shift=3):
    shift=int(shift)
    shifr = ''
    for i in text:
        if i in alf_small:
            shifr=shifr + alf_small[alf_small.index(i)-shift]
        elif i in alf_big:
            shifr=shifr + alf_big[alf_big.index(i)-shift]
        else:
            shifr=shifr + i
    return shifr

if shift=='':
    result = cezar(text)
else:
    result = cezar(text,shift)

# Вывод
print(f'Текст " {text} " зашифрован в " {result} " ')

