import json
import random
import math


class Node:
    """A class representing an individual node, and its weights to each node in the next layer."""
    def __init__(self, weights=None):
        if weights is None:
            weights = []
        self.weights = weights


class Layer:
    """
    A class representing a layer of the neural network, containing a list of inputs, a list of Node objects, and a
    float used to store the final output of the network for the last layer.
    """
    def __init__(self, node_amount):
        self.inputs = []
        self.output = 0
        self.nodes = [Node() for i in range(node_amount)]


class NeuralNetwork:
    """
    A class representing the entire neural network.
    Methods:
        parameters: Asks the user how they would like the neural network to be structured and returns a tuple of
        information based on their answers.
        input: Asks the user what data they would like to train the neural network on, and gives them the option to
        use a JSON file.
        structure: Generates the neural network structure.
        initialise: Produces random weight values between 0 and 1 for each node's weights.
        introduced: Introduces the data set one value at a time for the request set of values and number of epochs.
        Also calls functions to calculate outputs and update weights.
        output: Creates a weighted sum for each layer, and puts the weighted sum through an activation function.
        activation_function_calculation: Calculates the output of an activation function given an input, and returns
        the result.
        weight_update: Updates weights using back-propagation
        print: Prints the weights of the neural network at the end of calculations, as well as the final output of
        the neural network.
    Attributes:
        number_inputs: The amount of nodes on the input layer.
        hidden_units: A dictionary used to construct hidden layers, containing the layer number as a value and the
        amount of nodes in that layer as the key.
        epochs_num: The amount of epochs the neural network will use to update its weights.
        activation_function: The activation function the neural network will use.
        learning_rate: The neural network's learning rate.
        threshold: The neural network's threshold when using the step activation function.
        training_data: A data structure consisting of a list of lists, where each list of lists contains both a
        dictionary with the index of the input as a key and the input as a value, and the target output for the set
        of inputs.
        layers: A list of layers in the neural network.
    """
    def __init__(self):
        """Constructor used to create a NeuralNetwork object"""
        parameter_tuple = self.parameters()
        self.number_inputs = parameter_tuple[0]
        self.hidden_units = parameter_tuple[1]
        self.epochs_num = parameter_tuple[2]
        self.activation_function = parameter_tuple[3]
        self.learning_rate = parameter_tuple[4]
        self.threshold = parameter_tuple[5]
        self.training_data = self.input()
        self.layers = list()
        self.structure()
        self.initialise()

    def parameters(self):
        """
        Asks the user how they would like the neural network to be structured and returns a tuple of information based
        on their answers.
        """

        threshold = 0
        number_inputs = int(input("How many inputs for the neural network?\n"))
        number_layers = int(input("How many hidden layers would you like the neural network to have?\n"))
        hidden_units = dict()
        for i in range(number_layers):
            layer_nodes = int(input(f"How many nodes for hidden layer {i+1}?\n"))
            hidden_units.update({i: layer_nodes})

        epochs_num = int(input("How many epochs?\n"))
        activation_function = input("Which activation function would you like to use? Choose either sigmoid, step, "
                                    "sign, or hyperbolic_tan.\n")
        if activation_function == "step":
            threshold = float(input("Choose a threshold.\n"))
        learning_rate = float(input("What would you like the neural network's learning rate to be?\n"))

        return number_inputs, hidden_units, epochs_num, activation_function, learning_rate, threshold

    def input(self):
        """
        Asks the user what data they would like to train the neural network on, and gives them the option to use a JSON
        file. The user can input sets of nodes, and input the values for each node for each set.
        """
        file_read = input("Would you like to import the training data from a JSON file? Answer with either Y or N.\n")
        input_target_sets = list()

        if file_read.upper() == "Y":
            with open("inputs.json", "r") as input_file:
                inputs = json.load(input_file)
                input_file.close()
                input_target_sets = inputs["inputs"]

                for f in input_target_sets:
                    f[0] = {int(key): int(value) for key, value in f[0].items()}

        elif file_read.upper() == "N":
            num_sets = int(input("How many sets of inputs would you like?\n"))

            for i in range(num_sets):
                target_output = float(input(f"What would you like the target output for set {i+1} to be?\n"))
                inputs_dict = dict()

                for j in range(self.number_inputs):
                    node_input = float(input(f"What would you like input {j+1} to be?\n"))
                    inputs_dict.update({j: node_input})

                input_target_sets.append([inputs_dict, target_output])
        return input_target_sets

    def structure(self):
        """Generates the structure of t he neural network."""
        self.layers.append(Layer(self.number_inputs))
        for idx, _ in enumerate(self.hidden_units):
            self.layers.append(Layer(self.hidden_units[idx]))

    def initialise(self):
        """Adds random value from 0-1 to each weight of each node."""
        for idx, value in enumerate(self.layers):
            if idx + 1 == len(self.layers):
                for i in value.nodes:
                    i.weights.append(random.random())
            else:
                for i in value.nodes:
                    for j in self.layers[idx+1].nodes:
                        i.weights.append(random.random())

    def introduced(self):
        """
        Introduces sets of inputs in a random order, and each input within the set in a random order. For each epoch and
        set of inputs, calls methods to calculate the outputs for each layer of the neural network, then calls methods
        to update the weights of each node via back-propagation.
        """

        for i in range(self.epochs_num):
            random.shuffle(self.training_data)
            for idx, _ in enumerate(self.training_data):
                sample_order = [x for x in range(self.number_inputs)]
                random.shuffle(sample_order)

                for j in sample_order:
                    self.layers[0].inputs.append(self.training_data[idx][0][j])

                for idx2, value in enumerate(self.layers):
                    if idx2 < len(self.layers) - 1:
                        self.output(value, self.layers[idx2+1])
                    else:
                        predicted_output = self.output(value)

                for idx3, value in enumerate(self.layers):
                    if idx3 < len(self.layers) - 1:
                        self.weight_update(value, self.training_data[idx][1], predicted_output, self.layers[idx3+1])
                    else:
                        self.weight_update(value, self.training_data[idx][1], predicted_output)

                for k in self.layers:
                    k.inputs = []

        self.layers[-1].output = predicted_output

    def output(self, current_layer, next_layer=None):
        """Calculates outputs for a layer in the neural network."""
        if next_layer is None:
            weighted_sum = 0
            for idx, node in enumerate(current_layer.nodes):
                weighted_sum += (node.weights[0] * current_layer.inputs[idx])
            return self.activation_function_calculation(weighted_sum)

        for idx, _ in enumerate(current_layer.nodes[0].weights):
            weighted_sum = 0
            for idx2, node, in enumerate(current_layer.nodes):
                weighted_sum += (node.weights[idx] * current_layer.inputs[idx2])
            next_layer.inputs.append(self.activation_function_calculation(weighted_sum))

    def activation_function_calculation(self, weighted_sum):
        """Calculates an output for a node using a given activation function based on a weighted sum."""
        if self.activation_function == "sigmoid":
            return 1/(1 + math.exp(-weighted_sum))
        elif self.activation_function == "step":
            if weighted_sum >= self.threshold:
                return 1
            else:
                return 0
        elif self.activation_function == "sign":
            if weighted_sum >= 0:
                return 1
            else:
                return -1
        elif self.activation_function == "hyperbolic_tan":
            return(math.exp(weighted_sum) - math.exp(-weighted_sum)) / (math.exp(weighted_sum) + math.exp(-weighted_sum))

    def weight_update(self, current_layer, target_output, predicted_output, next_layer=None):
        """Updates a layer's weights in the neural network using back-propagation."""
        if next_layer is None:
            for i in current_layer.nodes:
                i.weights[0] = i.weights[0] + self.learning_rate * (target_output - predicted_output) * predicted_output
            return

        for i in current_layer.nodes:
            for idx, value in enumerate(i.weights):
                i.weights[idx] = value + self.learning_rate * (target_output - predicted_output) * next_layer.inputs[idx]

    def print(self):
        """
        Prints the weights of the neural network at the end of calculations, as well as the final output of
        the neural network.
        """
        print("These are the weights for each node of each layer of the neural network for each node:\n"
              "==================================================\n")
        for idx, value in enumerate(self.layers):
            if idx == 0:
                print("Input Layer:")
            else:
                print(f"Layer {idx}:")
            for idx2, value2 in enumerate(value.nodes):
                print(f"Node {idx2+1}:")
                for idx3, value3 in enumerate(value2.weights):
                    print(f"Weight to node {idx3+1} in next layer: {value3}")
        print(f"==================================================\nThe overall output value is "
              f"{self.layers[-1].output}.")


def main():
    neural_network = NeuralNetwork()
    neural_network.introduced()
    neural_network.print()


if __name__ == "__main__":
    main()
