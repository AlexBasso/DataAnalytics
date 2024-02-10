import matplotlib.pyplot as plt
import base64

from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph


# def get_plot1(x, y):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(10, 2.3))
#     x.reverse()
#     y.reverse()
#     plt.barh(x, y, color='lightgreen', height=0.5)
#
#     plt.xlabel('Sum of Profits')
#     plt.ylabel('Product type')
#     plt.title('Average Profits by Item \n')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#
#     graph = get_graph()
#     return graph


def get_plot1(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 2.3))
    plt.barh(x, y, color='lightgreen', height=0.5)

    plt.xlabel('Sum of Profits')
    plt.ylabel('Product type')
    plt.title('Average Profits by Item \n')
    plt.xticks(rotation=45)

    # Add labels to the bars
    for index, value in enumerate(y):
        plt.text(value, index, f'{int(value)}', va='center')

    plt.tight_layout()

    graph = get_graph()
    return graph


# def get_plot2(x, y):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(10, 2.3))
#     x.reverse()
#     y.reverse()
#     plt.barh(x, y, color='skyblue', height=0.5)
#
#     plt.xlabel('Sum of Sales')
#     plt.ylabel('Product type')
#     plt.title('Average Sales by Item \n')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#
#     graph = get_graph()
#     return graph


def get_plot2(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 2.3))
    x.reverse()
    y.reverse()
    bars = plt.barh(x, y, color='skyblue', height=0.5)

    plt.xlabel('Sum of Sales')
    plt.ylabel('Product type')
    plt.title('Average Sales by Item \n')
    plt.xticks(rotation=45)

    # Add labels to the bars
    for bar, value in zip(bars, y):
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value:.0f}',
                 ha='left', va='center', color='black')

    plt.tight_layout()

    graph = get_graph()
    return graph



def get_plot3(sales_by_year_month):
    plt.switch_backend('AGG')
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    fig.suptitle('Sales by Year and Month \n')

    for idx, (year, group) in enumerate(sales_by_year_month.groupby('year')):
        row = idx // 2
        col = idx % 2

        axs[row, col].plot(group['month'], group['sales'], label=str(year))
        axs[row, col].set_title(f'Year {year}')
        axs[row, col].set_xlabel('Month')
        axs[row, col].set_ylabel('Sales')
        axs[row, col].legend()

    fig.tight_layout(rect=[0, 0, 1, 0.96])

    graph = get_graph()

    return graph


def get_plot4(sub_cat_sales):
    total_sales = sub_cat_sales.sum()
    percentages = [f'{(val / total_sales * 100):.1f}%' if val / total_sales >= 0.05 else '' for val in
                   sub_cat_sales.values]
    labels_with_percentages = [f'{label} ' for label, percent in zip(sub_cat_sales.index, percentages)]

    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 8))
    plt.title('Sales by Sub-Category \n')

    plt.pie(sub_cat_sales, labels=sub_cat_sales.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    plt.legend(labels_with_percentages, loc="upper right")

    plt.tight_layout()

    graph = get_graph()

    return graph


def get_plot5(sub_cat_profit):
    sub_cat_profit_sorted = sub_cat_profit.sort_values()

    plt.switch_backend('AGG')
    plt.figure(figsize=(12, 8))

    sub_cat_profit_sorted.plot(kind='barh', color=['green' if profit >= 0 else 'red' for profit in sub_cat_profit_sorted],
                              legend=False)

    plt.title('Profit by Sub Category \n')
    plt.xlabel('Total Profit')
    plt.ylabel('Sub Category')

    for i, v in enumerate(sub_cat_profit_sorted):
        plt.text(v, i, f'{int(v):d}', color='black', ha='left', va='center')

    plt.tight_layout()

    graph = get_graph()
    return graph


def get_plot6(sub_cat_profit_margin):
    sub_cat_profit_margin_sorted = sub_cat_profit_margin.sort_values(by='profit_margin')

    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Assigning colors to bars based on profit margin
    colors = ['green' if profit_margin >= 0 else 'red' for profit_margin in sub_cat_profit_margin_sorted['profit_margin'].values]

    # Plotting bars one by one with assigned colors and adding values
    for index, (category, profit_margin) in enumerate(sub_cat_profit_margin_sorted['profit_margin'].items()):
        color = colors[index]
        ax.barh(category, profit_margin, color=color)
        ax.text(profit_margin, index, f'{profit_margin:.2f}', ha='left', va='center')

    plt.title('Profit Margin by Subcategory \n')
    plt.xlabel('Profit Margin')
    plt.ylabel('Subcategory')

    plt.tight_layout()

    graph = get_graph()
    return graph

