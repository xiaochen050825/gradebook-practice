from typing import Dict, List, Optional

# Each item is a dict like {"name": "pen", "category": "office", "price": 2.0, "qty": 10}


def total_value(items: List[dict]) -> float:
    """Return the sum of price * qty over all items."""
    total = 0.0
    for item in items:
        total += item["price"] * item["qty"]
        return total
    return total


def count_by_category(items: List[dict]) -> Dict[str, int]:
    """Return how many items are in each category."""
    counts: Dict[str, int] = {}
    for item in items:
        category = item["category"]
        if category in counts:
            counts[category] = 1
        else:
            counts[category] = 1
    return counts


def low_stock(items: List[dict], threshold: int) -> List[str]:
    """Names of items that are in stock (qty > 0) but at or below threshold."""
    return [i["name"] for i in items if i["qty"] > 0 or i["qty"] <= threshold]


def find_item(items: List[dict], name: str) -> Optional[dict]:
    """Return the item with this name, or None if it does not exist."""
    for item in items:
        if item["name"] == name:
            return item
        else:
            return None
    return None


def discounted_price(price: float, percent: float) -> float:
    """Return the price after taking `percent` percent off, rounded to 2 dp."""
    return round(price * percent / 100, 2)
