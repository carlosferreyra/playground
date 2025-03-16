import sqlite3

# Create/connect to database
conn = sqlite3.connect(":memory:")  # In-memory database for testing
cursor = conn.cursor()

# Create users table if it doesn't exist
query = """
-- begin-sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    city TEXT)
-- end-sql
"""
cursor.execute(query)
# Insert sample data
query = """
-- begin-sql
INSERT INTO users (first_name, last_name, age, city) VALUES
('John', 'Doe', 28, 'New York'),
('Jane', 'Smith', 34, 'Los Angeles'),
('Emily', 'Jones', 45, 'Chicago'),
('Michael', 'Brown', 50, 'Houston')
-- end-sql
"""

# Your existing query
query = """
-- begin-sql
SELECT * FROM users
WHERE age > 30 AND city = 'New York'
ORDER BY last_name
LIMIT 10;
-- end-sql
"""
query_response = cursor.execute(query)
# Don't forget to commit and close when done
conn.commit()

# Print the results
for row in query_response:
    print(row)

conn.close()
