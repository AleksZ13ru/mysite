from django.shortcuts import render
from django.utils import timezone
from .models import Schedule, People, Holiday, MicroSchedule
import calendar

# import datetime
# from dept.code.repack import repack

# Пример вывода: 16 сентября 2012
DATE_FORMAT = 'd E Y'


def dept_list(request):
    args = {}
    # schedules = Schedule.objects.all()
    # schedules = Schedule.today()
    # schedules_night = Schedule.today_night()
    schedules = Schedule.day()
    schedules_night = Schedule.day(night=True)
    # args = {'yesterday' : {sched: 'Смена№1', args_peoples_n:{'function': 'инженер', 'fio': 'Иванов'}},
    #         'today': 0,
    #         'tomorrow': +1}
    for schedule in schedules:
        args['sched'] = schedule.title
        peoples = People.objects.filter(schedule=schedule).filter(dayofquit=None)
        args_peoples = []
        for people in peoples:
            args_people = {'function': people.function, 'fio': people.fio()}
            args_peoples.append(args_people)
        args['args_peoples'] = args_peoples

    for schedule in schedules_night:
        args['sched_n'] = schedule.title
        peoples = People.objects.filter(schedule=schedule).filter(dayofquit=None)
        args_peoples = []
        for people in peoples:
            args_people = {'function': people.function, 'fio': people.fio()}
            args_peoples.append(args_people)
        args['args_peoples_n'] = args_peoples

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
    args['view_month'] = {'year': year, 'month': month, 'year_last': year - 1, 'year_next': year + 1}

    persons = Schedule.itermonthdates(year, month)  # Заполнение графика работы
    persons = Holiday.modify_schedule(year, month, persons)  # Заполнение отпусков
    persons = MicroSchedule.modify_schedule(year, month, persons)  # Заполнение подмена сменных
    persons = Schedule.delete_standart_person_in5day(year, month, persons)  # Вырез персон с обычным графиком работы
    persons = Schedule.delete_quit_person(year, month, persons)  # удаление уволевшихся

    args.update(persons)
    return render(request, 'dept/dept_calendar.html', {'args': args})
