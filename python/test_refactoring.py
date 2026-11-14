import pytest
from funding_raised import FundingRaised, RecordNotFound, COL_CITY, COL_ROUND

def _first_value(col_index):
    """Первое непустое значение из указанной колонки — гарантированно есть в данных."""
    rows = FundingRaised._load_rows()
    return next(row[col_index] for row in rows if row[col_index])

def test_where_returns_all_when_no_options():
    results = FundingRaised.where({})
    assert len(results) > 0
    assert all(isinstance(r, dict) for r in results)
    assert set(results[0]) >= {"company_name", "city", "state", "round"}


def test_where_filters_by_city():
    city = _first_value(COL_CITY)
    results = FundingRaised.where({"city": city})
    assert results
    assert all(r["city"] == city for r in results)


def test_where_applies_multiple_filters_as_and():
    row = FundingRaised._load_rows()[0]
    city, rnd = row[COL_CITY], row[COL_ROUND]
    results = FundingRaised.where({"city": city, "round": rnd})
    assert results
    assert all(r["city"] == city and r["round"] == rnd for r in results)


def test_where_unknown_filter_returns_all():
    results = FundingRaised.where({"unknown": "x"})
    assert len(results) == len(FundingRaised.where({}))


def test_find_by_raises_when_not_found():
    with pytest.raises(RecordNotFound):
        FundingRaised.find_by({"company_name": "__definitely_not_a_company__"})


def test_find_by_returns_single_dict():
    city = _first_value(COL_CITY)
    result = FundingRaised.find_by({"city": city})
    assert isinstance(result, dict)
    assert result["city"] == city


def test_row_to_dict_maps_all_fields():
    row = [str(i) for i in range(10)]
    d = FundingRaised._row_to_dict(row)
    assert d["permalink"] == "0"
    assert d["city"] == str(COL_CITY)
    assert d["round"] == str(COL_ROUND)