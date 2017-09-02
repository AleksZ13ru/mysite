from django.shortcuts import render, get_object_or_404
from .models import Memo


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
    # day = []
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

    memos = Memo.objects.all()  # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #for memo in memos:
    #    event = Memo.objects.filter(event__in=memo.id).len()

    # return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'docx/docx_list.html', {'memos': memos})


def docx_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'docx/docx_detail.html', {'memo': memo})
