"""
Excel to CSV Converter for MQL Dashboard

This script converts Excel files to CSV format for use with the MQL dashboard.
It handles data cleaning and formatting to ensure compatibility.
"""

import pandas as pd
import os
import sys
from pathlib import Path


def convert_excel_to_csv(excel_file="New MQLs Dataset.xlsx", output_file="mql.csv"):
    """
    Convert Excel file to CSV format with proper data cleaning.
    
    Args:
        excel_file (str): Path to the Excel file
        output_file (str): Path for the output CSV file
    """
    try:
        print(f"📄 Reading Excel file: {excel_file}")
        
        # Read Excel file
        if os.path.exists(excel_file):
            df = pd.read_excel(excel_file)
            print(f"✅ Successfully loaded {len(df)} rows from Excel file")
        else:
            print(f"❌ Excel file '{excel_file}' not found")
            return False
        
        # Display basic info about the data
        print(f"📊 Data shape: {df.shape}")
        print(f"🗂️ Columns: {list(df.columns)}")
        
        # Clean column names
        df.columns = df.columns.str.strip()
        
        # Remove completely empty rows
        df = df.dropna(how='all')
        
        # Save to CSV
        df.to_csv(output_file, index=False)
        print(f"✅ Successfully converted to CSV: {output_file}")
        print(f"📈 Final data shape: {df.shape}")
        
        # Display first few rows
        print("\n🔍 First 3 rows of converted data:")
        print(df.head(3).to_string())
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting Excel to CSV: {str(e)}")
        return False


def check_csv_format(csv_file="mql.csv"):
    """
    Check if the CSV file has the expected format for the dashboard.
    
    Args:
        csv_file (str): Path to the CSV file to check
    """
    try:
        if not os.path.exists(csv_file):
            print(f"❌ CSV file '{csv_file}' not found")
            return False
            
        df = pd.read_csv(csv_file)
        
        print(f"\n🔍 CSV File Analysis for {csv_file}:")
        print(f"   📈 Shape: {df.shape}")
        print(f"   🗂️ Columns: {list(df.columns)}")
        
        # Check for expected columns
        expected_columns = [
            'deal id', 'deal owner', 'stage', 'date for the stage', 
            'mrr', 'create date'
        ]
        
        found_columns = []
        missing_columns = []
        
        for col in expected_columns:
            # Check for exact match or case-insensitive match
            matches = [c for c in df.columns if c.lower().strip() == col.lower()]
            if matches:
                found_columns.append(matches[0])
            else:
                missing_columns.append(col)
        
        print(f"   ✅ Found columns: {found_columns}")
        if missing_columns:
            print(f"   ⚠️ Missing columns: {missing_columns}")
        
        # Check data types and sample values
        print("\n📊 Data Summary:")
        for col in df.columns[:6]:  # Show first 6 columns
            non_null_count = df[col].count()
            sample_value = df[col].dropna().iloc[0] if non_null_count > 0 else "N/A"
            print(f"   {col}: {non_null_count}/{len(df)} non-null, Sample: '{sample_value}'")
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking CSV format: {str(e)}")
        return False


def main():
    """
    Main function to handle Excel to CSV conversion.
    """
    print("🚀 MQL Data Converter")
    print("=" * 50)
    
    # Check if Excel file exists
    excel_files = [
        "New MQLs Dataset.xlsx",
        "mql.xlsx", 
        "data.xlsx"
    ]
    
    excel_file = None
    for file in excel_files:
        if os.path.exists(file):
            excel_file = file
            break
    
    if excel_file:
        print(f"📄 Found Excel file: {excel_file}")
        success = convert_excel_to_csv(excel_file)
        
        if success:
            check_csv_format("mql.csv")
            print("\n✅ Conversion completed successfully!")
            print("📈 You can now run the dashboard with: streamlit run streamlit_dashboard.py")
        else:
            print("\n❌ Conversion failed. Please check the error messages above.")
            
    else:
        print("⚠️ No Excel file found. Looking for existing CSV...")
        
        if os.path.exists("mql.csv"):
            print("📄 Found existing mql.csv file")
            check_csv_format("mql.csv")
        else:
            print("❌ No data file found. Please ensure you have either:")
            print("   - New MQLs Dataset.xlsx")
            print("   - mql.xlsx")
            print("   - data.xlsx")
            print("   - mql.csv")
            sys.exit(1)
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
