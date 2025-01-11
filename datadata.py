import datetime
import calendar

# №1
data_now = datetime.datetime.now()
week_day = data_now.weekday()
week_day_name = calendar.day_name[week_day]
print(week_day_name)

year_now = datetime.datetime.now().year
if year_now % 4 == 0 and year_now % 100 != 0 or year_now % 400 == 0:
    print('Високосный год')
else:
    print('Не високосный год')


# №2
# Определяем, сколько дней осталось до введенной даты от текущей даты
data = input('Введите дату в формате "год-месяц-день": ')
parsed_date = datetime.datetime.strptime(data, '%Y-%m-%d')
data_now1 = datetime.datetime.today()
date_math = parsed_date - data_now1
if parsed_date >= data_now1:
    print(f'До {parsed_date.date()} осталось {date_math.days} дней')
else:
    print(f'С {parsed_date.date()} прошло {abs(date_math.days + 1)} дней')

# Рассчитываем разницу между этими двумя датами и
# выводим результат в формате дней, часов и минут.
data_now2 = datetime.datetime.now()
compare = (parsed_date - data_now2)
total_seconds = (compare.days * 86400) + compare.seconds
minutes = round(total_seconds / 60)
hours = round(total_seconds / 3600)
print(f'Разница в днях - {compare.days} дней,\n В часах - {hours} часов,\n В минутах - {minutes} минут')





