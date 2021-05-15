from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager, datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'todays_date' : datetime.now()
    }
    return render(request, "login_register.html", context)

def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)

        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')

        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id

        print(new_user.password)

        return redirect('/wall')

    return redirect('/')

def login(request):
    if request.method=="POST":
        
        if not User.objects.authenticate(request.POST['email'], request.POST['password']):
            messages.error(request, "Invalid Email/Password")
            return redirect('/')

        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id

        return redirect('/wall')

    return redirect('/')

# def logout(request):
#     request.session.flush()
#     return redirect('/')

# def success(request):
#     if 'user_id' not in request.session:
#         return redirect('/')

#     context = {
#         "user": User.objects.get(id=request.session['user_id'])
#     }

#     return render(request, "success.html", context)