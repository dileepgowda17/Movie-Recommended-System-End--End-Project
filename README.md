# 🎬 Movie Recommendation System (End-to-End Project)

A complete **Movie Recommendation System** built using **Python**, **Streamlit**, and **Machine Learning**.  
The system suggests movies similar to the one selected by the user, based on content similarity.

---

## 🚀 Project Overview

This project demonstrates an **end-to-end implementation** of a recommendation system —  
from data preprocessing, model building, serialization, and deployment using Streamlit.

Users can select any movie, and the app recommends similar ones instantly.

---

## 🧠 Features

- 🔍 Recommends top similar movies based on content
- 💾 Uses **Pickle** to save and load the model efficiently
- 🧹 Includes complete data cleaning and preprocessing
- 🌐 Interactive **Streamlit web interface**
- 🧱 Isolated environment using `.venv` for easy setup
- ⚡ Fast and lightweight – no need to retrain each time

---

## 🏗️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Language | Python |
| Framework | Streamlit |
| Libraries | pandas, numpy, scikit-learn, pickle, difflib |
| Environment | `.venv` (Virtual Environment) |
| Version Control | Git & GitHub |

---

## 📁 Project Structure
Movie-Recommended-System-End--End-Project/ │ ├── 📄 app.py                        # Streamlit web app (main deployment file) ├── 📄 main.py                       # Core logic (data loading, similarity computation) ├── 📄 requirements.txt              # List of dependencies ├── 📄 README.md                     # Project documentation │ ├── 📁 .venv/                        # Virtual environment (created using: python -m venv .venv) │ ├── 📁 notebooks/                    # For experiments, data cleaning, and model building │   └── Movie_Recommendation_System.ipynb │ ├── 📁 data/                         # Dataset folder (movies, credits, etc.) │   ├── movies.csv │   └── credits.csv │ ├── 📁 models/                       # Folder to store trained model files │   └── similarity.pkl               # Pickled similarity matrix or model │ ├── 📁 utils/                        # Optional helper functions (loading data, recommending movies) │   └── utils.py │ ├── 📁 assets/                       # Screenshots, logos, or poster images │   └── demo_screenshot.png │ └── 📄 .gitignore                    # Files/folders to be ignored by Git (like .venv, pycache)

---

### 💡 Notes
- `.venv` helps isolate dependencies for your project.
- `models/similarity.pkl` is your **precomputed similarity matrix** (so Streamlit loads fast).
- `app.py` is the file you run using  
  ```bash
  streamlit run app.py

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dileepgowda17/Movie-Recommended-System-End--End-Project.git
   cd Movie-Recommended-System-End--End-Project

   ## 🧩 How It Works

1. **Data Collection & Cleaning**
   - The dataset (movies metadata) is loaded and cleaned using **pandas**.
   - Unnecessary or missing data is handled, and useful features such as *title*, *overview*, *genres*, *keywords*, *cast*, and *crew* are selected.

2. **Feature Engineering**
   - All selected text features are combined into a single column.
   - Text data is vectorized using **CountVectorizer** or **TfidfVectorizer** to convert it into numerical form.

3. **Similarity Calculation**
   - Cosine similarity is calculated between all movie vectors.
   - This creates a matrix showing how similar each movie is to others.

4. **Model Serialization**
   - The similarity matrix (and related data) is stored as a `.pkl` file using **Pickle**.
   - This avoids recomputing similarity each time and speeds up the app.

5. **Streamlit App**
   - A user-friendly web interface is built using **Streamlit**.
   - When a user selects a movie from the dropdown list:
     - The app loads the Pickle file.
     - Finds the most similar movies.
     - Displays the **top 5 recommendations**.

6. **Output Display**
   - The recommendations (movie titles and optionally posters) are shown instantly on the web page.

---

## 🎬 Sample Output

### 🎥 Example Input:
> **Movie Selected:** Inception

### 🍿 Recommended Movies:
| Rank | Movie Title |
|------|--------------|
| 1️⃣ | Interstellar |
| 2️⃣ | The Prestige |
| 3️⃣ | The Matrix |
| 4️⃣ | Shutter Island |
| 5️⃣ | Tenet |

### 💻 Streamlit App Example:
When you run the app using:
```bash
streamlit run app.py
