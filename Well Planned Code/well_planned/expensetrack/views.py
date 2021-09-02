from django.shortcuts import render, redirect
from .models import Expense, Income
from django.http import HttpResponse


# Create your views here.
# home
def home(request):
    expenses = Expense.objects.all()
    income = Income.objects.get(id = 1)
    if request.POST:
        month = request.POST['month']
        year = request.POST['year']
        expenses = Expense.objects.filter(date__year=year, date__month=month)

    return render(request, 'index1.html', {'expenses': expenses, 'income':income})

# create
def add(request):
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        
        income_fetched = Income.objects.get(id = 1)
        present_balance = income_fetched.balance
        income_fetched.balance = present_balance - int(amount)
        expense = Expense(item=item, amount=amount, category=category, date=date)
        expense.save()
        income_fetched.save()

    return redirect(home)

def addIncome(request):
    
    income_fetched = Income.objects.get(id = 1)
    present_balance = income_fetched.balance
    if request.method == 'POST':
        income = request.POST['amount']
    
        income_fetched.income = income
        income_fetched.balance = present_balance + int(income)
        income_fetched.save()

    return redirect(home)

def update(request, id):
    id = int(id)
    expense_fetched = Expense.objects.get(id = id)
    last_expense = expense_fetched.amount
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense_fetched.item = item
        expense_fetched.amount = amount
        expense_fetched.category = category
        expense_fetched.date = date

        
        income_fetched = Income.objects.get(id = 1)
        present_balance = income_fetched.balance
        income_fetched.balance = present_balance + int(last_expense) - int(amount)

        expense_fetched.save()
        income_fetched.save()

    return redirect(home)

def delete(request, id):
    id = int(id)
    expense_fetched = Expense.objects.get(id = id)
    last_expense = expense_fetched.amount
    income_fetched = Income.objects.get(id = 1)
    present_balance = income_fetched.balance
    income_fetched.balance = present_balance + int(last_expense)

    expense_fetched.delete()
    income_fetched.save()

    return redirect(home)