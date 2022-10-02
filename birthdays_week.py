from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    birthdays_days_week = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }

    day_mon = ''
    day_tue = ''
    day_wen = ''
    day_thu = ''
    day_fri = ''

    today_day = datetime.now()
    today_year = datetime.now().year

   # If it is Monday today when we create the 'table' of weekdays and names of birthdays persons
   # we will check previouse Saturday and Sunday to ad them to the 'table'
   # to congrat on the actual Monday

    if today_day.weekday() == 0:  # if today is Monday.
        day_start_week = -2
        day_end_week = 5

   # If it is Sunday today ...
   # we will cut off next Saturday and if it is Saturday today...
   # we will cut off next Saturday and Sunday not to ad them to the 'table'

    elif today_day.weekday() == 6:  # if today is Sunday.
        day_start_week = 0
        day_end_week = 6
    else:
        day_start_week = 0  # if any from Tuesday to Friday +  previous week Saturday
        day_end_week = 7

    for person in users:
        delta = person['birthday'].date().replace(
            year=today_year) - today_day.date()
        week_day = person['birthday'].weekday()

        if timedelta(days=day_start_week) <= delta < timedelta(days=day_end_week):

            if week_day == 0 or week_day == 5 or week_day == 6:
                day_mon += person['name'] + ', '
            elif week_day == 1:
                day_tue += person['name'] + ', '
            elif week_day == 2:
                day_wen += person['name'] + ', '
            elif week_day == 3:
                day_thu += person['name'] + ', '
            elif week_day == 4:
                day_fri += person['name'] + ', '

    birthdays_days_week.update({
        'Monday': day_mon[:-2],
        'Tuesday': day_tue[:-2],
        'Wednesday': day_wen[:-2],
        'Thursday': day_thu[:-2],
        'Friday': day_fri[:-2]
    })

    for key, value in birthdays_days_week.items():
        if len(value) != 0:
            print(f'{key}: {value}')


if __name__ == '__main__':

    users = [
        {'name': 'Bil_0', 'birthday': datetime(2000, 9, 23)},
        {'name': 'Den_0', 'birthday': datetime(1969, 9, 24)},
        {'name': 'Man_0', 'birthday': datetime(1985, 9, 25)},
        {'name': 'Fen', 'birthday': datetime(2002, 9, 26)},
        {'name': 'Dol', 'birthday': datetime(1999, 9, 27)},
        {'name': 'Bal', 'birthday': datetime(2001, 9, 28)},
        {'name': 'Gun', 'birthday': datetime(2010, 9, 29)},
        {'name': 'Bil', 'birthday': datetime(1975, 9, 30)},
        {'name': 'Man', 'birthday': datetime(2022, 10, 1)},
        {'name': 'Del', 'birthday': datetime(2012, 10, 2)},
        {'name': 'Bil_1', 'birthday': datetime(2022, 10, 3)},
        {'name': 'Del_1', 'birthday': datetime(2022, 10, 4)},
        {'name': 'Ben_1', 'birthday': datetime(1986, 10, 5)},
        {'name': 'Dol_1', 'birthday': datetime(2022, 10, 6)}
    ]
    get_birthdays_per_week(users)
