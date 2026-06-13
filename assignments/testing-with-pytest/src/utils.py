def is_palindrome(text: str) -> bool:
    """Return True if the given text is a palindrome."""
    normalized = ''.join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


def calculate_discount(price: float, discount_percent: float) -> float:
    """Return the price after applying a discount percentage."""
    if price < 0:
        raise ValueError("Price must be non-negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return round(price * (1 - discount_percent / 100), 2)


def format_full_name(first_name: str, last_name: str) -> str:
    """Return a properly formatted full name."""
    first = first_name.strip().title()
    last = last_name.strip().title()
    return f"{first} {last}"
