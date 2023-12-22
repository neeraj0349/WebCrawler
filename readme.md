# Web Crawler

This is a simple web crawler implemented in Python using Flask for the backend. The web application allows users to crawl a website and view the discovered links.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/neeraj0349/WebCrawler.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WebCrawler
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate   # On Windows
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter the URL and depth, and click "Crawl."

4. The links will be displayed on the webpage.

### Project Structure

- `app.py`: Flask application with the web crawler implementation.
- `templates/index.html`: HTML template for the frontend.
