import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

# Load CSV
df = pd.read_csv("C:\\Users\\rajve\\OneDrive\\Desktop\\lrlg\\insurance.csv")

# Push to MySQL
df.to_sql(
    name="insurance",
    con=engine,
    if_exists="replace",
    index=False
)



print("CSV uploaded successfully to MySQL database!")