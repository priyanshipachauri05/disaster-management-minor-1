import streamlit as st


# ============================================================
# PAGE CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #071522;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}


/* ================= HEADER ================= */

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


/* ================= METRIC CARDS ================= */

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


/* ================= CARD ACCENTS ================= */

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
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Real-time overview of disaster situation and response status'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# METRIC CARD FUNCTION
# ============================================================

def metric_card(icon, label, value, description, card_class):

    st.markdown(
        f"""
        <div class="metric-card {card_class}">

            <div class="metric-icon">
                {icon}
            </div>

            <div class="metric-label">
                {label}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-description">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SIX METRIC CARDS
# ============================================================

col1, col2, col3, col4, col5, col6 = st.columns(6)


with col1:
    metric_card(
        "🌊",
        "Disaster Type",
        "FLOOD",
        "Detected: 08 May 2024",
        "disaster-card"
    )


with col2:
    metric_card(
        "⚠️",
        "Severity Level",
        "HIGH",
        "Confidence: 92%",
        "severity-card"
    )


with col3:
    metric_card(
        "👥",
        "People Affected",
        "1,240",
        "Estimated",
        "people-card"
    )


with col4:
    metric_card(
        "📍",
        "Area Affected",
        "12.6 km²",
        "Total impacted area",
        "area-card"
    )


with col5:
    metric_card(
        "🚑",
        "Rescue Teams",
        "8",
        "Active in field",
        "team-card"
    )


with col6:
    metric_card(
        "📦",
        "Resources",
        "17",
        "Vehicles & equipment",
        "resource-card"
    )