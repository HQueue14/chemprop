import pandas as pd

# Define the file paths
input_file_path = '/Users/abdiwadud/chemprop/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/pretraining_rxn_solvent_ddGsolv_ddHsolv_500k.csv'
output_file_path = '/Users/abdiwadud/chemprop/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/pretraining_rxn_solvent_ddGsolv_ddHsolv_500k_cleaned.csv'

# Read the dataset
df = pd.read_csv(input_file_path)
print("Original DataFrame:")
print(df.head())
print(f"Original DataFrame dimensions: {df.shape}")

# Remove rows with missing values
df_cleaned = df.dropna()

# Remove rows that contain lowercase letters in any column
df_cleaned = df_cleaned[~df_cleaned.applymap(lambda x: any(c.islower() for c in str(x))).any(axis=1)]

print("\nCleaned DataFrame:")
print(df_cleaned.head())
print(f"Cleaned DataFrame dimensions: {df_cleaned.shape}")

# Save the cleaned dataset to a new CSV file
df_cleaned.to_csv(output_file_path, index=False)
print(f"\nCleaned CSV file saved to {output_file_path}")