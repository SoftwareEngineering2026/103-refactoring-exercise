const parseCsvSync = require('csv-parse/lib/sync');
const fs = require('fs');
const path = require('path');

function mapRow(row) {
  return {
    permalink: row[0],
    company_name: row[1],
    number_employees: row[2],
    category: row[3],
    city: row[4],
    state: row[5],
    funded_date: row[6],
    raised_amount: row[7],
    raised_currency: row[8],
    round: row[9],
  };
}

function applyFilters(data, options) {
  return data.filter((row) => {
    if (options.company_name && options.company_name !== row[1]) return false;
    if (options.city && options.city !== row[4]) return false;
    if (options.state && options.state !== row[5]) return false;
    if (options.round && options.round !== row[9]) return false;
    return true;
  });
}

class FundingRaised {
  static where(options = {}) {
    const funding_file = 'startup_funding.csv';
    const file_data = fs.readFileSync(path.join(__dirname, '..', funding_file)).toString();
    let csv_data = parseCsvSync(file_data);

    const funding_data = [];

    csv_data = applyFilters(csv_data, options);
    
    csv_data.forEach((row) => {
      funding_data.push(mapRow(row));
    });

    return funding_data;
  }

  static findBy(options = {}) {
    const funding_file = 'startup_funding.csv';
    const file_data = fs.readFileSync(path.join(__dirname, '..', funding_file)).toString();
    const csv_data = applyFilters(parseCsvSync(file_data), options);
   
    const row = csv_data[0];
    return row ? mapRow(row) : null;
  }
}

module.exports = FundingRaised;
