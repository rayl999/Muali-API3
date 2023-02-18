# This file will contain all functions related to creating loan payments schedule, amortized.

def pmt(loanAmount: float, annualRate: float, numPaymentsInYear: int, loanDuration: int):
    numPaymentsPeriod = numPaymentsInYear * loanDuration  # Total number of payments in months.
    r = annualRate / numPaymentsInYear  # Rate of payments.
    monthlyInstallment = loanAmount / ((((1 + r) ** numPaymentsPeriod) - 1) / (r * (1 + r) ** numPaymentsPeriod))
    return monthlyInstallment


def ipmt(loanAmount: float, annualRate: float, numPaymentsInYear: int, loanDuration: int):
    r = annualRate / numPaymentsInYear  # Rate of payments.
    interestAmount = (loanAmount * r +
                      pmt(loanAmount, annualRate, numPaymentsInYear, loanDuration)) - pmt(loanAmount, annualRate,
                                                                                          numPaymentsInYear,
                                                                                          loanDuration)
    return interestAmount


def ppmt(loanAmount: float, currentAmount: float, annualRate: float, numPaymentsInYear: int, loanDuration: int):
    principalAmount = pmt(loanAmount, annualRate, numPaymentsInYear, loanDuration) - ipmt(currentAmount, annualRate,
                                                                                          numPaymentsInYear,
                                                                                          loanDuration)
    return principalAmount

def amortizationSchedule(loanAmount: float, annualRate: float, numPaymentsInYear: int, loanDuration: int):
    numPaymentsPeriod = numPaymentsInYear * loanDuration  # Total number of payments in months.
    monthlyInstallment = round(pmt(loanAmount, annualRate, numPaymentsInYear, loanDuration), 2)
    i = 1
    amortizedSchedule = dict()
    currentAmount = loanAmount
    while i <= numPaymentsPeriod:
        # Update monthly payment each loop by recalculating principal and interest.
        principal = round(ppmt(loanAmount, currentAmount, annualRate, numPaymentsInYear, loanDuration), 2)
        interest = round(ipmt(currentAmount, annualRate, numPaymentsInYear, loanDuration), 2)
        currentAmount -= principal
        amortizedSchedule[i] = dict(monthlyPayment=monthlyInstallment, principal=principal, interest=interest,
                                    balance=round(max(0, currentAmount), 2))
        i += 1
    return amortizedSchedule
