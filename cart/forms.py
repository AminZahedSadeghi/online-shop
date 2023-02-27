from django import forms

class AddProductToCartForm(forms.Form):
    QTY_CHOICES = [(i, str(i)) for i in range(1, 31)]

    qty = forms.TypedChoiceField(choices=QTY_CHOICES, coerce=int)
    