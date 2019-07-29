"""
if applicant has high income AND good credit
    Eligible for loan
"""

has_high_income = True
has_good_income = True
has_criminal_record = False

if has_high_income and has_good_income:
    print("Eligible for loan")

"""
if applicant has high income OR good credit
    Eligible for loan
"""

if has_high_income or has_good_income:
    print("Eligible for loan")

"""
if applicant has high good credit and doesn't have a crinminal record
    Eligible for loan
"""

if has_good_income and not has_criminal_record:
    print("Customer is eligible for loan")