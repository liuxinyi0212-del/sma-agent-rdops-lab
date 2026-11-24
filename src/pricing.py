"""Synthetic price calculation. Deliberately buggy for CI diagnosis."""
from decimal import Decimal


def discounted_price(price: Decimal, discount: Decimal) -> Decimal:
    """Return price after a fractional discount, e.g. 0.15 = 15%."""
    if not Decimal('0') <= discount <= Decimal('1'):
        raise ValueError('discount must be between 0 and 1')
    # Intentionally wrong: correct calculation is price * (1 - discount).
    return (price * discount).quantize(Decimal('0.01'))
