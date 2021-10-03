def sex_to_number(sex, year):
    if 1800 <= year < 1900:
        return 9 if sex == 'MALE' else 0

    if 1900 <= year < 2000:
        return 1 if sex == 'MALE' else 2

    if 2000 <= year:
        return 3 if sex == 'MALE' else 4


def P4(info: list) -> str:
    sex, birth_year, birth_month, birth_day = info
    return f'{str(birth_year % 100).zfill(2)}{str(birth_month).zfill(2)}{str(birth_day).zfill(2)}{sex_to_number(sex, birth_year)}'
