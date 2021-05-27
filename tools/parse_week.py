from datetime import date
import calendar
from typing import Iterable


def parse_last_week(date_formated:Iterable) -> bool:

    _date = date.fromisoformat(date_formated[0])
    _year = _date.year
    _month = _date.month

    _last_day = max(calendar.monthrange(_year, _month))-7

    _ld_date = date(_year, _month, _last_day)

    if (_date.day >= _ld_date.day) and (_date.month == _ld_date.month):
        return True
    return False
