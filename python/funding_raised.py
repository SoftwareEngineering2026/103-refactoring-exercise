import csv

FIELDS = [
  'permalink', 'company_name', 'number_employees', 'category', 'city',
  'state', 'funded_date', 'raised_amount', 'raised_currency', 'round',
]

class FundingRaised:
  @staticmethod
  def _read_rows():
    with open("../startup_funding.csv", "rt") as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      next(reader)  # skip header
      return list(reader)

  @staticmethod
  def _to_record(row):
    return dict(zip(FIELDS, row))

  @staticmethod
  def where(options = {}):
    csv_data = FundingRaised._read_rows()

    funding = []
    if 'company_name' in options:
      result = []
      for row in csv_data:
        if row[1] == options['company_name']:
          result.append(row)
      csv_data = result

    if 'city' in options:
      result = []
      for row in csv_data:
        if row[4] == options['city']:
          result.append(row)
      csv_data = result

    if 'state' in options:
      result = []
      for row in csv_data:
        if row[5] == options['state']:
          result.append(row)
      csv_data = result

    if 'round' in options:
      result = []
      for row in csv_data:
        if row[9] == options['round']:
          result.append(row)
      csv_data = result

    output = []
    for row in csv_data:
      output.append(FundingRaised._to_record(row))

    return output

  @staticmethod
  def find_by(options):
    csv_data = FundingRaised._read_rows()

    if 'company_name' in options:
      for row in csv_data:
        if row[1] == options['company_name']:
          return FundingRaised._to_record(row)

    if 'city' in options:
      for row in csv_data:
        if row[4] == options['city']:
          return FundingRaised._to_record(row)

    if 'state' in options:
      for row in csv_data:
        if row[5] == options['state']:
          return FundingRaised._to_record(row)

    if 'round' in options:
      for row in csv_data:
        if row[9] == options['round']:
          return FundingRaised._to_record(row)

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
