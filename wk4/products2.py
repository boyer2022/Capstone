# Error handling for DB
import sqlite3

# Validation errors, row id

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    # Uncomment first conn.execute... to see difference
    # conn.execute('CREATE TABLE IF NOT EXISTS products (name TEXT UNIQUE, quantity INT)')
        # Alternative way to create primary keys. No need to call product_id for INSERT statement- will be numbered for you
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT)')

conn.close()

name = 'Fleece Gloves'
# Run with 2 the first time
# name = 'scarf'
# quantity = 2
# Change value of quantity the second time. Comment out one or the other
quantity = 20

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (?,?)', (name, quantity))
    conn.close()
except Exception as e:
    print('Error inserting ', e)

# Query the DB with row id. Sets as primary keys
conn = sqlite3.connect(db)
results = conn.execute('SELECT rowid, * FROM products')
for row in results:
    print(row)

print ('End of program')
