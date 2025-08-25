def order_by_year(data):
    if not data:
        print("No data provided")
        return
    data_sorted = sorted(data, key=lambda row: row["Year"])
    return data_sorted

def order_by_filmname(data):
    if not data:
        print("No data provided")
        return
    data_sorted = sorted(data, key=lambda row: row["Film"])
    return data_sorted

def order_by_studio(data):
    if not data:
        print("No data provided")
        return
    data_sorted = sorted(data, key=lambda row: row["Lead Studio"])

    return data_sorted
