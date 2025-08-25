def delete_column(data, column_name):
    if data:
        for row in data:
            row.pop(column_name, None)
    return data