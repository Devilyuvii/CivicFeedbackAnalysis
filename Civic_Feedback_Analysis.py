'''                                      CIVIC PROBLEMS FEEDBACK ANALYSIS                                           '''
'''----------------------------------------------------------------------------------------------------------------------'''
''' GOAL : COLLECT CIVIC PROBLEMS FEEDBACK FROM THE PEOPLE LIVING IN THEIR LOCALITY,
    SO THAT  AFTER ANALISING THE PEOPLE'S RESPONSE WHETHER (GOOD) OR (BAD) AND THEN SOLVE THE ISSUE ASAP! '''

'''Summary:

> Collects feedback from users about public services (Garbage, Water, Roads, Electricity).

> Validates inputs ('Good' or 'Bad' only).

> Saves the responses to a CSV file (appends if it exists).

> Reads all responses and generates pie charts to visualize how people feel about each service.'''


import pandas as pd
import os

# Define questions
questions = {
    "Garbage Collection": "",
    "Water Supply": "",
    "Road Conditions": "",
    "Electricity Facility": ""
}

# Ask each question
print("Please answer the following questions with 'Good' or 'Bad':\n")
for key in questions:
    while True:
        response = input(f"How is the {key.lower()} in your area? (Good/Bad): ").strip().capitalize() 
        if response in ['Good', 'Bad']:
            questions[key] = response
            break
        else:
            print("Invalid input. Please enter 'Good' or 'Bad'.")

# Convert to DataFrame
df = pd.DataFrame([questions])

# Save to CSV (append if file exists)
file_name = "public_feedback.csv"
if os.path.exists(file_name):
    df.to_csv(file_name, mode='a', header=False, index=False) #add (append) new data to the end of the file instead of overwriting it.
else:
    df.to_csv(file_name, index=False)

print("\nThank you for your feedback!")

import matplotlib.pyplot as plt

# Load feedback data
df = pd.read_csv("public_feedback.csv")

# Count Good/Bad responses per question
summary = df.apply(pd.Series.value_counts).fillna(0)

# Plotting
for column in df.columns:
    values = df[column].value_counts()
    labels = values.index
    sizes = values.values

    plt.figure(figsize=(5,5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
    plt.title(f"Feedback on {column}")
    plt.axis('equal')
    plt.tight_layout()
    plt.show() 

    
