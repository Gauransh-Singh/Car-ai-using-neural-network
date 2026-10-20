import random

LEFT = 0
SLIGHT_LEFT = 1
STRAIGHT = 2
SLIGHT_RIGHT = 3
RIGHT = 4

class Network:

    def __init__(self):
        self.input_size = 7
        self.hidden1_size = 16
        self.hidden2_size = 16
        self.output_size = 5

        self.weight1 = []
        self.weight2 = []
        self.weight3 = []

        self.bias1 = []
        self.bias2 = []
        self.bias3 = []

        self.weight1 = [
            [random.uniform(-1,1) for _ in range(self.input_size)]
            for _ in range(self.hidden1_size)
        ]

        self.weight2 = [
            [random.uniform(-1,1) for _ in range(self.hidden1_size)]
            for _ in range(self.hidden2_size)
        ]

        self.weight3 = [
            [random.uniform(-1,1) for _ in range(self.hidden2_size)]
            for _ in range(self.output_size)
        ]


    def feed_forward(self, inputs):

        hidden1 = []
        for neuron_wieghts in self.weight1:
            total = 0

            for i in range(self.input_size):
                total += inputs[i] * neuron_wieghts[i]

            total = self.activation_ReLU(total)
            hidden1.append(total)

        hidden2 = []
        for neuron_wieghts in self.weight2:
            total = 0

            for i in range(self.hidden1_size):
                total += hidden1[i] * neuron_wieghts[i]

            total = self.activation_ReLU(total)
            hidden2.append(total)

        output = []
        for neuron_wieghts in self.weight3:
            total = 0 

            for i in range(self.hidden2_size):
                total += hidden2[i] * neuron_wieghts[i]

            total = self.activation_ReLU(total)
            output.append(total)
            
        return output



    def activation_ReLU(self, x):
        return max(0,x)

    def choose_game_input(self, outputs):
        action = outputs.index(max(outputs))

        if action == LEFT:
            return LEFT
        elif action == SLIGHT_LEFT:
            return SLIGHT_LEFT
        elif action == STRAIGHT:
            return STRAIGHT
        elif action == SLIGHT_RIGHT:
            return SLIGHT_RIGHT
        else:
            return RIGHT

    def crossbreed():
        pass
     
if __name__ == "__main__":
    network = Network()

    test_inputs = [0.21, 0.25, 0.36, 0.67, 1.0, 1.0, 0.87]

    outputs = network.feed_forward(test_inputs)
    action = network.choose_game_input(outputs)

    print("Outputs:", outputs)
    print("Chosen action:", action)

