from mysite.models import UserPassword
from django.http import HttpResponse
import json

def register(request):
    if request.session.get('username', False):
        return HttpResponse("You've already register.")
    info = request.POST.dict()
    c = UserPassword.objects.create(username=info["username"],
                                    password=info["password"])
    c.save()
    request.session['registered'] = True
    return HttpResponse('Thanks for your registered!')


def login(request):
    info = request.POST.dict()
    try:
        user = UserPassword.objects.get(username=info["username"])
    except UserPassword.DoesNotExist:
        return HttpResponse("Sorry, No such user exists.")
    if not (info["password"] == user.password):
        return HttpResponse("Sorry, Your password is incorrect.")
    request.session['username'] = user.username
    return HttpResponse("Welcome, You are Loged in!")


def logout(request):
    user = UserPassword.objects.get(username=request.session['username'])
    del request.session['username']
    return HttpResponse("You're logged out.")


def dummy(request):
    if request.session.has_key("username"):
        username = request.session["username"]
        user = UserPassword.objects.get(username=username)
        return HttpResponse("This is your dummy page")
    else:
        return HttpResponse("Sorry, You are NOT logged in.")


def move(request):
    info = request.GET.get()
    data = json.loads(info)

    return HttpResponse(data)
