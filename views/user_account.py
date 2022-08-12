from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from tweet_app.models import UserAccount


@csrf_exempt
def registration(request):
    if not request.user.is_authenticated:
        if 'username' not in request.POST:
            return render(request, 'user_account/registration.html')

        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not UserAccount.objects.filter(username=username, email=email).exists():
            UserAccount.objects.create_user(username, email, password)
            authenticate(username=username, password=password)
        else:
            user = UserAccount.objects.get(username=username, email=email)
            if user and user.is_active:
                login(request, user)

        return HttpResponse({"success": True})
    else:
        return render(request, 'index.html')
