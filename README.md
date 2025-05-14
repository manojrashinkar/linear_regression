# 🏠 Home Price Prediction App

This is a simple Streamlit web application that predicts home prices based on area (in square feet) using **Linear Regression** from `scikit-learn`.

---

## 📦 Features

- Uploads and displays a dataset (`homeprices.csv`)
- Trains a linear regression model
- Accepts user input for area
- Predicts house price based on the input
- Displays a scatter plot with:
  - Existing data points
  - Best-fit regression line
  - Predicted point

---

## 🧠 Technologies Used

- Python 🐍
- Streamlit 🌐
- Pandas 📊
- scikit-learn 🤖
- Matplotlib 📈
- NumPy ➗

---

## 📁 File Structure

.
├── app.py # Main Streamlit app
├── homeprices.csv # Dataset file (area, price)
└── README.md # Project documentation

yaml
Copy
Edit

---

## ▶️ How to Run the App

### 1. Clone the repository (if applicable)

```bash
git clone https://github.com/yourusername/home-price-predictor.git
cd home-price-predictor
2. Install Dependencies
It’s best to use a virtual environment:

bash
Copy
Edit
pip install -r requirements.txt
Or install directly:

bash
Copy
Edit
pip install streamlit pandas scikit-learn matplotlib numpy
3. Run the App
bash
Copy
Edit
streamlit run app.py
##📌 Dataset Format
homeprices.csv should look like this:

csv
Copy
Edit
area,price
1000,200000
1500,300000
1800,350000
...
##📬 Contact
Created by Manoj Rashinkar – LinkedIn

