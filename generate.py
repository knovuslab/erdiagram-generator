import mysql.connector
import dotenv

dotenv.load_dotenv()

# Database connection configuration
config = {
    'user': dotenv.get_key('dbuser'),
    'password': dotenv.get_key('dbpassword'),
    'host': dotenv.get_key('dbhost'),
    'database': dotenv.get_key('dbname'),
    'raise_on_warnings': True
}

# Connect to the database
conn = mysql.connector.connect(**config)

# Get a cursor
cursor = conn.cursor()

# Get the list of tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Initialize Mermaid code
mermaid_code = "classDiagram\n"

# Loop through the tables and create classes/entities
for (table_name,) in tables:
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    
    mermaid_code += f"    class {table_name} {{\n"
    for column in columns:
        mermaid_code += f"        {column[0]} : {column[1]}\n"
    mermaid_code += "    }\n"

# Find relationships (Foreign Keys)
cursor.execute("""
    SELECT 
        TABLE_NAME,
        COLUMN_NAME,
        REFERENCED_TABLE_NAME,
        REFERENCED_COLUMN_NAME
    FROM
        INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE
        REFERENCED_TABLE_SCHEMA = %s AND
        REFERENCED_TABLE_NAME IS NOT NULL;
""", (config['database'],))

relationships = cursor.fetchall()

# Add relationships to Mermaid code
for rel in relationships:
    mermaid_code += f"    {rel[0]} --> {rel[2]}: {rel[1]} -> {rel[3]}\n"

# Close cursor and connection
cursor.close()
conn.close()

# Write Mermaid code to a file
with open(f'database_diagram_{config["database"]}.mmd', 'w') as f:
    f.write(mermaid_code)

print("Mermaid file has been generated successfully!")
