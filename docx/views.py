from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo, Event, Note, PeopleToWhom, PeopleWho
from .forms import EventForm, MemoForm, NoteForm
from django.utils import timezone
# from django.http import HttpResponse, JsonResponse
# from django.core import serializers

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import MemoSerializer


def docx_list(request):
    memos = Memo.objects.all()
    return render(request, 'docx/docx_list.html', {'memos': memos})


def docx_all(request):
    memos = Memo.objects.all().order_by('number').reverse()
    return render(request, 'docx/docx_all.html', {'memos': memos})


@csrf_exempt
def docx_json(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def docx_json_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        memo = Memo.objects.get(pk=pk)
    except Memo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MemoSerializer(memo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MemoSerializer(memo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        memo.delete()
        return HttpResponse(status=204)


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
