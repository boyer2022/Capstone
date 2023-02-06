# Import sqlite
import sqlite3

# Make a connection to the sqlite database
    # If DB does not exits it will be created, else will connect
conn = sqlite3.connect('first_db.sqlite')

# Run SQL queries
conn.execute('CREATE TABLE products (id int, name text)')
    # If table already exits, but will duplicate data
# conn.execute('CREATE TABLE IF NOT EXITS products (id int, name text)')

    # Adding data to table
conn.execute('INSERT INTO products values (1000, "hat")')
conn.execute('INSERT INTO products values (2000, "socks")')
conn.execute('INSERT INTO products values (500, "t-shirt")')
conn.execute('INSERT INTO products values (2500, "shoes")')

# Make sure changes are saved
conn.commit()

# Read from DB
results = conn.execute('SELECT * FROM products')

# Loop over results
for row in results:
    print(row)  # each row is a Tuple

# Close connection when done working with DB
conn.close()

