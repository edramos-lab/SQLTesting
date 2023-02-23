import pytest
import sqlite3

@pytest.fixture(scope="module")
def test_db():
    # create a test database
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()

    # create a customers table
    c.execute("CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, order_status TEXT)")

    # insert some test data
    c.execute("INSERT INTO customers (id, name, order_status) VALUES (1, 'Alice', 'pending')")
    c.execute("INSERT INTO customers (id, name, order_status) VALUES (2, 'Bob', 'completed')")
    c.execute("INSERT INTO customers (id, name, order_status) VALUES (3, 'Charlie', 'pending')")

    conn.commit()
    yield conn

    # close the database connection
    conn.close()
def test_get_customers_by_order_status(test_db):
    # execute the SQL script
    cursor = test_db.cursor()
    #cursor.execute("SELECT * FROM customers WHERE order_status='pending'")
    cursor.execute("SELECT * FROM customers WHERE order_status='completed'")
    rows = cursor.fetchall()

    # check the results
    assert len(rows) == 1
    assert rows[0][1] == 'Bob'
    #assert rows[1][1] == 'Charlie'
