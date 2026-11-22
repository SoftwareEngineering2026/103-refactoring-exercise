import csv
from pathlib import Path

DEFAULT_CSV_PATH = Path("../startup_funding.csv")

COLUMNS = (
    "permalink",
    "company_name",
    "number_employees",
    "category",
    "city",
    "state",
    "funded_date",
    "raised_amount",
    "raised_currency",
    "round",
)

FILTER_COLUMNS = {
    "company_name": 1,
    "city": 4,
    "state": 5,
    "round": 9,
}


class RecordNotFound(Exception):
    pass


class FundingRaised:
    @staticmethod
    def _load_rows(csv_path: Path = DEFAULT_CSV_PATH) -> list[list[str]]:
        with open(csv_path, "rt", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar='"')
            next(reader, None)  # skip header
            return list(reader)

    @staticmethod
    def _map_row(row: list[str]) -> dict[str, str]:
        return dict(zip(COLUMNS, row))

    @staticmethod
    def _validate_options(options: dict[str, str]) -> None:
        invalid_keys = set(options) - set(FILTER_COLUMNS)
        if invalid_keys:
            raise KeyError(f"Unknown filter options: {sorted(invalid_keys)}")

    @classmethod
    def where(
        cls,
        options: dict[str, str] | None = None,
        csv_path: Path = DEFAULT_CSV_PATH,
    ) -> list[dict[str, str]]:
        filters = options or {}
        cls._validate_options(filters)

        rows = cls._load_rows(csv_path)
        for key, value in filters.items():
            column_index = FILTER_COLUMNS[key]
            rows = [row for row in rows if row[column_index] == value]

        return [cls._map_row(row) for row in rows]

    @classmethod
    def find_by(
        cls,
        options: dict[str, str],
        csv_path: Path = DEFAULT_CSV_PATH,
    ) -> dict[str, str]:
        cls._validate_options(options)

        rows = cls._load_rows(csv_path)
        for key, value in options.items():
            column_index = FILTER_COLUMNS[key]
            for row in rows:
                if row[column_index] == value:
                    return cls._map_row(row)

        raise RecordNotFound
