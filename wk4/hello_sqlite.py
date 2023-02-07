# Import sqlite
import sqlite3

# Make a connection to the sqlite database
    # If DB does not exits it will be created, else will connect
conn = sqlite3.connect('first_db.sqlite')

# Run SQL queries
# conn.execute('CREATE TABLE products (id int, name text)')
    # If table already exits, but will duplicate data
conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')

    # Adding data to table
# conn.execute('INSERT INTO products values (1000, "hat")')
# conn.execute('INSERT INTO products values (2000, "socks")')
# conn.execute('INSERT INTO products values (500, "t-shirt")')
# conn.execute('INSERT INTO products values (2500, "shoes")')

# Make sure changes are saved
conn.commit()

# Read from DB
results = conn.execute('SELECT * FROM products')
# results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
first_row = results.fetchone()
print(first_row)

# Add new product to DB
new_id = int(input('enter new id: '))
new_name = input('enter new product: ')

# Adding new product using format string. NOT RECOMMENDED TO USE
    # Will crash program if double quotes or weird value
# conn.execute(f'INSERT INTO products VALUES ({new_id}, "{new_name}")')

    # Better solution: parameterized queries
        # will not crash with weird values
conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name))

conn.commit()

# Loop over results
for row in results:
    print(row)  # each row is a Tuple

# Updating a DB
updated_product = 'wool hat'
update_id = 1000
conn.execute('UPDATE products SET name = ? WHERE id = ?', (updated_product, update_id))
conn.commit()

# Delete from DB
delete_product = 'Helmet'
conn.execute('DELETE from PRODUCTS WHERE name = ?', (delete_product, )) # Must have comma after Tuple-(delete_product, ))
conn.commit()

# Close connection when done working with DB
conn.close()

