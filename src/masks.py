import logging
from typing import Union

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)

logger = logging.getLogger("masks")


def get_mask_card_number(card_number: int) -> Union[str, int]:
    """маскирует часть цифр номера карты и разделяет его по четверкам"""
    new_card_number = str(card_number)
    logging.info("Start")
    mask_card_number_1 = []
    mask_card_number_2 = []
    mask_card_number_1.extend([new_card_number[4:6], "**"])
    mask_card_string = "".join(mask_card_number_1)
    mask_card_number_2.extend(
        [new_card_number[:4], mask_card_string, "****", new_card_number[12:]]
    )
    new_card_string = " ".join(mask_card_number_2)
    logging.info("Return of mask card number")
    logging.info("Stop")
    return new_card_string


def get_mask_account(account_number: int) -> Union[str, int]:
    """маскирует часть цифр номера счета"""
    mask_account_number = []
    logging.info("Start")
    new_account_number = str(account_number)
    mask_account_number.extend(["**", new_account_number[-4:]])
    new_account_string = "".join(mask_account_number)
    logging.info("Return of mask account number")
    logging.info("Stop")
    return new_account_string


if __name__ == "__main__":
    print(get_mask_card_number(1324321343213213))
    print(get_mask_account(75645867564756664756))