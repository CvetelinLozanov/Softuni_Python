gpu_price = 250

budget = float(input())
number_of_gpus = int(input())
number_of_cpus = int(input())
number_of_memory = int(input())

total_costs_for_gpus = gpu_price * number_of_gpus
total_cost_for_cpu = (total_costs_for_gpus * 0.35) * number_of_cpus
total_costs_for_memory = (total_costs_for_gpus * 0.10) * number_of_memory
total_costs_for_all = total_cost_for_cpu + total_costs_for_memory + total_costs_for_gpus

if number_of_gpus > number_of_cpus:
    total_costs_for_all *= 0.85

if budget >= total_costs_for_all:
    print(f'You have {budget - total_costs_for_all:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_costs_for_all - budget:.2f} leva more!')