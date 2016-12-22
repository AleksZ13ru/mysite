from django.shortcuts import render
from django.utils import timezone
from .models import Schedule, People
import calendar

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


def dept_calendar(request):
    date = timezone.now()
    mycal = calendar.Calendar(firstweekday=0)
    args = {}
    days = []
    for i in mycal.itermonthdates(date.year, date.month):
        if i.month == date.month:
            days.append(i)
    args['day'] = days
    args['date'] = date  # current date
    args['schedules'] = Schedule.itermonthdates(timezone.now().year, timezone.now().month)
    return render(request, 'dept/dept_calendar.html', {'args': args})
