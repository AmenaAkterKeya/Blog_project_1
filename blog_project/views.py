from django.shortcuts import render
from posts.models import posts
def home(request):
    data = posts.objects.all()
    
    return render(request, 'index.html', {'data' : data})