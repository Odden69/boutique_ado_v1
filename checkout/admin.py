from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):  # Presents a list of editable order rows instead of having to 
    # go in to a specific order row to edit 
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',  # prevents editing of the values in these fields
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name', # order of fields in the form
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name', # Column display in the order list
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)  # Showing the order list with the most recent order at the top


admin.site.register(Order, OrderAdmin)
