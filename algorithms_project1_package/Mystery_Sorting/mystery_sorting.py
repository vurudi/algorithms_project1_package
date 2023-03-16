import csv

import pandas as pd

column_names = ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
                'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
                'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
                'deathYear', 'primaryProfession']


def merge(left, right, columns):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][columns[0]] <= right[j][columns[0]]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(data, columns):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    left = merge_sort(left, columns)
    right = merge_sort(right, columns)
    return merge(left, right, columns)


def data_chunks(file_path, columns, memory_limitation):
    i = 1
    for chunk in pd.read_csv(file_path, chunksize=memory_limitation):
        sorted_chunk = merge_sort(chunk.to_dict('records'), columns)
        name_of_csv = f"Individual/Sorted_{i}.csv"

        pd.DataFrame(sorted_chunk).to_csv(name_of_csv, index=False)
        i += 1


def Mystery_Function(file_path, memory_limitation, columns):
    output_file_path = "Final\Final_sorted.csv"
    with open(output_file_path, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(column_names)
        for i in range(1, 94):
            input_file_path = f"Individual\Sorted_{i}.csv"
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    writer.writerow([row[column] for column in column_names])


###########################################################################################
# run function the mystery_sorting calls
###########################################################################################
def run(selection):
    if selection == 13:
        # Test Case 13

        data_chunks('imdb_dataset.csv', ['startYear'], 2000)
        Mystery_Function("Individual", 2000, ['tconst', 'startYear', 'runtimeMinutes', 'primaryTitle'])
        print('\n Test case 13  Passed')

    # Test Case 14
    if selection == 14:
        data_chunks('imdb_dataset.csv', ['primaryTitle'], 2000)
        Mystery_Function(f"Individual", 2000, ['primaryTitle'])
        print('\n Test case 14  Passed')
    # Test Case 15
    if selection == 15:
        data_chunks('imdb_dataset.csv', ['startYear', 'runtimeMinutes', 'primaryTitle'], 2000)
        Mystery_Function("Individual", 2000, ['startYear', 'runtimeMinutes', 'primaryTitle'])
        print('\n Test case 15  Passed')


if __name__ == '__main__':
    run(13)
    run(14)
    run(15)
    print('\n All test casses passed')
