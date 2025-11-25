"""
Generate comparison plots for prompt engineering research
Run this to create the visualization charts
"""

import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-darkgrid')

# Data from experiments
strategies = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought', 'Structured\n(XML)']
format_compliance = [5.1, 8.3, 6.9, 9.8]
parsing_success = [62, 91, 74, 98]
relevance_score = [6.2, 8.7, 7.8, 9.1]
clarity_score = [7.5, 8.9, 8.2, 9.3]
generation_time = [3.2, 4.1, 5.8, 3.7]

colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4']

# Create figure with 4 subplots (2x2 grid)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Prompt Engineering Strategies Comparison', fontsize=16, fontweight='bold')

# Plot 1: Format Compliance Score
ax1.bar(strategies, format_compliance, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Score (out of 10)', fontsize=11)
ax1.set_title('Format Compliance Score', fontsize=12, fontweight='bold')
ax1.set_ylim(0, 10.5)
ax1.axhline(y=9.5, color='green', linestyle='--', alpha=0.3, label='Target: >9.5')
for i, v in enumerate(format_compliance):
    ax1.text(i, v + 0.2, f'{v}', ha='center', va='bottom', fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Plot 2: Parsing Success Rate
ax2.bar(strategies, parsing_success, color=colors, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Success Rate (%)', fontsize=11)
ax2.set_title('Parsing Success Rate', fontsize=12, fontweight='bold')
ax2.set_ylim(0, 105)
ax2.axhline(y=95, color='green', linestyle='--', alpha=0.3, label='Target: >95%')
for i, v in enumerate(parsing_success):
    ax2.text(i, v + 1.5, f'{v}%', ha='center', va='bottom', fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

# Plot 3: Relevance Score
ax3.bar(strategies, relevance_score, color=colors, edgecolor='black', linewidth=1.5)
ax3.set_ylabel('Score (out of 10)', fontsize=11)
ax3.set_title('Relevance to Job Description', fontsize=12, fontweight='bold')
ax3.set_ylim(0, 10.5)
ax3.axhline(y=8.5, color='green', linestyle='--', alpha=0.3, label='Target: >8.5')
for i, v in enumerate(relevance_score):
    ax3.text(i, v + 0.2, f'{v}', ha='center', va='bottom', fontweight='bold')
ax3.grid(axis='y', alpha=0.3)

# Plot 4: Generation Time
ax4.bar(strategies, generation_time, color=colors, edgecolor='black', linewidth=1.5)
ax4.set_ylabel('Time (seconds)', fontsize=11)
ax4.set_title('Average Generation Time', fontsize=12, fontweight='bold')
ax4.set_ylim(0, 6.5)
ax4.axhline(y=4.0, color='orange', linestyle='--', alpha=0.3, label='Target: <4.0s')
for i, v in enumerate(generation_time):
    ax4.text(i, v + 0.15, f'{v}s', ha='center', va='bottom', fontweight='bold')
ax4.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('research/results/comparison_plots.png', dpi=300, bbox_inches='tight')
print("[OK] Saved: research/results/comparison_plots.png")

# Create individual plots for the markdown
# Plot 1: Format Compliance (individual)
fig1, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(strategies, format_compliance, color=colors, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Score (out of 10)', fontsize=12)
ax.set_title('Format Compliance Score', fontsize=14, fontweight='bold')
ax.set_ylim(0, 10.5)
ax.axhline(y=9.5, color='green', linestyle='--', alpha=0.3, linewidth=2)
for i, v in enumerate(format_compliance):
    ax.text(i, v + 0.2, f'{v}/10', ha='center', va='bottom', fontweight='bold', fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('research/results/format_compliance_chart.png', dpi=300, bbox_inches='tight')
print("[OK] Saved: research/results/format_compliance_chart.png")
plt.close()

# Plot 2: Parsing Success (individual)
fig2, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(strategies, parsing_success, color=colors, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Success Rate (%)', fontsize=12)
ax.set_title('Parsing Success Rate', fontsize=14, fontweight='bold')
ax.set_ylim(0, 105)
ax.axhline(y=95, color='green', linestyle='--', alpha=0.3, linewidth=2, label='Production Target')
for i, v in enumerate(parsing_success):
    ax.text(i, v + 1.5, f'{v}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
ax.legend(loc='upper left')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('research/results/parsing_success_chart.png', dpi=300, bbox_inches='tight')
print("[OK] Saved: research/results/parsing_success_chart.png")
plt.close()

# Plot 3: Relevance (individual)
fig3, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(strategies, relevance_score, color=colors, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Score (out of 10)', fontsize=12)
ax.set_title('Relevance to Job Description', fontsize=14, fontweight='bold')
ax.set_ylim(0, 10.5)
ax.axhline(y=8.5, color='green', linestyle='--', alpha=0.3, linewidth=2)
for i, v in enumerate(relevance_score):
    ax.text(i, v + 0.2, f'{v}/10', ha='center', va='bottom', fontweight='bold', fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('research/results/relevance_score_chart.png', dpi=300, bbox_inches='tight')
print("[OK] Saved: research/results/relevance_score_chart.png")
plt.close()

# Plot 4: Generation Time (individual)
fig4, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(strategies, generation_time, color=colors, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Time (seconds)', fontsize=12)
ax.set_title('Average Generation Time', fontsize=14, fontweight='bold')
ax.set_ylim(0, 6.5)
ax.axhline(y=4.0, color='orange', linestyle='--', alpha=0.3, linewidth=2, label='Target: <4s')
for i, v in enumerate(generation_time):
    ax.text(i, v + 0.15, f'{v}s', ha='center', va='bottom', fontweight='bold', fontsize=11)
ax.legend(loc='upper left')
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('research/results/generation_time_chart.png', dpi=300, bbox_inches='tight')
print("[OK] Saved: research/results/generation_time_chart.png")
plt.close()

print("\n" + "="*60)
print("All plots generated successfully!")
print("="*60)
print("\nGenerated files:")
print("  - research/results/comparison_plots.png (combined)")
print("  - research/results/format_compliance_chart.png")
print("  - research/results/parsing_success_chart.png")
print("  - research/results/relevance_score_chart.png")
print("  - research/results/generation_time_chart.png")
print("\nUse these images in your research issue markdown file.")

