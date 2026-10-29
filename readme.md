# 🚗 Car AI from Scratch

### Autonomous Car Simulation Using Neural Networks and Evolutionary Algorithms

A 2D self-driving car simulation built with **Python and Pygame**, where virtual cars learn to navigate a road track using sensor readings, neural networks, and evolutionary optimization.

The project demonstrates how an AI controller can be developed from scratch and improved across generations without manually programming every driving decision.

---

## 📌 Project Overview

The simulation places a population of virtual cars on a predefined road track. Each car uses seven virtual sensors to measure distances to road boundaries. These readings are passed to a custom feed-forward neural network, which selects the car's driving action.

The system evaluates each network using distance travelled and checkpoints passed. Better-performing networks are selected and combined through crossover, while random mutations introduce variations. This process repeats over successive generations.

## ✨ Features

- 🚘 **Autonomous Driving:** Cars navigate the track without direct human control.
- 📡 **Seven Virtual Sensors:** Measure road-boundary distances using sensor rays.
- 🧠 **Custom Neural Network:** Implemented from scratch using Python.
- 🧬 **Evolutionary Learning:** Uses selection, crossover, mutation, and elitism.
- 🏁 **Checkpoint System:** Rewards progress along the track.
- 📊 **Fitness Evaluation:** Compares driving performance across the population.
- 🎮 **Real-Time Visualization:** Displays cars, road boundaries, sensors, and training progress.
- 🔄 **Generation-Based Training:** Repeatedly creates new populations to explore improved driving behaviours.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pygame | Simulation and graphics |
| Custom Neural Network | Sensor processing and action selection |
| Evolutionary Algorithm | Optimization of network parameters |
| Git and GitHub | Version control and project hosting |

## 🧠 Neural Network Architecture

The network processes seven normalized sensor readings and produces five driving-action scores.

```text
Input Layer       Hidden Layer 1      Hidden Layer 2      Output Layer

  7 neurons  ───►   16 neurons  ───►   16 neurons  ───►   5 neurons
 Sensors            Processing         Processing          Actions
```

**Architecture:** `7 → 16 → 16 → 5`

- **Input layer:** Receives seven sensor distances.
- **Hidden layers:** Use weighted connections, biases, and ReLU activation.
- **Output layer:** Represents five possible driving actions.

| Output Index | Action |
|---:|---|
| 0 | Left |
| 1 | Slight Left |
| 2 | Straight |
| 3 | Slight Right |
| 4 | Right |

The action with the highest output score is selected.

## 🧬 Evolutionary Learning Process

The simulation uses a population of **100 neural networks**.

1. **Initialize:** Generate randomly initialized neural networks.
2. **Simulate:** Each network controls a car on the track.
3. **Evaluate:** Measure distance travelled and checkpoints passed.
4. **Select:** Rank networks by fitness and select promising parents.
5. **Crossover:** Combine parameters from two parent networks.
6. **Mutation:** Randomly modify selected parameters.
7. **Elitism:** Preserve the two best networks unchanged.
8. **Repeat:** Create the next generation and continue training.

### Fitness Function

The current fitness function is:

\[
\text{Fitness}=\text{Distance Travelled}+(1000\times\text{Checkpoints Passed})
\]

This rewards both movement and progress through checkpoints.

## 📂 Project Structure

```text
Car-AI-From-Scratch/
│
├── main.py              # Main simulation and training loop
├── car.py               # Car movement and steering
├── road.py              # Track loading and road detection
├── sensor.py            # Virtual sensor rays and distance readings
├── network.py           # Neural network and evolutionary operations
├── checkpoints.py       # Checkpoint definitions and progress tracking
├── utils.py             # Helper functions
│
└── assets/
    ├── My Porche.png    # Car sprite
    └── track1.png       # Road track image
```

*Ensure the filenames and asset paths match your actual repository.*

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- Pygame
- The project source files and required assets

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Car-AI-From-Scratch
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Install dependencies

```bash
python -m pip install pygame-ce
```

The project imports the `pygame` module, which is provided by Pygame or pygame-ce.

### 3. Run the simulation

```bash
python main.py
```

The simulation window should display the road track and the cars controlled by their neural networks.

## 📈 Evaluation and Observations

The system can be evaluated using:

- Best fitness achieved in each generation
- Average population fitness
- Distance travelled before a crash
- Number of checkpoints passed
- Number of active cars remaining

A higher fitness score indicates better performance under the current fitness function, but it does not necessarily mean that the car completed a full lap.

## 🚧 Current Limitations

- The environment uses a simplified 2D track.
- Sensors measure road-boundary distances rather than processing camera images.
- Fitness depends on distance and checkpoint bonuses.
- Checkpoint detection may need improvement to confirm actual line crossings.
- Performance may vary across generations due to random initialization and mutation.
- Successful simulation does not establish that the system is suitable for real-world autonomous driving.

## 🔮 Future Improvements

- Save and load neural network checkpoints to resume training.
- Support multiple tracks and different starting positions.
- Improve checkpoint-crossing detection.
- Refine the fitness function to reward complete laps and efficient driving.
- Visualize neural network outputs and training statistics.
- Introduce more realistic vehicle physics and obstacle avoidance.
- Compare evolutionary strategies and alternative neural network architectures.

## 🎯 Learning Outcomes

This project provides practical experience with:

- Object-oriented programming in Python
- Real-time simulation using Pygame
- Sensor-based decision-making
- Neural network architecture and forward propagation
- Evolutionary optimization
- Fitness functions, selection, crossover, and mutation
- Debugging and modular software development

## 👨‍💻 Author

**Gauransh Singh**

GitHub: [Your GitHub Profile](https://github.com/Gauransh-Singh)

---

*Developed as an educational project to explore Artificial Intelligence, neural networks, and evolutionary learning through autonomous car simulation.*