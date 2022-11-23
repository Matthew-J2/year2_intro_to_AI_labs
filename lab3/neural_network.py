import json
import random

class Node:
    def __init__(self, weights=None):
        if weights is None:
            weights = []
        self.weights = weights


class Layer:
    def __init__(self, node_amount):
        self.inputs = []
        self.outputs = []
        self.nodes = [Node() for i in range(node_amount)]


class NeuralNetwork:
    def __init__(self, test):
        if test:
            pass
        else:
            parameter_tuple = self.parameters()
            self.number_inputs = parameter_tuple[0]
            self.hidden_units = parameter_tuple[1]
            self.epochs_num = parameter_tuple[2]
            self.activation_function = parameter_tuple[3]
            self.learning_rate = parameter_tuple[4]
            self.training_data = self.input()
            self.layers = list()
            for i in parameter_tuple:
                print(i)
            self.structure()
            print(self.layers)
            for i in self.layers:
                print(i.nodes)
                for j in i.nodes:
                    print(j.weights)
            self.initialise()
            for i in self.layers:
                print(i.nodes)
                for j in i.nodes:
                    print(j.weights)



    def parameters(self):
        number_inputs = int(input("How many inputs for the neural network?\n"))
        number_layers = int(input("How many layers would you like the neural network to have?\n"))
        hidden_units = dict()
        for i in range(number_layers):
            layer_nodes = int(input(f"How many nodes for hidden layer {i+1}?\n"))
            hidden_units.update({i: layer_nodes})

        epochs_num = int(input("How many epochs?\n"))
        activation_function = input("Which activation function would you like to use? Choose either sigmoid, step, "
                                    "sign, or hyperbolic_tan.\n")
        learning_rate = float(input("What would you like the neural network's learning rate to be?\n"))

        return number_inputs, hidden_units, epochs_num, activation_function, learning_rate

    def input(self):
        file_read = input("Would you like to import the training data from a JSON file? Answer with either Y or N.\n")
        input_target_sets = list()

        if file_read.upper() == "Y":
            with open("inputs.json", "r") as input_file:
                inputs = json.load(input_file)
                input_target_sets = inputs["inputs"]

        elif file_read.upper() == "N":
            num_sets = int(input("How many sets of inputs would you like?\n"))

            for i in range(num_sets):
                target_output = float(input(f"What would you like the target output for set {i+1} to be?\n"))
                inputs_dict = dict()

                for j in range(self.number_inputs):
                    node_input = float(input(f"What would you like input {j+1} to be?\n"))
                    inputs_dict.update({j: node_input})

                input_target_sets.append([inputs_dict, target_output])
        print(input_target_sets)
        return input_target_sets

    def structure(self):
        self.layers.append(Layer(self.number_inputs))
        for idx, _ in enumerate(self.hidden_units):
            self.layers.append(Layer(self.hidden_units[idx]))

    def initialise(self):
        for idx, value in enumerate(self.layers):
            if idx + 1 == len(self.layers):
                for i in value.nodes:
                    i.weights.append(random.random())
            else:
                for i in value.nodes:
                    for j in self.layers[idx+1].nodes:
                        i.weights.append(random.random())

    def introduced(self):
        for i in range(self.epochs_num):
            sample_order = [x for x in range(self.number_inputs)]
            random.shuffle(sample_order)

            for j in sample_order:
                self.layers[0].inputs.append(self.training_data[i][0][j])

            for idx, value in enumerate(self.layers):
                if idx < len(self.layers):
                    self.output(value, self.layers[idx+1])



    def output(self, current_layer, next_layer=None):
        if next_layer is None:
            next_layer = []
        # weighted_sums = []
        # for i in range(len(current_layer.nodes)):
        #     current_layer.nodes.weights[0] =
        #
        # for idx, value in enumerate(current_layer.nodes):
        #     x = value[idx] * current_layer.inputs
        #     for j in i.weights:
        #         weighted_sums.append(i.weights*)

    def activation_function_calculation(self):
        if self.activation_function == "sigmoid":
            pass
        elif self.activation_function == "step":
            pass
        elif self.activation_function == "sign":
            pass
        elif self.activation_function == "hyperbolic_tan":
            pass

    def weight_update(self):
        pass

    def print(self):
        pass


def main():
    neural_network = NeuralNetwork(0)
    neural_network.introduced()

if __name__ == "__main__":
    main()
