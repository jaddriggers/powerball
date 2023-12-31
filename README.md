# PowerBall Number Generator

This is a Streamlit application that generates Powerball lottery numbers and stores them in a SQLite database. The application also provides functionality to delete generated numbers from the database.

## Features

* Generate Powerball lottery numbers.
* Store generated numbers in a SQLite database.
* Option to delete specific set of numbers from the database.
* Web based user interface using Streamlit.

## Requirements

This application is written in Python and requires the following Python libraries:

* Streamlit
* SQLAlchemy
* SQLite
* pandas

## Installation & Setup

1. Clone this repository.
2. Navigate to the cloned project directory.
3. Install the required Python libraries using pip:

`pip install streamlit sqlalchemy pandas`

`pip install -r requirements.txt`
## How to run


After installing the required Python libraries, you can run the application using the following command:

`streamlit run powerball.py`

The application will be served on your local machine and can be accessed through a web browser at localhost:8501.

## Usage

1. Click the "Generate Numbers" button to generate a new set of Powerball numbers. These numbers will get saved in the database and will be displayed on the main screen.
2. To delete a specific set of numbers, select the ID from the sidebar and click "Delete Selected ID".
3. You can check your numbers at the official Powerball website through a link provided in the sidebar.

## License

This project is distributed under the MIT License. See '''LICENSE''' for more information.

