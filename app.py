import streamlit as st

st.title("AquaWise AI – Sustainable Water Management")

st.write("Agentic AI Demo for Leak Detection and Water Usage Analysis")

st.header("Enter Water Usage (Liters/day)")

mon = st.number_input("Monday", 0)
tue = st.number_input("Tuesday", 0)
wed = st.number_input("Wednesday", 0)
thu = st.number_input("Thursday", 0)
fri = st.number_input("Friday", 0)

if st.button("Analyze Water Usage"):
    st.subheader("Agent-wise Analysis")

    avg = (mon + tue + wed) / 3

    st.markdown("### 1️⃣ Input Intake Agent")
    st.write("Collected daily water usage data.")

    st.markdown("### 2️⃣ Pattern Analysis Agent")
    if thu > avg * 1.5 or fri > avg * 1.5:
        st.write("Abnormal spike detected towards end of week.")
    else:
        st.write("Usage pattern is consistent.")

    st.markdown("### 3️⃣ Leak Risk Assessment Agent")
    if thu > avg * 1.5 or fri > avg * 1.5:
        st.write("High probability of leakage or abnormal consumption.")
        severity = "High"
    else:
        st.write("Low leak risk detected.")
        severity = "Low"

    st.markdown("### 4️⃣ Decision Agent")
    st.write(f"Severity Level: **{severity}**")

    st.markdown("### 5️⃣ Advisory Agent")
    if severity == "High":
        st.write("Inspect pipelines, check storage tanks, and reduce unnecessary water use.")
    else:
        st.write("Continue regular monitoring and maintain efficient water practices.")

    st.markdown("### 6️⃣ Responsible AI Guardrail Agent")
    st.write("This system provides decision support only and encourages human verification.")
