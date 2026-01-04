# Academic Research Paper Recommendation Engine

This project implements a content-based recommendation system for academic research papers.  
It analyzes paper titles and abstracts, converts textual data into numerical features using TF-IDF vectorization, and computes similarity scores using cosine similarity to recommend relevant papers based on a user’s research interest.

## 📦 Dataset

The dataset is too large to be hosted directly on GitHub.

Download it from Kaggle:
https://www.kaggle.com/datasets/sumitm004/arxiv-scientific-research-papers-dataset

After downloading, place the CSV file in the project root directory.

## 🎯 Problem Statement
With millions of research papers published every year, finding relevant academic literature
has become increasingly difficult for students and researchers. Traditional keyword-based
search often returns overwhelming or irrelevant results.

This project aims to simplify academic discovery by recommending research papers based on
semantic similarity rather than exact keyword matching.

## 🚀 Features
- Topic-based academic paper recommendation
- TF-IDF vectorization for text representation
- Cosine similarity for ranking relevance
- Interactive web interface for real-time querying
- Displays paper titles with abstract previews

## 💡 Use Cases
- Students searching for papers for assignments or projects
- Researchers exploring new domains or literature reviews
- Educators recommending reading material
- Early-stage researchers identifying related work

## 🧠 How It Works
1. Load and clean the academic paper dataset  
2. Combine title and abstract into a single text field  
3. Convert text into TF-IDF vectors  
4. Compute similarity between user query and all papers  
5. Rank and display the most relevant papers  

## 🏗️ System Architecture
User Query  
→ Text Vectorization (TF-IDF)  
→ Cosine Similarity Calculation  
→ Top-N Relevant Papers  
→ Streamlit Interface Display

## 📊 Dataset Information
- Source: Kaggle (arXiv Scientific Research Papers)
- Fields Used:
  - Title
  - Abstract (Summary)
- Size: ~10k+ research papers
- Domains: Computer Science, Physics, Mathematics, Biology, etc.

## 📈 Performance Notes
- TF-IDF with max_features=10,000 ensures efficient memory usage
- Cosine similarity provides fast ranking for large document sets
- Suitable for real-time recommendations on moderate datasets

## 🖥️ Running the Project

### Install Dependencies
```bash
pip install pandas scikit-learn gradio streamlit

Run the Application (Gradio Demo)
python demo_gradio.py

Run the Application (Streamlit - Local)
streamlit run app.py

🧪 Sample Query
machine learning in healthcare

🛠️ Technologies Used

Python

Pandas

Scikit-learn

TF-IDF

Cosine Similarity

Gradio / Streamlit

📌 Future Improvements

Add keyword filtering and category-based recommendations

Integrate citation-based ranking

Improve UI with paper bookmarking and search history

📄 Author
> Aarav Jain
⭐ If you found this project useful, consider giving it a star!


