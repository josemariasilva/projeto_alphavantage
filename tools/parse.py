from datetime import date
import calendar
from tools.db_manager import create_db_table, update_table
from typing import Any, Iterable
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


def parse_arg() -> Iterable:
    """Argumentos inseridos no momento de execução

        retorno:
        --------
            retorna True se a alteração estiver completa ou False caso ter alteração no banco de dados.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--create", nargs=3, default=[], metavar='c',
                        help="c argumentos:[symbol, name, enabled]")
    parser.add_argument("--update", nargs=2, default=[], metavar='u',
                        help="u argumentos:[symbol, enabled]")
    parser.add_argument("--apikey", nargs=1, default=[], metavar='a',
                        help='a argumentos:[APIKEY]')

    value_c = parser.parse_args()
    value_u = parser.parse_args()
    value_api = parser.parse_args()

    if any(value_c.create):
        create_db_table(value_c.create)
        return True, None

    elif any(value_u.update):
        update_table(value_u.update)
        return True, None

    else:
        return False, value_api.apikey
