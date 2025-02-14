batch_size = 50
# Size of the hidden layers of the network.
hidden_dim = 512
# How many samples to check before one epoch. Kind of arbitrary.
samples_per_epoch = 500000
num_epochs = 50
learning_rate = 0.0000005
# Length of the sequence being passed to the LSTM or FFN.
seq_len = 5
# For the compression step with the LSTM how many strains to reduce it to.
reduced_num_strains = 36

# How to normalize the data.
norm_method = ['clr', 'zscore']

# Use conv
use_convs = False


additional_comments = ''
run_suffix = '_ffn_h{}_sl{}_rns{}_conv{}{}'.format(hidden_dim,
                                              seq_len,
                                              reduced_num_strains,
                                              use_convs,
                                              additional_comments)
model_name = 'model{}.pt'.format(run_suffix)
log_name = 'log{}.csv'.format(run_suffix)
output_dir = 'ffn_output'
