from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('home_page', permanent=True)