import streamlit as st
import pandas as pd
import snowflake.connector

# Set up connection to Snowflake
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account_name',
    warehouse='your_warehouse_name',
    database='your_database_name',
    schema='your_schema_name'
)

# Create Streamlit app
def main():
    st.title('CSV Wrangler')
    uploaded_file = st.file_uploader('Upload CSV', type='csv')
    if uploaded_file is not None:
        # Parse CSV file
        df = pd.read_csv(uploaded_file)

        # Wrangle the data
        # Example: Filter the data to keep only rows with a value greater than 0 in column A
        df = df[df['A'] > 0]

        # Load data to Snowflake
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS my_table (A INT, B VARCHAR)')
        cursor.executemany('INSERT INTO my_table (A, B) VALUES (?, ?)', df.values.tolist())
        cursor.close()
        conn.commit()

        st.success('Data uploaded successfully!')

if __name__ == '__main__':
    main()
