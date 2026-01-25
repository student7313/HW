def get_mask_card_number(card_number: int) -> str:
    """
    Переводит все в string и выдает результат формата XXXX XX** **** XXXX.
    Заменяет середину на "** **** " и добавляет пробел после четвертого символа.
    """
    card_number = str(card_number)
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(account_number: int) -> str:
    """Выдает текст формата **XXXX, где XXXX - последние 4 символа"""
    account_number = str(account_number)
    return "**" + account_number[-4:]
