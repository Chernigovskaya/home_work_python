import datetime


def time_new_year():
    current = datetime.datetime.now()
    new_year = datetime.datetime(current.year + 1, 1, 1)
    return (new_year - current).days



