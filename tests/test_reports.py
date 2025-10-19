import pytest
from reports import _generate_average_rating_report


@pytest.fixture()
def sample_products():
    return [
        {"brand": "apple", "rating": 5.0},
        {"brand": "samsung", "rating": 4.0},
        {"brand": "apple", "rating": 4.0},
        {"brand": "xiaomi", "rating": 3.0},
        {"brand": "samsung", "rating": 5.0},
        {"brand": "apple", "rating": 4.5}
    ]


def test_average_rating_calculation(sample_products):
    report = _generate_average_rating_report(sample_products.__iter__())
    # report = _generate_average_rating_report(iter(sample_products))
    report_dict = dict(report)

    assert report_dict["apple"] == pytest.approx(4.5)
    assert report_dict["samsung"] == pytest.approx(4.5)
    assert report_dict["xiaomi"] == pytest.approx(3.0)


def test_average_rating_sorting(sample_products):
    sample_products.append({"brand": "google pixel", "rating": 5.0})
    report = _generate_average_rating_report(sample_products.__iter__())

    ratings = [rating for brand, rating in report]

    assert ratings == sorted(ratings, reverse=True)

    assert report[0][0] == "google pixel"


def test_empty_input():
    report = _generate_average_rating_report([].__iter__())
    assert report == []


def test_data_with_missing_keys():
    products = [
        {"brand": "apple", "rating": 5.0},
        {"name": "hello kitty", "rating": 4.0},
        {"brand": "samsung"}
    ]
    report = _generate_average_rating_report(products.__iter__())
    assert len(report) == 1
    assert report[0][0] == "apple"
    assert report[0][1] == 5.0