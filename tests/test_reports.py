import pytest

from reports import _generate_average_rating_report, _generate_average_price_report


@pytest.fixture()
def sample_products():
    return [
        {"brand": "apple", "price": 995.99, "rating": 5.0},
        {"brand": "samsung", "price": 820.79, "rating": 4.0},
        {"brand": "apple", "price": 750.59, "rating": 4.0},
        {"brand": "xiaomi", "price": 510.0, "rating": 3.0},
        {"brand": "samsung", "price": 890.98, "rating": 5.0},
        {"brand": "apple", "price": 775.69, "rating": 4.5},
    ]


def test_average_rating_calculation(sample_products):
    report = _generate_average_rating_report(sample_products.__iter__())
    # report = _generate_average_rating_report(iter(sample_products))
    report_dict = dict(report)

    assert report_dict["apple"] == pytest.approx(4.5)
    assert report_dict["samsung"] == pytest.approx(4.5)
    assert report_dict["xiaomi"] == pytest.approx(3.0)


def test_average_rating_sorting(sample_products):
    sample_products.append({"brand": "google pixel", "price": 829.79, "rating": 5.0})
    report = _generate_average_rating_report(sample_products.__iter__())

    ratings = [rating for brand, rating in report]

    assert ratings == sorted(ratings, reverse=True)
    assert report[0][0] == "google pixel"


def test_empty_input():
    report = _generate_average_rating_report([].__iter__())
    assert report == []


def test_data_with_missing_keys():
    products = [
        {"brand": "apple", "price": 999, "rating": 5.0},
        {"name": "hello kitty", "price": 1, "rating": 4.0},
        {"brand": "samsung"},
    ]
    report = _generate_average_rating_report(products.__iter__())
    assert len(report) == 1
    assert report[0][0] == "apple"
    assert report[0][1] == 5.0


def test_average_price_calculation(sample_products):
    report = _generate_average_price_report(sample_products.__iter__())
    report_dict = dict(report)

    assert report_dict["apple"] == pytest.approx(840.76)
    assert report_dict["samsung"] == pytest.approx(855.88)
    assert report_dict["xiaomi"] == pytest.approx(510)


def test_average_price_calculation_with_invalid_data():
    products = [{"brand": "honor", "price": "n/a"}]
    report = _generate_average_price_report(products.__iter__())
    assert report == []
