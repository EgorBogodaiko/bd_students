import csv
import constants
import string
#read csv, and split on "," the line
import ast

def search(bd:str,field:str,value:str,type_output:int):
    """Принимает: базу данных, поле, по которому будет производиться поиск, 
    значение, по которому будет произовдиться поиск,
     тип вывода: 1 - вывести все строки, 2 - вывести идентификаторы найденных строк списком
     """
    with open(bd) as f:
        reader = csv.DictReader(f,delimiter='|')
        headers=reader.fieldnames
        if type_output == 1:
            print('Найденные строки:')
            print(headers)
            for item in reader:
                if item[field] == value:
                    print(list(item.values()))
        elif type_output == 2:
            print('Список ID найденных строк:')
            id_list=[]
            for item in reader:
                if item[field] == value:
                    id_list+=(item['id'])
            print(id_list)
        else:
            print('Неизвестный режим работы функции')


#search(constants.DATA_BASE_NAME,'last_name','nono',2)