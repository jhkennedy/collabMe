from datetime import date

current_year = date.today().year  


def clean_year(year_string):
    try:
        year = int(year_string[:4])  # Years are only 4 char; will catch YYYYa, YYYYb, etc.
    except ValueError as E:
        alts = ['prep', 'press', 'review', 'accepted']
        for alt in alts:
            if alt in year_string.lower():
                year = current_year
                break
        else:
            # alts loop fell through without finding a suitable alt
            raise E

    return year
