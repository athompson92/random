import time

class Payment(object):
    def __init__(self, principle, interest):
        self.interest = interest
        self.principle = principle

    def total(self):
        return self.interest + self.principle


class Loan(object):

    def __init__(self, loan_amount, down_payment, annual_interest_rate, years):
        self.current_balence = self.initial_loan_amount = loan_amount - down_payment
        self.down_payment = down_payment
        self.annual_interest_rate = annual_interest_rate
        self.term = years
        self.periods = years * 12
        self.current_period = 0
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
        r = self.annual_interest_rate / 12
        interest = r * self.current_balence
        principle = self.pmt - interest
        return Payment(principle, interest)

    def pay(self, payment):
        if int(self.current_balence - payment.principle) < 0:
            self.current_balence = 0
        else:
            self.current_balence -= payment.principle
        self.remaining_pmts -= 1

    def paid_off(self):
        return self.current_balence == 0


if __name__ == '__main__':
    l = Loan(20000, 1000, .075, 5)
    print ("Payment   Begining Balence    Interest    Principal \tEnding Balence")
    while (not l.paid_off()):
        p = l.current_payment()
        print ("{n:7.0f}\t{amt:18.2f}\t{intr:5.2f}\t{pr:11.2f}\t{bal:14.2f}".format(
        n=l.remaining_pmts + 1, amt=l.current_balence, intr=p.interest, pr=p.principle, bal=l.current_balence - p.principle))
        l.pay(p)
        if int(l.current_balence - p.principle) < 0:
            break
        time.sleep(0.2)
