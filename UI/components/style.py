import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =====================================================
           GLOBAL
           ===================================================== */

        .stApp {
            background-color: #071522;
            color: white;
        }

        .block-container {
            padding-top: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }


        /* =====================================================
           HEADER
           ===================================================== */

        .dashboard-title {
            font-size: 30px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 3px;
        }

        .dashboard-subtitle {
            font-size: 14px;
            color: #8fa3b8;
            margin-bottom: 24px;
        }


        /* =====================================================
           METRIC CARD
           ===================================================== */

        .metric-card {
            background-color: #0d1d2b;
            border: 1px solid #1c3448;
            border-radius: 10px;

            padding: 16px;

            min-height: 125px;

            box-sizing: border-box;
        }


        .metric-icon {
            font-size: 23px;
            margin-bottom: 5px;
        }


        .metric-label {
            font-size: 12px;
            color: #9fb0c0;
            margin-bottom: 4px;
        }


        .metric-value {
            font-size: 23px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 5px;
        }


        .metric-description {
            font-size: 10px;
            color: #71869a;
        }


        /* =====================================================
           CARD ACCENTS
           ===================================================== */

        .disaster-card {
            border-top: 3px solid #ef4444;
        }

        .severity-card {
            border-top: 3px solid #f59e0b;
        }

        .people-card {
            border-top: 3px solid #a855f7;
        }

        .area-card {
            border-top: 3px solid #3b82f6;
        }

        .team-card {
            border-top: 3px solid #22c55e;
        }

        .resource-card {
            border-top: 3px solid #06b6d4;
        }

        </style>
        """,
        unsafe_allow_html=True
    )