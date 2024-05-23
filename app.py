import streamlit as st
import pandas as pd

def main():
    st.title("HDFC Bank Statement Processor")
    st.write("Upload your HDFC bank statement (CSV) to generate charts.")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, sep=" , ")
            st.success("File uploaded successfully!")
            analyze(df)
        except Exception as e:
            st.error(f"An error occurred while reading the file: {e}")

def analyze(df):
    # What is the time period of this statement. 
    df = df.sort_values(by='Date')
    df = df.sort_values(by='Date')   
    oldest_date = df['Date'].min()
    most_recent_date = df['Date'].max()
    days_between = (most_recent_date - oldest_date).days
    st.write("This statement covers: ", days_between, " days")
    return True

if __name__ == "__main__":
    main()


