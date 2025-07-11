# main.py

import argparse
from tabulate import tabulate
import sys

from csv_processor import main_logic, operations, utils

def main():
    """Main function to parse arguments and run the CSV processor."""
    parser = argparse.ArgumentParser(description="A command-line tool to process CSV files.")
    parser.add_argument(
        '--file', 
        required=True, 
        help="Path to the input CSV file. (Required)"
    )
    parser.add_argument(
        '--where', 
        help="Filter condition, e.g., 'price>500' or 'brand=\"apple\"'"
    )
    parser.add_argument(
        '--aggregate', 
        help="Aggregation to perform, e.g., 'rating=avg'"
    )
    parser.add_argument(
        '--order-by',
        help="Sorting order, e.g., 'brand=desc' or 'price=asc'"
    )

    args = parser.parse_args()

    try:
        data = main_logic.load_data(args.file)

        if not data:
            print("The CSV file is empty or could not be read properly.")
            return

        # 1. Filtering
        if args.where:
            parsed_where = utils.parse_condition(args.where)
            if not parsed_where:
                raise ValueError("Invalid format for --where. Use 'column[>|=|<]value'.")
            col, op, val = parsed_where
            data = main_logic.apply_where(data, col, op, val)

        # 2. Sorting
        if args.order_by:
            parsed_orderby = utils.parse_key_value(args.order_by)
            if not parsed_orderby:
                 raise ValueError("Invalid format for --order-by. Use 'column=[asc|desc]'.")
            col, direction = parsed_orderby
            data = main_logic.apply_orderby(data, col, direction)

        # 3. Aggregation or Display
        if args.aggregate:
            parsed_aggregate = utils.parse_key_value(args.aggregate)
            if not parsed_aggregate:
                raise ValueError("Invalid format for --aggregate. Use 'column=[avg|min|max]'.")
            col, func = parsed_aggregate
            
            # Note: Aggregation is performed on the potentially filtered data
            result = operations.apply_aggregate(data, col, func)
            headers = result.keys()
            rows = [result.values()]
        else:
            # Display filtered/sorted data
            if not data:
                print("No data matches the specified criteria.")
                return
            headers = data[0].keys()
            rows = [row.values() for row in data]

        print(tabulate(rows, headers=headers, tablefmt="grid"))

    except (ValueError, KeyError, FileNotFoundError, IOError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()