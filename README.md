
# Retail Sales Dashboard
🚀 A web-based Retail Sales Dashboard built with Flask, Pandas, Matplotlib, and Seaborn to visualize sales trends, top-selling products, and category-wise sales.

## Live Demo
🌍 View Live App (Replace with your actual URL)

## Features
- [x] Visualizes daily sales trends using a line chart.
- [x] Displays top-selling products in a ranked bar chart.
- [x] Shows sales distribution by category with a bar graph.
- [x] Loads sales data dynamically from a CSV file.
- [x] Responsive UI (Bootstrap can be added for styling).
- [x] Deployed online with Render for public access.

## ⚡Tech Stack
- Backend: Flask (Python)
- Data Processing: Pandas
- Data Visualization: Matplotlib, Seaborn
- Frontend: HTML, CSS
- Deployment: Render

## Installation & Setup
1. Clone the repository
`https://github.com/ayanabedin1105/Retail-Sales-Dashboard-Python-1.0.git`

2. Install Dependencies
`pip install -r requirements.txt`

3. Run the Flask App Locally
`python app.py`

Open http://127.0.0.1:5000/ in your browser. 

## 🛠️ Deployment on Render
1. Push Code to Github
2. Deploy on Render
- Go to [Render](https://render.com/) and create an account.
- Click "**New Web Service**"" ➡️ Connect Github Repo
- Set Build Command:
`pip install -r requirements.txt`
- Set **Start Command**:
`gunicorn app:app`
- Click **Deploy** and wait a few minutes.
- Once deployed, you'll get a **public URL** like:
`https://your-render-url.onrender.com


## 📜 License
This project is open-sourced under the **MIT License**.

## 🤝 Contributions
Feel free to **fork** this repo, open **issues**, and submit **pull requests**!
