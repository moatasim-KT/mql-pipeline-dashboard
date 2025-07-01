#!/bin/bash

# Network Dashboard Launcher Script (Alternative)
echo "🌐 Starting MQL Pipeline Dashboard on Network Interface..."
echo "📊 Make sure mql.csv is in the current directory"
echo "🔗 Dashboard will be accessible from other devices on your network"
echo ""

# Install requirements if needed
echo "📦 Installing required packages..."
pip install -r requirements.txt

echo ""
echo "Transforming data to long format..."
python excel_to_csv.py

echo ""
echo "🎯 Launching Streamlit Dashboard on Network..."
echo "🔗 Access the dashboard at: http://YOUR_IP:8501"
echo "⚠️  Make sure your firewall allows connections on port 8501"
echo "⏹️  Press Ctrl+C to stop the dashboard"
echo ""

# Get local IP address
if command -v hostname &> /dev/null; then
    LOCAL_IP=$(hostname -I | awk '{print $1}')
    echo "🌐 Local IP Address: $LOCAL_IP"
    echo "🔗 Network URL: http://$LOCAL_IP:8501"
fi

echo ""

# Run the streamlit app with network access
streamlit run streamlit_dashboard.py --server.address=0.0.0.0
