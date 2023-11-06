import random
import numpy as np

# Define the road network with intersections and connecting roads
road_network = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Define parameters
population_size = 50
generations = 100
mutation_rate = 0.1
elite_percentage = 0.2

# Define traffic light timing plan
traffic_light_timing_plan = {
    'A': [10, 30],  # Green for 10 seconds, Red for 30 seconds
    'D': [30, 10],  # Green for 30 seconds, Red for 10 seconds
}

# Genetic Algorithm Functions
def generate_individual():
    timing_plan = {intersection: random.choice(traffic_light_timing_plan[intersection]) for intersection in road_network.keys()}
    return timing_plan

def calculate_fitness(individual):
    # Simulate traffic flow and calculate congestion or wait times
    total_wait_time = 0
    for _ in range(10):  # Simulate traffic for 10 iterations
        for intersection, light_duration in individual.items():
            total_wait_time += simulate_traffic_at_intersection(intersection, light_duration)
    return -total_wait_time  # Negative wait time as we want to minimize it

def simulate_traffic_at_intersection(intersection, light_duration):
    # Simulate traffic at an intersection and return the wait time
    green_time, red_time = traffic_light_timing_plan[intersection]
    total_time = green_time + red_time
    cycles = light_duration // total_time
    remaining_time = light_duration % total_time
    wait_time = cycles * red_time
    if remaining_time > green_time:
        wait_time += remaining_time - green_time
    return wait_time

def select_parents(population, fitness_scores):
    # Roulette wheel selection
    total_fitness = sum(fitness_scores)
    rand_value = random.uniform(0, total_fitness)
    partial_sum = 0
    for i, fitness in enumerate(fitness_scores):
        partial_sum += fitness
        if partial_sum > rand_value:
            return population[i]

def crossover(parent1, parent2):
    # Implement a uniform crossover operator
    child = {}
    for intersection in road_network.keys():
        child[intersection] = parent1[intersection] if random.random() < 0.5 else parent2[intersection]
    return child

def mutate(individual):
    # Implement a mutation operator to randomly change traffic light timings
    for intersection in road_network.keys():
        if random.random() < mutation_rate:
            individual[intersection] = random.choice(traffic_light_timing_plan[intersection])
    return individual

# Main Genetic Algorithm
population = [generate_individual() for _ in range(population_size)]

for generation in range(generations):
    fitness_scores = [calculate_fitness(ind) for ind in population]

    num_elites = int(elite_percentage * population_size)
    elites = [population[i] for i in np.argsort(fitness_scores)[:num_elites]]

    next_generation = elites

    while len(next_generation) < population_size:
        parent1 = select_parents(population, fitness_scores)
        parent2 = select_parents(population, fitness_scores)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)

    population = next_generation

# Select the best traffic light timing plan
best_timing_plan = max(population, key=calculate_fitness)
best_fitness = calculate_fitness(best_timing_plan)

# Print the results
print("Best Traffic Light Timing Plan:", best_timing_plan)
print("Fitness Score (Negative Wait Time):", best_fitness)
