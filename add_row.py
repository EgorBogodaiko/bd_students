from ui import give_int_ar

def add_row():
    """Принимает имя файла
    Реализует добавление строки и заполнение её полей вводом значений через консоль позльзователем
    Ничего не возвращает, может пинговать об успешном добавлениив консоль"""

    input_data = []
    id = give_int_ar('Введите порядковый номер: ')
    input_data.append(id)
    first_name = input('Введите имя: ')
    input_data.append(first_name)
    last_name = input('Введите Фамилию: ')
    input_data.append(last_name)   
    phone_num = give_int_ar('Введите телефон: ')        
    input_data.append(phone_num)
    comment = input('Введите комментарий: ')
    input_data.append(comment)
    file = open ('DB.csv', 'a')
    file.write(f'{input_data[0]}|{input_data[1]}|{input_data[2]}|{input_data[3]}|{input_data[4]}\n')
