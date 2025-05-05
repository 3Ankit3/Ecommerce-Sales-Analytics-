import pandas as pd 
import numpy as np 
from faker import Faker 
import random
from datetime import datetime,timedelta

fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

NUM_CUSTOMERS = 5000
NUM_PRODUCTS = 500
NUM_ORDERS = 20000
MAX_ITEMS_PER_ORDER = 5 
CATEGORIES = ['Electronics', 'Clothing', 'Books', 'Home', 'Beauty', 'Sports']
REGIONS = ['North', 'South', 'East', 'West', 'Central']

#1. Customers Table 
customers = []
for i in range(1,NUM_CUSTOMERS+1):
    customers.append({
        'customer_id':i,
        'name': fake.name(),
        'email': fake.email(),
        'region': random.choice(REGIONS),
        'join_date': fake.date_between(start_date = '-2y', end_date = 'today')
    })
df_customers = pd.DataFrame(customers)

#2. Products Table
products = []
for i in range(1,NUM_PRODUCTS + 1):
    category = random.choice(CATEGORIES)
    price = round(random.uniform(5,500),2)
    products.append({
        'product_id':i,
        'name':f"{fake.word().capitalize()} {category}",
        'category': category,
        'price': price,
        'stock':random.randint(10,500)
    })
df_products = pd.DataFrame(products)

#3. Orders Table
orders = []
for i in range(1, NUM_ORDERS+1):
    customer_id = random.randint(1,NUM_CUSTOMERS)
    order_date = fake.date_between(start_date = '-1y', end_date = 'today')
    status = random.choices(['completed','cancelled','returned'],weights = [0.85,0.10,0.050])[0]
    orders.append({
        'order_id':i,
        'customer_id':customer_id,
        'order_date': order_date,
        'status': status
    })
df_orders = pd.DataFrame(orders)

#4. Orders Table items
order_items = []
item_id = 1
for order in df_orders.itertuples():
    num_items = random.randint(1,MAX_ITEMS_PER_ORDER)
    selected_products = random.sample(range(1, NUM_PRODUCTS + 1), num_items)
    for product_id in selected_products:
        product_price = df_products.loc[df_products['product_id'] == product_id, 'price'].values[0]
        quantity = random.randint(1,5)
        order_items.append({
            'order_item_id': item_id,
            'order_id': order.order_id,
            'product_id':product_id,
            'quantity': quantity,
            'price': product_price
        })
        item_id += 1
df_order_items = pd.DataFrame(order_items)

#5. Payments table 
payment_methods = ['credit_card', 'paypal', 'bank_transfer', 'gift_card']
payments = []
payment_id = 1
for order in df_orders.itertuples():
    if order.status == 'completed':
        payment_date = order.order_date + timedelta(days = random.randint(0,3))
        payments.append({
            'payment_id': payment_id,
            'order_id': order.order_id,
            'method': random.choice(payment_methods),
            'amount': round(df_order_items[df_order_items['order_id'] == order.order_id]['price'].multiply(df_order_items[df_order_items['order_id'] == order.order_id]['quantity']).sum(),2),
            'payment_date': payment_date
        })
        payment_id += 1
df_payments = pd.DataFrame(payments)

# Save as CSV
df_customers.to_csv("customer.csv", index = False)
df_products.to_csv("products.csv", index = False)
df_orders.to_csv("orders.csv", index = False)
df_order_items.to_csv("order_items.csv", index = False)
df_payments.to_csv("payments.csv", index = False)

print("Mock Data generated and saved as csv files")