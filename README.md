
---

# 🏠 Home Price Prediction App

A simple and interactive **Streamlit** web application that predicts home prices based on the area (in square feet) using **Linear Regression** from `scikit-learn`.

---

## 📦 Features

* 📤 Upload and display a dataset (`homeprices.csv`)
* 📈 Train a linear regression model
* 🧮 Input area (in sq. ft.) to get price predictions
* 📊 Visualize:

  * Existing data points
  * Best-fit regression line
  * Predicted data point

---

## 🧠 Technologies Used

* **Python** 🐍
* **Streamlit** 🌐
* **Pandas** 📊
* **scikit-learn** 🤖
* **Matplotlib** 📈
* **NumPy** ➗

---

## 📁 File Structure

```
.
├── app.py            # Main Streamlit app
├── homeprices.csv    # Dataset file (area, price)
└── README.md         # Project documentation
```

---

## ▶️ How to Run the App

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/home-price-predictor.git
cd home-price-predictor
```

### 2. Install Dependencies

Using a virtual environment is recommended:

```bash
pip install -r requirements.txt
```

Or install them directly:

```bash
pip install streamlit pandas scikit-learn matplotlib numpy
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📌 Dataset Format

Ensure your `homeprices.csv` follows this structure:

```csv
area,price
1000,200000
1500,300000
1800,350000
...
```

---

## 📬 Contact

Created by **Manoj Rashinkar**
🔗 [LinkedIn](https://www.linkedin.com/in/manoj-rashinkar-82a4841b0/)

---


