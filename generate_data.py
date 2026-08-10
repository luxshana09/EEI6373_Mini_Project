import utils.session
import random
import csv

total_customers = 300
first_arrival = 0.0
min_gap = 0.5
max_gap = 2.0
min_service = 2.0
max_service = 6.0

customers = []
previous_arrival = first_arrival

for customer_id in range(1, total_customers + 1):
    if customer_id == 1:
        arrival = 0.0
    else:
        gap = round(random.uniform(min_gap, max_gap), 2)
        arrival = previous_arrival + gap
    
    service = random.uniform(min_service, max_service)
    

    arrival = round(arrival, 2)
    service = round(service, 2)
    
    customers.append([customer_id, arrival, service])
    
    previous_arrival = arrival

with open('supermarket_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Customer_ID', 'Arrival_Time', 'Service_Time'])
    writer.writerows(customers)

print("CSV file created")
