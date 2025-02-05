# Mood Tracker

## Description
Mood Tracker is a Flask web application that allows users to log, track, and manage their moods. Users can add mood entries, search for specific entries by title, and delete unwanted entries. The application helps users reflect on their emotional patterns over time.

## Features
- **User Authentication**: Secure login system using Flask-Login.
- **Mood Logging**: Users can add entries with a title, triggers, approaches, resolution, and satisfaction rating.
- **Search Functionality**: Quickly find past entries by searching for a title.
- **Entry Management**: Delete unwanted entries.
- **Recent Entries**: Displays the five most recent mood entries.
- **Dynamic UI**: Click on an entry to expand its details, with an option to return to the list.

## Installation
### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- Flask and dependencies

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/mood-tracker.git
   cd mood-tracker
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```sh
   flask db upgrade
   ```
5. Run the application:
   ```sh
   flask run
   ```
6. Open the app in your browser at `http://127.0.0.1:5000`

## Usage
- Log in or sign up.
- Add a new mood entry with a title, trigger, and satisfaction rating.
- Click on an entry to view full details.
- Search for an entry by title.
- Delete entries if needed.

## Technologies Used
- **Flask** - Backend framework
- **SQLite** - Database
- **Flask-Login** - User authentication
- **Bootstrap** - UI styling

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit changes and push.
4. Open a pull request.

## License
This project is licensed under the MIT License.

