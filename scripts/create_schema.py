import sqlite3
import pandas as pd
#print(sqlite3.sqlite_version)
conn = sqlite3.connect("C:/Users/vnaga/MUTUALFUND_ETL/data/warehouse/mutualfund.db")
cursor = conn.cursor()

with open("C:/Users/vnaga/MUTUALFUND_ETL/sql/schema.sql", "r") as f:
     content = f.read()
     #print("StarSchema Content:",content)
     cursor.executescript(f.read())
print("Star schema sql created successfully,Which contains all sql query of tables!")

#To see the all tables name
cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(table[0])
print("Database and tables created successfully.")
#to see the struture of dim_fund table
query = "PRAGMA table_info(dim_fund);"

df = pd.read_sql_query(query, conn)

print(df)
conn.commit()
conn.close()