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
