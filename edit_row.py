import os,csv
import constants as const  

def modify_row(bd,id_key,field,new_value):
    """Получает на вход: адрес БД, ключ строки, поле, новое значение поля"""
    """Поулчает на вход адрес БД и список ID строк, которые нужно удалить из БД, ничего не возвращает. """
    with open(bd) as f:
        input = open(bd, 'r',newline='')
        output = open('bd1.csv', 'w',newline='')
        writer = csv.writer(output,delimiter='|')
        headers=next(csv.reader(input,delimiter='|'))
        writer.writerow(headers)
        index_field_to_edit=(headers.index(field))
        for current_row in csv.reader(input,delimiter='|'):
            if current_row[0] == str(id_key):
                print(f'Подменяем {current_row[index_field_to_edit]} на {new_value}')
                current_row[index_field_to_edit]=new_value
            writer.writerow(current_row)
        input.close()
        output.close()
    os.remove(const.DATA_BASE_NAME)
    os.rename('bd1.csv', const.DATA_BASE_NAME)