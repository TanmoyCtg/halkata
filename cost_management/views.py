from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
# Create your views here.

def my_expense(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'cost/expense.html', context)
    
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST) # form is a object
        form.save()
        return redirect('costlist')
    else:
        form = ExpenseForm
    template_name = 'cost/add_expense.html'
    return render(request, template_name, {'form':form})