def report_analysis(
    order_counts,
    product_count,
    category_counts,
    category_revenue,
    avg_price,
    prices,
    customer_orders,
    customer_spent,
):
    print("Order ID Analysis:")
    print(f"Total unique Orders: {order_counts}")

    print("\nProduct Analysis:")
    print("Most popular products:")
    for product, count in sorted(
        product_count.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"{product}: {count} orders")
    print(f"Average Product Price: {avg_price:.2f}")

    print("\nCategory Analysis:")
    for category in category_counts:
        print(
            f"{category}: {category_counts[category]} products, Revenue:$ {category_revenue[category]:.2f}"
        )

    print("\nPrice Analysis:")
    print(f"Average Price: ${prices[0]:.2f}")
    print(f"Minimum Price: ${prices[1]:.2f}")
    print(f"Maximum Price: ${prices[2]:.2f}")

    print("\nQuantity Analysis:")
    print(f"Most Active Customers:")
    for customer, orders in sorted(
        customer_orders.items(), key=lambda x: x[1], reverse=True
    ):
        print(
            f"{customer}: {orders} orders, Total Spent: ${customer_spent[customer]:.2f}"
        )
    print(f"Highest value Customers")
    for customer, spent in sorted(
        customer_spent.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"{customer}: Total Spent: ${spent:.2f}")
