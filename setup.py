import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="hipporag",
    version="2.0.0-alpha.4",
    author="Bernal Jimenez Gutierrez",
    author_email="jimenezgutierrez.1@osu.edu",
    description="A powerful graph-based RAG framework that enables LLMs to identify and leverage connections within new knowledge for improved retrieval.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OSU-NLP-Group/HippoRAG",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    python_requires=">=3.10",
    install_requires=[
        "torch==2.5.1",
        "transformers==4.45.2",
        "openai==1.68.2",
        "litellm==1.73.1",
        "networkx==3.4.2",
        "python_igraph==0.11.8",
        "tiktoken==0.7.0",
        "pydantic==2.10.4",
        "tenacity==8.5.0",
        "einops",
        "tqdm",
        "boto3",
        "langchain-text-splitters",
    ]
)