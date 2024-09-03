#Список который позже принтится в формате матрицы
xoCoords = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

#bool переменная, отвечающая за "есть ли победитель?"
have_winner = bool(False)

#Цикл выполняется до тех пор, пока нет победителя
while not have_winner:
#Отрисовка матрицы крестиков-ноликов, в случае, если все элементы списка равны '-'
    if (xoCoords[0] == '-' and xoCoords[1] == '-' and xoCoords[2] == '-'
            and xoCoords[3] == '-' and xoCoords[4] == '-' and xoCoords[5] == '-'
            and xoCoords[6] == '-' and xoCoords[7] == '-' and xoCoords[8] == '-'):
        print('   1   2   3 ')
        print(f'1  {xoCoords[0]}   {xoCoords[1]}   {xoCoords[2]} ')
        print(f'2  {xoCoords[3]}   {xoCoords[4]}   {xoCoords[5]} ')
        print(f'3  {xoCoords[6]}   {xoCoords[7]}   {xoCoords[8]} \n')
#Если нет победителя, то ход игрока Х
    if not have_winner:
#Если в списке для Х еще есть место, то выполняется код
        if '-' in xoCoords:
            #Ввод данных от пользователя, положение в строке
            x1 = input('Игрок x\nВведите строку расположения: ')
            #Ввод данных от пользователя, положение в столбце
            x2 = input('Введите столбец расположения: ')
            print('')

            #Если введенные данные пользователем меньше 1, либо больше чем 3, либо ничего, то останавливаем цикл и программу
            if (int(x1) > 3 or int(x1) < 1 or int(x1) == int() or int(x1) == int()
                    or int(x2) > 3 or int(x2) < 1 or int(x2) == int() or int(x2) == int()):
                break

            x = 'x'
            o = 'o'
            coord_num = 0

            #Условия, которые говорят о замене символа '-', на выбранном пользователем месте, если там есть таковое. Если нет, то заменяется ближайшее свободное по списку
            if x1 == str(1) and x2 == str(1):
                if xoCoords[0] != x and xoCoords[0] != o:
                    xoCoords[0] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(1) and x2 == str(2):
                if xoCoords[1] != x and xoCoords[1] != o:
                    xoCoords[1] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(1) and x2 == str(3):
                if xoCoords[2] != x and xoCoords[2] != o:
                    xoCoords[2] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(2) and x2 == str(1):
                if xoCoords[3] != x and xoCoords[3] != o:
                    xoCoords[3] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(2) and x2 == str(2):
                if xoCoords[4] != x and xoCoords[4] != o:
                    xoCoords[4] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(2) and x2 == str(3):
                if xoCoords[5] != x and xoCoords[5] != o:
                    xoCoords[5] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(3) and x2 == str(1):
                if xoCoords[6] != x and xoCoords[6] != o:
                    xoCoords[6] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(3) and x2 == str(2):
                if xoCoords[7] != x and xoCoords[7] != o:
                    xoCoords[7] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1
            elif x1 == str(3) and x2 == str(3):
                if xoCoords[8] != x and xoCoords[8] != o:
                    xoCoords[8] = x
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = x
                            break
                        else:
                            coord_num = coord_num + 1

            #Отрисовка матрицы крестиков-ноликов с результатом
            print('   1   2   3 ')
            print(f'1  {xoCoords[0]}   {xoCoords[1]}   {xoCoords[2]} ')
            print(f'2  {xoCoords[3]}   {xoCoords[4]}   {xoCoords[5]} ')
            print(f'3  {xoCoords[6]}   {xoCoords[7]}   {xoCoords[8]} \n')

            #Условия победы при различных комбинациях
            if (xoCoords[0] == x and xoCoords[1] == x and xoCoords[2] == x
                    or xoCoords[3] == x and xoCoords[4] == x and xoCoords[5] == x
                    or xoCoords[6] == x and xoCoords[7] == x and xoCoords[8] == x
                    or xoCoords[0] == x and xoCoords[3] == x and xoCoords[6] == x
                    or xoCoords[1] == x and xoCoords[4] == x and xoCoords[7] == x
                    or xoCoords[2] == x and xoCoords[5] == x and xoCoords[8] == x
                    or xoCoords[0] == x and xoCoords[4] == x and xoCoords[8] == x
                    or xoCoords[2] == x and xoCoords[4] == x and xoCoords[6] == x):
                #Победитель есть, конец цикла и завершение программы
                have_winner = True
                print('Победил игрок X')
        else:
            #Поле заполнено, но победителя нет - конец цикла и завершение программы
            print('Ничья получается')
            break

#Ход игрока O. Тут все то же, что и у игрока Х
    if not have_winner:
        if '-' in xoCoords:
            o1 = input('Игрок o\nВведите строку расположения: ')
            o2 = input('Введите столбец расположения: ')
            print('')

            if (int(o1) > 3 or int(o1) < 1 or int(o1) == int() or int(o1) == int()
                    or int(o2) > 3 or int(o2) < 1 or int(o2) == int() or int(o2) == int()):
                break

            x = 'x'
            o = 'o'
            coord_num = 0

            if o1 == str(1) and o2 == str(1):
                if xoCoords[0] != o and xoCoords[0] != x:
                    xoCoords[0] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(1) and o2 == str(2):
                if xoCoords[1] != o and xoCoords[1] != x:
                    xoCoords[1] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(1) and o2 == str(3):
                if xoCoords[2] != o and xoCoords[2] != x:
                    xoCoords[2] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(2) and o2 == str(1):
                if xoCoords[3] != o and xoCoords[3] != x:
                    xoCoords[3] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(2) and o2 == str(2):
                if xoCoords[4] != o and xoCoords[4] != x:
                    xoCoords[4] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(2) and o2 == str(3):
                if xoCoords[5] != o and xoCoords[5] != x:
                    xoCoords[5] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(3) and o2 == str(1):
                if xoCoords[6] != o and xoCoords[6] != x:
                    xoCoords[6] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(3) and o2 == str(2):
                if xoCoords[7] != o and xoCoords[7] != x:
                    xoCoords[7] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1
            elif o1 == str(3) and o2 == str(3):
                if xoCoords[8] != o and xoCoords[8] != x:
                    xoCoords[8] = o
                else:
                    for n in xoCoords:
                        if n == '-':
                            xoCoords[coord_num] = o
                            break
                        else:
                            coord_num = coord_num + 1

            print('   1   2   3 ')
            print(f'1  {xoCoords[0]}   {xoCoords[1]}   {xoCoords[2]} ')
            print(f'2  {xoCoords[3]}   {xoCoords[4]}   {xoCoords[5]} ')
            print(f'3  {xoCoords[6]}   {xoCoords[7]}   {xoCoords[8]} \n')

            if (xoCoords[0] == o and xoCoords[1] == o and xoCoords[2] == o
                    or xoCoords[3] == o and xoCoords[4] == o and xoCoords[5] == o
                    or xoCoords[6] == o and xoCoords[7] == o and xoCoords[8] == o
                    or xoCoords[0] == o and xoCoords[3] == o and xoCoords[6] == o
                    or xoCoords[1] == o and xoCoords[4] == o and xoCoords[7] == o
                    or xoCoords[2] == o and xoCoords[5] == o and xoCoords[8] == o
                    or xoCoords[0] == o and xoCoords[4] == o and xoCoords[8] == o
                    or xoCoords[2] == o and xoCoords[4] == o and xoCoords[6] == o):
                have_winner = True
                print('Победил игрок O')
        else:
            print('Ничья получается')
            break
