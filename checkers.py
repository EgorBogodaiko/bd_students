import string
def check_menu_item(choise:str):
    """Принимает строку со значением
    Возвращает bool - является ли входящая строка опцией меню"""
    check=False
    if choise in ('1','2','3','4','5','6'):
        check = True        
    return check

def checker_field(field:str,value:str):
    result = False
    if field =='phone_num':
        if len(value)<=11 and value.isdigit():
            result=True
    elif field in ('first_name','last_name'):
        if value.isalpha()==True:
            result = True
    elif any(ch.isdigit() for ch in value)==False and len(value)<=30:
        result=True 
    return result
