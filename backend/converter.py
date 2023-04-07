import json
from datetime import datetime


def sql_datetime_to_datetime(dt):
    return datetime(year=dt.year,
                    month=dt.month,
                    day=dt.day,
                    hour=dt.hour,
                    minute=dt.minute,
                    second=dt.second)
