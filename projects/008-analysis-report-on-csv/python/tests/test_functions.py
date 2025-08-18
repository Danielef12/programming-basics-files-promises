import csv
import os
import tempfile
import unittest
from collections import defaultdict
from statistics import mean

from source.modules.analysis import (category_analysis, order_id_analysis,
                                     price_analysis, product_analysis,
                                     quantity_analysis)
from source.modules.read_and_clean_files import clean_data, read_csv


class TestReadCsvAndCleanData(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.tmp_path = self.tmpdir.name

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_read_csv_success(self):
        file_path = os.path.join(self.tmp_path, "test.csv")
        content = """OrderID,Product,Category,Price,Quantity,Customer
1001,Laptop,Electronics,900,2,Alice
1002,Tablet,Electronics,350,3,Bob
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        data = read_csv(file_path)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["Product"], "Laptop")
        self.assertEqual(data[1]["Customer"], "Bob")

    def test_read_csv_file_not_found(self):
        data = read_csv("non_existent.csv")
        self.assertEqual(data, [])

    def test_read_csv_invalid_csv(self):
        file_path = os.path.join(self.tmp_path, "bad.csv")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("OrderID,Product\n1001,Laptop\n1002")

        data = read_csv(file_path)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[1]["OrderID"], "1002")

    def test_clean_data_valid(self):
        data = [
            {"OrderID": "1001", "Product": "Laptop", "Category": "Electronics"},
            {"OrderID": "1002", "Product": "Tablet", "Category": "Electronics"},
        ]
        cleaned = clean_data(data)
        self.assertEqual(cleaned, data)

    def test_clean_data_with_missing_values(self):
        data = [
            {"OrderID": "1001", "Product": "Laptop", "Category": "Electronics"},
            {"OrderID": "1002", "Product": "", "Category": "Electronics"},
        ]
        cleaned = clean_data(data)
        self.assertEqual(len(cleaned), 1)
        self.assertEqual(cleaned[0]["Product"], "Laptop")

    def test_clean_data_empty_input(self):
        self.assertEqual(clean_data([]), [])


class TestAnalysisFunctions(unittest.TestCase):
    def setUp(self):
        self.data = [
            {
                "OrderID": "1001",
                "Product": "Laptop",
                "Category": "Electronics",
                "Price": "900",
                "Quantity": "2",
                "Customer": "Alice",
            },
            {
                "OrderID": "1002",
                "Product": "Smartphone",
                "Category": "Electronics",
                "Price": "600",
                "Quantity": "1",
                "Customer": "Bob",
            },
            {
                "OrderID": "1003",
                "Product": "Tablet",
                "Category": "Electronics",
                "Price": "350",
                "Quantity": "3",
                "Customer": "Alice",
            },
            {
                "OrderID": "1004",
                "Product": "Desk",
                "Category": "Furniture",
                "Price": "150",
                "Quantity": "1",
                "Customer": "Charlie",
            },
        ]

    def test_order_id_analysis(self):
        result = order_id_analysis(self.data)
        self.assertEqual(result, 4)

    def test_product_analysis(self):
        product_count, avg_price = product_analysis(self.data)
        self.assertEqual(product_count["Laptop"], 1)
        self.assertEqual(product_count["Tablet"], 1)
        self.assertAlmostEqual(avg_price, mean([900, 600, 350, 150]))

    def test_category_analysis(self):
        category_counts, category_revenue = category_analysis(self.data)
        self.assertEqual(category_counts["Electronics"], 3)
        self.assertEqual(category_counts["Furniture"], 1)
        self.assertEqual(category_revenue["Electronics"], 900 * 2 + 600 * 1 + 350 * 3)
        self.assertEqual(category_revenue["Furniture"], 150 * 1)

    def test_price_analysis(self):
        avg_price, min_price, max_price = price_analysis(self.data)
        self.assertAlmostEqual(avg_price, mean([900, 600, 350, 150]))
        self.assertEqual(min_price, 150)
        self.assertEqual(max_price, 900)

    def test_quantity_analysis(self):
        customer_orders, customer_spent = quantity_analysis(self.data)
        self.assertEqual(customer_orders["Alice"], 2)
        self.assertEqual(customer_orders["Bob"], 1)
        self.assertEqual(customer_spent["Alice"], 900 * 2 + 350 * 3)
        self.assertEqual(customer_spent["Charlie"], 150 * 1)


if __name__ == "__main__":
    unittest.main()
