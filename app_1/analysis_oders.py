from django.db.models import Sum, Count, F
from datetime import datetime, timedelta
from checkout.models import Order_Table
from django.db.models import Q
from django.db import models


def get_order_table_totals(start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.max.time())

    # Query for Order_Table
    order_table_totals = Order_Table.objects.filter(
        updated__range=(start_datetime, end_datetime)
    ).aggregate(
        total_count=Count('id'),
        pending_payment_count=Count('id', filter=models.Q(Order_Status='Pending payment')),
        pending_payment_subtotal=Sum('SubTotal_Price', filter=models.Q(Order_Status='Pending payment')),
        pending_payment_cost_price=Sum('order_table_2__Product__Cost_Price', filter=models.Q(Order_Status='Pending payment')),
        processing_count=Count('id', filter=models.Q(Order_Status='Processing')),
        processing_subtotal=Sum('SubTotal_Price', filter=models.Q(Order_Status='Processing')),
        processing_cost_price=Sum('order_table_2__Product__Cost_Price', filter=models.Q(Order_Status='Processing')),
        completed_count=Count('id', filter=models.Q(Order_Status='Completed')),
        completed_subtotal=Sum('SubTotal_Price', filter=models.Q(Order_Status='Completed')),
        completed_cost_price=Sum('order_table_2__Product__Cost_Price', filter=models.Q(Order_Status='Completed')),
        completed_revenue=Sum('SubTotal_Price', filter=models.Q(Order_Status='Completed')) - Sum('order_table_2__Product__Cost_Price', filter=models.Q(Order_Status='Completed')),

        on_hold_count=Count('id', filter=models.Q(Order_Status='On hold')),
        on_hold_subtotal=Sum('SubTotal_Price', filter=models.Q(Order_Status='On hold')),
        on_hold_cost_price=Sum('order_table_2__Product__Cost_Price', filter=models.Q(Order_Status='On hold')),
        picked_count=Count('id', filter=models.Q(Order_Status='Picked')),
        picked_subtotal=Sum('SubTotal_Price', filter=models.Q(Order_Status='Picked')),
        picked_cost_price=Sum('order_table_2__Product__Cost_Price', filter=models.Q(Order_Status='Picked')),
        cancelled_count=Count('id', filter=models.Q(Order_Status='Cancelled')),
        cancelled_subtotal=Sum('SubTotal_Price', filter=models.Q(Order_Status='Cancelled')),
        cancelled_cost_price=Sum('order_table_2__Product__Cost_Price', filter=models.Q(Order_Status='Cancelled')),
        # Add similar lines for other statuses
    )
    f=8
    f=8
    f=8

    return order_table_totals



def get_daily_totals():
    current_datetime = datetime.now()
    end_date = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = end_date - timedelta(days=1)
    daily_order_table_totals = get_order_table_totals(start_date, end_date)
    return daily_order_table_totals


def get_weekly_totals():
    current_datetime = datetime.now()
    end_date = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = end_date - timedelta(days=(end_date.weekday() + 1) % 7)  # Sunday of the week

    # print("w_start_date")
    # print(start_date)
    # print(end_date)

    weekly_order_table_totals = get_order_table_totals(start_date.date(), end_date.date())
    return weekly_order_table_totals
    # return 'DONE'


def get_monthly_totals():
    current_datetime = datetime.now()
    end_date = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = end_date.replace(day=1)  # 1st day of the month
    # print("m_start_date")
    # print(start_date)
    # print(end_date)

    monthly_order_table_totals = get_order_table_totals(start_date.date(), end_date.date())
    return monthly_order_table_totals
    # return 'DONE'

# Example usage
# daily_totals = get_daily_totals()
# weekly_totals = get_weekly_totals()
# monthly_totals = get_monthly_totals()

# print("Daily Totals:", daily_totals)
# print("Weekly Totals:", weekly_totals)
# print("Monthly Totals:", monthly_totals)



# Example usage
# start_date = datetime.now().date() - timedelta(days=7)  # Replace with your desired start date
# end_date = datetime.now().date()  # Replace with your desired end date
# order_table_totals = get_order_table_totals(start_date, end_date)
# print(order_table_totals)
