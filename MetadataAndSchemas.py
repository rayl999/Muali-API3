# This file contains ALL the metadata provided in the project. Whether it's /docs metadata, or function-specific
# metadata, or even categorization and schemas.

app_description = """
Muali API helps you do awesome stuff. 🚀

## Eligibility Prediction.

You can **predict the eligibility** of any user given the required information.

You will be able to:

* **Predict if user is eligible or not.**
* **Check maximum loan amount allowed for user given their eligibility.**
* **Check term/duration of the loan.**

## Schedule Generation.

You can **retrieve a detailed amortization schedule** of any loan.

You will be able to:

* **Retrieve an amortized schedule detailing monthly payments in terms of principal and interest.**

"""

tags_metadata = [
    {
        "name": "Loanee & Artificial Intelligence",
        "description": "Operations with loanees, and all artificial-intelligence methods.",
    },
        {
        "name": "Score",
        "description": "Operations with loanees, and all artificial-intelligence methods.",
    },
    {
        "name": "Schedules",
        "description": "Create amortized schedules based on specific inputs.",
    },
]

loanData_metadata = { # The class loanData parameters metadata. Class can be found in main.py
    "Credit History": {
        "Alias": "Credit History",
        "Title": "Credit History",
        "Description": "Credit history meets guidelines. If value is 1.00, it meets guidelines, otherwise it is 0.",
    },
    "Education": {
        "Alias": "Education",
        "Title": "Education",
        "Description": "Education of the loanee applicant. If 1, graduate, if 0, not graduate.",
    },
    "Gender": {
        "Alias": "Gender",
        "Title": "Gender",
        "Description": "The gender of the loanee applicant. If 1, is male, if 0, is female.",
    },
    "Married": {
        "Alias": "Married",
        "Title": "Married",
        "Description": "The marital status of the loanee applicant. if 1, is married, if 0, is not married.",
    },
    "Income": {
        "Alias": "Income",
        "Title": "Income",
        "Description": "The income of the applicant. Written in full, so if applicant earns 5000 you put 5000.",
    },
    "CoIncome": {
        "Alias": "Co Income",
        "Title": "Co Income",
        "Description": "The income of the Co-Applicant, who is the person applying for a loan alongside the applicant..",
    },
    "Self Employed": {
        "Alias": "Self Employed",
        "Title": "Self Employed",
        "Description": "The self-employment status of applicant. If 1, is self-employed, if 0, not self-employed.",
    },
}

scoreData_metadata = { # The class loanData parameters metadata. Class can be found in main.py
    "DebtRatio": {
        "Alias": "DebtRatio ",
        "Title": "DebtRatio ",
        "Description": "",
    },
    "MonthlyIncome": {
        "Alias": "MonthlyIncome",
        "Title": "MonthlyIncome",
        "Description": "",
    },
    "age": {
        "Alias": "age",
        "Title": "age",
        "Description": "",
    },
    "NumberOfOpenCreditLinesAndLoans": {
        "Alias": "NumberOfOpenCreditLinesAndLoans",
        "Title": "NumberOfOpenCreditLinesAndLoans",
        "Description": "",
    },
    "NumberRealEstateLoansOrLines": {
        "Alias": "NumberRealEstateLoansOrLines",
        "Title": "NumberRealEstateLoansOrLines",
        "Description": "",
    },
    "NumberOfTime3059DaysPastDueNotWorse": {
        "Alias": "NumberOfTime3059DaysPastDueNotWorse",
        "Title": "NumberOfTime3059DaysPastDueNotWorse",
        "Description": "",
    },
    "NumberOfTime6089DaysPastDueNotWorse": {
        "Alias": "NumberOfTime6089DaysPastDueNotWorse",
        "Title": "NumberOfTime6089DaysPastDueNotWorse",
        "Description": "",
    },
        "NumberOfTimes90DaysLate": {
        "Alias": "NumberOfTimes90DaysLate",
        "Title": "NumberOfTimes90DaysLate",
        "Description": "",
    },
}
loanData_examples = {
            "Valid Example 1":
                {
                    "summary": "First valid example.",
                    "description": "A valid example of a person whose credit history is eligible (1), is graduated (1),"
                                   "is a male (1), is not married (0), has an income of 5000, has no CoIncome since he"
                                   "is not married (0), and is not self employed (0)",
                    "value": {
                        "Credit History": 1,
                        "Education": 1,
                        "Gender": 1,
                        "Married": 0,
                        "Income": 5000,
                        "Co Income": 0,
                        "Self Employed": 0
                    }
                },
    "Valid Example 2":
        {
            "summary": "Second valid example.",
            "description": "A valid example of a person whose credit history is not eligible (1), is graduated (1),"
                           "is a female (1), is married (0), has an income of 9000, has CoIncome of 2350 since she"
                           "is married, and is self employed (1)",
            "value": {
                "Credit History": 0,
                "Education": 1,
                "Gender": 0,
                "Married": 1,
                "Income": 8000,
                "Co Income": 2350,
                "Self Employed": 1
            }
        },
        }

ammor_metadata = {  # The amortization schedule parameters metadata. Function can be found in main.py
    "Loan Amount": {
        "Alias": "Loan Amount",
        "Title": "Loan Amount",
        "Description": "The amount of the loan.",
        "Examples": {"Valid Example 1": {"value": 30000}, "Valid Example 2": {"value": 150000},
                     "Invalid Example 1": {"value": -30000}}
    },
    "Loan Duration": {
        "Alias": "Loan Duration",
        "Title": "Loan Duration",
        "Description": "The duration of the loan in years.",
        "Examples": {"Valid Example 1": {"value": 3}, "Valid Example 2": {"value": 10},
                     "Invalid Example 1": {"value": -5}}
    },
    "Number Of Payments": {
        "Alias": "Number of Payments Per Year",
        "Title": "Number of Payments",
        "Description": "Number of payments per year. If monthly, put 12.",
        "Examples": {"Valid Example 1": {"value": 12}, "Valid Example 2": {"value": 36},
                     "Invalid Example 1": {"value": 0}}
    },
    "Annual Rate": {
        "Alias": "Annual Interest Rate",
        "Title": "Annual Rate",
        "Description": "Annual Interest Rate. Value is multiplied by one hundred, "
                       "I.e. 0.085 is 8.5% annual interest rate.",
        "Examples": {"Valid Example 1": {"value": 0.015}, "Valid Example 2": {"value": 0.067},
                     "Invalid Example 1": {"value": -0.05}}
    }
}