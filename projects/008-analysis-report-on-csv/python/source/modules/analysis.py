from collections import defaultdict
from statistics import mean


def order_id_analysis(data):
    order_counts = {row["OrderID"] for row in data if row["OrderID"]}
    return len(order_counts)


def product_analysis(data):
    product_count = defaultdict(int)
    prices = []

    for row in data:
        product_count[row["Product"]] += 1
        prices.append(float(row["Price"]))

    avg_price = mean(prices) if prices else 0

    return product_count, avg_price


def category_analysis(data):
    category_counts = defaultdict(int)
    category_revenue = defaultdict(float)

    for row in data:
        category = row["Category"]
        category_counts[category] += 1
        category_revenue[category] += float(row["Price"]) * int(row["Quantity"])

    return category_counts, category_revenue


def price_analysis(data):
    prices = [float(row["Price"]) for row in data]
    return (
        mean(prices) if prices else 0,
        min(prices) if prices else 0,
        max(prices) if prices else 0,
    )


def quantity_analysis(data):
    customer_orders = defaultdict(int)
    customer_spent = defaultdict(float)

    for row in data:
        customer = row["Customer"]
        customer_orders[customer] += 1
        customer_spent[customer] += float(row["Price"]) * int(row["Quantity"])
    return customer_orders, customer_spent
