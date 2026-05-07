import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate monthly trend data for .lnk phishing attempts (last 6 months)
months = ['Nov 2025', 'Dec 2025', 'Jan 2026', 'Feb 2026', 'Mar 2026', 'Apr 2026']
attempts = [40, 42, 38, 45, 44, 54] # ~22% increase from Mar to Apr

df_trend = pd.DataFrame({'Month': months, 'LNK_Phishing_Attempts': attempts})

# 2. Visualization
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_trend, x='Month', y='LNK_Phishing_Attempts', marker='o', color='#e74c3c', linewidth=2.5)

# Highlight the spike
plt.annotate('22% Increase', xy=('Apr 2026', 54), xytext=('Mar 2026', 56),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, fontweight='bold')

plt.title('Trend Analysis: .lnk File Phishing Attempts (Finance/Fraud)', fontsize=14)
plt.ylabel('Number of Detected Attempts')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('incident_trend_report.png')

# 3. APP (Authorised Push Payment) vs. Traditional Fraud Data
categories = ['Traditional Fraud (Card Theft)', 'APP Scams (Social Engineering)']
counts = [15, 35] # Showing that APP is the dominant volume now
df_fraud = pd.DataFrame({'Category': categories, 'Incident_Count': counts})

plt.figure(figsize=(8, 5))
colors = ['#3498db', '#f39c12']
plt.bar(df_fraud['Category'], df_fraud['Incident_Count'], color=colors)
plt.title('Fraud Incident Breakdown: April 2026', fontsize=14)
plt.ylabel('Confirmed Incidents')
plt.tight_layout()
plt.savefig('app_fraud_breakdown.png')

print("Charts generated successfully.")
