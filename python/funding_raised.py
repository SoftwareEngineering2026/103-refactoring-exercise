import csv

class FundingRaised:
  @staticmethod
  def _row_to_dict(row):
    return {
      'permalink': row[0],
      'company_name': row[1],
      'number_employees': row[2],
      'category': row[3],
      'city': row[4],
      'state': row[5],
      'funded_date': row[6],
      'raised_amount': row[7],
      'raised_currency': row[8],
      'round': row[9]
    }


  @staticmethod
  def _load_data():
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      next(data)
      return list(data)


  @staticmethod
  def where(options = {}):
    csv_data = FundingRaised._load_data()

    filters = {
      'company_name': 1,
      'city': 4,
      'state': 5,
      'round': 9
    }

    for field, column_index in filters.items():
      if field in options:
        csv_data = [
          row for row in csv_data
          if row[column_index] == options[field]
        ]

    output = []
    for row in csv_data:
      output.append(FundingRaised._row_to_dict(row))

    return output

  @staticmethod
  def find_by(options):
    csv_data = FundingRaised._load_data()

    filters = {
      'company_name': 1,
      'city': 4,
      'state': 5,
      'round': 9
    }

    for field, column_index in filters.items():
      if field in options:
        for row in csv_data:
          if row[column_index] == options[field]:
            return FundingRaised._row_to_dict(row)

    raise RecordNotFound


class RecordNotFound(Exception):
  pass
