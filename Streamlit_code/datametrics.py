import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
import random
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="DataMetrics - Analytics Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .metric-box {
        border-radius: 10px;
        padding: 15px;
        background-color: #f0f2f6;
        margin-bottom: 15px;
    }
    .dashboard-card {
        border-radius: 10px;
        padding: 20px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        transition: transform 0.3s;
    }
    .dashboard-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    """, unsafe_allow_html=True)

# App header
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2489/2489753.png", width=100)
with col2:
    st.title("DataMetrics Analytics Hub")
    st.markdown("**Your one-stop platform for comprehensive data analytics**")

# Navigation
st.sidebar.title("🔍 Navigation")
app_mode = st.sidebar.radio(
    "Select Dashboard",
    ["🏠 Home", "🏥 Hospital Analytics", "🔒 Website Privacy Analytics"],
    index=0
)

# Home Page
if app_mode == "🏠 Home":
    st.header("Welcome to DataMetrics")
    st.markdown("""
    Explore our comprehensive analytics dashboards to gain valuable insights across different domains. 
    Select a dashboard from the sidebar to begin your analysis.
    """)
    
    # Dashboard cards
    st.subheader("Available Dashboards")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.markdown('<p class="big-font">🏥 Hospital Analytics</p>', unsafe_allow_html=True)
            st.markdown("""
            - Compare hospital performance metrics
            - Analyze patient handling capacity
            - Evaluate staff strength and waiting times
            """)
            if st.button("Go to Hospital Analytics", key="hospital_btn"):
                st.session_state.navigate_to = "hospital"
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
            st.markdown('<p class="big-font">🔒 Website Privacy Analytics</p>', unsafe_allow_html=True)
            st.markdown("""
            - Compare website privacy practices
            - Analyze cookie usage and tracking
            - Evaluate regulatory compliance
            """)
            if st.button("Go to Website Privacy Analytics", key="privacy_btn"):
                st.session_state.navigate_to = "privacy"
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Recent Activity Section
    st.subheader("📈 Recent Activity")
    
    # Sample activity data
    activity_data = pd.DataFrame({
        "Dashboard": ["Hospital Analytics", "Website Privacy", "Hospital Analytics", "Website Privacy"],
        "Action": ["Comparison viewed", "Report downloaded", "Data filtered", "New analysis saved"],
        "User": ["admin", "analyst1", "manager", "researcher"],
        "Time": ["2 minutes ago", "15 minutes ago", "1 hour ago", "3 hours ago"]
    })
    
    st.dataframe(
        activity_data,
        column_config={
            "Dashboard": "Dashboard",
            "Action": "Action",
            "User": "User",
            "Time": "When"
        },
        hide_index=True,
        use_container_width=True
    )
    
    # Quick Metrics
    st.subheader("🚀 Quick Metrics")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric("Total Dashboards", "2", "1 new this month")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with m2:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric("Active Users", "124", "12 today")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with m3:
        st.markdown('<div class="metric-box">', unsafe_allow_html=True)
        st.metric("Data Points", "1.2M", "Updated daily")
        st.markdown('</div>', unsafe_allow_html=True)

# Hospital Analytics (imported from previous code)
elif app_mode == "🏥 Hospital Analytics" or getattr(st.session_state, 'navigate_to', None) == "hospital":
    # Clear the navigation trigger
    if 'navigate_to' in st.session_state:
        del st.session_state.navigate_to
    
    # Import hospital analytics code here
    def generate_dummy_hospital_data():
        hospitals = [
            "St. Thomas' Hospital, London",
            "Queen Elizabeth Hospital, Birmingham",
            "Manchester Royal Infirmary",
            "Royal Infirmary of Edinburgh",
            "University Hospital of Wales, Cardiff",
            "Royal Liverpool University Hospital",
            "John Radcliffe Hospital, Oxford",
            "Addenbrooke's Hospital, Cambridge",
            "Royal Victoria Infirmary, Newcastle",
            "Southampton General Hospital"
        ]
        
        regions = ["London", "Midlands", "North West", "Scotland", "Wales", 
                   "North West", "South East", "East of England", "North East", "South"]
        
        data = []
        
        for i in range(len(hospitals)):
            beds = random.randint(500, 1500)
            annual_patients = random.randint(20000, 100000)
            avg_wait_time_ae = round(random.uniform(1.5, 6.5), 1)
            elective_wait_weeks = random.randint(2, 26)
            doctors = random.randint(100, 500)
            nurses = random.randint(200, 1000)
            satisfaction = round(random.uniform(60, 95), 1)
            
            data.append({
                "Hospital": hospitals[i],
                "Region": regions[i],
                "Total Beds": beds,
                "Annual Patients": annual_patients,
                "AE Waiting Time (hours)": avg_wait_time_ae,
                "Elective Wait (weeks)": elective_wait_weeks,
                "Doctors": doctors,
                "Nurses": nurses,
                "Staff Satisfaction (%)": satisfaction,
                "Bed Occupancy Rate (%)": round(random.uniform(75, 98), 1),
                "AE Target Met (%)": round(random.uniform(70, 95), 1)
            })
        
        return pd.DataFrame(data)

    # Load data
    df = generate_dummy_hospital_data()

    # Sidebar filters
    st.sidebar.title("🏥 Hospital Filters")
    selected_region = st.sidebar.multiselect(
        "Select Region(s)",
        options=df['Region'].unique(),
        default=df['Region'].unique()
    )

    selected_metric = st.sidebar.selectbox(
        "Primary Comparison Metric",
        options=['Total Beds', 'Annual Patients', 'AE Waiting Time (hours)', 
                 'Elective Wait (weeks)', 'Doctors', 'Nurses', 
                 'Staff Satisfaction (%)', 'Bed Occupancy Rate (%)', 'AE Target Met (%)'],
        index=0
    )

    # Filter data
    filtered_df = df[df['Region'].isin(selected_region)]

    # Main content
    st.title("🏥 UK Hospital Performance Comparison")
    st.markdown("Comparing key performance metrics across major UK hospitals using simulated data.")

    # KPI cards
    st.subheader("Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Average A&E Wait Time", 
                f"{filtered_df['AE Waiting Time (hours)'].mean():.1f} hours",
                delta=f"{(filtered_df['AE Waiting Time (hours)'].mean() - df['AE Waiting Time (hours)'].mean()):.1f} vs national avg")
    col2.metric("Average Elective Wait", 
                f"{filtered_df['Elective Wait (weeks)'].mean():.1f} weeks",
                delta=f"{(filtered_df['Elective Wait (weeks)'].mean() - df['Elective Wait (weeks)'].mean()):.1f} vs national avg")
    col3.metric("Average Bed Occupancy", 
                f"{filtered_df['Bed Occupancy Rate (%)'].mean():.1f}%",
                delta=f"{(filtered_df['Bed Occupancy Rate (%)'].mean() - df['Bed Occupancy Rate (%)'].mean()):.1f}% vs national avg")
    col4.metric("Average Staff Satisfaction", 
                f"{filtered_df['Staff Satisfaction (%)'].mean():.1f}%",
                delta=f"{(filtered_df['Staff Satisfaction (%)'].mean() - df['Staff Satisfaction (%)'].mean()):.1f}% vs national avg")

    # Main charts
    st.subheader(f"Hospital Comparison by {selected_metric}")
    fig1 = px.bar(filtered_df.sort_values(selected_metric, ascending=False),
                 x="Hospital", y=selected_metric,
                 color="Region",
                 title=f"{selected_metric} by Hospital",
                 text=selected_metric)
    fig1.update_layout(height=500)
    st.plotly_chart(fig1, use_container_width=True)

    # Scatter plot for capacity vs wait times
    st.subheader("Capacity vs Patient Wait Times")
    col1, col2 = st.columns(2)
    with col1:
        size_var = st.selectbox("Bubble Size", ['Total Beds', 'Annual Patients', 'Doctors', 'Nurses'], index=0)
    with col2:
        color_var = st.selectbox("Color by", ['Region', 'Staff Satisfaction (%)', 'AE Target Met (%)'], index=0)

    fig2 = px.scatter(filtered_df,
                     x="AE Waiting Time (hours)",
                     y="Elective Wait (weeks)",
                     size=size_var,
                     color=color_var,
                     hover_name="Hospital",
                     title="A&E Wait vs Elective Wait",
                     size_max=30)
    st.plotly_chart(fig2, use_container_width=True)

    # Staffing analysis
    st.subheader("Staffing Levels Analysis")
    fig3 = px.bar(filtered_df,
                 x="Hospital",
                 y=['Doctors', 'Nurses'],
                 title="Medical Staff by Hospital",
                 barmode='group')
    st.plotly_chart(fig3, use_container_width=True)

    # Back to home button
    if st.button("← Back to Home"):
        st.session_state.navigate_to = "home"
        st.experimental_rerun()

# Website Privacy Analytics (imported from previous code)
elif app_mode == "🔒 Website Privacy Analytics" or getattr(st.session_state, 'navigate_to', None) == "privacy":
    # Clear the navigation trigger
    if 'navigate_to' in st.session_state:
        del st.session_state.navigate_to
    
    # Import website privacy analytics code here
    def generate_dummy_website_data():
        websites = [
            "Amazon", "eBay", "Walmart", "Target", "Best Buy",  # E-commerce
            "Facebook", "Twitter", "Instagram", "LinkedIn", "TikTok",  # Social Media
            "CNN", "BBC", "New York Times", "Fox News", "The Guardian",  # News
            "Netflix", "Disney+", "Hulu", "Spotify", "YouTube",  # Entertainment
            "Bank of America", "Chase", "Wells Fargo", "HSBC", "Barclays",  # Banking
            "WebMD", "Mayo Clinic", "NIH", "Healthline", "CDC"  # Health
        ]
        
        industries = ["E-commerce"]*5 + ["Social Media"]*5 + ["News"]*5 + ["Entertainment"]*5 + ["Banking"]*5 + ["Health"]*5
        
        privacy_labels = ["Very Poor", "Poor", "Average", "Good", "Excellent"]
        
        data = []
        
        for i in range(len(websites)):
            total_cookies = random.randint(10, 100)
            tracking_cookies = random.randint(5, total_cookies)
            third_party_sharing = random.randint(0, tracking_cookies)
            cookie_banner_clarity = random.choice(privacy_labels)
            privacy_policy_readability = random.choice(privacy_labels)
            data_retention_months = random.randint(1, 60)
            gdpr_compliance = random.choice([True, False])
            ccpa_compliance = random.choice([True, False])
            opt_out_ease = random.choice(privacy_labels)
            dark_patterns = random.randint(0, 5)
            
            privacy_score = round(
                (100 - (tracking_cookies*0.5 + third_party_sharing*0.7 + 
                data_retention_months*0.2 + dark_patterns*5)) / 
                (1 + (privacy_labels.index(cookie_banner_clarity) + 
                  privacy_labels.index(privacy_policy_readability) + 
                  privacy_labels.index(opt_out_ease)) * 10), 1) * 10
            privacy_score = max(0, min(100, privacy_score))

            print("Tracking cookies:", tracking_cookies)
            print("Third-party sharing:", third_party_sharing)
            print("Data retention:", data_retention_months)
            print("Dark patterns:", dark_patterns)
            print("Clarity index:", privacy_labels.index(cookie_banner_clarity))
            print("Readability index:", privacy_labels.index(privacy_policy_readability))
            print("Opt-out ease index:", privacy_labels.index(opt_out_ease))
            print("Numerator:", (100 - (tracking_cookies*0.5 + third_party_sharing*0.7 + data_retention_months*0.2 + dark_patterns*5)))
            print("Denom:",(1 + (privacy_labels.index(cookie_banner_clarity) + privacy_labels.index(privacy_policy_readability) + privacy_labels.index(opt_out_ease)) * 10)) 
            print("Privacy score:", privacy_score)
            
            data.append({
                "Website": websites[i],
                "Industry": industries[i],
                "Total Cookies": total_cookies,
                "Tracking Cookies": tracking_cookies,
                "Third-Party Sharing": third_party_sharing,
                "% Tracking Cookies": round(tracking_cookies/total_cookies*100, 1),
                "% Shared with Third Parties": round(third_party_sharing/tracking_cookies*100, 1) if tracking_cookies > 0 else 0,
                "Cookie Banner Clarity": cookie_banner_clarity,
                "Privacy Policy Readability": privacy_policy_readability,
                "Data Retention (months)": data_retention_months,
                "GDPR Compliant": gdpr_compliance,
                "CCPA Compliant": ccpa_compliance,
                "Opt-Out Ease": opt_out_ease,
                "Dark Patterns Count": dark_patterns,
                "Privacy Score": privacy_score
            })
        
        return pd.DataFrame(data)

    # Load data
    df = generate_dummy_website_data()

    # Sidebar filters
    st.sidebar.title("🔍 Website Filters")
    selected_industries = st.sidebar.multiselect(
        "Select Industry(s)",
        options=df['Industry'].unique(),
        default=df['Industry'].unique()
    )

    selected_metric = st.sidebar.selectbox(
        "Primary Comparison Metric",
        options=['Total Cookies', 'Tracking Cookies', 'Third-Party Sharing', 
                 '% Tracking Cookies', '% Shared with Third Parties', 
                 'Privacy Score', 'Data Retention (months)', 'Dark Patterns Count'],
        index=5
    )

    privacy_threshold = st.sidebar.slider(
        "Minimum Privacy Score Threshold",
        min_value=0,
        max_value=100,
        value=0
    )

    # Filter data
    filtered_df = df[df['Industry'].isin(selected_industries) & (df['Privacy Score'] >= privacy_threshold)]

    # Main content
    st.title("🔒 Website Privacy Analytics Dashboard")
    st.markdown("Comparing privacy practices of popular websites across industries using simulated data.")

    # KPI cards
    st.subheader("Industry Privacy Overview")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Average Privacy Score", 
                f"{filtered_df['Privacy Score'].mean():.1f}/100",
                delta=f"{(filtered_df['Privacy Score'].mean() - df['Privacy Score'].mean()):.1f} vs all industries")
    col2.metric("Avg. Tracking Cookies", 
                f"{filtered_df['Tracking Cookies'].mean():.1f}",
                delta=f"{(filtered_df['Tracking Cookies'].mean() - df['Tracking Cookies'].mean()):.1f} vs all industries")
    col3.metric("GDPR Compliance Rate", 
                f"{filtered_df['GDPR Compliant'].mean()*100:.1f}%",
                delta=f"{(filtered_df['GDPR Compliant'].mean() - df['GDPR Compliant'].mean())*100:.1f}% vs all industries")
    col4.metric("Avg. Data Retention", 
                f"{filtered_df['Data Retention (months)'].mean():.1f} months",
                delta=f"{(filtered_df['Data Retention (months)'].mean() - df['Data Retention (months)'].mean()):.1f} vs all industries")

    # Main charts
    st.subheader(f"Website Comparison by {selected_metric}")
    fig1 = px.bar(filtered_df.sort_values(selected_metric, ascending=False),
                 x="Website", y=selected_metric,
                 color="Industry",
                 title=f"{selected_metric} by Website",
                 text=selected_metric,
                 hover_data=['Privacy Score', 'GDPR Compliant', 'CCPA Compliant'])
    fig1.update_layout(height=500)
    st.plotly_chart(fig1, use_container_width=True)

    # Privacy score vs tracking cookies
    st.subheader("Privacy Score vs Tracking Practices")
    col1, col2 = st.columns(2)
    with col1:
        size_var = st.selectbox("Bubble Size", ['Total Cookies', 'Data Retention (months)', 'Dark Patterns Count'], index=0)
    with col2:
        color_var = st.selectbox("Color by", ['Industry', 'GDPR Compliant', 'Opt-Out Ease'], index=0)

    fig2 = px.scatter(filtered_df,
                     x="Tracking Cookies",
                     y="Privacy Score",
                     size=size_var,
                     color=color_var,
                     hover_name="Website",
                     title="Tracking Cookies vs Privacy Score",
                     size_max=30)
    st.plotly_chart(fig2, use_container_width=True)

    # Compliance analysis
    st.subheader("Regulatory Compliance")
    fig3 = px.sunburst(filtered_df,
                      path=['Industry', 'Website'],
                      values='Privacy Score',
                      color='GDPR Compliant',
                      title="GDPR Compliance by Industry and Website")
    st.plotly_chart(fig3, use_container_width=True)

    # Cookie distribution by industry
    st.subheader("Cookie Distribution by Industry")
    fig4 = px.box(filtered_df,
                 x="Industry",
                 y=["Total Cookies", "Tracking Cookies"],
                 title="Cookie Distribution Across Industries")
    st.plotly_chart(fig4, use_container_width=True)

    # Back to home button
    if st.button("← Back to Home"):
        st.session_state.navigate_to = "home"
        st.experimental_rerun()

# Handle navigation from buttons
if getattr(st.session_state, 'navigate_to', None) == "home":
    st.experimental_rerun()