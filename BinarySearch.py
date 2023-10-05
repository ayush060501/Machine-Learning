def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

try:
    input_list = input("Enter a sorted list of numbers: ").split()
    sorted_list = [int(item) for item in input_list]
    target_value = int(input("Enter the target value to search for: "))

    result = binary_search(sorted_list, target_value)

    if result != -1:
        print(f"Element {target_value} found at index {result}")
    else:
        print(f"Element {target_value} not found in the list")
except ValueError:
    print("Invalid input. Please enter a valid sorted list of numbers and a target value.")
