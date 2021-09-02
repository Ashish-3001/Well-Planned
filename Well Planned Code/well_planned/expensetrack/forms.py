from django.forms import ModelForm
from .models import Expense, Income

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = 'income'