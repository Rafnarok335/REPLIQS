from django.shortcuts import render ,redirect
from .forms import CreateUser
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request, 'home.html')
@csrf_exempt
def register(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_manager = True
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)
@csrf_exempt
def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    elif request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            
            return redirect('assets')
            
    return render(request, 'login.html')
def assets(request):
    return render(request, 'asset.html')
