import csv

FIELDS = [
  'permalink', 'company_name', 'number_employees', 'category', 'city',
  'state', 'funded_date', 'raised_amount', 'raised_currency', 'round',
]

# Fields that can be used in where/find_by, in the order find_by checks them.
FILTER_FIELDS = ['company_name', 'city', 'state', 'round']

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
    records = [FundingRaised._to_record(row) for row in FundingRaised._read_rows()]
    for field in FILTER_FIELDS:
      if field in options:
        records = [record for record in records if record[field] == options[field]]
    return records

  @staticmethod
  def find_by(options):
    records = [FundingRaised._to_record(row) for row in FundingRaised._read_rows()]
    # Unlike where, options are not combined: the first field (in
    # FILTER_FIELDS order) that has a matching record wins.
    for field in FILTER_FIELDS:
      if field in options:
        for record in records:
          if record[field] == options[field]:
            return record

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
