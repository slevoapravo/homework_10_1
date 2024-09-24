from src.masks import get_mask_card_number


def mask_account_card(data_card: str) -> str:
    """функция, которая обрабатывает информацию о картах и счетах"""
    number_card = "".join(el if el.isdigit() else "" for el in data_card)
    number_card_mask = get_mask_card_number(number_card)
    name_card = "".join("" if el.isdigit() else el for el in data_card)
    data_card_mask = name_card + number_card_mask
    return data_card_mask


print(mask_account_card("Visa Platinum 7000792289606361"))