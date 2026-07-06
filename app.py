import streamlit as st
import google.generativeai as genai
import pandas as pd

# Setup
st.set_page_config(page_title="MetroPulse AI", layout="wide")
st.title("🏙️ MetroPulse: AI Decision Intelligence for Urban Mobility")
st.markdown("""
**Built using the Google Cloud Ecosystem:**
* **Core Intelligence Engine:** Powered by Gemini via the Gemini Enterprise Agent Platform
* **Analytics Layer:** Conversational Analytics & In-Context Intelligent Data Analytics
* **Deployment Workflow:** Serverless Continuous Deployment Pipeline
""")

# Secure API Key input for judges/testing
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # 1. Mock Data / File Upload
    st.subheader("Real-Time Transit & Crowd Sensor Logs")
    mock_data = {
        "Station": ["Central Hub", "West Gate", "South Park", "Arena Arena"],
        "Crowd_Level": ["Critical", "Normal", "Moderate", "High"],
        "Delay_Minutes": [22, 0, 5, 12],
        "Active_Incidents": ["Signal Failure", "None", "None", "Concert Exit Congestion"]
    }
    df = pd.DataFrame(mock_data)
    st.dataframe(df, use_container_width=True)

    # 2. AI Decision Query
    st.subheader("Ask the Decision Agent")
    user_query = st.text_input(
        "Ask for recommendations or dispatch plans:",
        value="Generate a dispatch and rerouting strategy for the critical bottleneck at Central Hub."
    )

    if st.button("Generate Action Plan"):
        with st.spinner("Analyzing transit patterns and generating optimization strategy..."):
            # Prepare context for the LLM
            context = f"Current Transit Logs:\n{df.to_string()}\n\nUser Request: {user_query}"
            
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(
                f"You are a City Dispatch Decision Intelligence Agent. Analyze this data and provide a concise, actionable 3-point operational response plan:\n\n{context}"
            )
            
            st.markdown("### 📋 Recommended Operational Response Plan")
            st.write(response.text)
else:
    st.warning("Please enter your Gemini API Key in the sidebar to run the live AI analysis.")
