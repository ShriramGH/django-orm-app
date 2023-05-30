from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required



# Create your views here.
def home(request):
    return render(request,"bank_accountapp/home.html")

@login_required(login_url='accounts/login/')
def names(request):
     return render(request,"bank_accountapp/account_details.html")

@permission_required('bank_accountapp.view_bank_branches',login_url='/accounts/login/')
def view_bank_branches(request):
    return render(request,"bank_accountapp/bank_branches.html")