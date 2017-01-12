from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
import random
import datetime
from django.utils import timezone
from .models import PollResult, Register, Equipment

# Пример вывода: 16 сентября 2012
DATE_FORMAT = 'd E Y'


def si8_list(request):
    return render(request, 'si8device/si8_list.html')


def si8_d3_list(request):
    # Obs = Register.objects.filter(register_enable=True)
    Obs = Equipment.objects.filter(equipment_enable=True)
    return render(request, 'si8device/si8_d3_list.html', {'Obs': Obs})


def si8_d3d3(request):
    return render(request, 'si8device/d3_v3.html')


def si8_d3d4(request):
    return render(request, 'si8device/d3_v4.html')


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

DB_DATETIME_FORMAT = '%m/%d/%Y %H:%M'
DB_DATE_FORMAT = '%m/%d/%Y'
DB_DATETIME_Z_FORMAT = '%m/%d/%Y 0:0'
DB_TIME_FORMAT = "%H:%M"


def c3_json_from_model(id):
    # tt = timezone.now()
    tt = timezone.datetime(2016, 12, 17, 0, 0)
    result = []
    # format PollResult.pollresult_time = '12/16/2016 07:30' '%m/%d/%Y %H:%M'
    starttimefilter = tt.strftime(DB_DATE_FORMAT)
    tt = tt.replace(day=tt.day+1)
    # stoptimefilter = tt.strftime(DB_DATE_FORMAT)
    points = PollResult.objects.filter(pollresult_register_id=id).filter(pollresult_time__startswith=starttimefilter)  # .filter(pollresult_time=starttimefilter)
    for point in points:
        y = point.pollresult_value
        t2 = timezone.datetime.strptime(point.pollresult_time, DB_DATETIME_FORMAT)
        # x = point.pollresult_time
        x = (t2.strftime(DB_TIME_FORMAT))
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
    content3 = c3_json_from_model(id=id)
    # content = [{"close": 7, "date": "00:00"}, {"close": 6, "date": "00:01"},...]
    # content = '{"x": ["00:00", "00:01", "00:02", "00:03"],"y": [180, 150, 300, 70]}'
    return HttpResponse(content3, content_type='application/json')
    # return HttpResponse(html)
