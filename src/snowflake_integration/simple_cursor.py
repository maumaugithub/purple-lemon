import snowflake.connector as snow

# Create a connection to Snowflake
snowflake.connector.connect(
    user='your_user',
    password='your_password',
    account='your_account',
    warehouse='your_warehouse',
    role='your_role',
    # url="my_url",
)

# Define a cursor
cursor = connection.cursor()

try:
    # Execute a SQL query against Snowflake to get the current_version
    cursor.execute("SELECT current_version()")
    one_row = cursor.fetchone()

    # Display the version information
    print(one_row[0])
finally:
    cursor.close()
connection.close()