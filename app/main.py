import streamlit as st
from app.qa_pipeline import QAPipeline
from app.config import APP_TITLE

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.title(APP_TITLE)

pipeline = QAPipeline()

uploaded_file = st.file_uploader("Upload a PDF or DOCX", type=["pdf", "docx"])

if uploaded_file:
    with st.spinner("Processing document..."):
        pipeline.ingest(uploaded_file)
    st.success("Document processed! Ask a question below.")

question = st.text_input("Ask a question about your document")

if question:
    with st.spinner("Thinking..."):
        answer, citations = pipeline.answer(question)
    st.markdown("### Answer")
    st.write(answer)

    if citations:
        st.markdown("### Sources")
        for c in citations:
            st.markdown(f"- {c}")