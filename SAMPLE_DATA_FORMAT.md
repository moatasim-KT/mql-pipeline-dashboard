# Sample MQL Data Structure

This file shows the expected structure for your MQL data. Your `mql.csv` file should contain columns similar to these:

## Required Columns

### Core Fields
- **Deal ID**: Unique identifier for each deal
- **Deal Owner**: Sales representative responsible for the deal
- **Stage**: Current pipeline stage (must match predefined stage order)
- **Date for the Stage**: Date when the deal entered current stage
- **MRR**: Monthly Recurring Revenue value
- **Create Date**: Original deal creation date

### Optional Fields
- **Deal Stage**: Alternative stage field
- **Entry/Exit**: Stage transition tracking
- **Est MRR ($)**: Estimated MRR if different from MRR

## Sample Data Format

```csv
Deal ID,Deal Owner,Stage,Date for the Stage,MRR,Create Date
DEAL-001,John Smith,B. MQL (Sales Pipeline),2024-01-15,$5000,2024-01-10
DEAL-002,Jane Doe,3. Middle / Validation (Sales Pipeline),2024-01-20,$12000,2024-01-05
DEAL-003,Mike Johnson,1. RFP (Sales Pipeline),2024-01-25,$8500,2024-01-12
DEAL-004,Sarah Wilson,5. Closed Won (Sales Pipeline),2024-01-30,$15000,2024-01-08
DEAL-005,Tom Brown,C. Pre-Pipeline (Sales Pipeline),2024-02-01,$3000,2024-01-28
```

## Data Preparation Tips

### Excel to CSV Conversion
If you have Excel files, use the provided conversion script:
```bash
python excel_to_csv.py
```

### Date Formats
Accepted date formats:
- `YYYY-MM-DD` (2024-01-15)
- `MM/DD/YYYY` (01/15/2024)
- `DD/MM/YYYY` (15/01/2024)
- `MM-DD-YYYY` (01-15-2024)

### MRR Formats
Accepted MRR formats:
- `$5000` or `$5,000`
- `5000` (numeric)
- `5000.00`
- Mixed currency symbols are cleaned automatically

### Stage Names
Ensure your stage names match the predefined order in the dashboard:

1. A. Marketing Engaged
2. B. MQL (Sales Pipeline)
3. C. Pre-Pipeline (Sales Pipeline)
4. 1. RFP (Sales Pipeline)
5. 2. Early / Opportunity (Sales Pipeline)
6. 3. Middle / Validation (Sales Pipeline)
7. 4. Late / Negotiation (Sales Pipeline)
8. 5. Close Won - No Effort (Sales Pipeline)
9. 5. Closed Lost (Sales Pipeline)
10. 5. Closed Won (Sales Pipeline)
11. Downgrade (Sales Pipeline)
12. Re-Subscribe (Sales Pipeline)
13. Subscription Cancelled (Sales Pipeline)
14. Upgrade (Sales Pipeline)

## Data Quality Checklist

- [ ] All required columns are present
- [ ] Date fields are in recognizable format
- [ ] MRR values are numeric or properly formatted
- [ ] Stage names match predefined order
- [ ] No completely empty rows
- [ ] Deal IDs are unique
- [ ] Owner names are consistent (no typos)

## Common Data Issues

### Missing Data
- Empty cells are handled automatically
- Missing dates will prevent time-series analysis
- Missing MRR values are treated as $0

### Inconsistent Naming
- Owner names with typos create separate entries
- Stage names must match exactly (case-sensitive)
- Column names are cleaned automatically

### Date Problems
- Invalid dates are ignored in time-series
- Mixed date formats may cause parsing issues
- Future dates are included but may skew analysis

## Getting Your Data Ready

1. **Export from your CRM** in Excel or CSV format
2. **Check column names** match expected format
3. **Verify stage names** against the predefined list
4. **Clean MRR values** remove any text or special formatting
5. **Standardize date format** to YYYY-MM-DD if possible
6. **Save as `mql.csv`** in the dashboard directory
7. **Run the dashboard** and check for any error messages

If you encounter issues, check the Dashboard Logic Documentation for detailed troubleshooting steps.
