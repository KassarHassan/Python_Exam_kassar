# Task 5 (easier): Sum purchases per customer

# Sample data
purchases = [
    ("Alice", 120),
    ("Bob",   80),
    ("Alice",  50),
    ("Bob",    20),
    ("Clara", 200)
]

# 1) Find each unique customer name
customers = set()                    # an empty set to hold names
for record in purchases:            
    name = record[0]                 # record[0] is the customer
    customers.add(name)              # add to the set (duplicates ignored)

# 2) For each customer, sum their purchases
for customer in customers:
    total = 0                        # start their total at zero
    for record in purchases:
        name, amount = record       # unpack the tuple
        if name == customer:        # if it’s this customer’s record
            total += amount         # add the amount
    # 3) Print the result
    print(f"{customer} spent ${total}")
