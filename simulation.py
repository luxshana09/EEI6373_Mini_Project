import csv

def run_experiment(filename, num_counters, speed_multiplier):
    # Read the customer data from the CSV file
    customers = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            customer_id = int(row[0])
            arrival = float(row[1])
            service = float(row[2])
            customers.append([customer_id, arrival, service])
    
    for c in customers:
        c[2] = c[2] * speed_multiplier   # New service time
    
    counters_free_time = [0.0] * num_counters
    
    # Lists to store results for each customer
    wait_times = []
    total_customers = len(customers)
    
    # For utilization tracking, we add up total busy time for each counter
    counter_busy_time = [0.0] * num_counters
    
    for customer in customers:
        cust_id = customer[0]
        arrival = customer[1]
        service = customer[2]
        
        # Find the counter that becomes free the earliest
        earliest_time = min(counters_free_time)
        earliest_counter = counters_free_time.index(earliest_time)
        
        # When does this customer start service?
        start_service = max(arrival, earliest_time)
        
        # How long did they wait?
        wait = start_service - arrival
        wait_times.append(wait)
        
        # When does this counter finish serving this customer?
        finish_time = start_service + service
        counters_free_time[earliest_counter] = finish_time
        
        # Add this service time to the counter's busy time
        counter_busy_time[earliest_counter] += service
    

    avg_wait = sum(wait_times) / len(wait_times)
    
    # 2. Average Queue Length (Little's Law: L = λ * W)
    # λ (arrival rate) = total customers / total time
    total_time = max(counters_free_time)
    arrival_rate = total_customers / total_time
    avg_queue_length = arrival_rate * avg_wait
    
    # 3. Counter Utilization (average % busy across all counters)
    total_busy_time = sum(counter_busy_time)
    total_available_time = num_counters * total_time
    avg_utilization = total_busy_time / total_available_time
    
    # 4. Total Time to serve all customers
    total_time_taken = total_time
    
    # Return all results as a dictionary
    return {
        'avg_wait': avg_wait,
        'avg_queue_length': avg_queue_length,
        'avg_utilization': avg_utilization,
        'total_time': total_time_taken
    }

print("SUPERMARKET SIMULATION RESULTS")

# Experiment 1: 2 counters, normal speed (1.0)
results1 = run_experiment('supermarket_data.csv', 2, 1.0)
print("Experiment 1 (2 counters, normal speed):")
print(f"  Avg Wait: {results1['avg_wait']:.2f} min")
print(f"  Avg Queue Length: {results1['avg_queue_length']:.2f} customers")
print(f"  Avg Utilization: {results1['avg_utilization']*100:.1f}%")
print(f"  Total Time: {results1['total_time']:.2f} min")
print()

# Experiment 2: 3 counters, normal speed
results2 = run_experiment('supermarket_data.csv', 3, 1.0)
print("Experiment 2 (3 counters, normal speed):")
print(f"  Avg Wait: {results2['avg_wait']:.2f} min")
print(f"  Avg Queue Length: {results2['avg_queue_length']:.2f} customers")
print(f"  Avg Utilization: {results2['avg_utilization']*100:.1f}%")
print(f"  Total Time: {results2['total_time']:.2f} min")
print()

# Experiment 3: 2 counters, 30% faster (0.7)
results3 = run_experiment('supermarket_data.csv', 2, 0.7)
print("Experiment 3 (2 counters, 30% faster):")
print(f"  Avg Wait: {results3['avg_wait']:.2f} min")
print(f"  Avg Queue Length: {results3['avg_queue_length']:.2f} customers")
print(f"  Avg Utilization: {results3['avg_utilization']*100:.1f}%")
print(f"  Total Time: {results3['total_time']:.2f} min")
print()

# Experiment 4: 3 counters, 30% faster
results4 = run_experiment('supermarket_data.csv', 3, 0.7)
print("Experiment 4 (3 counters, 30% faster):")
print(f"  Avg Wait: {results4['avg_wait']:.2f} min")
print(f"  Avg Queue Length: {results4['avg_queue_length']:.2f} customers")
print(f"  Avg Utilization: {results4['avg_utilization']*100:.1f}%")
print(f"  Total Time: {results4['total_time']:.2f} min")
print()

