import matplotlib.pyplot as plt

metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
scores = [0.7487, 0.6471, 0.6157, 0.6310]
colors = ["#DF87B3", "#60d38e", "#D1DA83", "#D1A968"]
    
# Creating the graph
plt.figure(figsize=(10, 6))
    
# Creating bars
bars = plt.bar(metrics, scores, color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)
    
# Customizing the graph
plt.title('Advanced Rule-Based AI: Diabetes Diagnosis Performance',fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Performance Score', fontsize=12, fontweight='bold')
plt.ylim(0, 1.0)
plt.grid(axis='y', alpha=0.3, linestyle='--')
    
# Adding value labels on top of bars
for bar, score in zip(bars, scores):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.02,
            f'{score:.3f}', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
plt.tight_layout()
plt.savefig('advanced_ai_performance.png', dpi=300, bbox_inches='tight')
plt.show()