# Import sqlite
import sqlite3

# Creating a global variable for context manager
db = 'second_db.sqlite'
# Create table function
def create_table():
    # Make a connection to the sqlite database
        # If DB does not exits it will be created, else will connect
        # Create context manager
            # No longer need to add conn.commit()
    with sqlite3.connect(db) as conn:
        # Run SQL queries
        # conn.execute('CREATE TABLE products (id int, name text)')
            # If table already exits, but will duplicate data
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    conn.close()    # Closing the function


# Insert example data Function
def insert_example_data():
    with sqlite3.connect(db) as conn:
                # Adding data to table
        conn.execute('INSERT INTO products values (1000, "hat")')
        conn.execute('INSERT INTO products values (2000, "socks")')
        conn.execute('INSERT INTO products values (500, "t-shirt")')
        conn.execute('INSERT INTO products values (2500, "shoes")')
    conn.close()

# Display all data function
def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')
    print('All products: ')
    # Read from DB
     # Loop over results
    for row in results:
        print(row)  # each row is a Tuple
    conn.close()

def display_one_product(product_name):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products WHERE name like ?', (product_name,))
    first_row = results.fetchone()
    if first_row:
        print('Your product is: ', first_row)
    else:
        print('Product not found.')
    conn.close()

# Create new product function
def create_new_product():
    # Add new product to DB
    new_id = int(input('Enter new id: '))
    new_name = input('Enter new product: ')
    with sqlite3.connect(db) as conn:
        # Adding new product using format string. NOT RECOMMENDED TO USE
            # Will crash program if double quotes or weird value
        # conn.execute(f'INSERT INTO products VALUES ({new_id}, "{new_name}")')

            # Better solution: parameterized queries
                # will not crash with weird values
        conn.execute(f'INSERT INTO products VALUES (?, ?)', (new_id, new_name))
    conn.close()    

def update_product():
    # Updating a DB
    updated_product = 'wool hat'
    update_id = 1000
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ?', (updated_product, update_id))
    conn.close()

def delete_product(product_name):
    # Delete from DB
    #delete_product = 'Helmet'
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from PRODUCTS WHERE name = ?', (product_name, )) # Must have comma after Tuple-(delete_product, ))
    conn.close()
  
# Close connection when done working with DB



# Functions to be created
    # Function calls
create_table()
insert_example_data()
display_all_data()
display_one_product('jacket')
display_one_product('coat')
create_new_product()
update_product()
delete_product('jacket')
display_all_data()


