import os
import sys
sys.path.append("/home/gridsan/yunsie/git_repo/chemprop")

import chemprop
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error



# Set the path to the model file and arguments

curr_dir = os.getcwd()
model_dir = os.path.join(curr_dir, 'ML_model_files/')

arguments = [
    '--test_path', 'sample_input_file.csv',
    '--preds_path', 'pred_results.csv',
    '--checkpoint_dir', model_dir,
    '--number_of_molecules', '2',
]

# make predictions
args = chemprop.args.PredictArgs().parse_args(arguments)
preds = chemprop.train.make_predictions(args=args)