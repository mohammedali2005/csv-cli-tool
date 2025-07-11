# CSV Command-Line Processor

A lightweight, standard-library-only Python tool for filtering, sorting, and aggregating data within CSV files directly from your terminal. This project was created as a technical assessment.

## Features

- **Read and Process CSV**: Handles any valid CSV file without external dependencies like Pandas.
- **Dynamic Filtering**: Filter rows based on conditions (`>`, `<`, `=`) on any column.
- **Data Aggregation**: Calculate `min`, `max`, and `avg` for numeric columns.
- **Flexible Sorting**: Sort data by any column in ascending (`asc`) or descending (`desc`) order.
- **Extensible Architecture**: Designed to easily add new aggregation functions or commands.
- **Robust Error Handling**: Provides clear feedback on invalid files, columns, or commands.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mohammedali2005/csv-cli-tool.git](https://github.com/mohammedali2005/csv-cli-tool.git)
    cd csv-cli-tool
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
    # Install requirements
    pip install -r requirements.txt
    ```

## Usage

The script is run via `main.py`. The `--file` argument is always required. Below are examples run against the provided `products.csv` file.

### 1. Filtering Example (`--where`)
This command shows all products from the "xiaomi" brand.
```bash
python main.py --file products.csv --where "brand=xiaomi"
```
<img width="346" height="120" alt="image" src="https://github.com/user-attachments/assets/c84dc690-9dd8-4ee7-9464-fc3bbdef5e72" />


### 2. Sorting Example (`--order-by`)
This command shows all products, sorted by rating from highest to lowest.
```bash
python main.py --file products.csv --order-by "rating=desc"
```
<img width="372" height="315" alt="image" src="https://github.com/user-attachments/assets/2819b8c5-d187-4613-8f0f-5c2ae9618b79" />


### 3. Aggregation Example (`--aggregate`)
This command calculates the average price of all products.
```bash
python main.py --file products.csv --aggregate "price=avg"
```

<img width="125" height="66" alt="image" src="https://github.com/user-attachments/assets/3243182a-9db7-479c-877a-e5f63dc099e8" />


### 4. Combined Example
This command finds all products with a price less than 500 and sorts them by price from lowest to highest.
```bash
python main.py --file products.csv --where "price<500" --order-by "price=asc"
```
<img width="345" height="172" alt="image" src="https://github.com/user-attachments/assets/8b4372fd-8ed4-4e4d-930a-385aa5e2aeed" />



## Running Tests

The project is covered by a full test suite using `pytest`. To run all tests and view the coverage report:

```bash
pytest --cov=csv_processor
```
<img width="1143" height="271" alt="image" src="https://github.com/user-attachments/assets/3cd1db8d-0333-4381-af8e-bd9bc2d69fdd" />
