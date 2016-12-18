from django.shortcuts import render
from django.utils import timezone
from .models import Schedule, People

# Пример вывода: 16 сентября 2012
DATE_FORMAT = 'd E Y'


def dept_list(request):
    args = {}
    schedules = Schedule.objects.all()
    for schedule in schedules:
        t = (timezone.now().toordinal()-schedule.startday.toordinal()+1) % 4
        if t == 0:
            i = 1
            args['sched'] = schedule.title
            peoples = People.objects.filter(schedule=schedule)
            for people in peoples:
                name = "man%d" % i
                args[name] = people.fio()
                i = i+1
    args['time'] = timezone.now()
    return render(request, 'dept/dept_list.html', {'args': args})
