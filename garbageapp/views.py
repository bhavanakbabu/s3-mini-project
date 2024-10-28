from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from garbageapp.models import driver, drivstatus, regcomp, userreg,bin,Notification

# Create your views here.
def index(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=userreg.objects.get(email=current_user)
        return render(request,"index.html",{'current_user':current_user,'user':user})
    return render(request,"index.html")
def userregister(request):
    if request.method=='POST':
        name=request.POST['name']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        mail=request.POST['email']
        phne=request.POST['mobile']
        usernameexists=userreg.objects.filter(username=name)
        emailexists=userreg.objects.filter(email=mail)
        if usernameexists:
            messages.error(request,"username already exsist")
        elif emailexists:
            messages.error(request,"Email already exsist")
        elif passw!=cpass:
            messages.error(request,"Password does not match")
        else:
            userreg.objects.create(username=name,password=passw,email=mail,phone=phne).save()
            return redirect("/")
    return render(request,"userregister.html")
def userlogin(request):
    if request.method=='POST':
        mail=request.POST['email']
        passw=request.POST['password']
        user=userreg.objects.filter(email=mail,password=passw)
        if user:
            request.session['email']=mail 
            return redirect("userpage")
        else:
            messages.error(request,"username and password doesnot match")
    return render(request,"userlogin.html")
def logout(request):
    del request.session['email']
    return redirect('/')

def userpage(request):
    if 'email' in request.session:
        current_user = request.session['email']
        user = userreg.objects.get(email=current_user)

        # Fetch complaints made by the current user
        user_complaints = regcomp.objects.filter(remail=current_user)

        # Fetch driver statuses associated with the user's area (if relevant)
        driver_updates = drivstatus.objects.filter(area=user.phone)  # Assuming phone is a proxy for area

        # Fetch notifications
        notifications = Notification.objects.filter(user=user).order_by('-timestamp')

        return render(request, "userpage.html", {
            'current_user': current_user,
            'user': user,
            'notifications': notifications
        })
    else:
        return redirect('login')
    

# def userpage(request):
#     if 'email' in request.session:
#         current_user=request.session['email']
#         user=userreg.objects.get(email=current_user)
#         return render(request,"userpage.html",{'current_user':current_user,'user':user})
    
    return render(request,"userpage.html")
def usercomp(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=userreg.objects.get(email=current_user)
        
        if request.method=='POST':
            compname=request.POST['username']
            comparea=request.POST['rarea']
            compemail=request.POST['remail']
            compl=request.POST['rcomp']
            compadd=request.POST['raddress']
            regcomp.objects.create(rarea=comparea,remail=compemail,rcomp=compl,raddress=compadd,username=compname)
            return redirect("userpage")
        return render(request,"usercomp.html",{'current_user':current_user,'user':user})
    return render(request,"usercomp.html")
def mycomplaint(request):
    if 'email' in request.session:
        current_user=request.session['email']
        user=userreg.objects.get(email=current_user)
        complaintuser=regcomp.objects.filter(remail=user.email)
        return render(request,"mycomplaint.html",{'complaint':complaintuser})
def admin2(request):
    notifications = Notification.objects.all().order_by('-timestamp')
    return render(request,"adminpage.html", {'notifications': notifications})

def adminlogin(request):
    adminuser="admin@gmail.com"
    pas="admin@123"
    if request.method=='POST':
        name=request.POST['email']
        passw=request.POST['password']
        if name==adminuser and passw==pas:
            request.session=name
            return redirect("admin2")
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,"adminlogin.html")

from .forms import NotificationForm  # Assuming a form for notifications

def admin_send_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin2')  # Redirect to admin dashboard or some page
    else:
        form = NotificationForm()

    return render(request, 'admin_send_notification.html', {'form': form})

def adminlogout(request):
    del request.session
    return redirect("/")

def createbin(request):
    if request.method == 'POST':
        binarea = request.POST['area']
        binmark = None
        drmail = request.POST['dmail']
        cperiod = request.POST['period']
        complaint_id = request.POST['complaint_id']  # Get the complaint ID from the form

        # Get the complaint object based on the ID
        complaint = regcomp.objects.get(id=complaint_id)
        
        # Create the bin and associate it with the complaint
        new_bin = bin.objects.create(
            area=binarea,
            landmark=binmark,
            dmail=drmail,
            period=cperiod,
            complaint=complaint
        )
        return redirect("admin2")

    # If GET request, fetch all complaints to display in the form
    complaints = regcomp.objects.filter(status='pending')  # Example filter for pending complaints
    return render(request, 'createbin.html', {'complaints': complaints})


    return render(request,"createbin.html")

def createdriver(request):
    if request.method=='POST':
        divname=request.POST['dname']
        divpass=request.POST['dpassword']
        divemail=request.POST['demail']
        divarea=request.POST['darea']
        driver.objects.create(dname=divname,dpassword=divpass,demail=divemail,darea=divarea)
        drivstatus.objects.create(drivername=divemail,area=divarea)
        return redirect("admin2")
    return render(request,"createdriver.html")

def driverlogin(request):
    if request.method=='POST':
        dvmail=request.POST['email']
        dvpassw=request.POST['password']
        driv=driver.objects.filter(demail=dvmail,dpassword=dvpassw)
        if driv:
            request.session['demail']=dvmail
            return redirect("driver2")
        else:
            messages.error(request,"username and password doesnot match")
    return render(request,"driverlogin.html")
def driverlogout(request):
    del request.session['demail']
    return redirect("/")
def driver2(request):
    return render(request,"driverpage.html")
def viewcomplaint(request):
    details=regcomp.objects.all()
    return render(request,"viewcomplaint.html",{'details':details})
def viewcomplaint2(request,id):
    complaint=regcomp.objects.get(id=id)
    if request.method=='POST':
        status=request.POST['Status']
        complaint.status=status
        complaint.save()
    return render(request,"complaint.html",{'regcomp':complaint})
def userdetails(request):
    details=userreg.objects.all()
    return render(request,"userdetails.html",{'details':details})
def updatebin(request):
    details=bin.objects.all()
    return render(request,"bin.html",{'details':details})
def updatebin1(request,id):
    bin1=bin.objects.get(id=id)
    if request.method=='POST':
        binarea=request.POST['area']
        binmark=request.POST['landmark']
        drmail=request.POST['dmail']
        cperiod=request.POST['period']
        bin1.area=binarea
        bin1.landmark=binmark
        bin1.dmail=drmail
        bin1.period=cperiod
        bin1.save()
        return redirect("admin2")
    return render(request,"updatebin.html",{'bin':bin1})
def deletebin(request,id):
    bin1=bin.objects.get(id=id)
    bin1.delete()
    return redirect("admin2")
def deletedriver(request,id):
    driver1=driver.objects.get(id=id)
    driver1.delete()
    return redirect("admin2")

def updatedriver(request):
    details=driver.objects.all()
    return render(request,"drivers.html",{'details':details})
def updatedriver1(request,id):
    driver1=driver.objects.get(id=id)
    driver2=drivstatus.objects.get(drivername=driver1.demail,area=driver1.darea)
    if request.method=='POST':
        divname=request.POST['dname']
        divpass=request.POST['dpassword']
        divemail=request.POST['demail']
        divarea=request.POST['darea']
        driver1.dname=divname
        driver1.dpassword=divpass
        driver1.demail=divemail
        driver1.darea=divarea
        driver2.drivername=divemail
        driver2.area=divarea
        driver1.save()
        driver2.save()
        return redirect("admin2")
    
    return render(request,"updatedriver.html",{'driver':driver1})


from django.shortcuts import render, redirect, get_object_or_404
from .models import driver, bin, drivstatus

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

def driverwork(request):
    if 'demail' in request.session:
        user = request.session['demail']
        drivermail = get_object_or_404(driver, demail=user)
        bins = bin.objects.filter(dmail=drivermail.demail)  # Get all bins assigned to the driver

        # Use .filter() instead of .get() to handle multiple objects
        reports = drivstatus.objects.filter(drivername=drivermail.demail)
        if not reports.exists():
            raise Http404("No drivstatus found for this driver.")
        report = reports.first()  # Retrieve the first result, or apply ordering as needed

        user_details = []
        for b in bins:
            if b.complaint:  # Check if the complaint is not None
                complaint = get_object_or_404(regcomp, id=b.complaint.id)  # Get the complaint related to the bin
                user_details.append({
                    'user_email': complaint.remail,  # User's email
                    'user_address': complaint.raddress,  # User address
                    'username': complaint.username,
                    'bin_area': b.area,
                    'bin_landmark': b.landmark,
                    'bin_period': b.period,
                    'status': report.status,  # Get the work status if applicable
                })
            else:
                # Optionally add a placeholder or skip this bin if no complaint is associated
                user_details.append({
                    'user_email': "N/A",
                    'user_address': "N/A",
                    'username': "N/A",
                    'bin_area': b.area,
                    'bin_landmark': b.landmark,
                    'bin_period': b.period,
                    'status': report.status,
                })

        print(f"User Details: {user_details}")  # Debugging line

        if request.method == 'POST':
            status = request.POST.get('Status')
            if status in dict(drivstatus.STATUS_CHOICES):
                report.status = status
                report.save()
            return redirect('driver2')

        return render(request, "driverwork.html", {
            'drivermail': drivermail,
            'bins': user_details,
            'report': report
        })

    
def workreport(request):
    report=drivstatus.objects.all()
    return render(request,"workreport.html",{'report':report})   
 
from django.contrib.auth.decorators import login_required

def user_notifications(request):
    if 'email' in request.session:
        current_user_email = request.session['email']
        user = userreg.objects.get(email=current_user_email)
        
        # Fetch notifications for the current user
        notifications = Notification.objects.filter(user=user).order_by('-timestamp')

        return render(request, 'userpage.html', {'notifications': notifications, 'user': user})
    else:
        return redirect('login')  # Redirect to login page if user is not logged in

def mark_notification_as_read(request, notification_id):
    if 'email' in request.session:
        current_user_email = request.session['email']
        user = userreg.objects.get(email=current_user_email)
        
        # Get the notification and mark it as read
        notification = get_object_or_404(Notification, id=notification_id, user=user)
        notification.is_read = True
        notification.save()
        
        return redirect('userpage')  # Redirect back to the user's page
    else:
        return redirect('login')  # Redirect to login if not logged in
    
def delete_notification(request, notification_id):
    if 'email' in request.session:
        current_user = request.session['email']
        notification = get_object_or_404(Notification, id=notification_id, user__email=current_user)
        notification.delete()
        return redirect('userpage')  # Redirect back to the user page after deletion
    else:
        return redirect('userlogin')  # Redirect to login if not logged in

def delete_notification_Admin(request, notification_id):
    if request.method == "POST":
        notification = get_object_or_404(Notification, id=notification_id)
        notification.delete()
        return redirect('admin2')
def payment(request):
    return render(request,"payment.html") 

def paycon(request):
    return render(request,"paycon.html")