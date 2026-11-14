import csv

COL_PERMALINK = 0
COL_COMPANY_NAME = 1
COL_NUMBER_EMPLOYEES = 2
COL_CATEGORY = 3
COL_CITY = 4
COL_STATE = 5
COL_FUNDED_DATE = 6
COL_RAISED_AMOUNT = 7
COL_RAISED_CURRENCY = 8
COL_ROUND = 9

class FundingRaised:

  @staticmethod
  def _load_rows():
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      next(data)
      return list(data)

  @staticmethod
  def _row_to_dict(row):
    return {
      'permalink':        row[COL_PERMALINK],
      'company_name':     row[COL_COMPANY_NAME],
      'number_employees': row[COL_NUMBER_EMPLOYEES],
      'category':         row[COL_CATEGORY],
      'city':             row[COL_CITY],
      'state':            row[COL_STATE],
      'funded_date':      row[COL_FUNDED_DATE],
      'raised_amount':    row[COL_RAISED_AMOUNT],
      'raised_currency':  row[COL_RAISED_CURRENCY],
      'round':            row[COL_ROUND],
    }


  @staticmethod
  def where(options = {}):
    csv_data = FundingRaised._load_rows()

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

    return [FundingRaised._row_to_dict(row) for row in csv_data]

  @staticmethod
  def find_by(options):
    csv_data = FundingRaised._load_rows()

    if 'company_name' in options:
      for row in csv_data:
        if row[1] == options['company_name']:
          return FundingRaised._row_to_dict(row)

    if 'city' in options:
      for row in csv_data:
        if row[4] == options['city']:
          return FundingRaised._row_to_dict(row)

    if 'state' in options:
      for row in csv_data:
        if row[5] == options['state']:
          return FundingRaised._row_to_dict(row)

    if 'round' in options:
      for row in csv_data:
        if row[9] == options['round']:
          return FundingRaised._row_to_dict(row)

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
