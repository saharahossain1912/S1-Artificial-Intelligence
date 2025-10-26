import matplotlib.pyplot as plt

metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
scores = [0.6901, 0.6364, 0.2612, 0.3704]
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']
    
# Creating the graph
plt.figure(figsize=(10, 6))
    
# Creating bars with different colors
bars = plt.bar(metrics, scores, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)
    
# Customizing the graph
plt.title('Simple Rule-Based AI: Diabetes Diagnosis Performance',fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Performance Score', fontsize=12, fontweight='bold')
plt.ylim(0, 1.0)
plt.grid(axis='y', alpha=0.3, linestyle='--')
    
# Adding value labels on top of bars
for bar, score in zip(bars, scores):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.02,
            f'{score:.3f}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
plt.tight_layout()
plt.savefig('simple_ai_performance.png', dpi=300, bbox_inches='tight')
plt.show()