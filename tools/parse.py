from datetime import date
import calendar
from tools.db_manager import create_db_table, update_table
from typing import Iterable
import argparse



def parse_last_week(date_formated: Iterable) -> bool:
    """filtra a ultima semana do mes.\n 
    (ultimo dia do calendario) - 7 >= (data do cadastro). \n
    compara com o dia cadastrado se esta dentro do range.
    
    Parametros:
    ----------
        data_formated : Iterable
            formato de date
    Retorno:
    -------
        retorna True se a data for a ultima semana do mes, caso contrario False.

    """

    _date = date.fromisoformat(date_formated[0])
    _year = _date.year
    _month = _date.month

    _last_day = max(calendar.monthrange(_year, _month))-7

    _ld_date = date(_year, _month, _last_day)

    if (_date.day >= _ld_date.day) and (_date.month == _ld_date.month):
        return True
    return False

def parse_arg() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--create", nargs=3, default=[], help="create and insert on database")
    parser.add_argument("--update", nargs=2, default=[], help="update value in table")

    value_c = parser.parse_args()
    value_u = parser.parse_args()
    create_db_table(value_c.create)
    update_table(value_u.update)


