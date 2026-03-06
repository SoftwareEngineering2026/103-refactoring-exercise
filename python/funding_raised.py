import csv
from csv_utils import get_row_from_csv_data

class FundingRaised:
  
  PERMALINK_INDEX = 0
  COMPANY_NAME_INDEX = 1
  NUMBER_EMPLOYEES_INDEX = 2
  CATEGORY_INDEX = 3
  CITY_INDEX = 4
  STATE_INDEX = 5
  FUNDED_DATE_INDEX = 6
  RAISED_AMOUNT_INDEX = 7
  RAISED_CURRENCY_INDEX = 8
  ROUND_INDEX = 9
  
  @staticmethod
  def _map_row_to_dict(row):
    """Convert a CSV row array into a mapped dictionary."""
    return {
      'permalink': row[FundingRaised.PERMALINK_INDEX],
      'company_name': row[FundingRaised.COMPANY_NAME_INDEX],
      'number_employees': row[FundingRaised.NUMBER_EMPLOYEES_INDEX],
      'category': row[FundingRaised.CATEGORY_INDEX],
      'city': row[FundingRaised.CITY_INDEX],
      'state': row[FundingRaised.STATE_INDEX],
      'funded_date': row[FundingRaised.FUNDED_DATE_INDEX],
      'raised_amount': row[FundingRaised.RAISED_AMOUNT_INDEX],
      'raised_currency': row[FundingRaised.RAISED_CURRENCY_INDEX],
      'round': row[FundingRaised.ROUND_INDEX]
    }

  @staticmethod
  def where(options = {}):
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      # skip header
      next(data)
      csv_data = []
      for row in data:
        csv_data.append(row)

    if 'company_name' in options:
      csv_data = get_row_from_csv_data(options['company_name'], csv_data, FundingRaised.COMPANY_NAME_INDEX)

    if 'city' in options:
      csv_data = get_row_from_csv_data(options['city'], csv_data, FundingRaised.CITY_INDEX)

    if 'state' in options:
      csv_data = get_row_from_csv_data(options['state'], csv_data, FundingRaised.STATE_INDEX)

    if 'round' in options:
      csv_data = get_row_from_csv_data(options['round'], csv_data, FundingRaised.ROUND_INDEX)
      
    output = []
    for row in csv_data:
      output.append(FundingRaised._map_row_to_dict(row))

    return output

  @staticmethod
  def find_by(options):
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      # skip header
      next(data)
      csv_data = []
      for row in data:
        csv_data.append(row)

    if 'company_name' in options:
      for row in csv_data:
        if row[FundingRaised.COMPANY_NAME_INDEX] == options['company_name']:
          return FundingRaised._map_row_to_dict(row)

    if 'city' in options:
      for row in csv_data:
        if row[FundingRaised.CITY_INDEX] == options['city']:
          return FundingRaised._map_row_to_dict(row)

    if 'state' in options:
      for row in csv_data:
        if row[FundingRaised.STATE_INDEX] == options['state']:
          return FundingRaised._map_row_to_dict(row)

    if 'round' in options:
      for row in csv_data:
        if row[FundingRaised.ROUND_INDEX] == options['round']:
          return FundingRaised._map_row_to_dict(row)

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
