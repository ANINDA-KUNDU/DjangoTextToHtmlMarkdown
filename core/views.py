from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Code
from django.utils import timezone
# Create your views here.

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def code(request):
    codes = Code.objects.filter( user = request.user ).order_by("-created_at")
    return render(request, 'core/code.html', {'codes': codes})

@login_required
def mark_down(request, pk):
    codes = get_object_or_404( Code, id = pk, user = request.user )
    return render(request, 'core/mark_down.html', {'codes': codes})

@login_required
def create_markdown(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        Code.objects.create(
            user = request.user,
            title = title,
            body = body,
            created_at = timezone.now()
        )
        return redirect('code')
    return render(request, 'core/create_markdown.html')