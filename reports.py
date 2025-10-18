from collections import defaultdict
from typing import Callable, Iterator

ReportData = list[tuple]

ReportGenerator = Callable[[Iterator[dict]], ReportData]


def _generate_average_rating_report(products: Iterator[dict]) -> ReportData:
    brand_ratings = defaultdict(list)

    for product in products:
        brand = product.get("brand")
        rating = product.get("rating")
        if brand and isinstance(rating, float):
            brand_ratings[brand].append(rating)
    # print(brand_ratings)

    average_ratings = []
    for brand, ratings in brand_ratings.items():
        avg_rating = sum(ratings) / len(ratings)
        average_ratings.append((brand, round(avg_rating, 2)))
    # print(average_ratings)

    average_ratings.sort(key=lambda item: item[1], reverse=True)

    return average_ratings

REPORTS: dict[str, ReportGenerator] = {
    "average-rating": _generate_average_rating_report,
}

HEADERS: dict[str, list[str]] = {
    "average-rating": ["brand", "rating"],
}


def generate_report(report_name: str, data: Iterator[dict]) -> tuple[ReportData, list[str]]:
    if report_name not in REPORTS:
        raise ValueError(f"Unknown report: '{report_name}'. Available reports: {list(REPORTS.keys())}")

    report_function = REPORTS[report_name]
    report_headers = HEADERS.get(report_name, [])

    report_data = report_function(data)

    return report_data, report_headers