from datetime import date, timedelta, datetime

initial_date = "1-01-1990"
final_date = "31-12-2000"
format = "%d-%m-%Y"
initial = datetime.strptime(initial_date, format)
final = datetime.strptime(final_date, format)

step = timedelta(1)
thurs = 0
day_tocount = ['Thu']

days = (final - initial).days
for x in range(days):
    day = initial.strftime("%a")
    print(day)
    if day in day_tocount:
        thurs += 1
    initial += step

print(thurs)