import time

import pandas as pd

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names = ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
                'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
                'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
                'deathYear', 'primaryProfession']


#############################################################################################################
# Data Filtering
#############################################################################################################

def data_filtering(filelocation, num):
    """
    Data Filtering is for the test cases from 7 to 10.
    filelocation: imdb_dataset.csv location
    num: if num == 1 -> filter data based on years (years in range 1941 to 1955)
         if num == 2 -> filter data based on genres (genres are either ‘Adventure’ or ‘Drama’)
         if num == 3 -> filter data based on primaryProfession (if primaryProfession column contains substrings
                        {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
         if num == 4 -> filter data based on primary Names which start with vowel character.

    """
    # Load the imdb_dataset.csv dataset
    df = pd.read_csv('imdb_dataset.csv')

    if num == 1:
        # NEED TO CODE
        # Implement your logic here for Filtering data based on years (years in range 1941 to 1955)
        # Filter data based on years (years in range 1941 to 1955)
        df_year = df[(df['startYear'] >= 1941) & (df['startYear'] <= 1955)]
        df_year.reset_index(drop=True).to_csv("imdb_years_df.csv", index=False)
        return df_year

    if num == 2:
        # Filter data based on genres (genres are either ‘Adventure’ or ‘Drama’)
        df_genres = df[df['genres'].isin(['Adventure', 'Drama'])]
        df_genres.reset_index(drop=True).to_csv("imdb_genres_df.csv", index=False)
        return df_genres

    if num == 3:
        # Filter data based on primaryProfession (if primaryProfession column contains substrings
        # {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
        df_professions = df[
            df['primaryProfession'].str.contains('assistant_director|casting_director|art_director|cinematographer')]
        df_professions.reset_index(drop=True).to_csv("imdb_professions_df.csv", index=False)
        return df_professions

    if num == 4:
        # Filter data based on primary Names which start with vowel character.
        df_vowels = df[df['primaryName'].str[0].str.lower().isin(['a', 'e', 'i', 'o', 'u'])]
        df_vowels.reset_index(drop=True).to_csv("imdb_vowel_names_df.csv", index=False)
        return df_vowels


#############################################################################################################
# Quick Sort
#############################################################################################################
def pivot_element(arr):
    # CODE For identifiying the pivot element
    # Set the pivot element as the first element of the array
    pivot = arr[0]
    # Set the left and right pointers
    left = 1
    right = len(arr) - 1

    # Loop until left and right pointers cross each other
    while left <= right:
        # Move left pointer to the right until an element greater than or equal to pivot is found
        while left <= right and arr[left] < pivot:
            left += 1
        # Move right pointer to the left until an element less than or equal to pivot is found
        while left <= right and arr[right] >= pivot:
            right -= 1
        # If left pointer is less than or equal to right pointer, swap the elements at the left and right pointers
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Swap the pivot element with the element at the right pointer to place the pivot in its correct position
    arr[0], arr[right] = arr[right], arr[0]
    pivot = arr[right]

    # Return the pivot element
    return pivot


def quicksort(arr, columns):
    """
    The function performs the QuickSort algorithm on a 2D array (list of lists), where
    the sorting is based on specific columns of the 2D array. The function takes two parameters:

    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on

    The function first checks if the length of the input array is less than or equal to 1,
    in which case it returns the array as is. Otherwise, it selects the middle element of
    the array as the pivot, and splits the array into three parts: left, middle, right.

    Finally, the function calls itself recursively on the left and right sub-arrays, concatenates
    the result of the recursive calls with the middle sub-array, and returns the final sorted 2D array.
    """
    if len(arr) <= 1:
        return arr

    # Step 1: Select middle row as pivot
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index][columns[0]]
    # NEED TO CODE
    # Implement Quick Sort Algorithm
    # Step 2: Partition array into left, middle, and right sub-arrays
    left, middle, right = [], [], []
    for row in arr:
        if row[columns[0]] < pivot:
            left.append(row)
        elif row[columns[0]] == pivot:
            middle.append(row)
        else:
            right.append(row)
    # Step 3: Recursively apply Quick Sort to left and right sub-arrays
    left = quicksort(left, columns)
    right = quicksort(right, columns)

    # return Sorted array
    # Step 4: Concatenate sorted sub-arrays to obtain final result
    return left + middle + right
    # Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    # column values in sublist must be according to the columns passed from the testcases.


#############################################################################################################
# Selection Sort
#############################################################################################################
def selection_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    # Determine the length of the input array
    n = len(arr)

    # Perform selection sort on the input array
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j][columns[0]] < arr[min_idx][columns[0]]:
                min_idx = j
            elif arr[j][columns[0]] == arr[min_idx][columns[0]]:
                for col in columns[1:]:
                    if arr[j][col] < arr[min_idx][col]:
                        min_idx = j
                        break

        # Swap the minimum element with the first element in the unsorted portion of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Return Sorted array
    return arr


#############################################################################################################
# Heap Sort
#############################################################################################################
def max_heapify(arr, n, i, columns):
    """
    arr: the input array that represents the binary heap
    n: The number of elements in the array
    i: i is the index of the node to be processed
    columns: The columns to be used for comparison

    The max_heapify function is used to maintain the max heap property
    in a binary heap. It takes as input a binary heap stored in an array,
    and an index i in the array, and ensures that the subtree rooted at
    index i is a max heap.
    """
    # Determine the left and right child indices
    left = 2 * i + 1
    right = 2 * i + 2

    # Initialize the index of the largest element
    largest = i

    # Compare the left child with the current node
    if left < n and all(arr[left][col] >= arr[largest][col] for col in columns):
        largest = left

    # Compare the right child with the current node
    if right < n and all(arr[right][col] >= arr[largest][col] for col in columns):
        largest = right

    # If the largest element is not the current node, swap the nodes and continue
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest, columns)


def build_max_heap(arr, n, i, columns):
    """
    arr: The input array to be transformed into a max heap
    n: The number of elements in the array
    i: The current index in the array being processed
    columns: The columns to be used for comparison

    The build_max_heap function is used to construct a max heap
    from an input array.
    """
    # NEED TO CODE
    # Implement heapify algorithm here
    # Determine the indices of the left and right children of the current node
    left = 2 * i + 1
    right = 2 * i + 2

    # Recursively call max_heapify on the left and right subtrees
    if left < n:
        build_max_heap(arr, n, left, columns)
    if right < n:
        build_max_heap(arr, n, right, columns)

    # Ensure that the current subtree is a max heap
    max_heapify(arr, n, i, columns)


def heap_sort(arr, columns):
    """
        arr: list of sublists which consists of records from the dataset in every sublists.
        columns: store the column indices from the dataframe.
        Finally, returns the final sorted 2D array.
    """
    # NEED TO CODE
    # Implement Heap Sort Algorithm
    # Convert the columns to a list of tuples with the element value and index, handling index out of range errors
    column_tuples = []
    for col in columns:
        if len(arr) > 0 and len(arr[0]) > col:
            column_tuples.append((arr[0][col], col))
        else:
            column_tuples.append((0, col))

    # Define a function to compare two elements based on the specified columns
    # Convert the columns to a list of tuples with the element value and index
    def cmp(a, b):
        for column, index in column_tuples:
            if index >= len(a):
                a_val = 0
            else:
                a_val = a[index]
            if index >= len(b):
                b_val = 0
            else:
                b_val = b[index]
            if a_val != b_val:
                return 1 if a_val > b_val else -1
        return 0

    # Convert the list to a heap
    def heapify(lst):
        for i in range(len(lst) // 2, -1, -1):
            sift_down(lst, i, len(lst))

    # Move the top element to its correct position in the heap
    def sift_down(lst, start, end):
        root = start
        while root * 2 + 1 < end:
            child = root * 2 + 1
            if child + 1 < end and cmp(lst[child], lst[child + 1]) == -1:
                child += 1
            if cmp(lst[root], lst[child]) == -1:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                return

    # Add error handling for sublists with length less than the maximum column index
    for i in range(len(arr)):
        while len(arr[i]) < max(columns) + 1:
            arr[i].append(0)

    heapify(arr)

    # Move the largest element to the end of the heap, then rebuild the heap
    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(arr, 0, end)

    # Remove extra zeros added for error handling
    for i in range(len(arr)):
        while arr[i][-1] == 0:
            arr[i].pop()

    # Return Sorted array
    return arr


#############################################################################################################
# Shell Sort
#############################################################################################################
def shell_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    # NEED TO CODE
    # Implement Shell Sort Algorithm
    # Determine the length of the input array
    n = len(arr)

    # Determine the gap sequence to use for shell sort
    gap_sequence = [1]
    while gap_sequence[-1] < n:
        gap_sequence.append(2 * gap_sequence[-1] + 1)
    gap_sequence = gap_sequence[:-1]

    # Perform shell sort for each gap in the gap sequence
    for gap in gap_sequence:
        # Perform insertion sort on each sublist of the input array
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and temp[columns[0]] < arr[j - gap][columns[0]]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

    # return Sorted array
    return arr
    # Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    # column values in sublist must be according to the columns passed from the testcases.


#############################################################################################################
# Merge Sort
#############################################################################################################
def merge(left, right, columns):
    """
    left: a list of lists representing the left sub-array to be merged
    right: a list of lists representing the right sub-array to be merged
    columns: a list of integers representing the columns to sort the 2D array on

    Finally, after one of the sub-arrays is fully merged, the function extends the result
    with the remaining elements of the other sub-array and returns the result as the final
    sorted 2D array.
    """
    # NEED TO CODE
    # Implement merge Logic

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][columns[0]] <= right[j][columns[0]]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    # return Sorted array
    return result


def merge_sort(data, columns):
    """
    data: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, the function returns the result of the merge operation as the final sorted 2D array.
    """
    # Need to Code
    # Implement Merge Sort Algorithm
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left1 = data[:mid]
    right1 = data[mid:]
    left = merge_sort(left1, columns)
    right = merge_sort(right1, columns)
    # return Sorted array
    return merge(left, right, columns)

    # Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    # column values in sublist must be according to the columns passed from the testcases.


#############################################################################################################
# Insertion Sort
#############################################################################################################
def insertion_sort(arr, columns):
    """
    Sorts a list of sublists by the values in the specified columns using insertion sort.

    Parameters:
    - arr: a list of sublists representing records from a dataset
    - columns: a list of column indices to sort by, in order of priority

    Returns:
    - a sorted list of sublists
    """
    for i in range(1, len(arr)):
        current = arr[i]
        j = i
        while j > 0 and compare(arr[j-1], current, columns) > 0:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current
    return arr


def compare(a, b, columns):
    """
    Compares two sublists by the values in the specified columns.

    Parameters:
    - a, b: two sublists to compare
    - columns: a list of column indices to sort by, in order of priority

    Returns:
    - 1 if a > b, 0 if a == b, -1 if a < b
    """
    for col in columns:
        if a[col] < b[col]:
            return -1
        elif a[col] > b[col]:
            return 1
    return 0




#############################################################################################################
# Sorting Algorithms Function Calls
#############################################################################################################
def sorting_algorithms(file_path, columns, select):
    # NEED TO CODE
    # Read imdb_dataset.csv
    # write code here Inorder to read imdb_dataset
    # df= #read imdb_dataset.csv data set using pandas library

    df = pd.read_csv(file_path)
    column_vals = [0] + [df.columns.get_loc(col) for col in columns]
    data = df.iloc[:, column_vals].values.tolist()

    #############################################################################################################
    # Donot Modify Below Code
    #############################################################################################################
    if (select == 1):
        start_time = time.time()
        output_list = insertion_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if (select == 2):
        start_time = time.time()
        output_list = selection_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if (select == 3):
        start_time = time.time()
        output_list = quicksort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if (select == 4):
        start_time = time.time()
        output_list = heap_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if (select == 5):
        start_time = time.time()
        output_list = shell_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if (select == 6):
        start_time = time.time()
        output_list = merge_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
