from django import forms
from .models import Strategy_details,Strategy_Parameters,Symbol

Days = (
    ('Sun','Sun'),
    ('Mon','Mon'),
    ('Tue','Tue'),
    ('Thu','Thu'),
    ('Fry','Fry'),
)


class Symbol_Form(forms.ModelForm):
    Exchange = forms.CharField(max_length=30)
    Symbol = forms.CharField(max_length=30)
    Execution_Days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Days)

    class Meta:
        model = Symbol
        fiels = ['Execution_Days']