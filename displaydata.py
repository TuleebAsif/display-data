import streamlit as st
import pandas as pd

def main():
    st.title("CSV Data Viewer")
    
    # Upload a CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Display the data table
        st.dataframe(df)
        
        # Show summary statistics
        st.subheader("Summary Statistics")
        st.write(df.describe())
        
        # Show a bar chart of the column names and their counts
        st.subheader("Column Counts")
        column_counts = df.count()
        st.bar_chart(column_counts)
        
        # Show a scatter plot of two numeric columns if available
        st.subheader("Scatter Plot")
        numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns
        if len(numeric_columns) >= 2:
            x_column = st.selectbox("X-axis column", numeric_columns)
            y_column = st.selectbox("Y-axis column", numeric_columns)
            st.write(f"Scatter plot of {x_column} vs {y_column}")
            st.scatter_chart(df[[x_column, y_column]])
        else:
            st.write("Not enough numeric columns to create a scatter plot.")
    
if __name__ == "__main__":
    main()
