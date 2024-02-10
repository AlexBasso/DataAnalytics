from django.shortcuts import render
from .models import Order
from .utils import get_plot1, get_plot2, get_plot3, get_plot4, get_plot5, get_plot6

import pandas as pd


def main_view(request):
    qs3 = Order.objects.all().values()
    data3 = pd.DataFrame(qs3)
    grouped_data3 = data3.groupby('category')['profit'].sum().reset_index()
    x2 = [x2 for x2 in grouped_data3['category']]
    y2 = [y2 for y2 in grouped_data3['profit']]
    chart1 = get_plot1(x2, y2)


    qs4 = Order.objects.all().values()
    data4 = pd.DataFrame(qs4)
    grouped_data4 = data4.groupby('category')['sales'].sum().reset_index()
    x2 = [x2 for x2 in grouped_data4['category']]
    y2 = [y2 for y2 in grouped_data4['sales']]
    chart2 = get_plot2(x2, y2)


    qs5 = Order.objects.all().values()
    data5 = pd.DataFrame(qs5)
    df_head = data5.head(50).drop('id', axis=1).copy()
    data5['order_date'] = pd.to_datetime(data5['order_date'])
    data5['year'] = data5['order_date'].dt.year
    data5['month'] = data5['order_date'].dt.month
    sales_by_year_month = data5.groupby(['year', 'month'])['sales'].sum().reset_index()
    chart3 = get_plot3(sales_by_year_month)


    qs6 = Order.objects.all().values()
    data6 = pd.DataFrame(qs6)
    grouped = data6.groupby('sub_category')['sales'].sum()
    chart4 = get_plot4(grouped)


    qs7 = Order.objects.all().values()
    data7 = pd.DataFrame(qs7)
    grouped = data7.groupby('sub_category')['profit'].sum()
    chart5 = get_plot5(grouped)


    qs8 = Order.objects.all().values()
    data8 = pd.DataFrame(qs8)
    grouped_avg = data8.groupby('sub_category').agg({'sales': 'mean', 'profit': 'mean'})
    grouped_avg['profit_margin'] = (grouped_avg['profit'] / grouped_avg['sales']) * 100
    grouped_avg = grouped_avg.drop(['sales', 'profit'], axis=1)
    chart6 = get_plot6(grouped_avg)

    context = {
        'df': data5.to_html(),
        'df_head': df_head.to_html(),
        'describe': data5.describe().to_html(),
        'shape': data5.shape,
        'columns': data5.columns,
        'chart1': chart1,
        'chart2': chart2,
        'chart3': chart3,
        'chart4': chart4,
        'chart5': chart5,
        'chart6': chart6,
    }

    return render(request, 'dataanalytics/main.html', context)
