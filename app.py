import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Passenger Demand Prediction", layout="centered")
st.title("🚍 Passenger Demand Prediction System ")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        required_cols = ["Hour", "Day_Type", "Route_ID", "Passenger_Count"]
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            st.error(f"Missing required columns: {missing}")
        else:
            day_dict = {
                "Monday": 0, "Tuesday": 1, "Wednesday": 2,
                "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
            }

            if pd.api.types.is_numeric_dtype(df["Day_Type"]):
                df["day_num"] = df["Day_Type"].astype(int)
            else:
                df["day_num"] = df["Day_Type"].astype(str).str.strip().map(day_dict)

            X = df[["Hour", "day_num", "Route_ID"]]
            y = df["Passenger_Count"]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=30
            )

            model = RandomForestRegressor(n_estimators=100, random_state=30)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            y_pred_int = np.round(y_pred).astype(int)

            results_df = pd.DataFrame({
                "Actual Passenger Count": y_test.values,
                "Predicted Passenger Count": y_pred_int
            })

            st.subheader("📊 Actual vs Predicted Passenger Count (First 5 Rows)")
            st.dataframe(results_df.head())

            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download Full Prediction Results",
                data=csv,
                file_name="passenger_demand_predictions.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error("⚠️ Something went wrong while processing your file.")
        st.text(f"Technical details: {e}")