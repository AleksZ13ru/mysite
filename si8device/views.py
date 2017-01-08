from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
import random
import datetime
import csv

# Пример вывода: 16 сентября 2012
DATE_FORMAT = 'd E Y'


def si8_list(request):
    return render(request, 'si8device/si8_list.html')


def si8_d3_list(request):
    return render(request, 'si8device/si8_d3_list.html')


def si8_d3d3(request):
    return render(request, 'si8device/d3.html')


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        result = []
        for i in range(1, 5):
            result.append(i)
        return result

    def get_data(self):
        """Return 3 datasets to plot."""
        result = []
        a = []
        for i in range(1, 5):
            a.append(random.randint(1, 10))
        result.append(a)
        return result


line_chart = TemplateView.as_view(template_name='si8device/line_chart.html')
line_chart_json = LineChartJSONView.as_view()

line_chartc3 = TemplateView.as_view(template_name='si8device/line_chartc3.html')
# line_chartc3_json = LineChartJSONView.as_view()

line_chartd3 = TemplateView.as_view(template_name='si8device/line_chartd3.html')


# line_chartc3_json = LineChartJSONView.as_view()


def c3_json_generate(id):
    tt = datetime.time()
    x = []
    y = []
    # result = {}
    for h in range(0, 24):
        tt = tt.replace(hour=h)
        yy = random.randint(1, 20)
        for m in range(0, 60):
            tt = tt.replace(minute=m)
            x.append(tt.strftime("%H:%M"))
            y.append(yy + random.randint(1, 3))
    result = JsonResponse({"x": x, "y": y})
    return result.content


def c3_json_generate_v2(id):
    tt = datetime.time()
    result = []
    for h in range(0, 24):
        tt = tt.replace(hour=h)
        yy = random.randint(1, 20)
        for m in range(0, 60):
            tt = tt.replace(minute=m)
            x = (tt.strftime("%H:%M"))
            y = (yy + random.randint(1, 3))
            e = {"date": x, "close": y}
            result.append(e)
    return JsonResponse(result, safe=False).content


def chartjs_json_generate_v2(id):
    labels = []
    data = []
    tt = datetime.time()
    for h in range(0, 24):
        tt = tt.replace(hour=h)
        yy = random.randint(1, 20)
        for m in range(0, 60):
            tt = tt.replace(minute=m)
            x = (tt.strftime("%H:%M"))
            y = (yy + random.randint(1, 3))
            labels.append(x)
            data.append(y)
    result = {'labels': labels, 'data': data}
    return JsonResponse(result).content


def line_chartjs_v2_json(request, id=0):
    content = chartjs_json_generate_v2(id)
    # content = '{"x": ["00:00", "00:01", "00:02", "00:03"],"y": [180, 150, 300, 70]}'
    return HttpResponse(content, content_type='application/json')


def line_chartc3_json(request, id=0):
    content2 = c3_json_generate_v2(id)
    content = '{"x": ["00:00", "00:01", "00:02", "00:03"],"y": [180, 150, 300, 70]}'
    return HttpResponse(content2, content_type='application/json')
    # return HttpResponse(html)
