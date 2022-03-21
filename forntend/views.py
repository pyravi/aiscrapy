from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'index.html') 


from django.http import HttpResponse
from django.core.mail import send_mail
# from django.shortcuts import render


def index(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        phone = request.POST.get('Phone')
        email = request.POST.get('Email')
        message = request.POST.get('Message')

        data = {
            'name':name,
            'phone':phone,
            "email":email,
            'message':message
        }
        print(data)
        message = '''
        Name:{}
        Phone:{}
        New Message:{}
        From:{}
        '''.format(data["name"],data["phone"],data["message"],data["email"])
        send_mail(data["message"],message,'',['aiscrappingsoftware@gmail.com'])
    # return HttpResponse("hello") 
    return render(request,'index.html') 

