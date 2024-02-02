from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain

prepared = False

def prepare():
    loader = DirectoryLoader("platform-docs-versions-main", glob="**/*.md", show_progress=True, loader_cls=UnstructuredMarkdownLoader) 
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
    )

    documents = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings()
    vector = FAISS.from_documents(documents, embeddings)
    prepared = True
    return vector


def answer_question(prompt):
    """answers the question about the API's documentations"""

    if not(prepared):
        vector = prepare()

    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}""")

    llm = Ollama(model="llama2")
    document_chain = create_stuff_documents_chain(llm, prompt)

    retriever = vector.as_retriever(search_type="similarity_score_threshold", 
                                    search_kwargs={"score_threshold": 0.5})
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": prompt})

    return response["answer"]

# def answer_question(prompt):
#     return "rien"