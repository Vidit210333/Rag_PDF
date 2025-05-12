import streamlit as st
from io import BytesIO
import os
import tempfile

from Helper import (
    extract_text_from_pdf,
    extract_text_from_url,
    get_text_chunks,
    get_vector_store,
    user_input,
)

# Replace this line with your real secret method
os.environ["GOOGLE_API_KEY"] = "AIzaSyCROWEOFoXucS-USWu_nG3184_IbHZJo3g"

def main():
    st.title("📚 PDF + URL Query Chatbot using Google Gemini")

    if "vector_db_loaded" not in st.session_state:
        st.session_state.vector_db_loaded = False

    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
    url_input = st.text_area("Enter URLs (one per line)")

    if st.button("Load Data"):
        all_text = ""

        # Process PDFs
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(file.read())
                temp_path = temp_file.name
            all_text += extract_text_from_pdf(temp_path)

        # Process URLs
        if url_input.strip():
            for url in url_input.strip().split("\n"):
                all_text += extract_text_from_url(url.strip())

        text_chunks = get_text_chunks(all_text)
        get_vector_store(text_chunks)

        st.success("✅ Data loaded and vector store created!")
        st.session_state.vector_db_loaded = True

    # Query Section
    user_question = st.text_input("Ask a question about the uploaded content")
    if st.button("Get Answer") and st.session_state.vector_db_loaded:
        with st.spinner("Searching for answers..."):
            response, docs = user_input(user_question)
            st.markdown("### 🧠 Answer")
            st.write(response['output_text'])

            with st.expander("🔍 View Retrieved Documents"):
                for i, doc in enumerate(docs):
                    st.markdown(f"**Document {i+1}:**")
                    st.write(doc.page_content)

if __name__ == "__main__":
    main()

