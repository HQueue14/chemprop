import os
import sys

sys.path.append("/home/gridsan/yunsie/git_repo/chemprop")

import chemprop
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Set the path to the model file and arguments
curr_dir = os.getcwd()
model_dir = os.path.join(curr_dir, '../ML_model_files')

# Ensure that paths are correctly set
test_path = os.path.join(curr_dir, 'sample_input_file.csv')
preds_path = os.path.join(curr_dir, 'pred_results.csv')

# Check if files and directories exist
if not os.path.exists(test_path):
    raise FileNotFoundError(f"Test file not found: {test_path}")
if not os.path.exists(model_dir):
    raise FileNotFoundError(f"Model directory not found: {model_dir}")

# Define arguments for chemprop
arguments = [
    '--test_path', test_path,  # Path to test input file
    '--preds_path', preds_path,  # Path to save predictions
    '--checkpoint_dir', model_dir,  # Path to the pre-trained model files
    '--number_of_molecules', '2',  # Number of molecules per input (if applicable)
    '--num_workers', '0',
]

# Make predictions
if __name__ == '__main__':
    try:
        # Parse arguments
        args = chemprop.args.PredictArgs().parse_args(arguments)

        # Generate predictions
        preds = chemprop.train.make_predictions(args=args)

        # Check if predictions are saved successfully
        if os.path.exists(preds_path):
            print(f"Predictions saved successfully to: {preds_path}")
        else:
            print("Error: Predictions file was not created.")
    except Exception as e:
        print(f"An error occurred: {e}")