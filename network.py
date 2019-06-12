import numpy
import services


class NeuralNetwork:

    def __init__(self):
        # weights between input and hidden layer
        self.weights_input_hidden = None
        # weights between hidden layer and output
        self.weights_hidden_output = None
        # threshold between input and hidden layer
        self.threshold_input_hidden = None
        # threshold between hidden and output layer
        self.threshold_hidden_output = None
        # hidden layer
        self.hidden = None
        # beta used in forward propagation
        self.beta_forward_propagation = None
        # beta used in backward propagation
        self.beta_backward_propagation = None

    def forward_propagation(self, input):
        temp1 = numpy.dot(input, self.weights_input_hidden)
        temp1 = temp1 - self.threshold_input_hidden
        self.hidden = services.sigmoid(temp1, self.beta_forward_propagation)
        temp2 = numpy.dot(self.hidden, self.weights_hidden_output)
        temp2 = temp2 - self.threshold_hidden_output
        calculated_output = services.sigmoid(temp2, self.beta_forward_propagation)
        return calculated_output

    def backward_propagation(self, input, calculated_output, output):
        delta_weights_hidden_output = numpy.dot(self.hidden.T, (-(output - calculated_output) * services.sigmoid_derivative(calculated_output, self.beta_backward_propagation)))
        delta_weights_input_hidden = numpy.dot(input.T,  (numpy.dot( -(output - calculated_output) * services.sigmoid_derivative(calculated_output, self.beta_backward_propagation),
                                                  self.weights_hidden_output.T) * services.sigmoid_derivative(self.hidden, self.beta_backward_propagation)))
        delta_threshold_hidden_output = (-(output - calculated_output) * services.sigmoid_derivative(calculated_output, self.beta_backward_propagation))
        delta_threshold_input_hidden = -(output - calculated_output) * services.sigmoid_derivative(calculated_output, self.beta_backward_propagation)*delta_threshold_hidden_output
        # update the weights with the derivative (slope) of the loss function
        self.weights_hidden_output -= delta_weights_hidden_output
        self.weights_input_hidden -=  delta_weights_input_hidden
        self.threshold_hidden_output -= delta_threshold_hidden_output
        self.threshold_input_hidden -= delta_threshold_input_hidden






