from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
# Create your views here.

def index(request):
    return render(request,'pages/index.html')
def contact(request):
    return render(request,'pages/contact.html')
#def blog(request):
#    return render(request,'pages/blog.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form' : form})
