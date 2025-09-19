def calculate_discount(base_price: float, discount_percentage: float) -> float:
    """
    Calculate the final price after applying a discount.

    Args:
        base_price (float): The original price of the product.
        discount_percentage (float): The discount percentage to apply.

    Returns:
        float: The price after the discount has been applied.
    """
    return base_price - (base_price * (discount_percentage / 100))