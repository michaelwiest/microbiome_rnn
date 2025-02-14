batch_size = 50
# Size of the hidden layers of the network.
hidden_dim = 128
# How many samples to check before one epoch. Kind of arbitrary.
samples_per_epoch = 500000
num_epochs = 50
learning_rate = 0.0000005
# Length of the sequence being passed to the LSTM or FFN.
seq_len = 15
# For the compression step with the LSTM how many strains to reduce it to.
reduced_num_strains = 50
# If this value is below one then it increases by that percent
# every epoch. If greater than one then it increases by that fixed
# amount after every epoch. Only used for RNN.
slice_incr_frequency = None


# Use the conv-LSTM?
use_convs = True


additional_comments = ''
run_suffix = '_LSTM_h{}_sl{}_rns{}_sif{}_conv{}{}'.format(hidden_dim,
                                              seq_len,
                                              reduced_num_strains,
                                              slice_incr_frequency,
                                              str(use_convs),
                                              additional_comments)
model_name = 'model{}.pt'.format(run_suffix)
log_name = 'log{}.csv'.format(run_suffix)
output_dir = 'rnn_output'
