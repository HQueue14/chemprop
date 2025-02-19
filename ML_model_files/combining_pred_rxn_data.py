import pandas as pd

# List of CSV files to concatenate
pred_csv_files = [
    'ML_model_files/pred_results_rxn_split_fold_0_v2.csv',
    'ML_model_files/pred_results_rxn_split_fold_1_v2.csv',
    'ML_model_files/pred_results_rxn_split_fold_2_v2.csv',
    'ML_model_files/pred_results_rxn_split_fold_3_v2.csv',
    'ML_model_files/pred_results_rxn_split_fold_4_v2.csv',
]

# Load and concatenate all CSV files
df_list = [pd.read_csv(file) for file in pred_csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# Print the first few rows of the combined DataFrame to verify
print("First few rows of the combined DataFrame:")
print(combined_df.head())

# Print the shape of the combined DataFrame to verify
print("\nShape of the combined DataFrame:", combined_df.shape)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('ML_model_files/combined_pred_rxn.csv', index=False)

print("\nCombined CSV file saved as 'combined_pred_rxn.csv'")