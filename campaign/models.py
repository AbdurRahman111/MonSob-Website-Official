from django.db import models
from datetime import datetime
from app_1.models import Category, Products
# Create your models here.
from checkout.models import Order_Table
from app_1.models import Staff_Access
from vendor_dashboard_app.models import vendor_registration_table






class Order_notifications(models.Model):
    class Meta:
        verbose_name_plural = 'Order Notifications'
    Notification_order = models.ForeignKey(Order_Table, on_delete = models.CASCADE, blank=True, null=True)
    Notification_text = models.TextField()
    Notification_stuff = models.ManyToManyField(Staff_Access, blank=True, null=True)
    Notification_time = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        u = Order_notifications.objects.all().count()
        alll = Order_notifications.objects.all().order_by('-id')

        c=0
        if u < 500:
            for i in alll:
                pass
        else:
            for i in alll:
                c = c+1
                if c<500:
                    pass
                else:
                    p = Order_notifications.objects.filter(id = i.id)
                    p.delete()



        return self.Notification_text
    
        
        
        
class Vendor_notifications(models.Model):
    class Meta:
        verbose_name_plural = 'Vendor Notifications'
    Notification_vendor = models.ForeignKey(vendor_registration_table, on_delete = models.CASCADE, blank=True, null=True)
    Notification_text = models.TextField()
    Notification_stuff = models.ManyToManyField(Staff_Access, blank=True, null=True)
    Notification_time = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        u = Vendor_notifications.objects.all().count()
        alll = Vendor_notifications.objects.all().order_by('-id')

        c=0
        if u < 500:
            for i in alll:
                pass
        else:
            for i in alll:
                c = c+1
                if c<500:
                    pass
                else:
                    p = Vendor_notifications.objects.filter(id = i.id)
                    p.delete()

        return self.Notification_text
        
        
        
        
        
        
        