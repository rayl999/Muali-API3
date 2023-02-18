from fastapi import FastAPI, Query, Body, status
import numpy as np
import pickle
import pandas as pd
import sklearn
from pydantic import BaseModel
import asyncio
from LoanSchedule import *
from MetadataAndSchemas import *;

app = FastAPI(title="Muali API.",
              version="0.0.6",
              description=app_description)
pickle_in = open('deploy_model.pkl', 'rb')
eligibilityML = pickle.load(pickle_in)

pickle_in2 = open('loan_amount_model.pkl', 'rb')
amountML = pickle.load(pickle_in2)

pickle_in3 = open('loan_amount_term_model.pkl', 'rb')
amountTermML = pickle.load(pickle_in3)

pickle_in4 = open('loan_score.pickle', 'rb')
score = pickle.load(pickle_in4)

class loanData(BaseModel):
    creditHistory: float = Body(...,
                                alias=loanData_metadata.get("Credit History").get("Alias"),
                                title=loanData_metadata.get("Credit History").get("Title"),
                                description=loanData_metadata.get("Credit History").get("Description"),
                                example=loanData_metadata.get("Credit History").get("Example"))
    Education: int = Body(...,
                          alias=loanData_metadata.get("Education").get("Alias"),
                          title=loanData_metadata.get("Education").get("Title"),
                          description=loanData_metadata.get("Education").get("Description"),
                          example=loanData_metadata.get("Education").get("Example"))
    Gender: float = Body(...,
                         alias=loanData_metadata.get("Gender").get("Alias"),
                         title=loanData_metadata.get("Gender").get("Title"),
                         description=loanData_metadata.get("Gender").get("Description"),
                         example=loanData_metadata.get("Gender").get("Example"))
    Married: int = Body(...,
                        alias=loanData_metadata.get("Married").get("Alias"),
                        title=loanData_metadata.get("Married").get("Title"),
                        description=loanData_metadata.get("Married").get("Description"),
                        example=loanData_metadata.get("Married").get("Example"))
    Income: float = Body(...,
                         alias=loanData_metadata.get("Income").get("Alias"),
                         title=loanData_metadata.get("Income").get("Title"),
                         description=loanData_metadata.get("Income").get("Description"),
                         example=loanData_metadata.get("Income").get("Example"))
    CoIncome: float = Body(...,
                           alias=loanData_metadata.get("CoIncome").get("Alias"),
                           title=loanData_metadata.get("CoIncome").get("Title"),
                           description=loanData_metadata.get("CoIncome").get("Description"),
                           example=loanData_metadata.get("CoIncome").get("Example"))
    selfEmployed: int = Body(...,
                             alias=loanData_metadata.get("Self Employed").get("Alias"),
                             title=loanData_metadata.get("Self Employed").get("Title"),
                             description=loanData_metadata.get("Self Employed").get("Description"),
                             example=loanData_metadata.get("Self Employed").get("Example"))



class scoreData(BaseModel):
    DebtRatio: int = Body(...,
                                alias=scoreData_metadata.get("DebtRatio").get("Alias"),
                                title=scoreData_metadata.get("DebtRatio").get("Title"),
                                description=scoreData_metadata.get("DebtRatio").get("Description"),
                                example=scoreData_metadata.get("DebtRatio").get("Example"))
    MonthlyIncome: int = Body(...,
                          alias=scoreData_metadata.get("MonthlyIncome").get("Alias"),
                          title=scoreData_metadata.get("MonthlyIncome").get("Title"),
                          description=scoreData_metadata.get("MonthlyIncome").get("Description"),
                          example=scoreData_metadata.get("MonthlyIncome").get("Example"))
    age: int = Body(...,
                        alias=scoreData_metadata.get("age").get("Alias"),
                        title=scoreData_metadata.get("age").get("Title"),
                        description=scoreData_metadata.get("age").get("Description"),
                        example=scoreData_metadata.get("age").get("Example"))
    NumberOfOpenCreditLinesAndLoans: int = Body(...,
                        alias=scoreData_metadata.get("NumberOfOpenCreditLinesAndLoans").get("Alias"),
                        title=scoreData_metadata.get("NumberOfOpenCreditLinesAndLoans").get("Title"),
                        description=scoreData_metadata.get("NumberOfOpenCreditLinesAndLoans").get("Description"),
                        example=scoreData_metadata.get("NumberOfOpenCreditLinesAndLoans").get("Example"))
    NumberRealEstateLoansOrLines: int = Body(...,
                        alias=scoreData_metadata.get("NumberRealEstateLoansOrLines").get("Alias"),
                        title=scoreData_metadata.get("NumberRealEstateLoansOrLines").get("Title"),
                        description=scoreData_metadata.get("NumberRealEstateLoansOrLines").get("Description"),
                        example=scoreData_metadata.get("NumberRealEstateLoansOrLines").get("Example"))
    NumberOfTime3059DaysPastDueNotWorse: int = Body(...,
                        alias=scoreData_metadata.get("NumberOfTime3059DaysPastDueNotWorse").get("Alias"),
                        title=scoreData_metadata.get("NumberOfTime3059DaysPastDueNotWorse").get("Title"),
                        description=scoreData_metadata.get("NumberOfTime3059DaysPastDueNotWorse").get("Description"),
                        example=scoreData_metadata.get("NumberOfTime3059DaysPastDueNotWorse").get("Example"))
    NumberOfTime6089DaysPastDueNotWorse: int = Body(...,
                        alias=scoreData_metadata.get("NumberOfTime6089DaysPastDueNotWorse").get("Alias"),
                        title=scoreData_metadata.get("NumberOfTime6089DaysPastDueNotWorse").get("Title"),
                        description=scoreData_metadata.get("NumberOfTime6089DaysPastDueNotWorse").get("Description"),
                        example=scoreData_metadata.get("NumberOfTime6089DaysPastDueNotWorse").get("Example"))
    NumberOfTimes90DaysLate: int = Body(...,
                        alias=scoreData_metadata.get("NumberOfTimes90DaysLate").get("Alias"),
                        title=scoreData_metadata.get("NumberOfTimes90DaysLate").get("Title"),
                        description=scoreData_metadata.get("NumberOfTimes90DaysLate").get("Description"),
                        example=scoreData_metadata.get("NumberOfTimes90DaysLate").get("Example"))

@app.post('/predict', tags=["Loanee & Artificial Intelligence"])
def checkEligibility(data: loanData = Body(..., examples=loanData_examples)):
    result = eligibilityML.predict([[data.creditHistory, data.Education, data.Gender]])
    value = ''
    if result[0] == 0:
        value = 'not eligiable'
    if result[0] == 1:
        value = 'eligiable'
    return {'prediction': value}


@app.post('/predictAmount', tags=["Loanee & Artificial Intelligence"])
def calcAmount(data: loanData = Body(..., examples=loanData_examples)):
    checkloanee = checkEligibility(data)
    amount = 0
    print(checkloanee)
    if list(checkloanee.values())[0] == 'not eligiable':
        return {'client is not eligible amount is': amount}
    else:
        if data.Income == 0:
            return {'client is not eligible amount is': amount}
        result = amountML.predict(
            [[data.Gender, data.Married, data.selfEmployed, (data.Income /3.75), data.CoIncome, data.creditHistory]])
        print(result)
        if result[0] != 0:
            return {'amount is': int(result[0]) * 1000 * 3.75}


@app.post('/predictAmountTerm', tags=["Loanee & Artificial Intelligence"])
async def calcAmountTerm(data: loanData = Body(..., examples=loanData_examples)):
    amount = calcAmount(data)
    print(amount.values())
    passToModel = float(list(amount.values())[0])
    if passToModel == 0:
        return {'client is not eligile amount is': -1}
    result = amountTermML.predict(
        [[data.Gender, data.Married, data.selfEmployed, (data.Income /3.75), data.CoIncome, passToModel, data.creditHistory]])
    print(result)
    if result[0] != 0:
        return {'term is': int(result[0]) * 3.75}




@app.post('/score', tags=["Score"])
def scoring(data: scoreData ):
    ind_variables = pd.DataFrame({
      'DebtRatio': [data.DebtRatio],
      'MonthlyIncome': [data.MonthlyIncome],
      'age': [data.age],
      'NumberOfOpenCreditLinesAndLoans': [data.NumberOfOpenCreditLinesAndLoans],
      'NumberRealEstateLoansOrLines': [data.NumberRealEstateLoansOrLines],
      'NumberOfTime30-59DaysPastDueNotWorse': [data.NumberOfTime3059DaysPastDueNotWorse],
      'NumberOfTime60-89DaysPastDueNotWorse': [data.NumberOfTime6089DaysPastDueNotWorse],
      'NumberOfTimes90DaysLate': [data.NumberOfTimes90DaysLate],
      'NumberOfDependents':[0], 
      'SeriousDlqin2yrs':[0], 
      'RevolvingUtilizationOfUnsecuredLines':[0]
    })
    result = score.score(ind_variables)

    return {'Score': result[0]}


@app.get("/amortizationSchedule", tags=["Schedules"])  # This function return the amortized schedule in JSON format.
async def calculateAmortizationSchedule(loanAmount: float = Query(...,
                                                                  alias=ammor_metadata.get("Loan Amount").get("Alias"),
                                                                  title=ammor_metadata.get("Loan Amount").get("Title"),
                                                                  description=ammor_metadata.get("Loan Amount").get(
                                                                      "Description"),
                                                                  examples=ammor_metadata.get("Loan Amount").get(
                                                                      "Examples")),
                                        loanDuration: int = Query(...,
                                                                  alias=ammor_metadata.get("Loan Duration").get(
                                                                      "Alias"),
                                                                  title=ammor_metadata.get("Loan Duration").get(
                                                                      "Title"),
                                                                  description=ammor_metadata.get("Loan Duration").get(
                                                                      "Description"),
                                                                  examples=ammor_metadata.get("Loan Duration").get(
                                                                      "Examples")),
                                        numPaymentsInYear: int = Query(...,
                                                                       alias=ammor_metadata.get(
                                                                           "Number Of Payments").get("Alias"),
                                                                       title=ammor_metadata.get(
                                                                           "Number Of Payments").get("Title"),
                                                                       description=ammor_metadata.get(
                                                                           "Number Of Payments").get("Description"),
                                                                       examples=ammor_metadata.get(
                                                                           "Number Of Payments").get("Examples")),
                                        annualRate: float = Query(...,
                                                                  alias=ammor_metadata.get("Annual Rate").get("Alias"),
                                                                  title=ammor_metadata.get("Annual Rate").get("Title"),
                                                                  description=ammor_metadata.get("Annual Rate").get(
                                                                      "Description"),
                                                                  examples=ammor_metadata.get("Annual Rate").get(
                                                                      "Examples"),
                                                                  le=1.00, ge=0.0)):
    return amortizationSchedule(loanAmount, annualRate, numPaymentsInYear, loanDuration)
