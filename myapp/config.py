import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()

### Private function to build the database connection string
def _build_database_uri() -> str:
    host = os.environ["DB_HOST"]
    port = os.environ.get("DB_PORT", "1433")
    database = os.environ["DB_NAME"]
    username = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    driver = os.environ.get(
        "DB_DRIVER",
        "ODBC Driver 18 for SQL Server"
    )
    encrypt = os.environ.get(
        "DB_ENCRYPT",
        "no"
    )
    trust_certificate = os.environ.get(
        "DB_TRUST_SERVER_CERTIFICATE",
        "no"
    )

    return (
        f"mssql+pyodbc://"
        f"{quote_plus(username)}:"
        f"{quote_plus(password)}@"
        f"{host}:{port}/"
        f"{database}"
        f"?driver={quote_plus(driver)}"
        f"&Encrypt={encrypt}"
        f"&TrustServerCertificate={trust_certificate}"
    )

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = _build_database_uri()