from .modules.analysis import (category_analysis, order_id_analysis,
                               price_analysis, product_analysis,
                               quantity_analysis)
from .modules.read_and_clean_files import clean_data, read_csv
from .modules.report_generator import report_analysis


def main():
    filename = "data.csv"
    data = read_csv(filename)

    if not data:
        return

    cleaned_data = clean_data(data)

    order_ids = order_id_analysis(cleaned_data)
    product_count, avg_price = product_analysis(cleaned_data)
    category_counts, category_revenue = category_analysis(cleaned_data)
    prices = price_analysis(cleaned_data)
    customer_orders, customer_spent = quantity_analysis(cleaned_data)

    report_analysis(
        order_ids,
        product_count,
        category_counts,
        category_revenue,
        avg_price,
        prices,
        customer_orders,
        customer_spent,
    )
