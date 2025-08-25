def add_row(data):
    if not data:
        print("No data provided")
        return
    columns = list(data[0].keys())
    new_row = {}

    print(f"Appending new row, columns available: {columns}")
    for column in columns:
        value = input(f"Enter new value for {column}: ").strip()
        new_row[column] = value
    data.append(new_row)
    print("Row appended successfully.")
    return new_row