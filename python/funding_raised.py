import csv
from csv_utils import get_row_from_csv_data

class FundingRaised:
  
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
      mapped = {}
      mapped['permalink'] = row[0]
      mapped['company_name'] = row[1]
      mapped['number_employees'] = row[2]
      mapped['category'] = row[3]
      mapped['city'] = row[4]
      mapped['state'] = row[5]
      mapped['funded_date'] = row[6]
      mapped['raised_amount'] = row[7]
      mapped['raised_currency'] = row[8]
      mapped['round'] = row[9]
      output.append(mapped)

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
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'city' in options:
      for row in csv_data:
        if row[4] == options['city']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'state' in options:
      for row in csv_data:
        if row[5] == options['state']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'round' in options:
      for row in csv_data:
        if row[9] == options['round']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
