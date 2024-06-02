import pandas as pd
import matplotlib.pyplot as plt

# Example historical revenue data for Amazon (in billions USD)
years = list(range(2009, 2024))
revenue = [24.51, 34.20, 48.08, 61.09, 74.45, 88.99, 107.00, 135.99, 177.87, 232.88, 280.52, 386.06, 469.82, 514.00, 560.00]

# Create a DataFrame
df = pd.DataFrame({'Year': years, 'Revenue': revenue})

# Plot revenue over time
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Revenue'], marker='o')
plt.title('Amazon Year-over-Year Revenue Growth')
plt.xlabel('Year')
plt.ylabel('Revenue (in billions USD)')
plt.grid(True)
plt.show()

# Check for year-over-year revenue growth
df['YoY Growth'] = df['Revenue'].pct_change() * 100
print(df)
