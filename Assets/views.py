from django.shortcuts import render , redirect
from .models import Assets , AssetAssign
from Company.models import Employee
# Create your views here.
#The assign view where assets are assigned to employees.
def assign(request):
    asset = Assets.objects.filter(asset_status='Available')
    context = {'asset':asset}
    if request.method == "POST":
        asset_id = request.POST.get('asset')
        asset_id1 = Assets.objects.get(asset_id=asset_id)
        emp_id = request.POST.get('name')
        emp_id1 = Employee.objects.get(username=emp_id)
        asset_assign_date = request.POST.get('assign_date')
        asset_return_date = request.POST.get('return_date')
        asset_assign_status = "Currently Assigned"
        asset_log= "Nothing"
        asset_assign = AssetAssign(asset_id=asset_id1,emp_id=emp_id1,asset_assign_date=asset_assign_date,asset_return_date=asset_return_date,asset_assign_status=asset_assign_status,asset_log=asset_log)
        asset_assign.save()
        return redirect('assets')
    return render(request,'assign.html',context)