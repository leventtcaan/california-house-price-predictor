# 🏠 California House Price Predictor

A complete end-to-end machine learning project that predicts house prices in California using XGBoost. The project includes:

- 📊 Exploratory Data Analysis (EDA) and feature engineering  
- 🧠 Model training & tuning with GridSearchCV  
- ⚙️ Backend API using FastAPI  
- 🎨 Frontend interface with Streamlit  
- ☁️ Deployed to [Streamlit Cloud](https://california-house-price-predictor-azzhpixhrzfjpvhnn4tfrg.streamlit.app/)

---

## 📁 Project Structure

```
house-price-predictor/
├── backend/               # Model training, evaluation, and preprocessing code
├── data/                  # Raw and processed datasets
├── frontend/              # Streamlit UI (optional split)
├── model/                 # Serialized ML models
├── app.py                 # Streamlit main app
├── main.py                # FastAPI backend for prediction
├── eda.ipynb              # Jupyter notebook for EDA & feature engineering
├── requirements.txt       # Required Python packages
└── xgboost_model.pkl      # Final trained model (XGBoost)
```

---

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/leventtcaan/california-house-price-predictor.git
cd california-house-price-predictor
```

2. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 🌟 Features

- Real-time house price prediction based on user input  
- Feature importance chart (XGBoost built-in)  
- Input validations and explanations (e.g., `median_income` is scaled ×1000)  
- Visual UI with Streamlit (map, sidebar, form, prediction card)  
- GridSearchCV used to optimize model hyperparameters  
- Fully deployed app on Streamlit Cloud

---

## 🔗 Live Demo

👉 [Try the live app here!](https://california-house-price-predictor-azzhpixhrzfjpvhnn4tfrg.streamlit.app/)

---

## 📊 Model Performance

- **Best Model:** XGBoost Regressor  
- **R² Score:** 0.84  
- **RMSE:** ~46,680  
- Parameters tuned using `GridSearchCV`  
- Evaluated against multiple regression algorithms (Linear, RF, DT, GBM)

---

## 💡 Technologies Used

- Python  
- Pandas, NumPy, Matplotlib  
- Scikit-learn, XGBoost  
- FastAPI  
- Streamlit  
- Git & GitHub

---

## 🤝 Contributions

This project is open for feedback, improvement, and collaboration. Feel free to fork, star, and open issues or PRs!

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📌 Note (Türkçe)

Bu proje, Kaliforniya'daki ev fiyatlarını tahmin eden bir makine öğrenimi modeli ve Streamlit arayüzü içermektedir. Daha fazla bilgi için yukarıdaki İngilizce açıklamalara göz atabilirsiniz.

