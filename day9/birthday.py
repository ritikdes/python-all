from datetime import datetime

def birthday_left(birth_month, birth_day):
    today = datetime.now()
    birthday_this_year = datetime(today.year, birth_month, birth_day)

    if birthday_this_year < today:
        target_date = datetime(today.year + 1, birth_month, birth_day)
    else:
        target_date = birthday_this_year

    diff = target_date - today

    return diff.days

m = int(input("Enter birth month(1-12): "))
d = int(input("Enter birth day(1-31): "))

days_left = birthday_left(m, d)
print(f"{days_left} days left until your next birthday!")