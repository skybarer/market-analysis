import pandas as pd

# Assuming we have historical data for SBI shares, let's create a sample dataset for demonstration.
# Ideally, this data should be fetched from a reliable financial data source.

data = {
    'Year': list(range(2009, 2024)),
    'Start_Price': [150, 180, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800],
    'End_Price':   [180, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate YoY percentage change
df['YoY_Change'] = ((df['End_Price'] - df['Start_Price']) / df['Start_Price']) * 100

print(df)
