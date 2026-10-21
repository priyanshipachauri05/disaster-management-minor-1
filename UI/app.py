import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AapdaSaarthi",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PAGE DEFINITIONS
# ============================================================

dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="🏠"
)


# ============================================================
# NAVIGATION
# ============================================================

pg = st.navigation([
    dashboard
])


# ============================================================
# RUN SELECTED PAGE
# ============================================================

pg.run()