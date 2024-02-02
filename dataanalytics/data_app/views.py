from django.shortcuts import render
from .models import Car, Sale
from .utils import get_plot

import pandas as pd

def main_view(request):
    qs = Car.objects.all().values()
    qs2 = Car.objects.all().values_list()
    data = pd.DataFrame(qs)
    data2 = pd.DataFrame(qs2)

    print('---------qs--------')
    print(qs)
    print('--------qs2---------')
    print(qs2)
    print('-------data----------')
    print(data)
    print('-------data2----------')
    print(data2)

    qs3 = Sale.objects.all()
    x = [x.item for x in qs3]
    print(x)
    y = [y.price for y in qs3]
    print(y)
    chart = get_plot(x, y)

    context = {
        'df': data.to_html(),
        'describe': data.describe().to_html(),
        'chart': chart,
    }
    return render(request, 'dataanalytics/main.html', context)



