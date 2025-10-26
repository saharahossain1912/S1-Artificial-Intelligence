#RULE BASED AI-1: Simple diabetes diagnosis based on basic thresholds
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
#creating a basic rule-based AI for diabetes diagnosis
def simple_diabetes_check(glucose, bmi, age):
    if glucose >= 135 and bmi >= 37:
        return 1  #The patient is Diabetic
    elif glucose >= 126 and age >= 55:
        return 1
    else:
        return 0  #Not Diabetic

#To evaluate the basic rule-based AI
def evaluate_simple_AI():
    df = pd.read_csv('Diabetes-Diagnosis(A1)/Diabetes-kaggle.csv')
    
    #Making predictions by looping through patient records
    predictions = []
    for index, row in df.iterrows():
        result = simple_diabetes_check(
            row['Glucose'], 
            row['BMI'], 
            row['Age']
        )
        predictions.append(result)
    
    df['basic_prediction'] = predictions
    
    # Calculating metrics to check how well the basic AI performed
    accuracy = accuracy_score(df['Outcome'], df['basic_prediction'])
    precision = precision_score(df['Outcome'], df['basic_prediction'])
    recall = recall_score(df['Outcome'], df['basic_prediction'])
    f1 = f1_score(df['Outcome'], df['basic_prediction'])
    
    print("BASIC DIABETES AI EVALUATION:")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")

    return accuracy, precision, recall, f1

if __name__ == "__main__":
    evaluate_simple_AI()