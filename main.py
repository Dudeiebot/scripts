import pandas as pd

"""
filtering and removing duplicates in csv or excel file
"""
# Load the Excel file
file_path = "~/"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Ensure column H exists
column_h = df.columns[5]  # Column H is the 8th column (zero-based index)

print("First two values in column H before processing:")
print(df.iloc[:2, 4])
# Normalize the column H data (strip spaces, convert to lowercase for better duplicate detection)
df[column_h] = df[column_h].astype(str).str.strip().str.lower()

# Drop duplicates based on column H
df_unique = df.drop_duplicates(
    subset=[column_h], keep="first"
)  # Keeps the first occurrence

# Save the cleaned file
output_path = ".csv"
df_unique.to_csv(output_path, index=False)

print(f"Filtered file saved as {output_path}")
