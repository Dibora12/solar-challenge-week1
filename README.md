# Solar Challenge - Week 1

## 🌱 Setup Instructions

1. Clone the repository:
   ```bash
   cd solar-challenge-week1
   git clone https://github.com/Dibora12/solar-challenge_week1.git
cd solar-challenge_week1
python -m venv .venv

# Activate the virtual environment
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

📁 Project Structure

solar-data_discovery/
├── notebooks/           # EDA notebooks for each country
├── app/                 # Streamlit dashboard code
├── data/                # Local storage for CSVs (not committed to Git)
├── .github/workflows/   # CI/CD pipeline configuration
├── scripts/             # Utility scripts
├── src/                 # Source code
└── tests/               # Test files
