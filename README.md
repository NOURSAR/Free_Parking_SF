# 🅿️ Free_Parking_SF
**A full-stack solution for finding free parking in San Francisco.**

## 📖 Background
Parking in San Francisco is a notorious "complex logic problem." I built this application to help users identify free parking zones, reducing the time and stress of urban commuting. This project demonstrates my ability to handle database relationships, backend routing, and front-end visualization.

## 💻 Tech Stack
* **Backend:** Python / Flask
* **Database:** SQL (PostgreSQL/SQLite) with SQLAlchemy ORM
* **Frontend:** HTML5, CSS3, JavaScript (Bootstrap)
* **Architecture:** Model-View-Controller (MVC)

## ⚙️ How to Run
1.  **Install dependencies:** `pip install -r requirements.txt`
2.  **Initialize Data:** `python3 seed_database.py` (This populates the SF parking coordinates).
3.  **Start Server:** `python3 server.py`
4.  **View:** Visit `http://127.0.0.1:5000` in your browser.

## 🏗️ Key Files
* `model.py`: Database schema for spots, users, and reviews.
* `crud.py`: Reusable functions for database interaction.
* `seed_database.py`: Uses DataSF open-source datasets to populate the application.
