import random
import math

# Define the cities and their coordinates
cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (4, 2),
    'D': (5, 5),
    'E': (7, 1),
    'F': (8, 4),
}

# Genetic Algorithm parameters
population_size = 100
generations = 1000
mutation_rate = 0.01

# Function to calculate the distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to calculate the total distance of a route
def calculate_route_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    total_distance += calculate_distance(cities[route[-1]], cities[route[0]])
    return total_distance

# Function to create an initial population of routes
def create_initial_population(cities, population_size):
    initial_population = []
    city_names = list(cities.keys())
    for _ in range(population_size):
        route = random.sample(city_names, len(city_names))
        initial_population.append(route)
    return initial_population

# Function to perform crossover (order crossover) between two routes
def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start, len(parent1))
    child = [None] * len(parent1)
    for i in range(start, end):
        child[i] = parent1[i]
    for city in parent2:
        if city not in child:
            for i in range(len(child)):
                if child[i] is None:
                    child[i] = city
                    break
    return child

# Function to perform mutation (swap mutation) on a route
def mutate(route):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Genetic Algorithm
population = create_initial_population(cities, population_size)

for generation in range(generations):
    # Calculate fitness for each route
    fitness_scores = [1 / calculate_route_distance(route) for route in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]

    # Select parents based on roulette wheel selection
    parents = random.choices(population, probabilities, k=population_size)

    # Perform crossover and mutation to create offspring
    offspring = []
    for i in range(0, population_size, 2):
        parent1, parent2 = parents[i], parents[i + 1]
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        offspring.extend([mutate(child1), mutate(child2)])

    # Replace the old population with the offspring
    population = offspring

# Find the best route in the final population
best_route = min(population, key=calculate_route_distance)
best_distance = calculate_route_distance(best_route)

print("Best Route:", best_route)
print("Best Distance:", best_distance)
