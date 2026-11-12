
import streamlit as st
import pandas as pd
from dashboard_engine import DashboardEngine

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="NEXUS | AI Traffic Command Centre",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CYBERPUNK NEON DESIGN
# --------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #101d42 0%, transparent 40%),
        radial-gradient(ellipse at 90% 10%, #251044 0%, transparent 35%),
        #070b16;
    color: #e8f3ff;
}

/* Hide Streamlit branding */
#MainMenu, footer, header {
    visibility: hidden;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1429, #090d1b);
    border-right: 1px solid #153b67;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #d7eaff;
}

/* Hero section */
.hero {
    background: linear-gradient(120deg, #101c38, #17102e);
    border: 1px solid #164e82;
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 28px;
    box-shadow: 0 0 25px rgba(0, 195, 255, 0.12);
}

.hero-title {
    font-size: 38px;
    font-weight: 900;
    letter-spacing: 3px;
    color: #ffffff;
    text-shadow: 0 0 15px #00c8ff;
}

.hero-subtitle {
    color: #80cfff;
    font-size: 13px;
    letter-spacing: 3px;
    margin-top: 8px;
}

/* Section titles */
.section-title {
    color: #00d9ff;
    font-size: 19px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-top: 20px;
    margin-bottom: 15px;
    text-shadow: 0 0 10px rgba(0, 217, 255, 0.4);
}

/* KPI cards */
.kpi-card {
    background: linear-gradient(145deg, #111d35, #0c1225);
    border: 1px solid #174b75;
    border-radius: 15px;
    padding: 22px;
    min-height: 125px;
    box-shadow: 0 0 16px rgba(0, 195, 255, 0.09);
    transition: 0.25s ease;
}

.kpi-card:hover {
    border-color: #00d9ff;
    box-shadow: 0 0 24px rgba(0, 217, 255, 0.25);
    transform: translateY(-3px);
}

.kpi-label {
    color: #8ca9c9;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.kpi-value {
    color: #00e5ff;
    font-size: 32px;
    font-weight: 900;
    margin-top: 10px;
    text-shadow: 0 0 12px rgba(0, 229, 255, 0.5);
}

/* Road cards */
.road-card {
    background: linear-gradient(145deg, #111b32, #0a1020);
    border: 1px solid #1c4165;
    border-radius: 13px;
    padding: 18px;
    margin-bottom: 12px;
}

.road-name {
    color: #ffffff;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 2px;
}

.road-detail {
    color: #9bb5d1;
    font-size: 13px;
    margin-top: 8px;
}

.neon {
    color: #00e5ff;
    font-weight: bold;
}

.status-low {
    color: #00ffae;
    font-weight: 800;
}

.status-medium {
    color: #ffe066;
    font-weight: 800;
}

.status-high {
    color: #ff9d42;
    font-weight: 800;
}

.status-critical {
    color: #ff426d;
    font-weight: 800;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #075baf, #6826bd);
    color: white;
    border: 1px solid #00cfff;
    border-radius: 10px;
    padding: 11px 20px;
    font-weight: 800;
    box-shadow: 0 0 13px rgba(0, 195, 255, 0.2);
    transition: 0.2s ease;
}

.stButton > button:hover {
    border-color: #ffffff;
    box-shadow: 0 0 22px rgba(0, 217, 255, 0.5);
    color: white;
}

/* Dataframes and charts */
div[data-testid="stDataFrame"],
div[data-testid="stMetric"] {
    background: #101a30;
    border-radius: 12px;
}

/* Dividers */
hr {
    border-color: #183c60;
}

/* Captions */
.stCaption {
    color: #7995b7;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ENGINE INITIALIZATION
# --------------------------------------------------

if "traffic_engine" not in st.session_state:
    st.session_state.traffic_engine = DashboardEngine()

if "last_cycle_result" not in st.session_state:
    st.session_state.last_cycle_result = None

engine = st.session_state.traffic_engine


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def section_title(title):
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )


def kpi_card(label, value):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def congestion_class(level):
    level = str(level).upper()

    classes = {
        "LOW": "status-low",
        "MEDIUM": "status-medium",
        "HIGH": "status-high",
        "CRITICAL": "status-critical"
    }

    return classes.get(level, "neon")


def road_card(road):
    level = str(road["congestion"]).upper()
    css_class = congestion_class(level)

    st.markdown(f"""
    <div class="road-card">
        <div class="road-name">◈ {road["road_id"]} ROAD</div>
        <div class="road-detail">
            Vehicles: <span class="neon">{road["vehicle_count"]}</span>
            &nbsp; | &nbsp;
            Density: <span class="neon">{road["density_percentage"]}%</span>
        </div>
        <div class="road-detail">
            Signal: <span class="neon">{road["signal"]}</span>
            &nbsp; | &nbsp;
            AI Prediction:
            <span class="{css_class}">{level}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;padding:15px 0;">
        <div style="font-size:38px;">🚦</div>
        <div style="font-size:25px;font-weight:900;
                    color:#00dcff;letter-spacing:4px;
                    text-shadow:0 0 12px #00bfff;">
            NEXUS
        </div>
        <div style="font-size:10px;color:#819cbd;
                    letter-spacing:2px;">
            TRAFFIC INTELLIGENCE
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### ◈ COMMAND MENU")

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "AI Intelligence",
            "Road Monitoring",
            "Analytics"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### ⚡ SIMULATION CONTROL")

    if st.button("▶ RUN SIMULATION CYCLE", use_container_width=True):
        with st.spinner("Executing traffic simulation..."):
            try:
                st.session_state.last_cycle_result = engine.run_cycle()
                st.success("Simulation cycle completed!")
                st.rerun()
            except Exception as error:
                st.error(f"Simulation error: {error}")

    if st.button("↻ RESET SIMULATION", use_container_width=True):
        try:
            st.session_state.traffic_engine = DashboardEngine()
            st.session_state.last_cycle_result = None
            st.rerun()
        except Exception as error:
            st.error(f"Reset error: {error}")

    st.divider()

    st.markdown("""
    <div style="font-size:11px;color:#6485a8;line-height:2;">
        SYSTEM STATUS: <span style="color:#00ffae;">● ONLINE</span><br>
        AI ENGINE: <span style="color:#00ffae;">● ACTIVE</span><br>
        MODE: SIMULATION<br>
        VERSION: 2.0 NEON
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# GET ACTUAL SYSTEM DATA
# --------------------------------------------------

snapshot = engine.get_snapshot()
roads = snapshot["roads"]


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div class="hero-title">NEXUS // COMMAND CENTRE</div>
    <div class="hero-subtitle">
        ARTIFICIAL INTELLIGENCE POWERED SMART TRAFFIC MANAGEMENT SYSTEM
    </div>
</div>
""", unsafe_allow_html=True)


# ==================================================
# PAGE 1: OVERVIEW
# ==================================================

if page == "Overview":

    section_title("◈ SYSTEM OVERVIEW")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card("Total Vehicles", snapshot["total_vehicles"])

    with col2:
        kpi_card("Emergency Vehicles", snapshot["total_emergency"])

    with col3:
        kpi_card("Active Roads", snapshot["total_roads"])

    with col4:
        kpi_card("Completed Cycles", snapshot["total_cycles"])

    section_title("◈ TRAFFIC NETWORK STATUS")

    left, right = st.columns([1.5, 1])

    with left:
        for road in roads:
            road_card(road)

    with right:
        st.markdown("#### NETWORK DENSITY")

        density_data = pd.DataFrame({
            "Road": [r["road_id"] for r in roads],
            "Density": [r["density_percentage"] for r in roads]
        })

        st.bar_chart(
            density_data.set_index("Road"),
            color="#00d9ff"
        )

        st.markdown("#### AVERAGE DENSITY")

        st.markdown(
            f'<div class="kpi-card">'
            f'<div class="kpi-label">NETWORK DENSITY</div>'
            f'<div class="kpi-value">{snapshot["average_density"]}%</div>'
            f'</div>',
            unsafe_allow_html=True
        )

    section_title("◈ LAST SIMULATION EVENT")

    if st.session_state.last_cycle_result:
        st.json(st.session_state.last_cycle_result)
    else:
        st.info("No simulation cycle has been executed in this dashboard session yet.")


# ==================================================
# PAGE 2: AI INTELLIGENCE
# ==================================================

elif page == "AI Intelligence":

    section_title("◈ ARTIFICIAL INTELLIGENCE ENGINE")

    col1, col2 = st.columns(2)

    with col1:
        kpi_card("ML MODEL", "RANDOM FOREST")

    with col2:
        kpi_card("ROADS ANALYSED", len(snapshot["predictions"]))

    section_title("◈ CONGESTION PREDICTIONS")

    prediction_df = pd.DataFrame(snapshot["predictions"])

    if not prediction_df.empty:

        display_columns = [
            "road_id",
            "vehicle_count",
            "density_percentage",
            "congestion_level",
            "confidence"
        ]

        st.dataframe(
            prediction_df[display_columns],
            use_container_width=True,
            hide_index=True
        )

        chart_data = prediction_df[
            ["road_id", "confidence"]
        ].set_index("road_id")

        section_title("◈ MODEL OUTPUT SCORES")

        st.bar_chart(chart_data, color="#b34dff")

        st.caption(
            "Scores represent the model's maximum predicted class "
            "probability. They are not calibrated confidence or "
            "proof of real-world prediction accuracy."
        )

    else:
        st.warning("No AI predictions available.")


# ==================================================
# PAGE 3: ROAD MONITORING
# ==================================================

elif page == "Road Monitoring":

    section_title("◈ INDIVIDUAL ROAD MONITORING")

    selected_road = st.selectbox(
        "SELECT ROAD",
        [road["road_id"] for road in roads]
    )

    road = next(
        item for item in roads
        if item["road_id"] == selected_road
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        kpi_card("VEHICLES", road["vehicle_count"])

    with col2:
        kpi_card("ROAD DENSITY", f'{road["density_percentage"]}%')

    with col3:
        kpi_card("AI CONGESTION", road["congestion"])

    section_title("◈ VEHICLE COMPOSITION")

    vehicle_data = {
        "Cars": road.get("car_count", 0),
        "Bikes": road.get("bike_count", 0),
        "Buses": road.get("bus_count", 0),
        "Emergency Vehicles": road.get("emergency_vehicle_count", 0)
    }

    composition_df = pd.DataFrame({
        "Vehicle Type": list(vehicle_data.keys()),
        "Count": list(vehicle_data.values())
    })

    st.bar_chart(
        composition_df.set_index("Vehicle Type"),
        color="#00e5ff"
    )

    section_title("◈ ROAD DETAILS")

    st.json(road)


# ==================================================
# PAGE 4: ANALYTICS
# ==================================================

elif page == "Analytics":

    section_title("◈ HISTORICAL TRAFFIC ANALYTICS")

    history_path = engine.history_path

    if history_path.exists():

        try:
            history_df = pd.read_csv(history_path)

            if not history_df.empty:

                col1, col2 = st.columns(2)

                with col1:
                    kpi_card("RECORDED OBSERVATIONS", len(history_df))

                with col2:
                    if "vehicle_count" in history_df.columns:
                        average_vehicles = round(
                            history_df["vehicle_count"].mean(), 2
                        )
                    else:
                        average_vehicles = 0

                    kpi_card("AVERAGE VEHICLES", average_vehicles)

                if "road_id" in history_df.columns and "vehicle_count" in history_df.columns:

                    section_title("◈ VEHICLE COUNT BY ROAD")

                    road_history = history_df.groupby(
                        "road_id"
                    )["vehicle_count"].mean()

                    st.bar_chart(
                        road_history,
                        color="#00d9ff"
                    )

                if "timestamp" in history_df.columns and "density_percentage" in history_df.columns:

                    section_title("◈ TRAFFIC DENSITY TREND")

                    history_df["timestamp"] = pd.to_datetime(
                        history_df["timestamp"],
                        errors="coerce"
                    )

                    history_df = history_df.dropna(
                        subset=["timestamp"]
                    )

                    if not history_df.empty:

                        density_history = history_df.sort_values(
                            "timestamp"
                        ).set_index("timestamp")

                        st.line_chart(
                            density_history["density_percentage"],
                            color="#b34dff"
                        )

                section_title("◈ RECENT TRAFFIC RECORDS")

                st.dataframe(
                    history_df.tail(50),
                    use_container_width=True,
                    hide_index=True
                )

            else:
                st.info("Traffic history file is currently empty.")

        except Exception as error:
            st.error(f"Could not read traffic history: {error}")

    else:
        st.info(
            "No traffic history found yet. "
            "Run a simulation cycle to start collecting records."
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown("""
<div style="text-align:center;padding:12px;color:#577391;
            font-size:11px;letter-spacing:2px;">
    NEXUS AI TRAFFIC COMMAND CENTRE
    &nbsp; | &nbsp; BUILT WITH PYTHON & MACHINE LEARNING
</div>
""", unsafe_allow_html=True)
