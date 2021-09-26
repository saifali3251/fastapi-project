import os
from pathlib import Path
from dotenv import load_dotenv
#from jose.constants import ALGORITHMS

env_path = Path('.') / '.env'
'''Above line : Python search for .env file and uses its key value pair'''
load_dotenv(dotenv_path=env_path)
'''This file is created for configuration of all variables in the project'''
class Settings:
  PROJECT_TITLE : str = "Jobboard"
  PROJECT_VERSION : str = "0.1.0"

  POSTGRES_USER : str = os.getenv("POSTGRES_USER")
  POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
  POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "localhost")
  POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) #default port 5432
  POSTGRES_DB : str = os.getenv("POSTGRES_DB","db_course")
  DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

  #SECRET_KEY : str =os.getenv("SECRET_KEY")
  #ALGORITHM = "HS256"
  #ACCESS_TOKEN_EXPIRE_MINUTES = 30



settings = Settings()