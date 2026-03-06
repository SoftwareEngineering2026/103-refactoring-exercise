def get_row_from_csv_data(option: str, csv_data: list, row_index: int):
    result = []
    for row in csv_data:
      if row[row_index] == option:
        result.append(row)
    return result