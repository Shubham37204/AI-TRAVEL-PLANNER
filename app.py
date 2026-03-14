# import streamlit as st
# from src.core.planner import TravelPlanner
# from dotenv import load_dotenv

# st.set_page_config(page_title="AI Travel Planner")
# st.title("AI Travel Item Planner")
# st.write("Plan your day journey by providing the city name and your interests")

# load_dotenv()

# with st.form("planner_form"):
#     city=st.text_input("Enter the city name")
#     interests=st.text_input("Enter you interest separated by commas")
#     submitted=st.form_submit_button("Generate itinerary")
    
#     if submitted:
#         if city and interests:
#             planner = TravelPlanner()
#             planner.set_city(city)
#             planner.set_interests(interests)
#             itinerary=planner.create_itinerary()
            
#             st.subheader("📄Your itinerary ")
#             st.markdown(itinerary)


import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Travel Planner")
st.write("Plan your perfect day trip using AI")

col1, col2 = st.columns(2)

with col1:
    city = st.text_input("🏙️ Enter City")

with col2:
    interests = st.text_input("🎯 Interests (food, history, culture)")

if st.button("Generate Itinerary ✨"):

    if city and interests:

        planner = TravelPlanner()

        planner.set_city(city)
        planner.set_interests(interests)

        with st.spinner("🤖 AI is planning your trip..."):
            itinerary = planner.create_itinerary()

        st.divider()

        st.subheader(f"📍 Travel Plan for {city}")

        st.markdown(
            f"""
            <div style="
            background-color:#111;
            padding:25px;
            border-radius:15px;
            border:1px solid #333;
            ">
            {itinerary}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter city and interests")