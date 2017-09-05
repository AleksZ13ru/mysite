from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo
from .forms import EventForm, MemoForm


def docx_list(request):
    # parsing_si8()
    # {'value': 51.8, 'now_date': datetime.datetime(2016, 12, 26, 7, 30), 'id_si8': 1}

    # html = "<html><body> This is %s view</body></html>" % "hello!"
    # return HttpResponse(html)
    # year = int(year)
    # month = int(month)
    # date = timezone.datetime(year=year, month=month, day=1)
    # my_cal = calendar.Calendar(firstweekday=0)
    args = {}
    # day = []
    # for i in my_cal.itermonthdates(year, month):
    #    if i.month == date.month:
    #        day.append(i)
    # args['day'] = day
    # args['view_month'] = {'year': year, 'month': month, 'year_last': year - 1, 'year_next': year + 1}

    # persons = Schedule.itermonthdates(year, month)  # Заполнение графика работы
    # persons = Holiday.modify_schedule(year, month, persons)  # Заполнение отпусков
    # persons = MicroSchedule.modify_schedule(year, month, persons)  # Заполнение подмена сменных
    # persons = Schedule.delete_standart_person_in5day(year, month, persons)  # Вырез персон с обычным графиком работы
    # persons = Schedule.delete_quit_person(year, month, persons)  # удаление уволевшихся

    # args.update(persons)

    memos = Memo.objects.all()  # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # for memo in memos:
    #    event = Memo.objects.filter(event__in=memo.id).len()

    # return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'docx/docx_list.html', {'memos': memos})


def docx_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    form = EventForm()
    # if request.method == "POST":
    #     form = EventForm(request.POST)
    #     if form.is_valid():
    #         event = form.save(commit=False)
    #
    #         event.memo = pk
    #         event.title = request.title
    #         event.day_create = request.day_create
    #         event.comment = request.comment
    #
    #         event.save()
    # else:
    #     form = EventForm()
    # # if request.method == "POST":
    # #     data = request.POST
    return render(request, 'docx/docx_detail.html', {'memo': memo, 'form': form})


def docx_new(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            memo.save()
            return redirect('docx_detail', pk=memo.pk)
    else:
        form = MemoForm()
    return render(request, 'docx/docx_edit.html', {'form': form})


def docx_edit(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            memo = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            memo.save()
            return redirect('docx_detail', pk=memo.pk)
    else:
        form = MemoForm(instance=memo)
    return render(request, 'docx/docx_edit.html', {'form': form})


def event_new(request, pk):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.memo = pk
            # post.author = request.user
            # post.published_date = timezone.now()
            event.save()
            return redirect('docx_detail', pk=pk)
            # else:
            # form = MemoForm()
    return redirect('docx_detail', pk=pk)
