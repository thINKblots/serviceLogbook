# Service Logbook

A simple Streamlit-based web application for tracking service logs, maintenance records, and repair documentation.

## Features

- **Add New Logs**: Record machine details, issues, and corrective actions
- **View All Logs**: Browse all service entries with expandable details
- **Delete Logs**: Remove outdated or incorrect entries
- **Persistent Storage**: All data is saved to a JSON file

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd serviceLogbook
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run st_app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Project Structure

- `st_app.py` - Main Streamlit application interface
- `log_manager.py` - Handles data loading and saving operations
- `app.py` - Command-line version of the logbook
- `requirements.txt` - Python package dependencies

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
