import pandas as pd

# List of CSV files to concatenate
csv_files = [
    'ML_model_files/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/train_test_split/fold_0/rxn_solvent_500k_random_testing_0.csv',
    'ML_model_files/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/train_test_split/fold_1/rxn_solvent_500k_random_testing_1.csv',
    'ML_model_files/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/train_test_split/fold_2/rxn_solvent_500k_random_testing_2.csv',
    'ML_model_files/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/train_test_split/fold_3/rxn_solvent_500k_random_testing_3.csv',
    'ML_model_files/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/train_test_split/fold_4/rxn_solvent_500k_random_testing_4.csv'
]

# Load and concatenate all CSV files
df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_rxn_solvent_500k_random_testing.csv', index=False)

# Load the CSV file into a DataFrame
df = pd.read_csv('combined_rxn_solvent_500k_random_testing.csv')

# Count the occurrences of each test_type
test_type_counts = df['test_type'].value_counts()

# Print the counts
print("Solvent split:", test_type_counts.get('solvent split', 0))
print("Rxn split:", test_type_counts.get('rxn split', 0))
print("Both:", test_type_counts.get('both', 0))