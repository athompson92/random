from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .loan import Loan
from .forms import LoanForm

def get_loan(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            with open("file", "w") as fd:
                fd.write(str(form.cleaned_data))
            data = form.cleaned_data
            l = Loan(float(data['loan_amount']),
                float(data['down_payment']),
                float(data['annual_interest_rate']),
                float(data['term']))
            l.amortize()
            
            return render(request, 'amortize/amortize.html', {'form': form, 'loan': l})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoanForm()

    return render(request, 'amortize/amortize.html', {'form': form})

def amortize_loan(request):
    if request.method == 'POST':
        l = Loan()
    pass
