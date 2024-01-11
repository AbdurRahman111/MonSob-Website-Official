from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from app_1.models import Staff_Access
from campaign.models import Order_notifications, Vendor_notifications
from vendor_dashboard_app.models import vendor_registration_table
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages


def reset_password(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        if request.method == "POST":
            erorr_message = ""
            current_Password = request.POST.get('current_Password')
            new_password = request.POST.get('new_password')
            re_type_new_password = request.POST.get('re_type_new_password')

            if staff_admin:
                usr_rol = staff_admin
            elif staff_shop_manager:
                usr_rol = staff_shop_manager
            elif staff_customer_support:
                usr_rol = staff_customer_support
            elif staff_upload_team:
                usr_rol = staff_upload_team

            get_staff = Staff_Access.objects.get(Username=usr_rol)

            if current_Password == get_staff.Password:
                if new_password == re_type_new_password:
                    get_staff.Password=new_password
                    get_staff.save()
                    messages.success(request, "Your Password is Update Successfully !!")
                    return redirect('deshboard_index')
                else:
                    erorr_message = "New Password & Re-type New Password !"
                    con = {'erorr_message': erorr_message}
                    return render(request, 'reset_password_staff.html', con)
            else:
                erorr_message = "Password is wrong !"
                con = {'erorr_message':erorr_message}
                return render(request, 'reset_password_staff.html', con)

        else:
            return render(request, 'reset_password_staff.html')
    else:
        return redirect('deshboard_login')



def all_notification(request, template='all_notification.html', page_template='all_notification_new.html'):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        all_Order_notifications = Order_notifications.objects.order_by('-Notification_time')
        qty_all_Order_notifications = all_Order_notifications.count()
        context = {
            'all_Order_notifications':all_Order_notifications,
            'qty_all_Order_notifications':qty_all_Order_notifications,
            'page_template': page_template,
        }
        if request.is_ajax():
            template = page_template
        return render(request, template, context)
    else:
        return redirect('deshboard_login')




def vendor_all_notification(request, template='vendor_all_notification.html', page_template='vendor_all_notification_new.html'):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        all_Order_notifications = Vendor_notifications.objects.order_by('-Notification_time')
        qty_all_Order_notifications = all_Order_notifications.count()
        context = {
            'all_Order_notifications':all_Order_notifications,
            'qty_all_Order_notifications':qty_all_Order_notifications,
            'page_template': page_template,
        }
        if request.is_ajax():
            template = page_template
        return render(request, template, context)
    else:
        return redirect('deshboard_login')



@csrf_exempt
def get_notification(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)



        new_thiks = Order_notifications.objects.order_by('-Notification_time')[:5]


        a = new_thiks.count()


        # new_thiks = base_notifications.objects.exclude(Notification_stuff = get_Staff_Access)
        # new_thiks = base_notifications.objects.filter(Notification_stuff__in = get_Staff_Access.id)


        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)



@csrf_exempt
def get_vendor_notification(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)

        new_thiks = Vendor_notifications.objects.order_by('-Notification_time')[:5]

        a = new_thiks.count()

        # new_thiks = base_notifications.objects.exclude(Notification_stuff = get_Staff_Access)
        # new_thiks = base_notifications.objects.filter(Notification_stuff__in = get_Staff_Access.id)


        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)


def upload_vendor_Store_details_notification(request, pk):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:

        vendor_registration_table_get = vendor_registration_table.objects.get(id=pk)
        return redirect('upload_vendor_Store_details', vendor_registration_table_get.vendor_phone_no)
    else:
        return redirect('deshboard_login')




@csrf_exempt
def get_notification_qty(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)

        new_thiks = Order_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')[:5]


        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)



@csrf_exempt
def vendor_get_notification_qty(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)

        new_thiks = Vendor_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')[:5]

        get_cat_seri = serializers.serialize('json', new_thiks)
        return JsonResponse(get_cat_seri, safe=False)



@csrf_exempt
def make_seen_notification(request):

    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')
    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)
        new_thiks = Order_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')

        for i in new_thiks:
            i.Notification_stuff.add(get_Staff_Access)
        return HttpResponse(True)




@csrf_exempt
def vendor_make_seen_notification(request):
    staff_admin = request.session.get('deshboard_admin_username')
    staff_shop_manager = request.session.get('deshboard_shop_manager_username')
    staff_customer_support = request.session.get('deshboard_customer_support_username')
    staff_upload_team = request.session.get('deshboard_upload_team_username')

    if staff_admin or staff_shop_manager or staff_customer_support or staff_upload_team:
        user_of_deshboard_now = ''
        if staff_admin:
            user_of_deshboard_now = staff_admin
        if staff_shop_manager:
            user_of_deshboard_now = staff_shop_manager
        if staff_customer_support:
            user_of_deshboard_now = staff_customer_support
        if staff_upload_team:
            user_of_deshboard_now = staff_upload_team


        get_Staff_Access = Staff_Access.objects.get(Username = user_of_deshboard_now)
        new_thiks = Vendor_notifications.objects.exclude(Notification_stuff__in = [get_Staff_Access]).order_by('-Notification_time')

        for i in new_thiks:
            i.Notification_stuff.add(get_Staff_Access)
        return HttpResponse(True)


def dashboard_old_order_report(request):
    return render(request, 'dashboard_old_order_report.html')