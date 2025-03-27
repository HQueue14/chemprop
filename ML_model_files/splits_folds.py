import pandas as pd

for fold in range(5):
    file_path = f'ML_model_files/RxnSolvKSE_dataset_v1.1/pretraining_set\
                /chosen_500k_data/train_test_split/fold_{fold}\
                /rxn_solvent_500k_random_testing_{fold}.csv'
    df = pd.read_csv(file_path)

    solvent_split_df = df[df['test_type'].isin(['solvent split'])]

    rxn_split_df = df[df['test_type'].isin(['rxn split'])]

    solvent_split_df.to_csv(f'ML_model_files/solvent_split_fold_{fold}.csv',
                            index=False)
    rxn_split_df.to_csv(f'ML_model_files/rxn_split_fold_{fold}.csv',
                        index=False)
