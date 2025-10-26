#RULE BASED AI-2: Advanced diabetes diagnosis based on multiple medical factors
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def advanced_diabetes_check(glucose, bmi, age, blood_pressure, insulin, dpf):
    if glucose >= 126: # RULE-1
        risk= 0 
        if bmi >= 30: risk += 1           # Obesity risk
        if age >= 45: risk += 1           # Age risk
        if blood_pressure >= 130: risk += 1  # Hypertension risk
        if dpf >= 0.8: risk += 1          # Family history risk
        
        if risk >= 1:  
            return 1  # The patient is Diabetic
    
    # RULE-2
    if glucose >= 200:
        return 1  # Diabetic
    
    # RULE-3
    if glucose >= 100: #(borderline state)
        risk = 0
        if bmi >= 30: risk += 1
        if age >= 45: risk += 1  
        if blood_pressure >= 130: risk += 1
        if insulin >= 120: risk += 1     
        if dpf >= 1.0: risk += 1          
        
        if risk >= 3: 
            return 1  # Diabetic
        
    return 0 # If none of the above, not diabetic
def evaluate_advanced_AI():
    df = pd.read_csv('Diabetes-Diagnosis(A1)/Diabetes-kaggle.csv')
    
    predictions = []
    for index, row in df.iterrows():
        result = advanced_diabetes_check(
            row['Glucose'],
            row['BMI'], 
            row['Age'],
            row['BloodPressure'],
            row['Insulin'],
            row['DiabetesPedigreeFunction']
        )
        predictions.append(result)
    
    df['advanced_predictions'] = predictions
    
    # Calculating the metrics
    accuracy = accuracy_score(df['Outcome'], df['advanced_predictions'])
    precision = precision_score(df['Outcome'], df['advanced_predictions'])
    recall = recall_score(df['Outcome'], df['advanced_predictions'])
    f1 = f1_score(df['Outcome'], df['advanced_predictions'])
    
    print("ADVANCED DIABETES AI EVALUATION:")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    
    return accuracy, precision, recall, f1


if __name__ == "__main__":
    evaluate_advanced_AI()
