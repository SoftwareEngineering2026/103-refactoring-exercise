import csv
import os


class RecordNotFound(Exception):
    pass


class FundingRaised:
    # Словарь для замены магических индексов
    _COLUMNS = {
        'permalink': 0, 'company_name': 1, 'number_employees': 2,
        'category': 3, 'city': 4, 'state': 5, 'funded_date': 6,
        'raised_amount': 7, 'raised_currency': 8, 'round': 9
    }

    @classmethod
    def _get_csv_path(cls):
        """Возвращает путь к CSV-файлу независимо от места запуска."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, 'startup_funding.csv')

    @classmethod
    def _read_csv(cls):
        """Читает CSV и возвращает список строк без заголовка."""
        with open(cls._get_csv_path(), 'r') as f:
            reader = csv.reader(f)
            next(reader)
            return list(reader)

    @classmethod
    def _filter_data(cls, data, filters):
        """Применяет фильтры к данным."""
        result = data
        for field, value in filters.items():
            if field in cls._COLUMNS:
                idx = cls._COLUMNS[field]
                result = [row for row in result if row[idx] == value]
        return result

    @classmethod
    def _row_to_dict(cls, row):
        """Преобразует строку в словарь."""
        return {name: row[idx] for name, idx in cls._COLUMNS.items()}

    @classmethod
    def where(cls, options=None):
        """Возвращает все записи, соответствующие фильтрам."""
        if options is None:
            options = {}
        data = cls._read_csv()
        filtered = cls._filter_data(data, options)
        return [cls._row_to_dict(row) for row in filtered]

    @classmethod
    def find_by(cls, options):
        """Возвращает первую запись, соответствующую фильтрам."""
        results = cls.where(options)
        if not results:
            raise RecordNotFound
        return results[0]
