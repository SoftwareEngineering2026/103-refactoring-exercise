import csv
import os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'startup_funding.csv')

FIELDS = [
  'permalink', 'company_name', 'number_employees', 'category', 'city',
  'state', 'funded_date', 'raised_amount', 'raised_currency', 'round',
]

# Fields that can be used in where/find_by, in the order find_by checks them.
FILTER_FIELDS = ['company_name', 'city', 'state', 'round']

class FundingRaised:
  @staticmethod
  def _read_rows():
    with open(CSV_PATH, "rt") as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      next(reader)  # skip header
      return list(reader)

  @staticmethod
  def _read_records():
    return [dict(zip(FIELDS, row)) for row in FundingRaised._read_rows()]

  @staticmethod
  def where(options=None):
    options = options or {}
    records = FundingRaised._read_records()
    for field in FILTER_FIELDS:
      if field in options:
        records = [record for record in records if record[field] == options[field]]
    return records

  @staticmethod
  def find_by(options):
    records = FundingRaised._read_records()
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
