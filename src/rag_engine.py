from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter

class MedicalRAGEngine:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        # Simulated medical guidelines document
        self.knowledge_base_text = """
        CLINICAL PROTOCOLS 2026:
        - Chest Pain/Shortness of Breath: High Urgency. Trigger Emergency Triage.
        - Dizziness post-surgery: High Urgency. Requires immediate clinical review.
        - Post-op Fatigue: Normal. Recommend rest.
        - Premium-Plus Insurance: Covers 100% of Emergency Visits and Specialist Consults.
        """
        self.vector_db = self._build_vector_store()

    def _build_vector_store(self):
        splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=20)
        docs = splitter.create_documents([self.knowledge_base_text])
        return Chroma.from_documents(docs, self.embeddings)

    def search(self, query):
        results = self.vector_db.similarity_search(query, k=1)
        return results[0].page_content if results else "No specific guideline found."