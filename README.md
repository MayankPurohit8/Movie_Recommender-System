# 🎥 Building a Movie Recommender System – My ML Project  

Have you ever finished watching a great movie and thought, *"What should I watch next?"*  
That’s exactly the problem I wanted to solve when I built this **Movie Recommender System**!  

This project combines **machine learning** and **real-time APIs** to suggest the **top 5 most similar movies** based on any movie you search for — along with their posters.  

---

## 💡 Project Idea  
The goal was to build a **content-based recommendation engine** that analyzes movie descriptions, genres, and metadata, then finds similar movies using **cosine similarity**.  

It’s simple, fast, and effective — no user ratings required!  

---

## 🛠️ How I Built It  

### 1️⃣ Data Preparation  
- Loaded a movies dataset and cleaned it (removed duplicates, handled missing values).  
- Combined features like **title, genres, and overview** into a single `tags` column.  
- Converted tags into numerical vectors using `CountVectorizer`.  

### 2️⃣ Recommendation Engine  
- Calculated pairwise similarity between movies using **cosine similarity**.  
- Precomputed a similarity matrix and stored it as a `.pkl` file for faster runtime.  

### 3️⃣ Interactive Web App  
- Built a **Streamlit** interface where users can select a movie from a dropdown.  
- On click, the app fetches the **top 5 most similar movies** and displays their posters using the **TMDb API**.  

---

## 🚀 Features  
✅ Content-based filtering (no user ratings needed)  
✅ Top 5 similar movies in seconds  
✅ Real-time poster fetching with TMDb API  
✅ Clean, interactive UI built with Streamlit  

---

## 📸 Sneak Peek  
_Add a screenshot or GIF of your app running here!_

---

## 📂 Project Structure  
```bash
.
├── app.py                # Main Streamlit app
├── movies.pkl            # Preprocessed movie dataset
├── similarity.pkl        # Precomputed similarity matrix
├── requirements.txt      # Dependencies
└── README.md             # This documentation


You can try this project locally by following these steps:

# 1. Clone the repository
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py

