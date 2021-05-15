from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "messages": Message.objects.all(),
        "comments": Comment.objects.all()
    }
    return render(request, "index.html", context)

def message(request):
    if request.method=="POST":
        errors = Message.objects.message_validator(request.POST)

        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/wall')

        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.create(user=user, message=request.POST['message'])

    return redirect('/wall')

def comment(request, id):
    if request.method == "POST":
        errors = Comment.objects.comment_validator(request.POST)

        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/wall')

        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id=id)
        comment = Comment.objects.create(user=user, message=message, comment=request.POST['comment'])

    return redirect('/wall')

def delete(request, id):
    if request.method == "POST":
        message = Message.objects.get(id=id)
        message.delete()

    return redirect('/wall')