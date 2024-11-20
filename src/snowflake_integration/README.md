Currently, snowflake-connector-python supports Python 3.12
# Installation
```bash
pip install snowflake-connector-python
```

## To migrate from previous version
If you have both snowflake and snowflake-connector-python installed in your virtual environment you will get

"AttributeError: module 'snowflake' has no attribute 'connector'"

You need to uninstall snowflake
```bash
pip uninstall snowflake
```

## Sample code
```python
import snowflake.connector

# Connection to Snowflake
con = snowflake.connector.connect(
    user='your_user',
    password='your_password',
    account='your_account',
    warehouse='your_warehouse',
    role='your_role'
)
```
# Using Pandas DF with Snowflake
```bash
pip install "snowflake-connector-python[secure-local-storage,pandas]"
```

# Distributing Workloads
```python
with connect(...) as conn:
    with conn.cursor() as cur:
        # Execute a query.
        cur.execute('select seq4() as n from table(generator(rowcount => 100000));')

        # Return a Pandas DataFrame containing all of the results.
        table = cur.fetch_pandas_all()

        # Or iterate over a list of Pandas DataFrames for result batches.
        for dataframe_for_batch in cur.fetch_pandas_batches():
          my_dataframe_processing_function(dataframe_for_batch)
```