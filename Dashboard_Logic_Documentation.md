# MQL Pipeline Dashboard - Logic and Visualization Documentation

## Table of Contents
1. [Overview](#overview)
2. [Data Loading and Preprocessing](#data-loading-and-preprocessing)
3. [Stage Ordering Logic](#stage-ordering-logic)
4. [Filtering System](#filtering-system)
5. [Key Metrics Calculations](#key-metrics-calculations)
6. [Visualization Logic](#visualization-logic)
7. [Data Transformations](#data-transformations)
8. [Alert System](#alert-system)
9. [Export Functionality](#export-functionality)
10. [Making Changes](#making-changes)

## Overview

The MQL (Marketing Qualified Lead) Pipeline Dashboard is a comprehensive Streamlit application designed to analyze and visualize sales pipeline data. It provides insights into deal progression, performance metrics, time trends, and conversion rates across different stages of the sales funnel.

## Data Loading and Preprocessing

### File Loading (`load_data()` function)
The dashboard expects a CSV file named `mql.csv` in the same directory. The preprocessing steps include:

#### 1. Column Name Standardization
```python
# Clean column names - convert to lowercase and strip whitespace
df.columns = df.columns.str.strip().str.lower()

# Map expected column names to standardized names
column_mapping = {
    "deal id": "deal_id",
    "deal owner": "deal_owner", 
    "stage": "stage",
    "date for the stage": "date",
    "mrr": "mrr",
    "est mrr ($)": "est_mrr",
    "create date": "create_date",
    "deal stage": "deal_stage",
    "entry/exit": "entry_exit",
}
```

**Purpose**: Ensures consistent column naming regardless of how the source data is formatted.

#### 2. Date Processing
```python
# Primary date field processing
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year_month"] = df["date"].dt.to_period("M")

# Backup date processing
if "create_date" in df.columns:
    df["create_date"] = pd.to_datetime(df["create_date"], errors="coerce")
    # Use create_date as fallback if main date is missing
    if "date" not in df.columns or df["date"].isna().all():
        df["date"] = df["create_date"]
        df["year_month"] = df["date"].dt.to_period("M")
```

**Purpose**: 
- Converts date strings to datetime objects for time-series analysis
- Creates monthly periods for aggregation
- Provides fallback date handling if primary date field is missing

#### 3. MRR (Monthly Recurring Revenue) Cleaning
```python
def clean_mrr_value(x):
    if pd.isna(x) or str(x).strip() == "":
        return 0.0
    str_val = str(x).replace("$", "").replace(",", "")
    first_part = str_val.split("$")[0]
    try:
        return float(first_part) if first_part else 0.0
    except (ValueError, TypeError):
        return 0.0

df["clean_mrr"] = df["mrr"].apply(clean_mrr_value)
```

**Purpose**: 
- Removes currency symbols and formatting
- Handles missing or invalid values
- Converts to numeric format for calculations

## Stage Ordering Logic

### Predefined Stage Order
```python
STAGE_ORDER = [
    "A. Marketing Engaged",
    "B. MQL (Sales Pipeline)",
    "C. Pre-Pipeline (Sales Pipeline)",
    "1. RFP (Sales Pipeline)",
    "2. Early / Opportunity (Sales Pipeline)",
    "3. Middle / Validation (Sales Pipeline)",
    "4. Late / Negotiation (Sales Pipeline)",
    "5. Close Won - No Effort (Sales Pipeline)",
    "5. Closed Lost (Sales Pipeline)",
    "5. Closed Won (Sales Pipeline)",
    "Downgrade (Sales Pipeline)",
    "Re-Subscribe (Sales Pipeline)",
    "Subscription Cancelled (Sales Pipeline)",
    "Upgrade (Sales Pipeline)",
]
```

### Stage Ordering Functions

#### `apply_stage_ordering(df)`
```python
def apply_stage_ordering(df):
    if "stage" in df.columns:
        df["stage"] = pd.Categorical(df["stage"], categories=STAGE_ORDER, ordered=True)
    return df
```

**Purpose**: Converts the stage column to a categorical type with proper ordering for consistent visualization sorting.

#### `get_ordered_stages(df)`
```python
def get_ordered_stages(df):
    if "stage" not in df.columns:
        return []
    existing_stages = df["stage"].dropna().unique()
    ordered_stages = [stage for stage in STAGE_ORDER if stage in existing_stages]
    return ordered_stages
```

**Purpose**: Returns only the stages that exist in the data, in the correct predefined order.

## Filtering System

### Filter Creation (`create_sidebar_filters()`)

#### 1. Date Range Filter
- Uses the earliest and latest dates in the dataset as default range
- Allows users to narrow down analysis to specific time periods

#### 2. Stage Filter
- Multiselect dropdown with all existing stages
- Defaults to all stages selected
- Uses ordered stages for consistent presentation

#### 3. Deal Owner Filter
- Multiselect dropdown with all unique deal owners
- Limits to first 10 owners by default if more than 10 exist
- Prevents overwhelming UI with too many options

#### 4. MRR Range Filter
- Slider control for minimum and maximum MRR values
- Uses actual data range as bounds
- Allows filtering out very small or very large deals

### Filter Application (`filter_data()`)
Sequentially applies each filter to the dataset:
1. Date range filtering
2. Stage filtering  
3. Owner filtering
4. MRR range filtering

## Key Metrics Calculations

### `display_key_metrics(df)`

#### 1. Total Deals
```python
total_deals = len(df)
```
**Logic**: Simple count of all rows (deals) in the filtered dataset.

#### 2. Pipeline Value
```python
total_pipeline = df["clean_mrr"].sum()
```
**Logic**: Sum of all MRR values across all deals in the pipeline.

#### 3. Average Deal Size
```python
avg_deal_size = df["clean_mrr"].mean()
```
**Logic**: Mean MRR value across all deals.

#### 4. Active Stages
```python
active_stages = df["stage"].nunique()
```
**Logic**: Count of unique stages present in the filtered data.

## Visualization Logic

### 1. Pipeline Overview (`create_pipeline_overview()`)

#### Deals by Stage (Horizontal Bar Chart)
```python
stage_counts = df["stage"].value_counts()
ordered_stages = get_ordered_stages(df)
stage_counts = stage_counts.reindex([s for s in ordered_stages if s in stage_counts.index])
```

**Logic**: 
- Counts deals in each stage
- Reorders according to predefined stage order
- Shows distribution of deals across pipeline stages

#### Pipeline Distribution (Pie Chart)
```python
stage_mrr = df.groupby("stage")["clean_mrr"].sum()
```

**Logic**:
- Groups deals by stage and sums MRR values
- Shows monetary value distribution across stages
- Helps identify where most value is concentrated

### 2. Time Series Analysis (`create_time_series_analysis()`)

#### Monthly Deal Volume
```python
monthly_deals = df.groupby(df["date"].dt.to_period("M")).size()
```

**Logic**: Groups deals by month and counts occurrences to show deal volume trends over time.

#### Monthly MRR Trend
```python
monthly_mrr = df.groupby(df["date"].dt.to_period("M"))["clean_mrr"].sum()
```

**Logic**: Groups deals by month and sums MRR to show revenue trends over time.

#### Deals by Stage Over Time
```python
monthly_stage_deals = df.groupby([df["date"].dt.to_period("M"), "stage"]).size().reset_index()
```

**Logic**: 
- Two-level grouping: first by month, then by stage
- Shows how different stages perform over time
- Enables both stacked bar and line chart visualizations

#### MRR by Stage Over Time
```python
monthly_stage_mrr = df.groupby([df["date"].dt.to_period("M"), "stage"])["clean_mrr"].sum().reset_index()
```

**Logic**: Similar to deal counts but focuses on monetary value progression by stage over time.

#### Monthly Summary Statistics
```python
monthly_totals = df.groupby(df["date"].dt.to_period("M")).agg({
    "deal_id": "nunique", 
    "clean_mrr": "sum"
}).round(2)

monthly_totals["MRR Growth %"] = monthly_totals["Total MRR"].pct_change() * 100
monthly_totals["Deal Growth %"] = monthly_totals["Total Deals"].pct_change() * 100
```

**Logic**:
- Aggregates monthly totals
- Calculates month-over-month growth percentages
- Provides quantitative growth metrics

### 3. Performance Analysis (`create_performance_analysis()`)

#### Owner Performance Metrics
```python
owner_performance = df.groupby("deal_owner").agg({
    "deal_id": "nunique",
    "clean_mrr": ["sum", "mean"]
}).round(2)
```

**Logic**:
- Groups by deal owner
- Calculates total deals, total MRR, and average MRR per owner
- Identifies top performers and deal size patterns

#### Scatter Plot Analysis
- X-axis: Number of deals (volume)
- Y-axis: Average deal size (efficiency)
- Size: Total MRR (overall performance)

**Purpose**: Identifies different performance patterns:
- High volume, low average: Many small deals
- Low volume, high average: Few large deals
- High volume, high average: Top performers

### 4. Funnel Analysis (`create_funnel_analysis()`)

#### Funnel Visualization
```python
stage_counts = df["stage"].value_counts()
ordered_stage_counts = []
for stage in ordered_stages:
    if stage in stage_counts.index:
        ordered_stage_counts.append(stage_counts[stage])
```

**Logic**: 
- Uses predefined stage order to show pipeline progression
- Each stage shows how many deals remain
- Visualizes drop-off between stages

#### Conversion Rate Calculation
```python
for i in range(len(ordered_stage_counts) - 1):
    conversion_rate = (ordered_stage_counts[i + 1] / ordered_stage_counts[i]) * 100
```

**Logic**:
- Calculates percentage of deals that move from one stage to the next
- Identifies bottlenecks in the sales process
- Shows stage-to-stage conversion efficiency

## Data Transformations

### Categorical Ordering
All stage-related visualizations use pandas Categorical data type to ensure consistent ordering:
```python
df["stage"] = pd.Categorical(df["stage"], categories=STAGE_ORDER, ordered=True)
```

### Period Conversion
Date fields are converted to periods for time-series aggregation:
```python
df["year_month"] = df["date"].dt.to_period("M")
```

### Aggregation Patterns
The dashboard uses several aggregation patterns:

1. **Count Aggregation**: `df.groupby("column").size()`
2. **Sum Aggregation**: `df.groupby("column")["mrr"].sum()`
3. **Multiple Aggregation**: `df.groupby("column").agg({"col1": "sum", "col2": "mean"})`
4. **Multi-level Grouping**: `df.groupby([df["date"].dt.to_period("M"), "stage"])`

## Alert System

### `create_alerts_monitoring(df)`

#### Low Pipeline Value Alert
```python
if total_pipeline < 50000:
    alerts.append(f"🚨 Low Pipeline Value: ${total_pipeline:,.0f} (Threshold: $50,000)")
```

#### High Deal Concentration Alert
```python
top_owner_percentage = (owner_counts.iloc[0] / len(df)) * 100
if top_owner_percentage > 50:
    alerts.append(f"⚠️ High Deal Concentration: {top_owner_percentage:.1f}% with single owner")
```

#### Low Recent Activity Alert
```python
recent_deals = df[df["date"] >= (datetime.now() - timedelta(days=30))]
if len(recent_deals) < 10:
    alerts.append(f"📉 Low Recent Activity: Only {len(recent_deals)} deals in last 30 days")
```

**Purpose**: Provides automated monitoring of key business metrics and potential issues.

## Export Functionality

### Filtered Data Export
Exports the current filtered dataset as CSV with timestamp.

### Performance Report Export
Exports owner performance metrics as a separate CSV file.

**Logic**: Uses pandas `to_csv()` method with Streamlit's download button functionality.

## Making Changes

### Adding New Visualizations

1. **Create a new function** following the naming pattern `create_[visualization_name](df)`
2. **Add data validation** at the beginning to check for required columns
3. **Apply stage ordering** if the visualization involves stages
4. **Use consistent styling** with plotly color schemes
5. **Add the visualization** to an appropriate tab in the main function

### Modifying Stage Order

1. **Update the STAGE_ORDER list** at the top of the file
2. **Test with your data** to ensure all stages are represented
3. **Verify funnel analysis** still works correctly

### Adding New Filters

1. **Add filter creation** in `create_sidebar_filters()`
2. **Add filter application** in `filter_data()`
3. **Test with edge cases** (empty selections, no data matching filter)

### Modifying Data Preprocessing

1. **Update column mapping** in `load_data()` if source data structure changes
2. **Add new cleaning functions** for additional data types
3. **Update the clean_mrr_value function** if MRR format changes

### Adding New Metrics

1. **Add calculation** in `display_key_metrics()`
2. **Handle missing data** gracefully
3. **Format appropriately** (currency, percentages, etc.)

### Error Handling Guidelines

- Always check if required columns exist before processing
- Use `pd.isna()` and `.dropna()` for missing data handling
- Provide informative error messages to users
- Use try-except blocks for data conversion operations

### Performance Considerations

- Use `@st.cache_data` decorator for expensive operations
- Limit data size in visualizations (e.g., top 10 performers)
- Consider pagination for large datasets
- Use efficient pandas operations (vectorized operations over loops)

## Troubleshooting Common Issues

### Data Not Loading
- Check if `mql.csv` exists in the correct directory
- Verify column names match expected mapping
- Check for special characters in data

### Visualizations Not Showing
- Verify required columns exist in the data
- Check if filters are too restrictive
- Ensure data types are correct (dates, numbers)

### Performance Issues
- Reduce date range in filters
- Limit number of selected owners
- Check for very large datasets

### Incorrect Stage Ordering
- Verify STAGE_ORDER list includes all stages in your data
- Check for typos or case sensitivity issues
- Ensure `apply_stage_ordering()` is called before visualizations

This documentation provides a comprehensive understanding of the dashboard's logic and should enable anyone to maintain, modify, or extend the functionality as needed.