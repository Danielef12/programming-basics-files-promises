from tabulate import tabulate

def data_visualize(dataset):
    if not dataset:
        print("No dataset provided")
        return
    headers = list(dataset[0].keys())
    data = list(row.values() for row in dataset)
    print(tabulate(data, headers=headers))