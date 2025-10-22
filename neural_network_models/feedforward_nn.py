import torch.nn as nn

class FeedforwardNN(nn.Module):
    def __init__(self, input_neuron_num, h1_neuron_num, output_neuron_num):
        super(FeedforwardNN, self).__init__()
        # 1st fully connected (hidden) layer
        self.h1_linear_func = nn.Linear(input_neuron_num, h1_neuron_num)
        self.h1_activation_func = nn.Sigmoid()

        # output layer
        # note: since our goal is to predic a real number,
        #       we do not use any activation function in output layer
        self.output_linear_func = nn.Linear(h1_neuron_num, output_neuron_num)

    def forward(self, x):
        # 1st hidden layer
        x = self.h1_linear_func(x)
        x = self.h1_activation_func(x)

        # output layer
        x = self.output_linear_func(x)
        return x
