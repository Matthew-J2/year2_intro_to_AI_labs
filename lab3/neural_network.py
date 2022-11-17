class NeuralNetwork:
    def __init__(self, test):
        if test:
            pass
        else:
            parameter_tuple = parameters()
            self.training_data = input()
            self.number_inputs = parameter_tuple[0]
            self.hidden_units = parameter_tuple[1]
            self.output_units = parameter_tuple[2]
            self.epochs_num = parameter_tuple[3]
            self.activation_function = parameter_tuple[4]
            self.learning_rate = parameter_tuple[5]

    def parameters(self):
        number_inputs = int(input("How many inputs for the neural network?\n"))
        number_layers = int(input("How many layers would you like the neural network to have?\n"))
        hidden_units = dict()
        for i in range(number_layers):
            layer_nodes = int(input(f"How many nodes for hidden layer {i}?\n"))
            hidden_units[i].append(layer_nodes)
        output_units = int(input("How many outputs for the neural network?\n"))
        epochs_num = int(input("How many epochs?\n"))
        activation_function = input("Which activation function would you like to use? Choose either sigmoid, step, "
                                    "sign, or hyperbolic_tan.\n")
        learning_rate = int(input("What would you like the neural network's learning rate to be?"))

        return number_inputs, hidden_units, output_units, epochs_num, activation_function, learning_rate

    def input(self):

        return 0

    def structure(self):
        pass

    def initialise(self):
        pass

    def introduced(self):
        pass

    def output(self):
        pass

    def weight_update(self):
        pass

    def print(self):
        pass


def main():
    neural_network = NeuralNetwork(0)


if __name__ == "__main__":
    main()
