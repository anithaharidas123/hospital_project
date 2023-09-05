from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import admin
from .models import doctor
# Create your views here.
def base(request):
    return render (request,'base.html')
def base2(request):
    return render(request,'base2.html')
def home(request):
    return render (request,'HOME.html')
def contact_us(request):
    return render(request,'contact_us.html')
def about_us(request):
    return render(request,'about_us.html')
def admin_home(request):
    return render(request,'ADMIN.html')
def admin_signup(request):
    if request.method == 'POST':
        f_name = request.POST.get("f_name")
        l_name = request.POST.get('LAST_NAME')


        uname = request.POST.get('USERNAME')
        passw = request.POST.get('PASSWORD')
        rec =admin(first_name = f_name,last_name=l_name,USERNAME=uname, PASSWORD=passw)
        rec.save()
        return render(request, 'admin_signup.html')
    return render(request,'admin_signup.html')
def admin_login(request):
    if request.method == 'POST':

        username = request.POST.get('USERNAME')
        password = request.POST.get('PASSWORD')

        # print(username)
        check_user = admin.objects.filter(USERNAME=username,PASSWORD=password)
        if check_user:

            request.session["admin1"] = username
            return redirect('admin_dashboard')
        else:
            return HttpResponse('Please enter valid Username or Password.')


    return render(request, 'admin_login.html')
def admin_dashboard(request):

    if 'admin1' in request.session:

        current_user = request.session['admin1']

        data = admin.objects.filter(USERNAME=current_user)
        # for i in data:
        #     print(i.first_name)
        param = {
            'data' : data,
            'current_user': current_user
        }
        return render(request, 'admin_dashboard.html', param)

    return render(request, 'admin_dashboard.html')
def admin_dash1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        param = {
            'data' : data,
            'current_user': current_user,
            'admin_dash1' :1,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect ('admin_login')
def doctor1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        param = {
            'data':data,
            'current_user': current_user,
            'doctor1':1,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect ('doctor1')

def patient1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        param = {
            'data': data,
            'current_user':current_user,
            'patient1': 1,
        }
        return render(request, 'admin_dashboard.html',param)
    else:
        return redirect('patient1')
def appointment1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        param = {
            'data': data,
            'current_user':current_user,
            'appointment1': 1,
        }
        return render(request, 'admin_dashboard.html',param)
    else:
        return redirect('appointment1')
def doctor_home(request):
    return render(request,'DOCTOR.html')
def doctor_signup(request):
    if request.method == 'POST':
        f_name = request.POST.get("f_name")
        l_name = request.POST.get('LAST_NAME')

        uname = request.POST.get('USERNAME')
        passw = request.POST.get('PASSWORD')
        department = request.POST.get('department')
        # print(department)

        mobile = request.POST.get('Mobile')
        address = request.POST.get('Address')
        f = request.POST.get('photo')
        rec = doctor(first_name=f_name, last_name=l_name, USERNAME=uname, PASSWORD=passw,DEPARTMENT=department,MOBILE=mobile,ADDRESS=address,File=f)
        rec.save()
        return render(request, 'doctor_signup.html')
    return render(request, 'doctor_signup.html')
def doctor_login(request):
    if request.method == 'POST':

        username = request.POST.get('USERNAME')
        password = request.POST.get('PASSWORD')

        # print(username)
        check_user = doctor.objects.filter(USERNAME=username, PASSWORD=password)
        if check_user:

            request.session["doctor1"] = username
            return redirect('doctor_dashboard')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'doctor_login.html')
def doctor_dashboard(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']

        data = doctor.objects.filter(USERNAME=current_user)

        param = {
            'data': data,
            'current_user': current_user
        }
        return render(request, 'doctor_dashboard.html', param)

    return render(request, 'doctor_dashboard.html')
def doctor_dash1(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
        data = doctor.objects.filter(USERNAME=current_user)
        param = {
            'data' : data,
            'current_user': current_user,
            'doctor_dash1':1,
        }
        return render(request, 'doctor_dashboard.html', param)
    else:
        return redirect('doctor_login')

def patient_dash1(request):
    return render(request, 'doctor_dashboard.html')