from django.shortcuts import render, redirect


def main_page(request):
    try:
        if not request.user.is_authenticated:
            return redirect('user_account/register')
        else:
            return render(request, 'index.html')
    except Exception as e:
        raise
