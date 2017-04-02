from django.shortcuts import render
from django.utils import timezone
from .models import Schedule, People, Holiday
import calendar
import datetime
from dept.code.repack import repack

# Пример вывода: 16 сентября 2012
DATE_FORMAT = 'd E Y'


def dept_list(request):
    args = {}
    # schedules = Schedule.objects.all()
    schedules = Schedule.today()
    for schedule in schedules:
        args['sched'] = schedule.title
        peoples = People.objects.filter(schedule=schedule)
        args_peoples = []
        for people in peoples:
            args_people = {'function': people.function, 'fio': people.fio()}
            args_peoples.append(args_people)
        args['args_peoples'] = args_peoples
    args['time'] = timezone.now()
    return render(request, 'dept/dept_list.html', {'args': args})


def dept_calendar(request, year=timezone.now().year, month=timezone.now().month):
    year = int(year)
    month = int(month)
    date = timezone.datetime(year=year, month=month, day=1)
    my_cal = calendar.Calendar(firstweekday=0)
    args = {}
    day = []
    for i in my_cal.itermonthdates(year, month):
        if i.month == date.month:
            day.append(i)
    args['day'] = day
    args['view_month'] = {'year': year, 'month': month, 'year_last': year-1, 'year_next': year+1}
    test_list = Schedule.itermonthdates(year, month)
    day5 = Schedule.schedule_in5day(year, month)
    t = Holiday.modify_schedule(year, month, test_list)
    t2 = Holiday.modify_schedule_in5day(t, day5)
    args.update(t2)
    return render(request, 'dept/dept_calendar.html', {'args': args})
