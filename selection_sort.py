def greedy_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print the current state of the array after each selection step (for demonstration)
        print(f"After iteration {i + 1}: {arr}")

    return arr

def get_input_array():
    # Prompt the user to enter the elements of the array
    print("Enter the elements of the array (space-separated):")
    input_str = input().strip()
    input_list = list(map(int, input_str.split()))
    return input_list

def main():
    # Get the input array from the user
    input_array = get_input_array()

    # Display the original input array
    print("Original Array:", input_array)

    # Sort the input array using greedy Selection Sort
    sorted_array = greedy_selection_sort(input_array.copy())

    # Display the sorted array
    print("Sorted Array:", sorted_array)

if __name__ == "__main__":
    main()
