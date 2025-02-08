# FOR REFERENCE ONLY
# from haystack.document_stores import ElasticsearchDocumentStore
# from haystack import Document
# from haystack.nodes import BM25Retriever
#
#
# # Initialize the Elasticsearch document store
# document_store = ElasticsearchDocumentStore(
#     host="localhost",
#     port=9200,
#     username="",  # Only if security is enabled
#     password="",  # Only if security is enabled
#     index="my_docs",  # Name of the index where documents will be stored
#     create_index=True  # Set to False if using an existing index
# )
#
#
#
# docs = [
#     Document(content="Ollama is a fast and efficient AI model for NLP tasks."),
#     Document(content="Haystack provides a powerful framework for building RAG pipelines."),
# ]
#
# document_store.write_documents(docs)
#
#
# retriever = BM25Retriever(document_store=document_store)
#
# query = "What is Ollama?"
# retrieved_docs = retriever.retrieve(query, top_k=5)
#
# for doc in retrieved_docs:
#     print(doc.content)