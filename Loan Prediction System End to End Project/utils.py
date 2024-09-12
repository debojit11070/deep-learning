# import numpy as np 
# import joblib 


# def preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
#        CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
#        Property_Area):
#     test_data = [[Gender, Married, Education, Self_Employed, ApplicantIncome,
#        CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
#        Property_Area] ]  
#     trained_model = joblib.load("model.pkl") 
#     prediction = trained_model.predict(test_data) 

#     return prediction 


def preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
                   CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                   Property_Area):
    # Dummy implementation for demonstration
    # Replace with your actual preprocessing and prediction logic
    if Credit_History == '1':
        return 'Approved'
    else:
        return 'Not Approved'
