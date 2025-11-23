from collections import defaultdict
from typing import Iterator
from base_report import ReportData, Report


class AverageRatingReport(Report):
    def generate(self, products: Iterator[dict]) -> ReportData:
        brand_ratings: dict[str, list[float]] = defaultdict(list)

        for product in products:
            brand = product.get("brand")
            raw_ratings = product.get("rating")

            try:
                ratings = float(raw_ratings)
            except (TypeError, ValueError):
                continue

            if brand:
                brand_ratings[brand].append(ratings)
        # print(brand_ratings)

        average_ratings: ReportData = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            average_ratings.append((brand, round(avg_rating, 2)))
        # print(average_ratings)

        average_ratings.sort(key=lambda item: item[1], reverse=True)
        return average_ratings


class AveragePriceReport(Report):
    def generate(self, products: Iterator[dict]) -> ReportData:
        price_ratings: dict[str, list[float]] = defaultdict(list)

        for product in products:
            brand = product.get("brand")
            raw_price = product.get("price")

            try:
                price = float(raw_price)
            except (TypeError, ValueError):
                continue

            if brand:
                price_ratings[brand].append(price)

        average_prices: ReportData = []
        for brand, price in price_ratings.items():
            if not price:
                continue
            avg_price = sum(price) / len(price)
            average_prices.append((brand, round(avg_price, 2)))

        average_prices.sort(key=lambda item: item[1], reverse=True)
        return average_prices


REPORTS: dict[str, type[Report]] = {
    "average_rating": AverageRatingReport,
    "average_price": AveragePriceReport,
}

HEADERS: dict[str, list[str]] = {
    "average-rating": ["brand", "rating"],
    "average-price": ["brand", "price"],
}


def generate_report(report_name: str, data: Iterator[dict]) \
        -> tuple[ReportData, list[str]]:
    if report_name not in REPORTS:
        raise ValueError(
            f"Unknown report: '{report_name}'. "
            f"Available reports: {list(REPORTS.keys())}"
        )

    report_cls: type[Report] = REPORTS[report_name]
    report_obj = report_cls()
    report_headers: list[str] = HEADERS.get(report_name, [])
    report_data: ReportData = report_obj.generate(data)

    return report_data, report_headers
