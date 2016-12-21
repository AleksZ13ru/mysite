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
    #date.day = 1

    mycal = calendar.Calendar(firstweekday=0)
    #mount = calendar.monthrange(timezone.now().year, timezone.now().month)
    #mount_len = mount[1]
    #mount_start_wek = mount[0]
    args = {}
    day = []
    for i in mycal.itermonthdates(timezone.now().year, timezone.now().month):
        if i.month == date.month:
            day.append(i)
    args['day'] = day
    args['schedules'] = Schedule.itermonthdates(timezone.now().year, timezone.now().month)
    return render(request, 'dept/dept_calendar.html', {'args': args})
