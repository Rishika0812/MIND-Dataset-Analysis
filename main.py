import streamlit as st
import overview, behaviors_news, entity_analysis, relation_analysis

st.set_page_config(page_title="MIND Dashboard", page_icon="📰", layout="centered")


st.markdown(
    """
    <style>
        /* Main container styling */
        .main-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Title styling */
        .main-title {
            font-size: 50px;
            font-weight: bold;
            color: #F39C12;
            text-align: center;
            padding: 20px 0;
        }

        .main-description {
            font-size: 22px;
            text-align: center;
            color: #4A90E2;
            padding: 10px;
        }

        /* Card container */
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }

        /* Individual card styling */
        .card {
            background-color: #F39C12;
            color: white;
            width: 250px;
            height: 150px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
        }

        /* Card text styling */
        .card-title {
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
        }

        /* Loading spinner styling */
        .stSpinner {
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def navigate_to(page_name):
    with st.spinner(f"Loading {page_name}..."):
        st.session_state.current_page = page_name

if "current_page" not in st.session_state:
    st.session_state.current_page = "Main"


st.markdown("<div class='main-container'>", unsafe_allow_html=True)


if st.session_state.current_page == "Main":
    st.markdown("<div class='main-title'>Welcome to the MIND Dataset Dashboard!</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-description'>Explore the MIND Dataset with exciting analysis on behaviors, news, entities, and relations.</div>", unsafe_allow_html=True)

    
    st.markdown("<div class='card-container'>", unsafe_allow_html=True)

    if st.button("🔍 Overview: Dataset Summary", key="overview"):
        navigate_to("Overview")

    if st.button("📰 Behavior-News: User Engagement", key="behavior_news"):
        navigate_to("Behavior-News")

    if st.button("📊 Entity Analysis: Insights", key="entity_analysis"):
        navigate_to("Entity Analysis")

    if st.button("🔗 Relation Analysis: Connections", key="relation_analysis"):
        navigate_to("Relation Analysis")

    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Overview":
    overview.render()
    if st.button("Back to Main"):
        navigate_to("Main")


elif st.session_state.current_page == "Behavior-News":
    behaviors_news.render()
    if st.button("Back to Main"):
        navigate_to("Main")


elif st.session_state.current_page == "Entity Analysis":
    entity_analysis.render()
    if st.button("Back to Main"):
        navigate_to("Main")


elif st.session_state.current_page == "Relation Analysis":
    relation_analysis.render()
    if st.button("Back to Main"):
        navigate_to("Main")


st.markdown("</div>", unsafe_allow_html=True)
