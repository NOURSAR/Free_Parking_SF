Free_Parking_SF
Free_Parking_SF is a web-based application designed to help drivers navigate the challenging parking landscape of San Francisco by identifying free parking locations. The app leverages a Flask backend and a relational database to provide users with reliable, location-based parking data.

🚀 Features
Interactive Parking Map: View free parking spots across various SF neighborhoods.

Database Integration: Persistent storage of parking locations, user reviews, or spot characteristics.

CRUD Functionality: Backend support for Creating, Reading, Updating, and Deleting parking data.

Mobile-Friendly Design: Built with a focus on responsive HTML/CSS for use on the go.

🛠️ Tech Stack
Backend: Python, Flask

Database: SQLAlchemy (PostgreSQL/SQLite)

Frontend: HTML5, CSS3, JavaScript (Bootstrap)

Deployment: Configured for Linux/Nginx environments via flask.service

📂 Project Structure
server.py: The main entry point for the Flask application and routing.

model.py: Defines the database schema (Tables for Users, Spots, etc.).

crud.py: Contains logic for database operations.

seed_database.py: Script to populate the database with initial San Francisco parking data.

static/: Contains CSS, images, and client-side JavaScript.

templates/: Jinja2 HTML templates for the UI.

⚙️ Installation & Setup
1. Clone the Repository
Bash

git clone https://github.com/NOURSAR/Free_Parking_SF.git
cd Free_Parking_SF
2. Set Up Virtual Environment
Bash

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
3. Initialize the Database
Bash

# Create and seed the database with SF parking data
python3 seed_database.py
4. Run the Application
Bash

python3 server.py
The app will be available at http://localhost:5000.

📝 Usage
Launch the app and search for your destination in San Francisco.

The map will display icons indicating verified free parking zones.

(Optional) Log in to save favorite spots or contribute new findings.
