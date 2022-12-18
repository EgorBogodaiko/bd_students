import csv
import constants
import string
#read csv, and split on "," the line
global bd

with open(constants.DATA_BASE_NAME) as f:
    bd = csv.reader(f,delimiter='|')
    headers = next(reader)

def search(bd,fields,vaule,type_output):
    """Принимает: базу данных, поле, по которому будет производиться поиск, 
    значение, по которому будет произовдиться поиск,
     тип вывода: 1 - вывести все строки, 2 - вывести идентификаторы найденных строк списком"""
    
    for row in bd:
    #if current rows 2nd value is equal to input, print that row
        row = row.split('|')
    if number == row[1]:
         print (row)


    return found_items
