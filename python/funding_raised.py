import csv
from csv_utils import get_row_from_csv_data

class FundingRaised:
  
  @staticmethod
  def _map_row_to_dict(row):
    """Convert a CSV row array into a mapped dictionary."""
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
  def where(options = {}):
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      # skip header
      next(data)
      csv_data = []
      for row in data:
        csv_data.append(row)

    if 'company_name' in options:
      csv_data = get_row_from_csv_data(options['company_name'], csv_data, 1)

    if 'city' in options:
      csv_data = get_row_from_csv_data(options['city'], csv_data, 4)

    if 'state' in options:
      csv_data = get_row_from_csv_data(options['state'], csv_data, 5)

    if 'round' in options:
      csv_data = get_row_from_csv_data(options['round'], csv_data, 9)
      
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
        if row[1] == options['company_name']:
          return FundingRaised._map_row_to_dict(row)

    if 'city' in options:
      for row in csv_data:
        if row[4] == options['city']:
          return FundingRaised._map_row_to_dict(row)

    if 'state' in options:
      for row in csv_data:
        if row[5] == options['state']:
          return FundingRaised._map_row_to_dict(row)

    if 'round' in options:
      for row in csv_data:
        if row[9] == options['round']:
          return FundingRaised._map_row_to_dict(row)

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
