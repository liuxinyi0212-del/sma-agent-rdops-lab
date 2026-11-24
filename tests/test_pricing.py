from decimal import Decimal
from src.pricing import discounted_price


def test_zero_discount_keeps_price():
    assert discounted_price(Decimal('100.00'), Decimal('0')) == Decimal('100.00')


def test_fifteen_percent_discount():
    assert discounted_price(Decimal('100.00'), Decimal('0.15')) == Decimal('85.00')


def test_invalid_discount_is_rejected():
    import pytest
    with pytest.raises(ValueError):
        discounted_price(Decimal('100.00'), Decimal('1.5'))
