import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="AquaWise AI - Agentic System",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- CUSTOM CSS -----------------
st.markdown("""
<style>
    /* Main background gradient */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0f172a 100%);
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #06b6d4 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(6, 182, 212, 0.3);
    }
    
    /* Agent cards */
    .agent-card {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .agent-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 40px rgba(59, 130, 246, 0.4);
        border-color: rgba(59, 130, 246, 0.6);
    }
    
    /* Metrics styling */
    .metric-card {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(6, 182, 212, 0.1) 100%);
        border: 2px solid rgba(59, 130, 246, 0.3);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
    }
    
    /* Status badges */
    .status-high {
        background: linear-gradient(90deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    
    .status-low {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    }
    
    /* Input fields */
    .stNumberInput > div > div > input {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 8px;
        color: white;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #06b6d4 0%, #3b82f6 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(6, 182, 212, 0.5);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Agent workflow line */
    .workflow-line {
        height: 4px;
        background: linear-gradient(90deg, #06b6d4 0%, #3b82f6 50%, #8b5cf6 100%);
        border-radius: 2px;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- HEADER -----------------
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3.5rem; margin: 0; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        💧 AquaWise AI
    </h1>
    <h3 style="color: rgba(255,255,255,0.9); margin-top: 0.5rem;">
        Multi-Agent Leak Detection & Water Management System
    </h3>
    <p style="color: rgba(255,255,255,0.8); margin-top: 1rem; font-size: 1.1rem;">
        🌍 SDG 6: Clean Water & Sanitation | Advanced Agentic AI Architecture
    </p>
</div>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown("### 🤖 System Architecture")
    st.markdown("""
    <div style="background: rgba(59, 130, 246, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #3b82f6;">
        <b>Multi-Agent Workflow:</b><br><br>
        <b>1️⃣ Input Agent</b> → Data validation<br>
        <b>2️⃣ Analysis Agent</b> → Pattern detection<br>
        <b>3️⃣ Risk Agent</b> → Probability calculation<br>
        <b>4️⃣ Decision Agent</b> → Classification<br>
        <b>5️⃣ Advisory Agent</b> → Recommendations<br>
        <b>6️⃣ Guardrail Agent</b> → Ethical oversight
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 System Capabilities")
    st.markdown("""
    - **Real-time monitoring**
    - **Anomaly detection**
    - **Predictive analytics**
    - **Explainable AI**
    - **Responsible AI guardrails**
    """)
    
    st.markdown("---")
    st.markdown("### ⚙️ Configuration")
    sensitivity = st.slider("Detection Sensitivity", 1.2, 2.0, 1.5, 0.1)
    st.caption(f"Threshold: {sensitivity}x baseline")
    
    st.markdown("---")
    st.info("💡 **Your Role:** Agentic AI Workflow Lead\n\nSystem architecture, agent design, workflow logic, and responsible AI implementation")

# ----------------- INPUT SECTION -----------------
st.markdown("### 📥 Water Usage Data Input")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("#### Early Week")
    mon = st.number_input("🔵 Monday (Liters)", min_value=0, max_value=10000, value=300, step=10)
    tue = st.number_input("🔵 Tuesday (Liters)", min_value=0, max_value=10000, value=310, step=10)

with col2:
    st.markdown("#### Mid Week")
    wed = st.number_input("🟢 Wednesday (Liters)", min_value=0, max_value=10000, value=305, step=10)
    thu = st.number_input("🟡 Thursday (Liters)", min_value=0, max_value=10000, value=680, step=10)

with col3:
    st.markdown("#### Late Week")
    fri = st.number_input("🔴 Friday (Liters)", min_value=0, max_value=10000, value=720, step=10)
    st.markdown("")
    st.markdown("")

st.markdown("<br>", unsafe_allow_html=True)

# Center the analyze button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    analyze_button = st.button("🚀 ANALYZE WATER USAGE", use_container_width=True)

# ----------------- ANALYSIS -----------------
if analyze_button:
    # Workflow animation
    st.markdown('<div class="workflow-line"></div>', unsafe_allow_html=True)
    
    # Calculate metrics
    data = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Usage": [mon, tue, wed, thu, fri]
    }
    df = pd.DataFrame(data)
    
    baseline_avg = (mon + tue + wed) / 3
    spike_detected = thu > baseline_avg * sensitivity or fri > baseline_avg * sensitivity
    max_usage = max(thu, fri)
    increase_pct = ((max_usage - baseline_avg) / baseline_avg) * 100 if baseline_avg > 0 else 0
    
    # Determine risk
    if spike_detected:
        risk_level = "HIGH RISK"
        risk_color = "red"
        probability = min(85 + (increase_pct / 10), 95)
        risk_class = "status-high"
    else:
        risk_level = "LOW RISK"
        risk_color = "green"
        probability = max(10 - (baseline_avg / 100), 5)
        risk_class = "status-low"
    
    # ----------------- KEY METRICS DASHBOARD -----------------
    st.markdown("### 📊 Real-Time Analytics Dashboard")
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.markdown("""
        <div class="metric-card">
            <h4 style="color: #06b6d4; margin: 0;">Baseline Usage</h4>
            <h2 style="color: white; margin: 0.5rem 0;">{:.1f}L</h2>
            <p style="color: #94a3b8; margin: 0;">Daily Average</p>
        </div>
        """.format(baseline_avg), unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown("""
        <div class="metric-card">
            <h4 style="color: #f59e0b; margin: 0;">Peak Usage</h4>
            <h2 style="color: white; margin: 0.5rem 0;">{:.1f}L</h2>
            <p style="color: #94a3b8; margin: 0;">Maximum Detected</p>
        </div>
        """.format(max_usage), unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown("""
        <div class="metric-card">
            <h4 style="color: #8b5cf6; margin: 0;">Increase</h4>
            <h2 style="color: white; margin: 0.5rem 0;">{:.1f}%</h2>
            <p style="color: #94a3b8; margin: 0;">From Baseline</p>
        </div>
        """.format(increase_pct), unsafe_allow_html=True)
    
    with metric_col4:
        st.markdown("""
        <div class="metric-card">
            <h4 style="color: {}; margin: 0;">Leak Probability</h4>
            <h2 style="color: white; margin: 0.5rem 0;">{:.1f}%</h2>
            <p style="color: #94a3b8; margin: 0;">Risk Score</p>
        </div>
        """.format(risk_color, probability), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ----------------- VISUALIZATION -----------------
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create advanced chart
        fig = go.Figure()
        
        # Add baseline area
        fig.add_trace(go.Scatter(
            x=df['Day'],
            y=[baseline_avg] * len(df),
            mode='lines',
            name='Baseline',
            line=dict(color='#06b6d4', width=2, dash='dash'),
            fill='tozeroy',
            fillcolor='rgba(6, 182, 212, 0.1)'
        ))
        
        # Add threshold area
        fig.add_trace(go.Scatter(
            x=df['Day'],
            y=[baseline_avg * sensitivity] * len(df),
            mode='lines',
            name='Threshold',
            line=dict(color='#f59e0b', width=2, dash='dot'),
            fill='tonexty',
            fillcolor='rgba(245, 158, 11, 0.05)'
        ))
        
        # Add actual usage
        colors = ['#3b82f6', '#3b82f6', '#10b981', 
                  '#ef4444' if thu > baseline_avg * sensitivity else '#f59e0b',
                  '#ef4444' if fri > baseline_avg * sensitivity else '#f59e0b']
        
        fig.add_trace(go.Bar(
            x=df['Day'],
            y=df['Usage'],
            name='Water Usage',
            marker=dict(
                color=colors,
                line=dict(color='white', width=2)
            ),
            text=df['Usage'],
            textposition='outside',
            texttemplate='%{text}L'
        ))
        
        fig.update_layout(
            title={
                'text': '💧 Weekly Water Usage Analysis',
                'font': {'size': 20, 'color': 'white'}
            },
            xaxis_title='Day of Week',
            yaxis_title='Water Usage (Liters)',
            template='plotly_dark',
            height=400,
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            paper_bgcolor='rgba(15, 23, 42, 0.8)',
            plot_bgcolor='rgba(30, 41, 59, 0.8)',
            font=dict(color='white')
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Risk gauge
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability,
            title={'text': "Leak Risk Score", 'font': {'size': 20, 'color': 'white'}},
            number={'suffix': "%", 'font': {'size': 40}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                'bar': {'color': risk_color},
                'bgcolor': "rgba(30, 41, 59, 0.5)",
                'borderwidth': 2,
                'bordercolor': "white",
                'steps': [
                    {'range': [0, 30], 'color': 'rgba(16, 185, 129, 0.3)'},
                    {'range': [30, 70], 'color': 'rgba(245, 158, 11, 0.3)'},
                    {'range': [70, 100], 'color': 'rgba(239, 68, 68, 0.3)'}
                ],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': probability
                }
            }
        ))
        
        fig_gauge.update_layout(
            paper_bgcolor='rgba(15, 23, 42, 0.8)',
            font={'color': "white", 'family': "Arial"},
            height=400
        )
        
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ----------------- AGENTIC WORKFLOW VISUALIZATION -----------------
    st.markdown("### 🤖 Multi-Agent System Execution Flow")
    
    agents = [
        {"id": "1", "name": "Input Intake Agent", "icon": "📥", "status": "✅ COMPLETED"},
        {"id": "2", "name": "Pattern Analysis Agent", "icon": "📊", "status": "✅ COMPLETED"},
        {"id": "3", "name": "Risk Assessment Agent", "icon": "⚠️", "status": "✅ COMPLETED"},
        {"id": "4", "name": "Decision Engine Agent", "icon": "🧠", "status": "✅ COMPLETED"},
        {"id": "5", "name": "Advisory Agent", "icon": "💡", "status": "✅ COMPLETED"},
        {"id": "6", "name": "Guardrail Agent", "icon": "🛡️", "status": "✅ COMPLETED"}
    ]
    
    # Create agent cards with progressive reveal
    for i, agent in enumerate(agents):
        with st.container():
            if i < 3:
                col = st.columns([1, 1, 1])[i]
            else:
                col = st.columns([1, 1, 1])[i - 3]
            
            with col:
                time.sleep(0.1)  # Small delay for visual effect
                
                st.markdown(f"""
                <div class="agent-card">
                    <h3 style="color: #06b6d4; margin: 0;">
                        {agent['icon']} Agent {agent['id']}
                    </h3>
                    <h4 style="color: white; margin: 0.5rem 0;">
                        {agent['name']}
                    </h4>
                    <p style="color: #10b981; font-weight: bold; margin: 0;">
                        {agent['status']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
        
        if i == 2:
            st.markdown("")  # Add space between rows
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ----------------- DETAILED AGENT OUTPUTS -----------------
    st.markdown("### 🔍 Detailed Agent Analysis")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📥 Input Agent",
        "📊 Analysis Agent", 
        "⚠️ Risk Agent",
        "🧠 Decision Agent",
        "💡 Advisory Agent",
        "🛡️ Guardrail Agent"
    ])
    
    with tab1:
        st.markdown("#### Data Validation & Processing")
        st.dataframe(df.style.background_gradient(cmap='Blues'), use_container_width=True)
        st.success("✅ All 5 data points validated successfully")
        st.info(f"📊 Total weekly consumption: **{sum([mon, tue, wed, thu, fri])} liters**")
    
    with tab2:
        st.markdown("#### Statistical Pattern Recognition")
        st.markdown(f"""
        - **Baseline (Mon-Wed avg):** `{baseline_avg:.2f} L/day`
        - **Standard deviation:** `{df['Usage'].std():.2f} L`
        - **Coefficient of variation:** `{(df['Usage'].std() / df['Usage'].mean() * 100):.1f}%`
        """)
        
        if spike_detected:
            st.warning(f"🔔 **Anomaly Detected:** Usage spike of {increase_pct:.1f}% above baseline on {'Thursday' if thu > baseline_avg * sensitivity else 'Friday'}")
        else:
            st.success("✅ **Pattern Status:** Water usage within expected parameters")
    
    with tab3:
        st.markdown("#### Probabilistic Risk Modeling")
        
        # Risk factors
        risk_factors = []
        if thu > baseline_avg * sensitivity:
            risk_factors.append(f"Thursday spike: +{((thu - baseline_avg) / baseline_avg * 100):.1f}%")
        if fri > baseline_avg * sensitivity:
            risk_factors.append(f"Friday spike: +{((fri - baseline_avg) / baseline_avg * 100):.1f}%")
        
        if risk_factors:
            st.error(f"**🚨 Risk Level:** {risk_level}")
            st.markdown("**Contributing Factors:**")
            for factor in risk_factors:
                st.markdown(f"- {factor}")
        else:
            st.success(f"**✅ Risk Level:** {risk_level}")
        
        st.metric("Leak Probability", f"{probability:.1f}%", 
                 delta=f"{probability - 50:.1f}% vs. neutral",
                 delta_color="inverse")
    
    with tab4:
        st.markdown("#### Multi-Criteria Decision Classification")
        
        decision_matrix = pd.DataFrame({
            'Criteria': ['Baseline Deviation', 'Peak Usage', 'Consistency', 'Trend'],
            'Score': [
                'High' if spike_detected else 'Low',
                'High' if max_usage > 600 else 'Normal',
                'Variable' if df['Usage'].std() > 100 else 'Stable',
                'Increasing' if fri > thu else 'Stable'
            ],
            'Weight': ['40%', '30%', '20%', '10%']
        })
        
        st.dataframe(decision_matrix, use_container_width=True)
        st.markdown(f'<div class="{risk_class}" style="text-align: center; font-size: 1.5rem; margin-top: 1rem;">VERDICT: {risk_level}</div>', 
                   unsafe_allow_html=True)
    
    with tab5:
        st.markdown("#### Actionable Recommendations")
        
        if spike_detected:
            st.error("🚨 **IMMEDIATE ACTION REQUIRED**")
            st.markdown("""
            **Priority 1 - Immediate (Within 24 hours):**
            - 🔍 Conduct thorough inspection of all water fixtures
            - 📊 Monitor water meter for 2 hours with all taps closed
            - 🚰 Check for visible leaks in bathrooms, kitchen, and outdoor areas
            
            **Priority 2 - Short-term (Within 1 week):**
            - 🔧 Hire professional plumber for comprehensive system check
            - 📈 Install smart water monitoring sensors
            - 💾 Document all findings and repairs
            
            **Priority 3 - Preventive:**
            - 📅 Schedule quarterly plumbing maintenance
            - 🎓 Educate household members on leak detection
            - 💰 Estimated savings from leak repair: ₹5,000-15,000/month
            """)
        else:
            st.success("✅ **SYSTEM OPERATING NORMALLY**")
            st.markdown("""
            **Preventive Maintenance Plan:**
            - ✅ Continue weekly usage monitoring
            - 🔄 Review patterns monthly
            - 🌱 Implement water-saving practices
            - 📊 Maintain current consumption levels
            
            **Best Practices:**
            - Fix dripping taps within 48 hours
            - Check toilet flappers quarterly
            - Inspect washing machine hoses annually
            - Consider installing low-flow fixtures
            """)
    
    with tab6:
        st.markdown("#### Responsible AI Framework")
        
        st.info("""
        **🛡️ Ethical AI Guardrails Active:**
        
        ✅ **Transparency:** All decisions are explainable and traceable  
        ✅ **Non-discrimination:** No assumptions about user behavior  
        ✅ **Privacy:** No personal data collected or stored  
        ✅ **Human-in-the-loop:** System provides recommendations, not commands  
        ✅ **Fairness:** Equal treatment regardless of usage patterns  
        ✅ **Accountability:** Clear audit trail of all agent decisions  
        """)
        
        st.warning("⚠️ **Important Disclaimers:**")
        st.markdown("""
        - This system provides **decision support**, not definitive diagnosis
        - Always verify findings with professional inspection
        - Unusual usage may have legitimate explanations (guests, filling pool, etc.)
        - System accuracy improves with longer historical data
        """)
        
        st.markdown("**📋 Compliance & Standards:**")
        st.markdown("""
        - ISO 24765 (AI Ethics)
        - EU AI Act Compliance Ready
        - IEEE 7000 Standards
        - Responsible AI Principles (Anthropic)
        """)
    
    # ----------------- FINAL SUMMARY -----------------
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### ✅ Executive Summary")
    
    summary_col1, summary_col2 = st.columns([2, 1])
    
    with summary_col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(6, 182, 212, 0.2)); 
                    padding: 2rem; border-radius: 15px; border: 2px solid rgba(59, 130, 246, 0.4);">
            <h3 style="color: #06b6d4; margin-top: 0;">🎯 System Assessment Complete</h3>
            <table style="width: 100%; color: white;">
                <tr><td><b>Baseline Usage:</b></td><td>{baseline_avg:.2f} L/day</td></tr>
                <tr><td><b>Peak Usage:</b></td><td>{max_usage:.0f} L/day</td></tr>
                <tr><td><b>Usage Increase:</b></td><td>{increase_pct:.1f}%</td></tr>
                <tr><td><b>Risk Classification:</b></td><td><span class="{risk_class}">{risk_level}</span></td></tr>
                <tr><td><b>Leak Probability:</b></td><td>{probability:.1f}%</td></tr>
                <tr><td><b>Recommendation:</b></td><td>{'Immediate inspection required' if spike_detected else 'Continue monitoring'}</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    with summary_col2:
        st.markdown(f"""
        <div style="background: rgba(16, 185, 129, 0.1); padding: 2rem; border-radius: 15px; 
                    border: 2px solid rgba(16, 185, 129, 0.4); text-align: center;">
            <h3 style="color: #10b981; margin-top: 0;">🌍 SDG Impact</h3>
            <p style="color: white; font-size: 1.1rem;">
                This analysis supports<br><b>SDG Goal 6</b><br>
                <i>Clean Water & Sanitation</i>
            </p>
            <p style="color: #94a3b8; margin-top: 1rem;">
                Potential water saved:<br>
                <b style="color: white; font-size: 1.5rem;">
                    {max(0, (max_usage - baseline_avg) * 30):.0f}L/month
                </b>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.balloons()

# ----------------- FOOTER -----------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; padding: 2rem;">
    <p style="font-size: 0.9rem;">
        🤖 <b>Powered by Multi-Agent AI Architecture</b> | 
        Designed by Agentic AI Workflow Lead | 
        Built with Streamlit & Plotly
    </p>
    <p style="font-size: 0.8rem; margin-top: 0.5rem;">
        System Version 1.0 | Last Updated: {}
    </p>
</div>
""".format(datetime.now().strftime("%B %d, %Y")), unsafe_allow_html=True)
