import matplotlib.pyplot as plt
import base64

from io import BytesIO


def get_graph():
    buffer = BytesIO()
    # print('---------buffer = BytesIO()----------')
    # print(buffer)
    plt.savefig(buffer, format='png')
    # print('---------plt.savefig(buffer, format="png")----------')
    # print(plt)
    buffer.seek(0)
    # print('---------buffer.seek(0)----------')
    # print(buffer)
    image_png = buffer.getvalue()
    # print('---------image_png = buffer.getvalue()----------')
    # print(image_png)
    graph = base64.b64encode(image_png)
    # print('---------graph = base64.b64encode(image_png)----------')
    # print(graph)
    graph = graph.decode('utf-8')
    # print('--------graph = graph.decode("utf-8")-----------')
    # print(graph)
    buffer.close()
    return graph


def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('sales_of_items')
    print('x:', x)
    print('y:', y)
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()

    graph = get_graph()
    return graph


def get_plot2(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 2))
    print('plot2 x:', x)
    print('plot2 y:', y)
    x.reverse()
    y.reverse()
    plt.barh(x, y, color='skyblue', height=0.5)

    # Adding labels and title
    plt.xlabel('Sum of Sales')
    plt.ylabel('Product type')
    plt.title('Average Sales by Item')
    plt.xticks(rotation=45)
    plt.tight_layout()

    graph = get_graph()
    return graph


def get_plot3(sales_by_year_month):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 2))
    sales_by_year_month['year_month'] = sales_by_year_month['year'].astype(str) + '-' + sales_by_year_month[
        'month'].astype(str)
    print('sales_by_year_month after combining: \n', sales_by_year_month)

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    fig.suptitle('Sales by Year and Month')

    for idx, (year, group) in enumerate(sales_by_year_month.groupby('year')):
        row = idx // 2
        col = idx % 2

        axs[row, col].plot(group['month'], group['sales'], label=str(year))
        axs[row, col].set_title(f'Year {year}')
        axs[row, col].set_xlabel('Month')
        axs[row, col].set_ylabel('Sales')
        axs[row, col].legend()

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    # plt.tight_layout()

    graph = get_graph()

    return graph
