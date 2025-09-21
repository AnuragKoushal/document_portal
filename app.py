import streamlit as st

st.set_page_config(page_title="Startup Analyst Demo", layout="centered")
st.title("AI Analyst for Startup Evaluation")

st.markdown(
    "Upload a founder document or public data to receive an actionable investor summary."
)

uploaded_file = st.file_uploader(
    "Upload a pitch deck, transcript, update, or email",
    type=["pdf", "txt", "docx"]
)

doc_type = st.selectbox(
    "Select document type:",
    ["Pitch Deck", "Call Transcript", "Founder Update", "Investor Email"]
)

results = {
    "Pitch Deck": {
        "summary": "Startup leverages AI-driven analytics for B2B workflow automation. Leadership includes industry veterans.",
        "benchmarks": "ARR: $130K (sector median: $120K). Retention rate: 88%.",
        "risk": "Recent team churn noted. Revenue projections realistic.",
        "recommendation": "Advise deeper technical diligence and customer call."
    },
    "Call Transcript": {
        "summary": "Founders communicate strong technical roadmap and go-to-market. Robust competitor awareness.",
        "benchmarks": "TAM: $1.4B (consistent with sector). Hiring pace is aggressive, meets startup peer standards.",
        "risk": "Customer engagement metrics are limited. Current pipeline validation needed.",
        "recommendation": "Monitor for pipeline growth and product fit in next update."
    },
    "Founder Update": {
        "summary": "Product milestone reached. First enterprise customer signed. Pipeline expanding.",
        "benchmarks": "Lead-to-close ratio: 28% (sector: 25-32%). Monthly cash burn: $22K (under industry norm).",
        "risk": "Relying heavily on one key client. Revenue targets may be optimistic.",
        "recommendation": "Request client diversification plan for risk mitigation."
    },
    "Investor Email": {
        "summary": "Bridge round sought to extend runway; reference to new partnership signed.",
        "benchmarks": "Runway: 14 months (healthy if new round closes).",
        "risk": "Key partnership not verified. Revenue lagging prior projections.",
        "recommendation": "Request proof of partnership and updated forecast before term sheet."
    }
}

if uploaded_file is not None:
    st.success(f"{uploaded_file.name} uploaded successfully.")
    result = results[doc_type]
    st.subheader("Investor-Ready AI Analyst Note")
    st.markdown(f"**Executive Summary:** {result['summary']}")
    st.markdown(f"**Benchmarks:** {result['benchmarks']}")
    st.markdown(f"**Risk Flags:** {result['risk']}")
    st.markdown(f"**Recommendation:** {result['recommendation']}")
    st.info("This is a demo. Actual AI-powered analysis would use Vertex AI or Gemini integration.")
else:
    st.info("Please upload a document and select document type to view analysis.")

st.markdown("---")
st.caption("Hackathon Demo – AI Startup Analyst, Streamlit.")
