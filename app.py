# import streamlit as st
# from Helper import user_input
# from evaluate import load
# # Load the ROUGE metric
# import evaluate

# def create_ui():
#     st.title("PDF made easy!")
#     # st.sidebar.image("image.png", use_column_width=True)
#     st.sidebar.write("### Welcome to PDF made easy!")
#     st.sidebar.write("Ask a question below and get instant insights.")

#     # Add some instructions
#     st.markdown("### Instructions")
#     st.markdown(
#         """
#         1. Enter your question in the text box below.
#         2. Click on 'Submit' to get the response.
#         3. View the answer generated based on the context from the PDFs and URLs provided.
#         """
#     )

#     # Get user input
#     question = st.text_input("Ask a question:")

#     # Call user_input function when user clicks submit
#     if st.button("Submit"):
#         with st.spinner("Generating response..."):
#             response , context_docs = user_input(question)
#             rouge = evaluate.load('rouge')
#             output_text = response.get('output_text', 'No response')  # Extract the 'output_text' from the response
#             context = ' '.join([doc.page_content for doc in context_docs])
#             # Ensure predictions and references are lists of strings
#             results = rouge.compute(predictions=[output_text], references=[context])
#             st.success("Response:")
#             st.write(output_text)
#             st.success("Rougue score:")
#             st.write(results)

#     # Add some footer
#     st.markdown("---")
#     st.markdown("**Powered by**: Vidit Agrawal ")

# # Main function to run the app
# def main():
#     create_ui()

# if __name__ == "__main__":
#     main()

# app.py

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

