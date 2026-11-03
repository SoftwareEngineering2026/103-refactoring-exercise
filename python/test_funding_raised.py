import pytest

from funding_raised import FundingRaised, RecordNotFound

TOTAL_ROWS = 1460

LIFELOCK_ROUND_B = {
  'permalink': 'lifelock', 'company_name': 'LifeLock', 'number_employees': '',
  'category': 'web', 'city': 'Tempe', 'state': 'AZ', 'funded_date': '1-May-07',
  'raised_amount': '6850000', 'raised_currency': 'USD', 'round': 'b',
}

LIFELOCK_ROUND_A = dict(LIFELOCK_ROUND_B, funded_date='1-Oct-06', raised_amount='6000000', round='a')


def test_where_without_options_returns_all_rows():
  assert len(FundingRaised.where({})) == TOTAL_ROWS


def test_where_ignores_unknown_options():
  assert len(FundingRaised.where({'unknown': 'value'})) == TOTAL_ROWS


def test_where_combines_options_with_and():
  assert FundingRaised.where({'city': 'Tempe', 'state': 'CA'}) == []


def test_where_returns_full_record():
  assert FundingRaised.where({'city': 'Tempe'})[0] == LIFELOCK_ROUND_B


def test_find_by_city():
  assert FundingRaised.find_by({'city': 'Tempe'}) == LIFELOCK_ROUND_B


def test_find_by_round():
  assert FundingRaised.find_by({'round': 'a'}) == LIFELOCK_ROUND_A


def test_find_by_checks_company_name_first():
  row = FundingRaised.find_by({'company_name': 'Facebook', 'city': 'Tempe'})
  assert row['company_name'] == 'Facebook'


def test_find_by_falls_back_to_next_option():
  row = FundingRaised.find_by({'company_name': 'NotFacebook', 'city': 'Tempe'})
  assert row == LIFELOCK_ROUND_B


def test_find_by_raises_when_nothing_matches():
  with pytest.raises(RecordNotFound):
    FundingRaised.find_by({'company_name': 'NotFacebook'})


def test_find_by_raises_without_options():
  with pytest.raises(RecordNotFound):
    FundingRaised.find_by({})
