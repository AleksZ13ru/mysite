from django.shortcuts import render
from django.utils import timezone
from .models import Schedule, People, Holiday
import calendar
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


def dept_calendar(request):
    date = timezone.now()
    my_cal = calendar.Calendar(firstweekday=0)
    args = {}
    day = []
    for i in my_cal.itermonthdates(timezone.now().year, timezone.now().month):
        if i.month == date.month:
            day.append(i)
    args['day'] = day
    # args['schedules'] = Schedule.itermonthdates(timezone.now().year, timezone.now().month)
    # test_list = repack(args['schedules'])

    # test_list = repack(Schedule.itermonthdates(timezone.now().year, timezone.now().month))
    test_list = Schedule.itermonthdates_v2(timezone.now().year, timezone.now().month)
    # args['persons'] = test_list
    # args['persons1'] = Holiday.modify_schedule(timezone.now().year, timezone.now().month, test_list)

    args.update(Holiday.modify_schedule_v3(timezone.now().year, timezone.now().month, test_list))
    return render(request, 'dept/dept_calendar.html', {'args': args})
