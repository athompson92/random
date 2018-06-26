from django.db import models

# Create your models here.
import time

class Payment(object):
    #principle = models.DecimalField(max_digits=30, decimal_places=2)
    #interest = models.DecimalField(max_digits=30, decimal_places=2)
    def __init__(self, pmt_num, beginning_bal, principle, interest):
        #super(models.Model, self).__init__(self, *args, **kwargs)
        self.pmt_num = pmt_num
        self.beginning_balence = beginning_bal
        self.interest = interest
        self.principle = principle
        self.ending_balence = beginning_bal - principle

    def total(self):
        return self.interest + self.principle


class Loan(models.Model):

    def __init__(self, loan_amount, down_payment, annual_interest_rate, years, *args, **kwargs):
        super(models.Model, self).__init__(self, *args, **kwargs)
        self.current_balence = self.initial_loan_amount = loan_amount - down_payment 
        self.down_payment = down_payment
        self.annual_interest_rate = annual_interest_rate
        self.term = years
        self.periods = years * 12
        self.current_period = 0
        self.payments = []
        """
                  /  r(1 + r)^n  \
           A = P |----------------|
                  \ (1 + r)^n - 1/
        """
        P = self.initial_loan_amount
        r = self.annual_interest_rate / 12
        n = self.periods
        top = r * (1 + r)**n
        bottom = (1 + r)**n - 1
        self.pmt = P * (top / bottom) # A
        self.remaining_pmts = n - 1

    def current_payment(self):
        pmt_num = self.periods - self.remaining_pmts
        r = self.annual_interest_rate / 12
        interest = r * self.current_balence
        principle = self.pmt - interest
        
        return Payment(pmt_num, self.current_balence, principle, interest)

    def pay(self, payment):
        if int(self.current_balence - payment.principle) < 0:
            self.current_balence = 0
        else:
            self.current_balence -= payment.principle
        self.remaining_pmts -= 1

    def paid_off(self):
        return self.current_balence == 0

    def amortize(self):
        while (not self.paid_off()):
            p = self.current_payment()
            self.payments.append(p)
            self.pay(p)
            if int(self.current_balence - p.principle) < 0:
                break


