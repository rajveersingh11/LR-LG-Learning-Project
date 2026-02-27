# LR + LG Learning Project

This project is a simple machine-learning practice setup with:
- Linear Regression (`lr.py`) on insurance data
- Logistic Regression (`lg.py`) on a toy COVID dataset
- MySQL data loading (`mysql_db.py`)
- Flask prediction API (`app.py`)

## Project Structure

```text
lrlg/
|- app.py                 # Flask API for predictions using insurance_model.pkl
|- lr.py                  # Trains Linear Regression pipeline and saves insurance_model.pkl
|- lg.py                  # Trains Logistic Regression model and saves covid_model.pkl
|- mysql_db.py            # Loads insurance.csv into MySQL table `insurance`
|- insurance.csv          # Dataset for Linear Regression
|- covid_toy.csv          # Dataset for Logistic Regression
|- insurance_model.pkl    # Saved model from lr.py
|- covid_model.pkl        # Saved model from lg.py
|- requirements.txt       # Python dependencies
|- pyproject.toml         # Project metadata and dependencies
|- .env                   # MySQL connection variables
|- README.md              # Project documentation
```

## What Each Script Does

### 1) `mysql_db.py`
- Reads `insurance.csv`
- Connects to MySQL using `.env` values
- Writes data into table `insurance`

### 2) `lr.py`
- Reads insurance data from MySQL table `insurance`
- Applies preprocessing:
  - Numeric columns: scaling (`StandardScaler`)
  - Categorical columns: one-hot encoding (`OneHotEncoder`)
- Trains a `LinearRegression` model in a `Pipeline`
- Prints transformed shape, predictions, and R2 score
- Saves model as `insurance_model.pkl`

### 3) `lg.py`
- Reads `covid_toy.csv`
- Fills missing values in `fever` with mean
- Label-encodes categorical columns
- Trains `LogisticRegression`
- Prints accuracy
- Saves model as `covid_model.pkl`

### 4) `app.py`
- Loads `insurance_model.pkl`
- Exposes POST endpoint: `/predict`
- Accepts JSON input and returns prediction

## Setup

### 1) Create and activate virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
pip install -r requirements.txt
```

## Environment Variables (`.env`)

Set these values in `.env`:

```env
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=your_database_name
```

## Run Order (Recommended)

1. Load CSV into MySQL:

```powershell
python mysql_db.py
```

2. Train linear regression model:

```powershell
python lr.py
```

3. (Optional) Train logistic regression model:

```powershell
python lg.py
```

4. Start Flask API:

```powershell
python app.py
```

## API Usage

Endpoint:
- `POST http://127.0.0.1:5000/predict`

Example request body:

```json
{
  "input": [25, 0, 22.0, 1, 0, 2]
}
```

Example response:

```json
{
  "prediction": 12345
}
```

## Notes

- This is a learning project; scripts are intentionally simple.
- A few files currently use absolute Windows paths. For portability, prefer relative paths.
- `lg.py` currently imports `engine` from `mysql_db.py` but does not use it.
