from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import random
# Пример вывода: 16 сентября 2012
DATE_FORMAT = 'd E Y'


def si8_list(request):
    return render(request, 'si8device/si8_list.html')


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        result = []
        for i in range(1, 50):
            result.append(i)
        return result

    def get_data(self):
        """Return 3 datasets to plot."""
        result = []
        a = []
        for i in range(1, 50):
            a.append(random.randint(1, 10))
        result.append(a)
        return result


line_chart = TemplateView.as_view(template_name='si8device/line_chart.html')
line_chart_json = LineChartJSONView.as_view()
