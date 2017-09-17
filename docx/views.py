from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo, Event, Note, PeopleToWhom, PeopleWho
from .forms import EventForm, MemoForm, NoteForm
from django.utils import timezone


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


def docx_all(request):
    memos = Memo.objects.all().order_by('number').reverse()
    return render(request, 'docx/docx_all.html', {'memos': memos})


# адресат
def docx_destination(request, pk):
    memos = Memo.objects.filter(to_whom=pk).order_by('number').reverse()
    # memos = Memo.objects.all()
    PeopleToWhom_text = "Адресат: " + PeopleToWhom.objects.get(pk=pk).name
    return render(request, 'docx/docx_all.html', {'memos': memos, "PeopleToWhom_text": PeopleToWhom_text})


# исполнитель
def docx_executor(request, pk):
    memos = Memo.objects.filter(who=pk).order_by('number').reverse()
    # memos = Memo.objects.all()
    PeopleWho_text = "Исполнитель: " + PeopleWho.objects.get(pk=pk).fio()
    return render(request, 'docx/docx_all.html', {'memos': memos, "PeopleWho_text": PeopleWho_text})


# по дате - год, месяц
def docx_calendar(request, year=timezone.now().year, month=timezone.now().month):
    memos = Memo.objects.filter(day_create__month=month).filter(day_create__year=year).order_by('number').reverse()
    # memos = Memo.objects.all()
    return render(request, 'docx/docx_all.html', {'memos': memos})


def docx_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    # form = EventForm()
    # if request.method == "POST":
    #     form = EventForm(request.POST)
    #     if form.is_valid():
    #         event = form.save(commit=False)
    #
    #         event.memo = memo
    #         # event.title = request.title
    #         # event.day_create = request.day_create
    #         # event.comment = request.comment
    #
    #         event.save()
    # else:
    form_event = EventForm()
    form_note = NoteForm()
    return render(request, 'docx/docx_detail.html', {'memo': memo, 'form_event': form_event, 'form_note': form_note})


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
            memo.save()
            return redirect('docx_detail', pk=memo.pk)
    else:
        form = MemoForm(instance=memo)
    return render(request, 'docx/docx_edit.html', {'memo': memo, 'form': form})


def event_new(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    # form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.memo = memo
            event.save()
    return redirect('docx_detail', pk=pk)


def event_del(request, pk):
    event = get_object_or_404(Event, pk=pk)
    pk_memo = event.memo.pk
    event.delete()
    return redirect('docx_detail', pk=pk_memo)


def note_new(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    # form = EventForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.memo = memo
            note.save()
    return redirect('docx_detail', pk=pk)


def note_del(request, pk):
    note = get_object_or_404(Note, pk=pk)
    pk_memo = note.memo.pk
    note.delete()
    return redirect('docx_detail', pk=pk_memo)


def note_end(request, pk):
    note = get_object_or_404(Note, pk=pk)
    pk_memo = note.memo.pk
    if note.note_end:
        note.note_end = False
    else:
        note.note_end = True
    note.save()
    return redirect('docx_detail', pk=pk_memo)
