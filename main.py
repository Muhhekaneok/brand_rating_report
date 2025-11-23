import argparse

from tabulate import tabulate

from data_processing import read_items_from_csv
from reports import generate_report, REPORTS, HEADERS


def main():
    parser = argparse.ArgumentParser(
        description="Generate product rating report from csv-files"
    )

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="List of paths to csv-files to be processed",
    )

    parser.add_argument(
        "--report",
        choices=REPORTS.keys(),
        required=True,
        help="Report name to generate",
    )

    args = parser.parse_args()

    data_iter = read_items_from_csv(args.files)

    try:
        report_data, report_header = generate_report(args.report, data_iter)

        if report_data:
            print(
                tabulate(
                    report_data,
                    headers=report_header,
                    showindex=range(1, len(report_data) + 1),
                )
            )
        else:
            print("No data found")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
