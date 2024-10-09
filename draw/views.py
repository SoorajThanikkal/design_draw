from django.shortcuts import render, redirect
from .models import Design,UserR
from django.contrib.auth.decorators import login_required



def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        wser=UserR(name=username, password=password)
        wser.save()
        return redirect('login')
    return render(request,'registration.html')
def logi(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserR.objects.filter(name=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('create_design')
    return render(request, 'login.html')
def create_design(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        data = request.POST.get('data')
        try:
            uid=request.session['user_id']
            usr=UserR.objects.get(id=uid)
            design = Design.objects.create(user=usr, name=name, data=data)
        except Exception as e:
            print(e)
            return redirect('login')
        return redirect('edit_design', design_id=design.id)
    return render(request, 'create_design.html')


def edit_design(request, design_id):
    try:
        uid=request.session['user_id']
        usr=UserR.objects.get(id=uid)
        design = Design.objects.get(id=design_id, user=usr)
    except:
        return redirect('login')
    if request.method == 'POST':
        design.data = request.POST.get('data')
        design.save()
    return render(request, 'edit_design.html', {'design': design})
