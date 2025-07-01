#!/bin/bash

# MQL Dashboard Launcher Script
echo "🚀 Starting MQL Pipeline Dashboard..."
echo "📊 Make sure mql.csv is in the current directory"
echo "🌐 Dashboard will open in your browser automatically"
echo ""

# Install requirements if needed
echo "📦 Installing required packages..."
pip install -r requirements.txt

echo ""
echo "Transforming data to long format..."
python excel_to_csv.py

echo ""
echo "🎯 Launching Streamlit Dashboard..."
echo "🔗 Access the dashboard at: http://localhost:8501"
echo "⏹️  Press Ctrl+C to stop the dashboard"
echo ""

# Run the streamlit app
streamlit run streamlit_dashboard.py
