import csv

class FundingRaised:
  @staticmethod
  def _load_data():
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      next(data)
      return list(data)
    
  @staticmethod
  def _map_row(row):
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
    csv_data = FundingRaised._load_data()
   

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
  output.append(FundingRaised._map_row(row))

return output

  @staticmethod
  def find_by(options):
    csv_data = FundingRaised._load_data()
   

    if 'company_name' in options:
      for row in csv_data:
        if row[1] == options['company_name']:
  return FundingRaised._map_row(row)

    if 'city' in options:
      for row in csv_data:
        if row[4] == options['city']:
  return FundingRaised._map_row(row)

    if 'state' in options:
      for row in csv_data:
        if row[5] == options['state']:
  return FundingRaised._map_row(row)

    if 'round' in options:
      for row in csv_data:
        if row[9] == options['round']:
  return FundingRaised._map_row(row)

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
