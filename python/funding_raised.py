import csv


class FundingRaised:
  FILTER_FIELDS = {
    'company_name': 1,
    'city': 4,
    'state': 5,
    'round': 9
  }

  @staticmethod
  def _read_csv():
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      next(data)  # skip header
      return [row for row in data]

  @staticmethod
  def _filter_rows(csv_data, options):
    for field, index in FundingRaised.FILTER_FIELDS.items():
      if field in options:
        csv_data = [
          row for row in csv_data
          if row[index] == options[field]
        ]
    return csv_data

  @staticmethod
  def where(options=None):
    if options is None:
      options = {}

    csv_data = FundingRaised._read_csv()
    csv_data = FundingRaised._filter_rows(csv_data, options)

    return [
      FundingRaised._row_to_dict(row)
      for row in csv_data
    ]

  @staticmethod
  def find_by(options):
    csv_data = FundingRaised._read_csv()

    for field, index in FundingRaised.FILTER_FIELDS.items():
      if field in options:
        for row in csv_data:
          if row[index] == options[field]:
            return FundingRaised._row_to_dict(row)

    raise RecordNotFound

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


class RecordNotFound(Exception):
  pass

