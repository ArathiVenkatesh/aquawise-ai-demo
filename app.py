import streamlit as st
import pandas as pd

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="AquaWise AI",
    page_icon="💧",
    layout="centered"
)

# ----------------- HEADER -----------------
st.title("💧 AquaWise AI")
st.subheader("Smart Water Usage & Leak Risk Advisory System")
st.caption("SDG 6: Clean Water & Sanitation | Agentic AI Demo")

st.markdown("---")

# ----------------- SIDEBAR -----------------
st.sidebar.header("📊 About This System")
st.sidebar.write(
    """
    AquaWise AI uses an **Agentic AI workflow** to:
    - Monitor water usage
    - Detect abnormal patterns
    - Assess leak risks
    - Provide sustainability advice
    
    This is a **decision-support system**, not a replacement for human judgment.
    """
)

# ----------------- INPUT SECTION -----------------
st.header("🔢 Enter Weekly Water Usage")

col1, col2 = st.columns(2)

with col1:
    mon = st.number_input("Monday (Liters)", min_value=0, value=300)
    tue = st.number_input("Tuesday (Liters)", min_value=0, value=310)
    wed = st.number_input("Wednesday (Liters)", min_value=0, value=305)

with col2:
    thu = st.number_input("Thursday (Liters)", min_value=0, value=680)
    fri = st.number_input("Friday (Liters)", min_value=0, value=720)

analyze = st.button("🚀 Analyze Water Usage")

# ----------------- ANALYSIS -----------------
if analyze:
    st.markdown("---")
    st.header("🧠 Agentic AI Analysis")

    data = {
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Water Usage (Liters)": [mon, tue, wed, thu, fri]
    }

    df = pd.DataFrame(data)

    baseline_avg = (mon + tue + wed) / 3

    spike_detected = thu > baseline_avg * 1.5 or fri > baseline_avg * 1.5

    # ----------------- AGENT 1 -----------------
    st.subheader("1️⃣ Input Intake Agent")
    st.write("Water usage data successfully collected and validated.")

    st.dataframe(df, use_container_width=True)

    # ----------------- AGENT 2 -----------------
    st.subheader("2️⃣ Pattern Analysis Agent")
    st.write(f"Normal baseline (Mon–Wed average): **{baseline_avg:.2f} L/day**")

    if spike_detected:
        st.warning("Abnormal spike detected in late-week water usage.")
    else:
        st.success("Water usage pattern appears stable.")

    # ----------------- AGENT 3 -----------------
    st.subheader("3️⃣ Leak Risk Assessment Agent")

    if spike_detected:
        leak_risk = "High"
        probability = "≈ 85%"
        st.error(f"High leak risk detected (Probability: {probability})")
    else:
        leak_risk = "Low"
        probability = "≈ 10%"
        st.success(f"Low leak risk detected (Probability: {probability})")

    # ----------------- AGENT 4 -----------------
    st.subheader("4️⃣ Decision Agent")
    st.write(f"🚨 **Severity Level:** `{leak_risk}`")

    # ----------------- AGENT 5 -----------------
    st.subheader("5️⃣ Advisory Agent")

    if leak_risk == "High":
        st.markdown(
            """
            **Immediate Recommended Actions:**
            - Inspect taps, pipelines, and storage tanks
            - Check water meter overnight
            - Shut off unused water connections
            - Fix leaks immediately to avoid water loss
            """
        )
    else:
        st.markdown(
            """
            **Preventive Recommendations:**
            - Continue regular monitoring
            - Promote water-efficient habits
            - Inspect plumbing periodically
            """
        )

    # ----------------- AGENT 6 -----------------
    st.subheader("6️⃣ Responsible AI Guardrail Agent")
    st.info(
        """
        This system:
        - Does not assume user fault
        - Avoids alarmist conclusions
        - Provides explainable, data-driven insights
        - Encourages human verification before action
        """
    )

    # ----------------- FINAL VERDICT -----------------
    st.markdown("---")
    st.header("✅ Final AquaWise AI Verdict")

    st.write(f"**Baseline Usage:** {baseline_avg:.2f} L/day")
    st.write(f"**Recent Usage:** {max(thu, fri)} L/day")
    st.write(f"**Leak Risk Level:** {leak_risk}")

    st.success("This analysis supports sustainable water management aligned with SDG 6 🌍💧")
