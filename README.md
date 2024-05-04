# Search and Sort API

This project implements a RESTful API using Flask for searching and sorting data. It provides endpoints to search for items based on category, item name, and price range, and allows sorting the results in ascending or descending order based on price.

## Data Source

The data used by this API is sourced from Armenia's best technology-selling online shops. It is stored in a Firebase Realtime Database, which provides open read and write abilities for seamless access to the data. Parse logic is in data_scrapper.py

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/RobertArustamyan/Electroinc-shop-scrapping.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the API endpoints:

    - **GET /test**: Test endpoint to check if the server is running.
    - **POST /getData**: Endpoint to search for and sort data.

    Example request body for `/getData`:
    ```json
    {
        "category": "phone",
        "item_name": "iphone",
        "min_price": 0,
        "max_price": 15000,
        "price": "asc"
    }
    ```

    The `category`, `item_name`, `min_price`, and `max_price` fields are used to filter the data. The `price` field specifies the sorting order, either "asc" for ascending or "desc" for descending.

## Dependencies

- Flask
- Flask-Cors
- firebase-admin
- python-dotenv

## Configuration

- Make sure you connected to right fire-base [FireBaseLink](https://electro-shops-arm-default-rtdb.europe-west1.firebasedatabase.app/)
- Update the port and host settings in `app.py` if necessary.
