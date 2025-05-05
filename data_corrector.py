import pandas as pd
import random
from faker import Faker

customers_df = pd.read_csv("customer.csv")
customer_ids = customers_df['customer_id'].tolist()

fake = Faker()
num_orders = 20000
statuses = ['completed','cancelled','returned']

orders = []
for order_id in range(1, num_orders+1):
    order = {
        'order_id': order_id,
        'customer_id': random.randint(1,3469),
        'order_date': fake.date_between(start_date='-1y', end_date='today'),
        'status':random.choice(statuses)
    }
    orders.append(order)

orders_df = pd.DataFrame(orders)
orders_df.to_csv('orders_corrected.csv', index = False)

print("corrected data saved")