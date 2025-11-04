import streamlit as st
import pandas as pd

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="💎 Diamond Price Calculator",
    page_icon="💎",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    /* Background & text */
    body {
        background-color: #f7f9fc;
        color: #222;
    }

    /* Title */
    .title {
        text-align: center;
        font-size: 2.2em;
        color: #0a3d62;
        font-weight: 700;
        margin-bottom: 0.2em;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #34495e;
        margin-bottom: 2em;
    }

    /* Card style for outputs */
    .result-box {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 15px;
    }

    .result-value {
        font-size: 1.5em;
        color: #16a085;
        font-weight: 600;
    }

    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }

    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">💎 Diamond Price Per Carat Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your diamond data and get the total weight and average price instantly.</div>', unsafe_allow_html=True)

# ---------- DATA INPUT ----------
empty_data = pd.DataFrame({
    "chavni": [],
    "price": [],
    "weight": []
    
})

df = st.data_editor(
    empty_data,
    num_rows="dynamic",
    use_container_width=True,
    key="diamond_table"
)

# ---------- CALCULATION ----------
if not df.empty and df["weight"].sum() > 0:
    df["total_value"] = df["weight"] * df["price"]
    total_weight = df["weight"].sum()
    total_value = df["total_value"].sum()
    weighted_avg_price = total_value / total_weight

    st.markdown(f"""
        <div class="result-box">
            <div><b>Total Weight</b></div>
            <div class="result-value">{total_weight:.2f} carats</div>
        </div>
        <div class="result-box">
            <div><b>Weighted Average Price per Carat</b></div>
            <div class="result-value">₹ {weighted_avg_price:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("Please enter at least one row of data above to see results.")

# ---------- FOOTER ----------
st.markdown("<br><hr><center>💠 Created with ❤️ using Streamlit</center>", unsafe_allow_html=True)
