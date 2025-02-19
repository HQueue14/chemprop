import pandas as pd

# Loop through folds 0 to 4
for fold in range(5):
    # Load the CSV file into a DataFrame
    file_path = f'ML_model_files/RxnSolvKSE_dataset_v1.1/pretraining_set/chosen_500k_data/train_test_split/fold_{fold}/rxn_solvent_500k_random_testing_{fold}.csv'
    df = pd.read_csv(file_path)

    # Filter the DataFrame for 'solvent split' and 'both'
    solvent_split_df = df[df['test_type'].isin(['solvent split'])]

    # Filter the DataFrame for 'rxn split' and 'both'
    rxn_split_df = df[df['test_type'].isin(['rxn split'])]

    # Save the filtered DataFrames to new CSV files in the ML_model_files folder
    solvent_split_df.to_csv(f'ML_model_files/solvent_split_fold_{fold}.csv', index=False)
    rxn_split_df.to_csv(f'ML_model_files/rxn_split_fold_{fold}.csv', index=False)