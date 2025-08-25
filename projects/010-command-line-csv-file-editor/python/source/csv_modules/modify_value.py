def modify_value(data, row_num, column_name, new_value):
    try:
        row_index = row_num - 1

        if not (0 <= row_index < len(data)):
            return False, f"Row #{row_num} does not exist"
        if column_name not in data[row_index]:
            return False, f"Column '{column_name}' does not exist"

        data[row_index][column_name] = new_value
        return True, f"Modified {column_name} with new value: {new_value}."
    except Exception as e:
        return False, f"Error: {e}"