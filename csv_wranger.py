import streamlit as st
import pandas as pd
import base64

st.title('CSV Wrangler')

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Read file and display in table
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    # Drop columns
    if st.checkbox('Drop columns'):
        columns = st.multiselect('Select columns to drop', options=df.columns)
        df = df.drop(columns=columns)
        st.write(df)
    
    # Filter rows
    if st.checkbox('Filter rows'):
        column = st.selectbox('Select a column', options=df.columns)
        value = st.text_input('Enter a value')
        filtered_df = df[df[column] == value]
        st.write(filtered_df)
    
    # Sort data
    if st.checkbox('Sort data'):
        column = st.selectbox('Select a column to sort by', options=df.columns)
        ascending = st.checkbox('Sort ascending')
        sorted_df = df.sort_values(by=column, ascending=ascending)
        st.write(sorted_df)
    
    # Download modified data
    if st.button('Download CSV'):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="modified_data.csv">Download CSV</a>'
        st.markdown(href, unsafe_allow_html=True)

