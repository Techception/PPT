import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

engine = create_engine('sqlite:///practice.db')

"""
with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM user'))
    print(result.fetchone())
"""

df = pd.read_sql('SELECT * FROM user',engine)
print(df)
