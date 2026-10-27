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

        self.bias1 = [
            random.uniform(-1, 1)
            for _ in range(self.hidden1_size)
        ]
        self.bias2 = [
            random.uniform(-1, 1)
            for _ in range(self.hidden2_size)
        ]
        self.bias3 = [
            random.uniform(-1, 1)
            for _ in range(self.output_size)
        ]

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

            total += self.bias1[len(hidden1)]
            total = self.activation_ReLU(total)
            
            hidden1.append(total)

        hidden2 = []
        for neuron_wieghts in self.weight2:
            total = 0

            for i in range(self.hidden1_size):
                total += hidden1[i] * neuron_wieghts[i]

            total += self.bias2[len(hidden2)]
            total = self.activation_ReLU(total)
            hidden2.append(total)

        output = []
        for neuron_wieghts in self.weight3:
            total = 0 

            for i in range(self.hidden2_size):
                total += hidden2[i] * neuron_wieghts[i]

            total += self.bias3[len(output)]
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


    def breed(self, other, mutation_rate=0.05, mutation_strength=0.2):
        child = Network()

        for child_layer, parent_a_layer, parent_b_layer in [
            (child.weight1, self.weight1, other.weight1),
            (child.weight2, self.weight2, other.weight2),
            (child.weight3, self.weight3, other.weight3),
        ]:
            for i in range(len(child_layer)):
                for j in range(len(child_layer[i])):
                    if random.random() < 0.5:
                        weight = parent_a_layer[i][j]
                    else:
                        weight = parent_b_layer[i][j]

                    if random.random() < mutation_rate:
                        weight += random.uniform(
                            -mutation_strength,
                            mutation_strength
                        )
                    child_layer[i][j] = weight

        for child_biases, parent_a_biases, parent_b_biases in [
            (child.bias1, self.bias1, other.bias1),
            (child.bias2, self.bias2, other.bias2),
            (child.bias3, self.bias3, other.bias3),
        ]:
            for i in range ( len(child_biases)):
                if random.random() < 0.5:
                    value = parent_a_biases[i]
                else:
                    value = parent_b_biases[i]

                if random.random() < mutation_rate:
                    value += random.uniform(
                        -mutation_strength,
                        mutation_strength
                    )

                child_biases[i] = value
                
        return child
