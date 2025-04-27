def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.

    Returns:
        float: The final price after discount, or the original price if the discount is less than 20%.
    """
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Return the price after subtracting the discount amount
        return price - discount_amount
    # If the discount is less than 20%, return the original price
    return price

# Prompt the user to enter the original price of the item
try:
    original_price = float(input("Enter the original price of the item: "))  # Convert input to a floating-point number
    discount_percentage = float(input("Enter the discount percentage: "))  # Convert input to a floating-point number

    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the appropriate message based on whether the discount was applied
    if discount_percentage >= 20:
        # If a discount was applied, show the final price
        print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        # If no discount was applied, show the original price
        print(f"No discount applied. The original price remains: ${original_price:.2f}")
except ValueError:
    # Handle cases where the user enters non-numeric values
    print("Invalid input. Please enter numeric values for the price and discount percentage.")
