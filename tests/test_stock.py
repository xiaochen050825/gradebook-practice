from inventory.stock import (
    total_value, count_by_category, low_stock, find_item, discounted_price,
)

ITEMS = [
    {"name": "pen", "category": "office", "price": 2.0, "qty": 10},
    {"name": "stapler", "category": "office", "price": 15.0, "qty": 2},
    {"name": "apple", "category": "food", "price": 1.5, "qty": 0},
    {"name": "bread", "category": "food", "price": 4.0, "qty": 3},
]


def test_total_value():
    assert total_value(ITEMS) == 2.0 * 10 + 15.0 * 2 + 0 + 4.0 * 3


def test_count_by_category():
    assert count_by_category(ITEMS) == {"office": 2, "food": 2}


def test_low_stock():
    assert low_stock(ITEMS, 3) == ["stapler", "bread"]


def test_find_item_exists():
    assert find_item(ITEMS, "bread")["price"] == 4.0


def test_find_item_missing():
    assert find_item(ITEMS, "laptop") is None


def test_discounted_price():
    assert discounted_price(80.0, 25) == 60.0
