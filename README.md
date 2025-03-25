# 🏠 California House Price Predictor

This is a machine learning project that predicts house prices in California using a trained XGBoost model. It includes:

- 📊 Data preprocessing and feature engineering
- 📈 Model training with hyperparameter tuning using GridSearchCV
- 🌐 FastAPI backend for real-time predictions
- 🎨 Streamlit frontend for user-friendly interaction

---

## 📁 Project Structure
house-price-predictor/
├── backend/
├── data/
├── frontend/
├── model/
├── app.py
├── main.py
├── requirements.txt
├── eda.ipynb
└── xgboost_model.pkl
---

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/leventtcaan/california-house-price-predictor.git
cd california-house-price-predictor

2. **Install dependencies:**
pip install -r requirements.txt

🧠 How It Works
	•	main.py: Loads the trained model and serves predictions via a FastAPI backend.
	•	app.py: Interactive Streamlit frontend that collects user input and displays predictions.
	•	xgboost_model.pkl: Trained XGBoost model stored via joblib.

🌍 Try the Live App
👉 https://california-house-price-predictor-azzhpixhrzfjpvhnn4tfrg.streamlit.app/

💡 Features
	•	One-click predictions using an interactive form
	•	Real-time feedback
	•	Feature importance visualization (based on model weights)
	•	Input explanations (e.g., median_income is scaled ×1000)

📊 Model Performance
	•	Best model: XGBoost Regressor
	•	RMSE: ~46,680
	•	R² Score: ~0.84
	•	Tuned using GridSearchCV

🤝 Contributions

Feel free to open issues or submit pull requests!

📝 License

This project is licensed under the MIT License.

📌 Note (Türkçe)

Bu proje, Kaliforniya’daki ev fiyatlarını tahmin eden bir makine öğrenimi modeli ve Streamlit arayüzü içermektedir. Daha fazla bilgi için yukarıdaki İngilizce açıklamalara göz atabilirsiniz.
