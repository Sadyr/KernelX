import datetime

def calculate_age(born):
    today = datetime.datetime.today()
    print(today)
    try:  # raised when birth day is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day - 1)

    import pdb
    pdb.set_trace()

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year