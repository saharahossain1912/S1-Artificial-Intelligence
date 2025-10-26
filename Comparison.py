# AI COMPARISON: Simple vs Advanced Rule-Based AI (comparison of their performance metrics)
import pandas as pd

from Simple_diabetes_ai import evaluate_simple_AI
from Advanced_diabetes_ai import evaluate_advanced_AI

def ai_comparison():
    print(" \nCOMPARISON OF RULE-BASED AI SYSTEMS\n ")

    #Evaluating both AIs and gettig their metrics
    accuracy_1, precision_1, recall_1, f1_1 = evaluate_simple_AI()
    print("\n")
    accuracy_2, precision_2, recall_2, f1_2 = evaluate_advanced_AI()

    # Combining results into a comparison DataFrame
    results = pd.DataFrame({
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
        'Simple_AI': [accuracy_1, precision_1, recall_1, f1_1],
        'Advanced_AI': [accuracy_2, precision_2, recall_2, f1_2]
    })
    # Printing comparison table
    print("\n")
    print(" PERFORMANCE COMPARISON ")
    print("========================================")
    print(results.to_string(index=False))

    # To Determine which AI performed better overall (based on average score)
    simple_avg = (accuracy_1 + precision_1 + recall_1 + f1_1) / 4
    advanced_avg = (accuracy_2 + precision_2 + recall_2 + f1_2) / 4

    if advanced_avg > simple_avg:
        print("The Advanced Rule-Based AI performed better overall")
    elif simple_avg > advanced_avg:
        print("The Simple Rule-Based AI performed better overall")
    else:
        print("Both AIs performed equally well.")

if __name__ == "__main__":
    ai_comparison()
