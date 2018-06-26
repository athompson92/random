from django import forms

class LoanForm(forms.Form):
    loan_amount = forms.DecimalField(
        required=True,
        max_digits=20,
        decimal_places=2)
    down_payment = forms.DecimalField(
        required=True,
        max_digits=20,
        decimal_places=2)
    annual_interest_rate = forms.DecimalField(
        required=True,
        max_digits=3,
        decimal_places=2)
    term = forms.IntegerField(required=True)

