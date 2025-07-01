# 📊 MQL Pipeline Dashboard

A comprehensive interactive Streamlit dashboard for Marketing Qualified Lead (MQL) pipeline analysis with data visualization, performance metrics, and business intelligence features.

## 🌟 Features

- **Interactive Pipeline Analysis**: Real-time filtering and visualization of sales pipeline data
- **Time Series Analysis**: Track deals and revenue trends over time with monthly aggregations
- **Performance Metrics**: Individual and team performance analysis with detailed breakdowns
- **Sales Funnel Visualization**: Conversion rate analysis and bottleneck identification
- **Automated Alerts**: Business intelligence monitoring with customizable thresholds
- **Data Export**: Export filtered data and performance reports
- **Responsive Design**: Professional UI with gradient styling and intuitive navigation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/moatasim-KT/mql-pipeline-dashboard.git
   cd mql-pipeline-dashboard
   ```

2. **Make the launcher script executable:**
   ```bash
   chmod +x run_dashboard.sh
   ```

3. **Run the dashboard:**
   ```bash
   ./run_dashboard.sh
   ```

The script will automatically:
- Install required Python packages
- Process your data file
- Launch the Streamlit dashboard
- Open your browser to `http://localhost:8501`

### Manual Installation

If you prefer manual setup:

```bash
# Install dependencies
pip install -r requirements.txt

# Process data (if you have Excel files)
python excel_to_csv.py

# Launch dashboard
streamlit run streamlit_dashboard.py
```

## 📊 Data Requirements

### Required CSV Format

Place your data file as `mql.csv` in the project root. The expected columns are:

| Column Name | Description | Example |
|-------------|-------------|----------|
| `Deal ID` | Unique deal identifier | "DEAL-001" |
| `Deal Owner` | Sales representative | "John Smith" |
| `Stage` | Current pipeline stage | "B. MQL (Sales Pipeline)" |
| `Date for the Stage` | Stage entry date | "2024-01-15" |
| `MRR` | Monthly Recurring Revenue | "$5,000" |
| `Create Date` | Deal creation date | "2024-01-10" |

### Supported Stage Order

The dashboard recognizes these predefined stages in order:

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

## 🛠️ Dashboard Sections

### 1. 📊 Pipeline Overview
- Deal distribution across stages
- MRR distribution visualization
- Key performance indicators

### 2. 📈 Time Series Analysis
- Monthly deal volume trends
- Revenue progression over time
- Stage-specific temporal analysis
- Growth rate calculations

### 3. 🏆 Performance Analysis
- Individual sales rep performance
- Deal volume vs. deal size analysis
- Top performer identification
- Performance benchmarking

### 4. 🔄 Funnel Analysis
- Sales pipeline visualization
- Stage-to-stage conversion rates
- Bottleneck identification
- Drop-off analysis

### 5. 🚨 Alerts & Monitoring
- Pipeline value monitoring
- Deal concentration alerts
- Activity level warnings
- Automated threshold checking

### 6. 📥 Export Functionality
- Filtered data export
- Performance report generation
- CSV download capabilities

## 🎯 Filtering Options

### Available Filters

- **Date Range**: Filter by specific time periods
- **Pipeline Stages**: Select specific stages for analysis
- **Deal Owners**: Focus on individual or team performance
- **MRR Range**: Filter by deal size thresholds

### Real-time Updates

All visualizations and metrics update automatically when filters are applied, providing instant insights into your filtered dataset.

## 📊 Key Metrics

### Core KPIs

- **Total Deals**: Count of deals in filtered dataset
- **Pipeline Value**: Sum of all MRR values
- **Average Deal Size**: Mean MRR per deal
- **Active Stages**: Number of unique pipeline stages
- **Conversion Rates**: Stage-to-stage progression percentages
- **Growth Rates**: Month-over-month change calculations

## 🔧 Customization

### Modifying Stage Order

Edit the `STAGE_ORDER` list in `streamlit_dashboard.py`:

```python
STAGE_ORDER = [
    "Your Custom Stage 1",
    "Your Custom Stage 2",
    # Add your stages here
]
```

### Adding New Visualizations

1. Create a new function following the pattern `create_[name](df)`
2. Add data validation and error handling
3. Apply consistent styling with plotly
4. Add to the appropriate tab in the main function

### Customizing Alerts

Modify thresholds in `create_alerts_monitoring()`:

```python
# Example: Change pipeline value threshold
if total_pipeline < 100000:  # Change from 50000 to 100000
    alerts.append(f"Low Pipeline Value: ${total_pipeline:,.0f}")
```

## 📚 Documentation

For detailed technical documentation, see:
- **[Dashboard Logic Documentation](Dashboard_Logic_Documentation.md)**: Complete explanation of all visualizations and data transformations

## 🔍 Troubleshooting

### Common Issues

**Dashboard won't start:**
- Ensure Python 3.8+ is installed
- Check that `mql.csv` exists in the project directory
- Verify all requirements are installed: `pip install -r requirements.txt`

**Data not loading:**
- Verify CSV file format matches expected columns
- Check for special characters or encoding issues
- Ensure date formats are readable by pandas

**Visualizations missing:**
- Check if required columns exist in your data
- Verify filters aren't too restrictive
- Ensure stage names match the predefined order

### Performance Optimization

- Use date range filters to limit dataset size
- Reduce the number of selected deal owners for large datasets
- Consider data aggregation for very large files

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

### Development Guidelines

- Follow existing code style and structure
- Add docstrings to new functions
- Include error handling for edge cases
- Test with various data formats
- Update documentation for new features

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

For questions or support:
- GitHub: [@moatasim-KT](https://github.com/moatasim-KT)
- Issues: [GitHub Issues](https://github.com/moatasim-KT/mql-pipeline-dashboard/issues)

## 🚀 Roadmap

### Upcoming Features

- [ ] Advanced forecasting capabilities
- [ ] Email alert notifications
- [ ] Integration with CRM systems
- [ ] Custom dashboard themes
- [ ] Real-time data connections
- [ ] Machine learning insights
- [ ] Mobile responsive design improvements

---

**Built with ❤️ using Streamlit, Plotly, and Pandas**