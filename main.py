import pygame
import random
from car import Car
from road import Road
from sensor import Sensor
from network import Network, LEFT, SLIGHT_LEFT, STRAIGHT, SLIGHT_RIGHT, RIGHT
from checkpoints import Checkpoints

pygame.init()

WIDTH,HEIGHT = 1080, 720 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lets Race")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

road = Road()
checkpoint = Checkpoints()


POPULATION_SIZE = 100
MAX_FRAMES = 1800

def create_population(parent_networks=None):
    cars = []

    for i in range(POPULATION_SIZE):
        if parent_networks is None:
            network = Network()

        elif i < 2:
            network = parent_networks[i]

        else:
            parent_a = random.choice(parent_networks)
            parent_b = random.choice(parent_networks)
            network = parent_a.breed(parent_b)

        car = Car()
        sensor = Sensor(car)

        cars.append({
            "car": car,
            "sensor": sensor,
            "network": network,
            "crashed": False,
            "distance_travelled": 0,
            "fitness": 0,
            "frames_survived": 0
        })

    return cars


cars = create_population()
generation = 1
running = True




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for driver in cars:
        car = driver["car"]
        sensor = driver["sensor"]
        network = driver["network"]

        if driver["crashed"]:
            continue

        sensor.update(road)

        outputs = network.feed_forward(sensor.readings)
        action = network.choose_game_input(outputs)

        if action == STRAIGHT:
            car.accelerate()

        elif action == SLIGHT_LEFT:
            car.accelerate()
            car.steer(-0.8)

        elif action == SLIGHT_RIGHT:
            car.accelerate()
            car.steer(0.8)

        elif action == LEFT:
            car.steer(-0.8)

        elif action == RIGHT:
            car.steer(0.8)

        previous_x = car.x
        previous_y = car.y

        car.update_position()

        distance_moved = (
            (car.x - previous_x) ** 2 +
            (car.y - previous_y) ** 2
        )** 0.5

        driver["distance_travelled"] = (
            driver.get("distance_travelled", 0) + distance_moved
        )

        driver["frames_survived"] += 1
        driver["fitness"] = driver["distance_travelled"]

        if not road.is_on_road(car.x, car.y):
            driver["crashed"] = True
            car.stop()

            print(
                f"Car finished | "
                f"Frames: {driver['frames_survived']} | "
                f"Distance: {driver['distance_travelled']:.1f} |"
                f"Fitness: {driver['fitness']:.1f}"
            )

        elif driver["frames_survived"] >= MAX_FRAMES:
            driver["crashed"] = True
            car.stop()
            print(f"Car timed out | " 
                  f"Fitness: {driver['fitness']:.1f}"
                  )

    if all(driver["crashed"] for driver in cars):
        ranked_cars = sorted(
            cars,
            key=lambda driver: driver['fitness'],
            reverse= True
        )

        print("Generation {generation} finished!")

        for rank, driver in enumerate(ranked_cars[:10], start=1):
            print(
            f"Rank {rank} | "
            f"Fitness: {driver['fitness']:.1f} | "
            f"Distance: {driver['distance_travelled']:.1f}" 
            )

        breeding_pool = [
            driver["network"]
            for driver in ranked_cars[:10]
        ]

        cars = create_population(breeding_pool)
        generation += 1

        print(f"Started Generation {generation}!")

    road.draw(screen)
    checkpoint.draw(screen)

    for driver in cars:
        driver["car"].draw(screen)
        if not driver["crashed"]:
            driver["sensor"].draw(screen)

    pygame.display.flip()
    active_cars = sum(
        not driver["crashed"] for driver in cars
    )

    status = font.render(
        f"Generation: {generation} | Active cars: {active_cars}",
        True,
        (255, 255, 255)
    )

    screen.blit(status, (20, 20))
    clock.tick(60)

pygame.quit()
