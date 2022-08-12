from django.shortcuts import render, redirect


def main_page(request):
    try:
        if request.user.is_authenticated():
            return redirect('user_account')
        else:
            return render(request, 'registration.html')
    except Exception:
        return redirect('user_account')

