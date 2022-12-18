def check_menu_item(choise:str):
    """Принимает строку со значением
    Возвращает bool - является ли входящая строка опцией меню"""
    check=False
    if choise in ('1','2','3','4','5','6'):
        check = True        
    return check
