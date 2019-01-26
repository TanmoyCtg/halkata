from django import forms 
from .models import Expense 

class ExpenseForm(forms.ModelForm):
    class Meta:
        # need to clarify for which model 
        # we need to make form
        # Expense model we need form
        # __all__ makes field for Expense models all field
        model=Expense
        fields='__all__'

