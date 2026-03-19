const parseCsvSync = require('csv-parse/lib/sync');
const fs = require('fs');
const path = require('path');

const COLUMNS = Object.freeze({
  PERMALINK: 0,
  COMPANY_NAME: 1,
  NUMBER_EMPLOYEES: 2,
  CATEGORY: 3,
  CITY: 4,
  STATE: 5,
  FUNDED_DATE: 6,
  RAISED_AMOUNT: 7,
  RAISED_CURRENCY: 8,
  ROUND: 9,
});

function mapRow(row) {
  return {
    permalink: row[COLUMNS.PERMALINK],
    company_name: row[COLUMNS.COMPANY_NAME],
    number_employees: row[COLUMNS.NUMBER_EMPLOYEES],
    category: row[COLUMNS.CATEGORY],
    city: row[COLUMNS.CITY],
    state: row[COLUMNS.STATE],
    funded_date: row[COLUMNS.FUNDED_DATE],
    raised_amount: row[COLUMNS.RAISED_AMOUNT],
    raised_currency: row[COLUMNS.RAISED_CURRENCY],
    round: row[COLUMNS.ROUND],
  };
}

function applyFilters(data, options) {
  return data.filter(row => {
    if (options.company_name && options.company_name !== row[COLUMNS.COMPANY_NAME]) return false;
    if (options.city && options.city !== row[COLUMNS.CITY]) return false;
    if (options.state && options.state !== row[COLUMNS.STATE]) return false;
    if (options.round && options.round !== row[COLUMNS.ROUND]) return false;
    return true;
  });
}

class FundingRaised {
  static loadData() {
    const funding_file = 'startup_funding.csv';
    const file_data = fs.readFileSync(path.join(__dirname, '..', funding_file)).toString();
    return parseCsvSync(file_data);
  }

  static where(options = {}) {
    const csv_data = applyFilters(this.loadData(), options);
    return csv_data.map(mapRow);
  }

  static findBy(options = {}) {
    const csv_data = applyFilters(this.loadData(), options);
    const row = csv_data[0];
    return row ? mapRow(row) : null;
  }
}

module.exports = FundingRaised;
