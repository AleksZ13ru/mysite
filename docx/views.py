from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def docx_list(request):
    # parsing_si8()
    # {'value': 51.8, 'now_date': datetime.datetime(2016, 12, 26, 7, 30), 'id_si8': 1}

    #html = "<html><body> This is %s view</body></html>" % "hello!"
    #return HttpResponse(html)
    #year = int(year)
    #month = int(month)
    #date = timezone.datetime(year=year, month=month, day=1)
    #my_cal = calendar.Calendar(firstweekday=0)
    args = {}
    day = []
    #for i in my_cal.itermonthdates(year, month):
    #    if i.month == date.month:
    #        day.append(i)
    #args['day'] = day
    #args['view_month'] = {'year': year, 'month': month, 'year_last': year - 1, 'year_next': year + 1}

    #persons = Schedule.itermonthdates(year, month)  # Заполнение графика работы
    #persons = Holiday.modify_schedule(year, month, persons)  # Заполнение отпусков
    #persons = MicroSchedule.modify_schedule(year, month, persons)  # Заполнение подмена сменных
    #persons = Schedule.delete_standart_person_in5day(year, month, persons)  # Вырез персон с обычным графиком работы
    #persons = Schedule.delete_quit_person(year, month, persons)  # удаление уволевшихся

    #args.update(persons)
    return render(request, 'docx/docx_list.html', {'args': args})
