def add_column(data):
    while column_name := input("Enter new column name: ").strip():
        if not column_name:
            print("Column name cannot be empty")
            continue
        if column_name in data[0]:
            overwrite = input(f"Column '{column_name}' already exists, overwrite it?")
            if overwrite.lower() not in ["yes", "y", "ye", "y"]:
                continue
        break
    print(f"Column '{column_name}' has been added.")
    print(f"Manually adding value for {column_name}: {len(data)} rows.")
    for i, row in enumerate(data):
        print(f"Row #{i+1}: {dict(list(row.items())[:3])}")
        value = input(f"Enter new value for {column_name}: ").strip()
        row[column_name] = value
    print(f"Column '{column_name}' filled manually successfully.")

