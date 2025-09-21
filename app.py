import streamlit as st
import requests
import json

API_BASE = ""  # Set your FastAPI backend URL here

st.set_page_config(page_title="Document Portal", layout="wide")

st.title("📚 Document Portal")

# Create tabs instead of manual JS switching
tabs = st.tabs(["🔎 Document Analysis", "🆚 Document Compare", "💬 Doc Chat"])

# ================= ANALYSIS =================
with tabs[0]:
    st.subheader("Analyze a Document")
    st.caption("Upload a PDF and get structured analysis.")

    file = st.file_uploader("Upload PDF", type=["pdf"], key="analysis_file")
    if st.button("Run Analysis", key="analyze_btn"):
        if file is None:
            st.warning("Please upload a PDF.")
        else:
            with st.spinner("Running analysis…"):
                try:
                    files = {"file": file.getvalue()}
                    res = requests.post(f"{API_BASE}/analyze", files={"file": file})
                    if res.status_code == 200:
                        st.json(res.json())
                    else:
                        st.error(f"Error: {res.text}")
                except Exception as e:
                    st.error(f"Request failed: {e}")

# ================= COMPARE =================
with tabs[1]:
    st.subheader("Compare Two Documents")
    st.caption("Upload a reference PDF and an actual PDF to see page-wise differences.")

    col1, col2 = st.columns(2)
    with col1:
        ref_file = st.file_uploader("Reference PDF", type=["pdf"], key="ref_file")
    with col2:
        act_file = st.file_uploader("Actual PDF", type=["pdf"], key="act_file")

    if st.button("Compare", key="compare_btn"):
        if not ref_file or not act_file:
            st.warning("Please upload both PDFs.")
        else:
            with st.spinner("Comparing…"):
                try:
                    files = {
                        "reference": ref_file,
                        "actual": act_file,
                    }
                    res = requests.post(f"{API_BASE}/compare", files=files)
                    if res.status_code == 200:
                        data = res.json().get("rows", [])
                        if data:
                            st.table(data)
                        else:
                            st.info("No differences found.")
                    else:
                        st.error(f"Error: {res.text}")
                except Exception as e:
                    st.error(f"Request failed: {e}")

# ================= CHAT =================
with tabs[2]:
    st.subheader("Chat with your Documents")
    st.caption("Upload PDF/DOCX/TXT; we’ll index to FAISS and enable RAG chat.")

    chat_files = st.file_uploader("Upload files", type=["pdf", "docx", "txt"], accept_multiple_files=True, key="chat_files")

    col1, col2, col3 = st.columns(3)
    with col1:
        session_id = st.text_input("Session ID (optional)")
    with col2:
        chunk_size = st.number_input("Chunk size", value=1000, min_value=200, step=100)
    with col3:
        chunk_overlap = st.number_input("Chunk overlap", value=200, min_value=0, step=50)

    col4, col5 = st.columns(2)
    with col4:
        k = st.number_input("Top-K", value=5, min_value=1, max_value=20)
    with col5:
        use_session = st.checkbox("Use session-based FAISS", value=True)

    if st.button("Build / Update Index", key="build_index"):
        if not chat_files:
            st.warning("Please upload at least one file.")
        else:
            with st.spinner("Building index…"):
                try:
                    files = [("files", f) for f in chat_files]
                    data = {
                        "session_id": session_id or "",
                        "use_session_dirs": str(use_session).lower(),
                        "chunk_size": str(chunk_size),
                        "chunk_overlap": str(chunk_overlap),
                        "k": str(k),
                    }
                    res = requests.post(f"{API_BASE}/chat/index", files=files, data=data)
                    if res.status_code == 200:
                        st.success(res.json())
                    else:
                        st.error(f"Error: {res.text}")
                except Exception as e:
                    st.error(f"Indexing failed: {e}")

    st.divider()

    question = st.text_input("Your Question", placeholder="Ask a question about your documents…")
    if st.button("Send", key="ask_btn"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking…"):
                try:
                    data = {
                        "question": question,
                        "use_session_dirs": str(use_session).lower(),
                        "k": str(k),
                    }
                    if use_session and session_id:
                        data["session_id"] = session_id
                    res = requests.post(f"{API_BASE}/chat/query", data=data)
                    if res.status_code == 200:
                        st.markdown("### Answer")
                        st.write(res.json().get("answer", "No answer."))
                    else:
                        st.error(f"Error: {res.text}")
                except Exception as e:
                    st.error(f"Query failed: {e}")

# Footer
st.markdown("---")
st.caption("© Document Portal • Streamlit UI (hooked to FastAPI backend)")
