# Декодировщик Цезаря

# Алфавит (маленький, большой)
a = 'а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ы,ь,э,ю,я'
alf_small = list(a.split(','))
alf_big = [i.title() for i in alf_small]
alf_small_rev = list(alf_small.__reversed__())
alf_big_rev = list(alf_big.__reversed__())

# Ввод текста пользователем
text = input('Введите текст для декодирования ')
shift = input('Введите шифт (=на сколько позиций нужно сдвинуть букву при шифровании) ')


# Функция ДЕкодирование Цезаря
def cezar (text, shift=3):
    shift=int(shift)
    shifr = ''
    for i in text:
        if i in alf_small_rev:
            shifr=shifr + alf_small_rev[alf_small_rev.index(i)-shift]
        elif i in alf_big_rev:
            shifr=shifr + alf_big_rev[alf_big_rev.index(i)-shift]
        else:
            shifr=shifr + i
    return shifr

if shift=='':
    result = cezar(text)
else:
    result = cezar(text,shift)

# Вывод
print(f'Текст " {text} " декодирован в " {result} " ')