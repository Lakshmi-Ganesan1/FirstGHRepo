# Flask Cities API

This is a simple Flask application that provides an API to get a list of cities for a given country.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/FirstGHRepo.git
    cd FirstGHRepo
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install Flask
    ```

## Running the Application

1. Navigate to the project directory:

    ```sh
    cd /workspaces/FirstGHRepo
    ```

2. Run the Flask application:

    ```sh
    python main.py
    ```

3. The application will start and you can access it at `http://127.0.0.1:5000`.

## API Endpoints

- `GET /cities/<country>`: Returns a list of cities for the specified country.

    Example:

    ```sh
    curl http://127.0.0.1:5000/cities/USA
    ```

    Response:

    ```json
    {
        "USA": ["New York", "Los Angeles", "Chicago"]
    }
    ```

## License

This project is licensed under the MIT License.