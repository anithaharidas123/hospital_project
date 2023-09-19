from datetime import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import admin
from .models import doctor
from .models import patient_tb
from .models import book_appointment
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
        doc_log=0
        doc_log_on=0
        for i in data:
            if i.status=='onhold':
                doc_log = 1
            else:
                doc_log_on=1
        print(doc_log)
        param = {
            'data': data,
            'current_user': current_user,
            'doc_log': doc_log,
            'doc_log_on': doc_log_on,
        }
        return render(request, 'doctor_dashboard.html', param)

    return render(request, 'doctor_dashboard.html')
def doctor_dash1(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
       # print(current_user)
        data = doctor.objects.filter(USERNAME=current_user)
        data2 = patient_tb.objects.count()
        data3 = book_appointment.objects.count()
        s=book_appointment.objects.filter(status='Booked')
        data4=s.count()
        # for i in data2:
        #     s=i.count()
        doc_log = 0
        doc_log_on = 0
        for i in data:
            if i.status == 'onhold':
                doc_log = 1
            else:
                doc_log_on = 1

        param = {
            'data': data,
            'data2': data2,
            'data3': data3,
            'data4': data4,
            's':s,
            'current_user': current_user,
            'doctor_dash1': 1,
            'doc_log' : doc_log,
            'doc_log_on':  doc_log_on,
        }
        return render(request, 'doctor_dashboard.html', param)
    else:
        return render(request, 'doctor_dashboard.html')

def Your_Patient_Record(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
        data = doctor.objects.filter(USERNAME=current_user)
        for i in data:
            data2 = patient_tb.objects.filter(DOCTOR_DEPARTMENT=i.USERNAME)


        doc_log = 0
        doc_log_on = 0
        for i in data:
            if i.status == 'onhold':
                doc_log = 1
            else:
                doc_log_on = 1

        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
            'Your_Patient_Record': 1,
            'doc_log': doc_log,
            'doc_log_on': doc_log_on,
        }

        return render(request, 'doctor_dashboard.html', param)

    else:
        return render(request, 'doctor_dashboard.html')
def view_your_appointments(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
        data = doctor.objects.filter(USERNAME=current_user)
        for i in data:
            data2 = book_appointment.objects.filter(Doctor_Department=i.USERNAME)


        doc_log = 0
        doc_log_on = 0
        for i in data:
            if i.status == 'onhold':
                doc_log = 1
            else:
                doc_log_on = 1

        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
            'view_your_appointments': 1,
            'doc_log': doc_log,
            'doc_log_on': doc_log_on,
        }

        return render(request, 'doctor_dashboard.html', param)

    else:
        return render(request, 'doctor_dashboard.html')



def patient_dash1(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
        # print(current_user)
        data = doctor.objects.filter(USERNAME=current_user)
        doc_log = 0
        doc_log_on = 0
        for i in data:
            if i.status == 'onhold':
                doc_log = 1
            else:
                doc_log_on = 1

        param = {
            'data': data,
            'current_user': current_user,
            'patient_dash1': 1,
            'doc_log': doc_log,
            'doc_log_on': doc_log_on,
        }

        return render(request, 'doctor_dashboard.html',param)

    else:
        return render(request, 'doctor_dashboard.html')

def appo_dash1(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
        # print(current_user)
        data = doctor.objects.filter(USERNAME=current_user)
        doc_log = 0
        doc_log_on = 0
        for i in data:
            if i.status == 'onhold':
                doc_log = 1
            else:
                doc_log_on = 1

        param = {
            'data': data,
            'current_user': current_user,
            'appo_dash1': 1,
            'doc_log': doc_log,
            'doc_log_on': doc_log_on,
        }

        return render(request, 'doctor_dashboard.html',param)
    else:
        return render(request, 'doctor_dashboard.html')


def approve_doc1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2 = doctor.objects.all()
        param = {
            'data': data,
            'data2':data2,
            'current_user': current_user,
            'approve_doc1': 1,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')
def approve_tick(request,id):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2=doctor.objects.get(id=id)
        data2.status = 'Permanent'
        data2.save()
        param = {
            'data': data,
            'current_user': current_user,
            'data2': data2,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('approve_doc1')
def reject_icon(request,id):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2=doctor.objects.get(id=id)
        if data2.status == 'rejected':
            data2.delete()
            param = {
                'data': data,
                'current_user': current_user,
                'data2': data2,
            }
            return render(request, 'admin_dashboard.html', param)
        else:
            return redirect('approve_doc1')

def ad_drec(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2 = doctor.objects.all()
        param = {
            'data': data,
            'current_user': current_user,
            'data2': data2,
            'ad_drec': 1,

        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')

def reg_doc(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)



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


            rec1 = doctor(first_name= f_name,status = 'permanent', last_name=l_name, USERNAME=uname, PASSWORD=passw,DEPARTMENT=department,MOBILE=mobile,ADDRESS=address,File=f,)

            rec1.save()


            return render(request, 'admin_dashboard.html')
        param = {
                'data': data,
                'current_user': current_user,

                'reg_doc': 1,

            }
        return render(request, 'admin_dashboard.html', param)

    return render(request, 'admin_dashboard.html')
def patient(request):
    return render(request,'PATIENT.html')
def patient_signup(request):


    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        # print(f_name)
        l_name = request.POST.get('LAST_NAME')

        uname = request.POST.get('USERNAME')
        passw = request.POST.get('PASSWORD')
        # department = request.POST.get('department')
        # print(department)
        doctor_n = request.POST.get('doctor')

        mobile = request.POST.get('Mobile')
        address = request.POST.get('Address')
        symptoms = request.POST.get('Symptoms')
        rec2=patient_tb(firstname=f_name, lastname=l_name, USERNAME=uname, PASSWORD=passw, DOCTOR_DEPARTMENT=doctor_n, MOBILE=mobile, ADDRESS=address, Symptoms=symptoms)
        rec2.save()
        return render(request, 'patient_login.html')
    param = {
        'd': doctor.objects.all()
    }
    return render(request, 'patient_signup.html',param)
def patient_login(request):
    if request.method == 'POST':

        username = request.POST.get('USERNAME')
        password = request.POST.get('PASSWORD')

        # print(username)
        check_user = patient_tb.objects.filter(USERNAME=username, PASSWORD=password)
        if check_user:

            request.session["patient1"] = username
            return redirect('patient_dashboard')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'patient_login.html')
def logout(request):
    if 'admin1' in request.session:
        del request.session['admin1']
        return render(request,'HOME.html')
    elif 'doctor1' in request.session:
        del request.session['doctor1']
        return render(request, 'HOME.html')
    elif 'patient1' in request.session:
        del request.session['patient1']
        return render(request, 'HOME.html')

def d_spec(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        gynac=doctor.objects.filter(DEPARTMENT='Gynaecology')
        emergency=doctor.objects.filter(DEPARTMENT='Emergency Medicine')
        pediat=doctor.objects.filter(DEPARTMENT='Pediatrics')
        param = {
            'data': data,
            'current_user': current_user,
            'gynac': gynac,
            'emergency' : emergency,
            'pediat' : pediat,
            'd_spec': 1,

        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')




def approve_appointment2(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2 = doctor.objects.all()
        data3 = book_appointment.objects.filter(status='onhold')
        # for i in data3:
        #     print (i.firstname)
        param = {
            'data': data,
            'data2': data2,
            'data3': data3,
            'current_user': current_user,
            'approve_appointment2': 1,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')

def appo_book_tick(request,id):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data3 = book_appointment.objects.get(id=id)

        data3.status = 'Booked'
        data3.save()
        param = {
            'data': data,
            'current_user': current_user,
            'data3': data3,

        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('approve_appointment2')

def reject_book_icon(request,id):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data3 = book_appointment.objects.get(id=id)
        if data3.status == 'rejected':
            data3.delete()
            param = {
                'data': data,
                'current_user': current_user,
                'data3': data3,
            }
            return render(request, 'admin_dashboard.html', param)
        else:
            return redirect('approve_appointment2')


def app_tick_pat(request,id):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data3 = patient_tb.objects.get(id=id)

        data3.status = 'Registered'
        rec= book_appointment(Description=data3.Symptoms,Doctor_Department=data3.DOCTOR_DEPARTMENT,status='Booked')
        data3.save()
        param = {
            'data': data,
            'current_user': current_user,
            'data3': data3,
            'rec': rec,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('approve_patient2')

def reject_icon_pat(request,id):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data3 = patient_tb.objects.get(id=id)
        if data3.status == 'rejected':
            data3.delete()
            param = {
                'data': data,
                'current_user': current_user,
                'data3': data3,
            }
            return render(request, 'admin_dashboard.html', param)
        else:
            return redirect('approve_patient2')

def patient_dashboard(request):
    if 'patient1' in request.session:
        current_user = request.session['patient1']

        data = patient_tb.objects.filter(USERNAME=current_user)

        pat_log=0
        pat_log_on=0
        for i in data:
            if i.status=='onhold':
                pat_log = 1
            else:
                pat_log_on=1

        param = {
            'data': data,

            'current_user': current_user,
            'pat_log': pat_log,
            'pat_log_on': pat_log_on,
        }
        return render(request, 'patient_dashboard.html', param)

    return render(request, 'patient_dashboard.html')
def patient_dash_main(request):
    if 'patient1' in request.session:
        current_user = request.session['patient1']
       # print(current_user)
        data = patient_tb.objects.filter(USERNAME=current_user)

        current_datetime = datetime.now()
        for i in data:
            data2 = doctor.objects.filter(USERNAME=i.DOCTOR_DEPARTMENT)

        pat_log = 0
        pat_log_on = 0
        for i in data:
            if i.status == 'onhold':
                pat_log = 1
            else:
                pat_log_on = 1

        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
            'current_datetime': current_datetime,
            'patient_dash_main': 1,
            'pat_log' : pat_log,
            'pat_log_on':  pat_log_on,
        }
        return render(request, 'patient_dashboard.html', param)
    else:
        return render(request, 'patient_dashboard.html')
def patient_appoi(request):
    if 'patient1' in request.session:
        current_user = request.session['patient1']
        data = patient_tb.objects.filter(USERNAME=current_user)

        pat_log = 0
        pat_log_on = 0
        for i in data:
            if i.status == 'onhold':
                pat_log = 1
            else:
                pat_log_on = 1

        param = {
            'data': data,
            'current_user': current_user,
            'patient_appoi': 1,
            'pat_log': pat_log,
            'pat_log_on':  pat_log_on,
        }
        return render(request, 'patient_dashboard.html', param)
    else:
        return render(request, 'patient_dashboard.html')
def book_appoi_pat(request):
    if 'patient1' in request.session:
        current_user = request.session['patient1']
        data = patient_tb.objects.filter(USERNAME=current_user)
        for i in data:
           patient_name= i.firstname

        data2 = doctor.objects.all()

        pat_log = 0
        pat_log_on = 0
        for i in data:
            if i.status == 'onhold':
                pat_log = 1
            else:
                pat_log_on = 1
        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
            'book_appoi_pat': 1,
            'pat_log': pat_log,
            'pat_log_on': pat_log_on,
            'patient_name': patient_name,
        }


        if request.method == 'POST':
            Description = request.POST.get('freeform')
            Doctor_Department = request.POST.get('doctor')

            rec3= book_appointment(Description=Description,Doctor_Department=Doctor_Department,Name=patient_name)
            rec3.save()
            return redirect('book_app')

    return render(request, 'patient_dashboard.html', param)



    # else:
    #     return render(request, 'patient_dashboard.html')

def book_app(request):
    if 'patient1' in request.session:
        current_user = request.session['patient1']
        data = patient_tb.objects.filter(USERNAME=current_user)
        data2 =book_appointment.objects.all()
        pat_log = 0
        pat_log_on = 0
        for i in data:
            if i.status == 'onhold':
                pat_log = 1
            else:
                pat_log_on = 1

        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
            'book_app': 1,
            'pat_log': pat_log,
            'pat_log_on':  pat_log_on,
        }
        return render(request, 'patient_dashboard.html', param)
    else:
        return redirect('patient_dash_main')

def approve_patient2(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2 = patient_tb.objects.all()
        param = {
            'data': data,
            'data2':data2,
            'current_user': current_user,
            'approve_patient2': 1,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')
def patient_record2(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data3 = patient_tb.objects.all()
        param = {
            'data': data,
            'data3': data3,
            'current_user': current_user,
            'patient_record2': 1,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')

def delete_appointments(request):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
        data = doctor.objects.filter(USERNAME=current_user)
        for i in data:
            data2 = book_appointment.objects.filter(Doctor_Department=i.USERNAME)


        doc_log = 0
        doc_log_on = 0
        for i in data:
            if i.status == 'onhold':
                doc_log = 1
            else:
                doc_log_on = 1

        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
            'delete_appointments': 1,
            'doc_log': doc_log,
            'doc_log_on': doc_log_on,
        }

        return render(request, 'doctor_dashboard.html', param)

    else:
        return render(request, 'doctor_dashboard.html')

def ip_button(request,id):
    if 'doctor1' in request.session:
        current_user = request.session['doctor1']
        data = doctor.objects.filter(USERNAME=current_user)
        data2 = book_appointment.objects.get(id=id)
        data2.status = 'admit_processing'
        data2.save()
        doc_log = 0
        doc_log_on = 0
        for i in data:
            if i.status == 'onhold':
                doc_log = 1
            else:
                doc_log_on = 1

        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,

            'doc_log': doc_log,
            'doc_log_on': doc_log_on,
        }

        return render(request, 'doctor_dashboard.html', param)

    else:
        return render(request, 'doctor_dashboard.html')

def admit_patient1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2 = book_appointment.objects.filter(status='admit_processing')
        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
            'admit_patient1': 1,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')

def admit_tick_click(request,id):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        data2 = book_appointment.objects.get(id=id)
        data2.status = 'Admitted'
        data2.save()
        param = {
            'data': data,
            'data2': data2,
            'current_user': current_user,
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')

def discharge_admin(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = admin.objects.filter(USERNAME=current_user)
        # data2 = book_appointment.objects.get(id=id)
        #     if (request.method == 'POST'):


        param = {
            'data': data,
            # 'data2': data2,
            'current_user': current_user,
            'discharge_admin':1
        }
        return render(request, 'admin_dashboard.html', param)
    else:
        return redirect('admin_dashboard')