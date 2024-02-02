from import_export import resources, fields, widgets
from .models import Order
from datetime import datetime, timedelta


class OrderResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    row_id = fields.Field(column_name='row_id', attribute='row_id', widget=widgets.NumberWidget())
    order_id = fields.Field(column_name='order_id', attribute='order_id', widget=widgets.CharWidget())

    order_date = fields.Field(
        attribute='order_date',
        widget=widgets.DateWidget(format='%m/%d/%Y')
    )

    ship_date = fields.Field(
        attribute='ship_date',
        widget=widgets.DateWidget(format='%m/%d/%Y')
    )

    def before_import_row(self, row, **kwargs):
        # print(row)
        row['order_date'] = datetime(1899, 12, 30) + timedelta(days=int(row['order_date']))
        row['ship_date'] = datetime(1899, 12, 30) + timedelta(days=int(row['ship_date']))
        # print(row)

    class Meta:
        model = Order
        # exclude = ('id',)
        fields = ('row_id', 'order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_id', 'customer_name',
                  'segment', 'country', 'city', 'state', 'postal_code', 'region', 'product_id', 'category',
                  'sub_category', 'product_name', 'sales', 'quantity', 'discount', 'profit')
        export_order = ('row_id', 'order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_id', 'customer_name',
                        'segment', 'country', 'city', 'state', 'postal_code', 'region', 'product_id', 'category',
                        'sub_category', 'product_name', 'sales', 'quantity', 'discount', 'profit')
