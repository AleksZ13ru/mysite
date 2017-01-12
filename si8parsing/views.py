from django.http import HttpResponse
from django.shortcuts import render
from .code2 import findfile, parsing_si8
from .models import File


def parsing(request):
    listsfile = File.objects.all().order_by('name')
    return render(request, 'si8parsing/parsing.html', {'listsfile': listsfile})


def si8_find_file(request):
    findfile()
    #TemplateView.as_view(template_name='si8parsing/parsing.html')
    html = "<html><body> This is %s view</body></html>" % "hello!"
    return HttpResponse(html)


def si8_pars_file(request, pk):
    parsing_si8(pk)
    html = "<html><body> This is %s parsing</body></html>" % pk
    return HttpResponse(html)
"""
def parsing(request):
    findfile()
    # parsing_si8()
    # {'value': 51.8, 'now_date': datetime.datetime(2016, 12, 26, 7, 30), 'id_si8': 1}

    html = "<html><body> This is %s view</body></html>" % "hello!"
    return HttpResponse(html)
"""