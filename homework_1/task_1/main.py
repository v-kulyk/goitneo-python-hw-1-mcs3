import calendar
from collections import defaultdict
from datetime import datetime,timedelta


def get_birthdays_per_week(people: list):
    today = datetime.today().date()

    output_data = defaultdict(list)

    for person in people:
        birthday = person.get("birthday").date()

        celebration_date = birthday.replace(year=today.year)

        if celebration_date < today:
            celebration_date = celebration_date.replace(year=today.year + 1)

        delta_to_celebration = celebration_date - today

        if delta_to_celebration.days >= 7:
            continue

        if celebration_date.weekday() in [5, 6]:
            celebration_date = celebration_date + \
                timedelta(days=7 - celebration_date.weekday())

        output_data[celebration_date.weekday()].append(person.get('name'))
        sorted(output_data)

    for weekday_index in output_data.keys():
        day_name = calendar.day_name[weekday_index]
        celebrator_names = ", ".join(output_data.get(weekday_index))

        print(f"{day_name}: {celebrator_names}")


get_birthdays_per_week([
    {"name": "John Gates", "birthday": datetime(1965, 9, 28)},
    {"name": "Peter Gates", "birthday": datetime(1975, 10, 15)},
    {"name": "Kevin Gates", "birthday": datetime(1985, 10, 16)},
    {"name": "Igor Gates", "birthday": datetime(1995, 10, 17)},
    {"name": "Vlad Gates", "birthday": datetime(2000, 10, 18)},
    {"name": "Isaak Gates", "birthday": datetime(2007, 11, 18)},
])
