def delete_row(data, row_index):
    if data:
        if row_index < 0 or row_index >= len(data):
            print(f"Value '{row_index}' is out of range")
            return False
        del data[row_index]
        print(f"Value '{row_index}' has been removed")
        return True
    return False