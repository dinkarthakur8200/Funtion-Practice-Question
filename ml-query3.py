"""
Problem Description:

You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. All people want to go from the ground floor to the top floor. Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.



Input:

Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people the lift can carry in one round.



Output:

An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.



Example:

Input: n = 10, capacity = 3
Output: 4
 
Input: n = 7, capacity = 4
Output: 2
"""
def calculate_lift_rounds(n: int, capacity: int) -> int:
    """
    Calculate the number of rounds a lift needs to make to transport all people.
    
    Args:
        n (int): Total number of people waiting for the lift
        capacity (int): Maximum number of people the lift can carry in one round
        
    Returns:
        int: Number of rounds needed to transport all people
        
    Raises:
        ValueError: If n or capacity is negative
    """
    # Input validation
    if n < 0 or capacity <= 0:
        raise ValueError("Number of people and capacity must be positive numbers")
    
    # Calculate rounds
    full_rounds = n // capacity  # Integer division to get complete rounds
    remaining_people = n % capacity  # Get remaining people after full rounds
    
    # If there are remaining people, we need one more round
    total_rounds = full_rounds + (1 if remaining_people > 0 else 0)
    
    return total_rounds

# Test cases
def test_lift_rounds():
    assert calculate_lift_rounds(10, 3) == 4, "Test case 1 failed"
    assert calculate_lift_rounds(7, 4) == 2, "Test case 2 failed"
    assert calculate_lift_rounds(0, 5) == 0, "Test case 3 failed"
    assert calculate_lift_rounds(5, 5) == 1, "Test case 4 failed"
    assert calculate_lift_rounds(6, 5) == 2, "Test case 5 failed"
    print("All test cases passed!")

if __name__ == "__main__":
    test_lift_rounds()