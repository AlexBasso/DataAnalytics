from django.shortcuts import render
from .models import Car, Sale, Order, Person
from .utils import get_plot, get_plot2, get_plot3

import pandas as pd

def main_view(request):
    # qs = Car.objects.all().values()
    # qs2 = Car.objects.all().values_list()
    # data = pd.DataFrame(qs)
    # data2 = pd.DataFrame(qs2)
    #
    # # print('---------qs--------')
    # # print(qs)
    # # print('--------qs2---------')
    # # print(qs2)
    # # print('-------data----------')
    # # print(data)
    # # print('-------data2----------')
    # # print(data2)
    #
    #
    #
    # qs3 = Sale.objects.all().values()
    # print('qs3: ', qs3)
    # data3 = pd.DataFrame(qs3)
    # print('data3: \n', data3)
    #
    # grouped_data = data3.groupby('item')['price'].mean().reset_index()
    # # Extract 'item' and 'price' columns from the grouped data
    # x = grouped_data['item'].tolist()
    # y = grouped_data['price'].tolist()
    #
    # # Print the result
    # print('Grouped Data: \n', grouped_data)
    # print('mean x: ', x)
    # print('mean y: ', y)
    #
    #
    # # x = [x for x in data3['item']]
    # # print('this is x: ', x)
    # # y = [y for y in data3['price']]
    # # print('this is y: ', y)
    # # chart = get_plot(x, y)
    #
    # x = [x for x in grouped_data['item']]
    # print('this is x: ', x)
    # y = [y for y in grouped_data['price']]
    # print('this is y: ', y)
    # chart = get_plot(x, y)

    qs4 = Order.objects.all().values()
    data4 = pd.DataFrame(qs4)
    grouped_data4 = data4.groupby('category')['sales'].sum().reset_index()
    print('Grouped Data4: \n', grouped_data4)


    x2 = [x2 for x2 in grouped_data4['category']]
    print('this is x: ', x2)
    y2 = [y2 for y2 in grouped_data4['sales']]
    print('this is y: ', y2)
    chart2 = get_plot2(x2, y2)


    qs5 = Order.objects.all().values()
    data5 = pd.DataFrame(qs5)
    df_head = data5.head(50).drop('id', axis=1).copy()
    # print('before: \n', data5)
    data5['order_date'] = pd.to_datetime(data5['order_date'])
    # print('after: \n', data5)

    data5['year'] = data5['order_date'].dt.year
    data5['month'] = data5['order_date'].dt.month
    # print('month: \n', data5)

    sales_by_year_month = data5.groupby(['year', 'month'])['sales'].sum().reset_index()
    print('sales_by_year_month: \n', sales_by_year_month)
    chart3 = get_plot3(sales_by_year_month)

    context = {
        'df': data5.to_html(),
        'df_head': df_head.to_html(),
        'describe': data5.describe().to_html(),
        'shape': data5.shape,
        'columns': data5.columns,
        # 'chart': chart,
        'chart2': chart2,
        'chart3': chart3,

    }
    return render(request, 'dataanalytics/main.html', context)



