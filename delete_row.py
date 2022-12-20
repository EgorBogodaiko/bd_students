
import csv
import os
import constants as const

def delete_row(bd,rows_numbers):
    """Поулчает на вход адрес БД и список ID строк, которые нужно удалить из БД, ничего не возвращает. """
    with open(bd) as f:
        input = open(bd, 'r',newline='')
        output = open('bd1.csv', 'w',newline='')
        writer = csv.writer(output)
        for row in csv.reader(input):
            id=str(row[0]).split('|')[0]
            if id not in rows_numbers:
                writer.writerow(row)
            else:
                print('Удалена строка  c ID: ',id,'\n')
        input.close()
        output.close()
    os.remove(const.DATA_BASE_NAME)
    os.rename('bd1.csv', const.DATA_BASE_NAME)
