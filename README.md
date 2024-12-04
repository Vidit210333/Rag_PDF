**Overview** --> 
This project involves the development of an AI-powered chatbot designed to query and retrieve information from PDFs and articles. The chatbot leverages advanced tools and technologies to provide accurate and context-aware responses.

*Features* --> 
Document Querying: Allows users to query multiple PDFs and articles for relevant information.
Contextual Understanding: Uses advanced techniques to provide meaningful responses based on the input query.
Memory and Efficiency: Implements state-of-the-art vector-based search for fast and efficient querying.
*Tools and Technologies* -->
LangChain: A framework for building applications with language models, enabling easy chaining of prompts and tasks.
Retrieval-Augmented Generation (RAG): Combines retrieval mechanisms with language generation models to enhance response accuracy.
Gemini-Pro LLM: A large language model that powers the chatbot’s conversational abilities.
FAISS: A vector database for efficient similarity search and clustering of documents.
*How It Works* --> 
Data Ingestion: PDFs and articles are processed and converted into text data.
Vectorization: Text data is transformed into embeddings using a pre-trained model and stored in FAISS.
Query Processing: User queries are processed, and relevant embeddings are retrieved using vector similarity.
Response Generation: The Gemini-Pro LLM generates context-aware responses using the retrieved information.
Interactive Chatbot: An interface allows users to interact with the chatbot, ask questions, and receive detailed answers.
*Use Cases* -->
Knowledge retrieval from large document sets.
FAQ automation for organizations.
Personalized learning or research assistance.
