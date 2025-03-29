import pandas as pd

# Read the original CSV with the correct separator
df = pd.read_csv('metadata.csv', sep='|', header=None)

# Create a new dataframe with 3 columns where second column is replicated
new_df = pd.DataFrame({
    'col1': df[0],  # First part (ID)
    'col2': df[1],  # Second part (text)
    'col3': df[1]   # Replicated text
})

# Save to new CSV with | separator
new_df.to_csv('metadata_three_columns.csv', sep='|', index=False, header=False)