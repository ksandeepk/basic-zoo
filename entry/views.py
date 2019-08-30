from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import areg,booking
from random import randint
from django.core.mail import send_mail 
lp=''
import random
import datetime
import time

# Create your views here.
def zoo(request):
    return render(request,'zoo.html')

def adm(request):
    return render(request,'log.html')

def adminreg(request):
    if request.method=="POST":
        name=request.POST['nm']
        uname=request.POST['uname']
        mobile=request.POST['mob']
        password=request.POST['psd']
        rp=areg(name=name,username=uname,mobile=mobile,password=password)
        rp.save()    
        return render(request,'reg.html',{'msg':' Registration completed Sucessfully'})
    return render(request,'reg.html')

def log(request):
    if request.method=="POST":
        unam=request.POST['uname']
        password=request.POST['psd']
        al=areg.objects.get(username=unam,password=password)
        if al:
            return render(request,'adash.html')
        else:
            return HttpResponse("check details") 
    return render(request,'log.html')        

def display(request):
    tk=booking.objects.all()
    return render(request,'tkt.html',{'tk':tk})  


def usr(request):
    return render(request,'usr.html')

def book(request):
    if request.method=='POST':
        n='TK' 
        for i in range(0,4):
            n=n+str(randint(0,9))
        ticket_id=n
        uname=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mob']
        password=request.POST['psd'] 
        total=request.POST['mem']   
        vage=request.POST['age']
        country=request.POST['cntry']
        city=request.POST['city']
        id_proof=request.POST['proof']
        id_number=request.POST['num']
        vehical_no=request.POST['vehical']
        date=request.POST['date']
        time=request.POST['time']
        tk=booking(ticket_id=ticket_id,name=uname,vage=vage,email=email,mobile=mobile,password=password,vtotal=total,date=date,
                    country=country,city=city,id_proof=id_proof,id_number=id_number,vehical_no=vehical_no,time=time)
        tk.save()
        tid=request.session['id']=tk.ticket_id    
        sub="Ticket confirmation"
        sender='sandeep96424@yahoo.in'
        to=request.POST['email']
        msg="Hello Mr/Ms:"+request.POST['name']+"\n"+"Ticket_ID:"+tid+"\n"+"Total Members:"+request.POST['mem']+"\n"+"Visit Date:"+request.POST['date']+"\n"+"Time:"+request.POST['time']+"\n"+"-Thank you. Happy Joureny"+"\n"+"it is auto generated mail"
        send_mail(sub,msg,sender,[to])
        return render(request,'ticket.html',{'msg':"Ticket Booked Successfully",'email':tk.email,'ticket_id':tk.ticket_id,'name':tk.name,'vtotal':tk.vtotal,'date':tk.date,'time':tk.time})
    return render(request,'book.html')

def ulog(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['psd']
        lp=booking.objects.get(email=email,password=password)
        if lp:
            return render(request,'udash.html')
        else:
            return HttpResponse("check details") 
    return render(request,'ulog.html')

# def udash(request):
#     return render(request,'udash.html')

def ticket(request):
    if request.method=='POST':
        tid=request.POST['td']
        tkt=booking.objects.filter(ticket_id=tid)
        if tkt:
            return render(request,'udash.html',{'tkt':tkt})
        else:
            return render(request,'udash.html',{'msg':"Enter Correct Ticket_ID"})
        





def demo_piechart(request):
    """
    pieChart page
    """
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('piechart.html', data)
