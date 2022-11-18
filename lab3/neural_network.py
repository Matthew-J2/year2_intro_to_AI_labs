import json

class NeuralNetwork:
    def __init__(self, test):
        if test:
            pass
        else:
            parameter_tuple = self.parameters()
            self.training_data = self.input()
            self.number_inputs = parameter_tuple[0]
            self.hidden_units = parameter_tuple[1]
            self.output_units = parameter_tuple[2]
            self.epochs_num = parameter_tuple[3]
            self.activation_function = parameter_tuple[4]
            self.learning_rate = parameter_tuple[5]
            for i in parameter_tuple:
                print(i)

    def parameters(self):
        number_inputs = int(input("How many inputs for the neural network?\n"))
        number_layers = int(input("How many layers would you like the neural network to have?\n"))
        hidden_units = dict()
        for i in range(number_layers):
            layer_nodes = int(input(f"How many nodes for hidden layer {i}?\n"))
            hidden_units.update({i: layer_nodes})
        output_units = int(input("How many outputs for the neural network?\n"))
        epochs_num = int(input("How many epochs?\n"))
        activation_function = input("Which activation function would you like to use? Choose either sigmoid, step, "
                                    "sign, or hyperbolic_tan.\n")
        learning_rate = int(input("What would you like the neural network's learning rate to be?\n"))

        return number_inputs, hidden_units, output_units, epochs_num, activation_function, learning_rate

    def input(self):
        file_read = input("Would you like to import the training data from a JSON file? Answer with either Y or N.\n")
        input_sets = list()

        if file_read == "Y":
            pass
        elif file_read == "N":
            num_sets = input("How many sets of inputs would you like?\n")

            for i in range(num_sets):
                target_output = input("What would you like the target output to be?\n")
                inputs_dict = dict()
                num_inputs = input("How many inputs would you like?\n")

                for i in range(num_inputs):
                    node_input = input(f"What would you like input {i+1} to be?\n")
                    inputs_dict.update({i: node_input})

                input_sets.append([inputs_dict, target_output])

        return inputs_dict

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
