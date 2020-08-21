from django import forms

class InputPostForm(forms.Form):
    select_choices = (
        (True, 'Boast'),
        (False, 'Roast')
        )
    text = forms.CharField(max_length=140)
    boast = forms.ChoiceField(
        choices=select_choices, label="Type:", initial='', widget=forms.Select())
    