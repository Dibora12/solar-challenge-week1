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

📁## 📁 Project Structure
```
solar-data_discovery/
├── notebooks/         # Jupyter notebooks (EDA & visualizations)
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── figures/
├── app/               # Streamlit dashboard code
│   ├── main.py
│   └── utils.py
├── data/              # Raw and cleaned CSVs (local, not committed)
├── .github/
│   └── workflows/
│       └── ci.yml     # CI/CD pipeline config
├── scripts/           # Utility scripts
├── src/               # Core processing logic
├── tests/             # Unit and integration tests
└── requirements.txt   # Project dependencies
```
## 🧪 Running the Analysis

Open notebooks:
```
jupyter notebook notebooks/
```
View visualizations:
   - Located in notebooks/figures/
