# Academic Research Paper Recommendation Engine

This project implements a content-based recommendation system for academic research papers.  
It analyzes paper titles and abstracts, converts textual data into numerical features using TF-IDF vectorization, and computes similarity scores using cosine similarity to recommend relevant papers based on a user’s research interest.

## 📦 Dataset

The dataset is too large to be hosted directly on GitHub.

Download it from Kaggle:
https://www.kaggle.com/datasets/sumitm004/arxiv-scientific-research-papers-dataset

After downloading, place the CSV file in the project root directory.


## 🚀 Features
- Topic-based academic paper recommendation
- TF-IDF vectorization for text representation
- Cosine similarity for ranking relevance
- Interactive web interface for real-time querying
- Displays paper titles with abstract previews

## 🧠 How It Works
1. Load and clean the academic paper dataset  
2. Combine title and abstract into a single text field  
3. Convert text into TF-IDF vectors  
4. Compute similarity between user query and all papers  
5. Rank and display the most relevant papers  

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


Aarav Jain
