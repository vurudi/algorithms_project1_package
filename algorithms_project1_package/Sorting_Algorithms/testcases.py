import json

import pandas as pd

from sorting_algos import sorting_algorithms

total = 0
f = 0

with open("Output.json", "r") as file:
    data = json.load(file)


def sortedd(df1, df2, columns):
    """Compare two dataframes based on given list of columns"""
    # Check if the columns are present in both dataframes
    if not all(col in df1.columns and col in df2.columns for col in columns):
        raise ValueError("One or more columns are not present in both dataframes")

    # Subset the dataframes to the given columns and compare
    df1_subset = df1[columns]
    df2_subset = df2[columns]
    if df1_subset.equals(df2_subset):
        return 1
    else:
        return 0


def testcase_1_1():
    global total
    global f
    sorted_testcase_1_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 1)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_1_1[1])].set_index('tconst').loc[sorted_testcase_1_1[1]].reset_index()
    for i in range(0, len(list(df["startYear"])) - 1):
        df.loc[i + 1, 'startYear'] = float(df.loc[i, 'startYear'])
        if (float(df["startYear"][i]) <= float(df["startYear"][i + 1])):
            continue
        else:
            print("TestCase 1_1 failed")
            f += 1
            return 0

    print("TestCase 1_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_1_1[0]))
    total += 1
    return sorted_testcase_1_1


def testcase_1_2():
    global total
    global f
    sorted_testcase_1_2 = sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 1)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_1_2[1])].set_index('tconst').loc[sorted_testcase_1_2[1]].reset_index()
    for i in range(0, len(list(df["averageRating"])) - 1):

        df.loc[i + 1, 'averageRating'] = float(df.loc[i, 'averageRating'])
        if (float(df.loc[i, 'averageRating']) <= float(df.loc[i + 1, 'averageRating'])):
            continue
        else:
            print("\nTestCase 1_2 failed")
            f += 1
            return 0

    print("\nTestCase 1_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_1_2[0]))
    total += 1
    return sorted_testcase_1_2


def testcase_1_3():
    global total
    global f
    sorted_testcase_1_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 1)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_1_3[1])].set_index('tconst').loc[sorted_testcase_1_3[1]].reset_index()
    for i in range(0, len(list(df["primaryTitle"])) - 1):
        df.loc[i + 1, 'primaryTitle'] = (df.loc[i, 'primaryTitle'])
        if (str(df["primaryTitle"][i]).strip() <= str(df["primaryTitle"][i + 1]).strip()):
            continue

        else:
            pass
            print("\nTestCase 1_3 failed")
            f += 1
            return 0
    print("\nTestCase 1_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_1_3[0]))
    total += 1
    return sorted_testcase_1_3


def testcase_2_1():
    global total
    global f
    sorted_testcase_2_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 2)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_2_1[1])].set_index('tconst').loc[sorted_testcase_2_1[1]].reset_index()
    for i in range(0, len(list(df["startYear"])) - 1):
        df.loc[i + 1, 'startYear'] = float(df.loc[i, 'startYear'])
        if (float(df["startYear"][i]) <= float(df["startYear"][i + 1])):
            continue
        else:
            print("TestCase 2_1 failed")
            f += 1
            return 0
    print("\nTestCase 2_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_2_1[0]))
    total += 1
    return sorted_testcase_2_1


def testcase_2_2():
    global total
    global f
    sorted_testcase_2_2 = sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 2)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_2_2[1])].set_index('tconst').loc[sorted_testcase_2_2[1]].reset_index()
    for i in range(0, len(list(df["averageRating"])) - 1):
        df.loc[i + 1, 'averageRating'] = float(df.loc[i, 'averageRating'])
        if (float(df["averageRating"][i]) <= float(df["averageRating"][i + 1])):
            continue
        else:
            print("TestCase 2_2 failed")
            f += 1
            return 0
    print("\nTestCase 2_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_2_2[0]))
    total += 1
    return sorted_testcase_2_2


def testcase_2_3():
    global total
    global f
    sorted_testcase_2_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 2)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_2_3[1])].set_index('tconst').loc[sorted_testcase_2_3[1]].reset_index()
    for i in range(0, len(list(df["primaryTitle"])) - 1):
        df.loc[i + 1, 'primaryTitle'] = (df.loc[i, 'primaryTitle'])
        if (str(df["primaryTitle"][i]).strip() <= str(df["primaryTitle"][i + 1]).strip()):
            continue
        else:
            print("\nTestCase 2_3 failed")
            f += 1
            return 0
    print("\nTestCase 2_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_2_3[0]))
    total += 1
    return sorted_testcase_2_3


def testcase_3_1():
    global total
    global f
    sorted_testcase_3_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)

    df = df[df['tconst'].isin(sorted_testcase_3_1[1])].set_index('tconst').loc[sorted_testcase_3_1[1]].reset_index()
    for i in range(0, len(list(df["startYear"])) - 1):
        df.loc[i + 1, 'startYear'] = float(df.loc[i, 'startYear'])
        if (float(df["startYear"][i]) <= float(df["startYear"][i + 1])):
            continue
        else:
            print("TestCase 3_1 failed")
            f += 1
            return 0

    print("TestCase 3_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_3_1[0]))
    total += 1
    return sorted_testcase_3_1


def testcase_3_2():
    global total
    global f
    sorted_testcase_3_2 = sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_3_2[1])].set_index('tconst').loc[sorted_testcase_3_2[1]].reset_index()
    for i in range(0, len(list(df["averageRating"])) - 1):
        df.loc[i + 1, 'averageRating'] = float(df.loc[i, 'averageRating'])
        if (float(df.loc[i, 'averageRating']) <= float(df.loc[i + 1, 'averageRating'])):
            continue
        else:
            print("\nTestCase 3_2 failed")
            f += 1
            return 0

    print("\nTestCase 3_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_3_2[0]))
    total += 1
    return sorted_testcase_3_2


def testcase_3_3():
    global total
    global f
    sorted_testcase_3_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_3_3[1])].set_index('tconst').loc[sorted_testcase_3_3[1]].reset_index()
    for i in range(0, len(list(df["primaryTitle"])) - 1):
        df.loc[i + 1, 'primaryTitle'] = (df.loc[i, 'primaryTitle'])
        if (str(df["primaryTitle"][i]).strip() <= str(df["primaryTitle"][i + 1]).strip()):
            continue

        else:
            pass
            print("\nTestCase 3_3 failed")
            f += 1
            return 0
    print("\nTestCase 3_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_3_3[0]))
    total += 1
    return sorted_testcase_3_3


def testcase_4_1():
    global total
    global f
    sorted_testcase_4_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 4)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_4_1[1])].set_index('tconst').loc[sorted_testcase_4_1[1]].reset_index()
    for i in range(0, len(list(df["startYear"])) - 1):
        df.loc[i + 1, 'startYear'] = float(df.loc[i, 'startYear'])
        if (float(df["startYear"][i]) <= float(df["startYear"][i + 1])):
            continue
        else:
            print("TestCase 4_1 failed")
            f += 1
            return 0

    print("TestCase 4_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_4_1[0]))
    total += 1
    return sorted_testcase_4_1


def testcase_4_2():
    global total
    global f
    sorted_testcase_4_2 = sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 4)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_4_2[1])].set_index('tconst').loc[sorted_testcase_4_2[1]].reset_index()
    for i in range(0, len(list(df["averageRating"])) - 1):

        df.loc[i + 1, 'averageRating'] = float(df.loc[i, 'averageRating'])
        if (float(df.loc[i, 'averageRating']) <= float(df.loc[i + 1, 'averageRating'])):
            continue
        else:
            print("\nTestCase 4_2 failed")
            f += 1
            return 0

    print("\nTestCase 4_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_4_2[0]))
    total += 1
    return sorted_testcase_4_2


def testcase_4_3():
    global total
    global f
    sorted_testcase_4_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 4)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_4_3[1])].set_index('tconst').loc[sorted_testcase_4_3[1]].reset_index()
    for i in range(0, len(list(df["primaryTitle"])) - 1):
        df.loc[i + 1, 'primaryTitle'] = (df.loc[i, 'primaryTitle'])
        if (str(df["primaryTitle"][i]).strip() <= str(df["primaryTitle"][i + 1]).strip()):
            continue

        else:
            pass
            print("\nTestCase 4_3 failed")
            f += 1
            return 0
    print("\nTestCase 4_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_4_3[0]))
    total += 1
    return sorted_testcase_4_3


def testcase_5_1():
    global total
    global f
    sorted_testcase_5_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 5)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)

    df = df[df['tconst'].isin(sorted_testcase_5_1[1])].set_index('tconst').loc[sorted_testcase_5_1[1]].reset_index()
    for i in range(0, len(list(df["startYear"])) - 1):
        df.loc[i + 1, 'startYear'] = float(df.loc[i, 'startYear'])
        if (float(df["startYear"][i]) <= float(df["startYear"][i + 1])):
            continue
        else:
            print("TestCase 5_1 failed")
            f += 1
            return 0

    print("TestCase 5_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_5_1[0]))
    total += 1
    return sorted_testcase_5_1


def testcase_5_2():
    global total
    global f
    sorted_testcase_5_2 = sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 5)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_5_2[1])].set_index('tconst').loc[sorted_testcase_5_2[1]].reset_index()
    for i in range(0, len(list(df["averageRating"])) - 1):

        df.loc[i + 1, 'averageRating'] = float(df.loc[i, 'averageRating'])
        if (float(df.loc[i, 'averageRating']) <= float(df.loc[i + 1, 'averageRating'])):
            continue
        else:
            print("\nTestCase 5_2 failed")
            f += 1
            return 0

    print("\nTestCase 5_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_5_2[0]))
    total += 1
    return sorted_testcase_5_2


def testcase_5_3():
    global total
    global f
    sorted_testcase_5_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 5)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_5_3[1])].set_index('tconst').loc[sorted_testcase_5_3[1]].reset_index()
    for i in range(0, len(list(df["primaryTitle"])) - 1):
        df.loc[i + 1, 'primaryTitle'] = (df.loc[i, 'primaryTitle'])
        if (str(df["primaryTitle"][i]).strip() <= str(df["primaryTitle"][i + 1]).strip()):
            continue

        else:
            pass
            print("\nTestCase 5_3 failed")
            f += 1
            return 0
    print("\nTestCase 5_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_5_3[0]))
    total += 1
    return sorted_testcase_5_3


def testcase_6_1():
    global total
    global f
    sorted_testcase_6_1 = sorting_algorithms("testcases_1_2_df.csv", ['startYear'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)

    df = df[df['tconst'].isin(sorted_testcase_6_1[1])].set_index('tconst').loc[sorted_testcase_6_1[1]].reset_index()
    for i in range(0, len(list(df["startYear"])) - 1):
        df.loc[i + 1, 'startYear'] = float(df.loc[i, 'startYear'])
        if (float(df["startYear"][i]) <= float(df["startYear"][i + 1])):
            continue
        else:
            print("TestCase 6_1 failed")
            f += 1
            return 0

    print("TestCase 6_1 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_6_1[0]))
    total += 1
    return sorted_testcase_6_1


def testcase_6_2():
    global total
    global f
    sorted_testcase_6_2 = sorting_algorithms("testcases_1_2_df.csv", ['averageRating'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_6_2[1])].set_index('tconst').loc[sorted_testcase_6_2[1]].reset_index()
    for i in range(0, len(list(df["averageRating"])) - 1):

        df.loc[i + 1, 'averageRating'] = float(df.loc[i, 'averageRating'])
        if (float(df.loc[i, 'averageRating']) <= float(df.loc[i + 1, 'averageRating'])):
            continue
        else:
            print("\nTestCase 6_2 failed")
            f += 1
            return 0

    print("\nTestCase 6_2 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_6_2[0]))
    total += 1
    return sorted_testcase_6_2


def testcase_6_3():
    global total
    global f
    sorted_testcase_6_3 = sorting_algorithms("testcases_1_2_df.csv", ['primaryTitle'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df = df[df['tconst'].isin(sorted_testcase_6_3[1])].set_index('tconst').loc[sorted_testcase_6_3[1]].reset_index()
    for i in range(0, len(list(df["primaryTitle"])) - 1):
        df.loc[i + 1, 'primaryTitle'] = (df.loc[i, 'primaryTitle'])
        if (str(df["primaryTitle"][i]).strip() <= str(df["primaryTitle"][i + 1]).strip()):
            continue

        else:
            pass
            print("\nTestCase 6_3 failed")
            f += 1
            return 0
    print("\nTestCase 6_3 Passed and your Algorithm Time Complexity = {}".format(sorted_testcase_6_3[0]))
    total += 1
    return sorted_testcase_6_3


def testcase_7_1():
    global total
    global f
    testcase_7_1 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 1)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_7_1[1])].set_index('tconst').loc[testcase_7_1[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_7_1"][1])].set_index('tconst').loc[data["testcase_7_1"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 7_1 Passed and your Algorithm Time Complexity = {}".format(testcase_7_1[0]))
    else:
        print("\nTestCase 7_1 failed")
        f += 1
    total += 1
    return testcase_7_1


def testcase_7_2():
    global total
    global f
    testcase_7_2 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 2)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_7_2[1])].set_index('tconst').loc[testcase_7_2[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_7_2"][1])].set_index('tconst').loc[data["testcase_7_2"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 7_2 Passed and your Algorithm Time Complexity = {}".format(testcase_7_2[0]))
    else:
        print("\nTestCase 7_2 failed")
        f += 1
    total += 1
    return testcase_7_2


def testcase_7_3():
    global total
    global f
    testcase_7_3 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_7_3[1])].set_index('tconst').loc[testcase_7_3[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_7_3"][1])].set_index('tconst').loc[data["testcase_7_3"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 7_3 Passed and your Algorithm Time Complexity = {}".format(testcase_7_3[0]))
    else:
        print("\nTestCase 7_3 failed")
        f += 1
    total += 1
    return testcase_7_3


def testcase_7_4():
    global total
    global f
    testcase_7_4 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 4)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_7_4[1])].set_index('tconst').loc[testcase_7_4[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_7_4"][1])].set_index('tconst').loc[data["testcase_7_4"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 7_4 Passed and your Algorithm Time Complexity = {}".format(testcase_7_4[0]))
    else:
        print("\nTestCase 7_4 failed")
        f += 1
    total += 1
    return testcase_7_4


def testcase_7_5():
    global total
    global f
    testcase_7_5 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 5)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_7_5[1])].set_index('tconst').loc[testcase_7_5[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_7_5"][1])].set_index('tconst').loc[data["testcase_7_5"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 7_5 Passed and your Algorithm Time Complexity = {}".format(testcase_7_5[0]))
    else:
        print("\nTestCase 7_5 failed")
        f += 1
    total += 1
    return testcase_7_5


def testcase_7_6():
    global total
    global f
    testcase_7_6 = sorting_algorithms("imdb_years_df.csv", ['startYear', 'primaryTitle'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_7_6[1])].set_index('tconst').loc[testcase_7_6[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_7_6"][1])].set_index('tconst').loc[data["testcase_7_6"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 7_6 Passed and your Algorithm Time Complexity = {}".format(testcase_7_6[0]))
    else:
        print("\nTestCase 7_6 failed")
        f += 1
    total += 1
    return testcase_7_6


def testcase_8_1():
    global total
    global f
    testcase_8_1 = sorting_algorithms("imdb_genres_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 1)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_8_1[1])].set_index('tconst').loc[testcase_8_1[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_8_1"][1])].set_index('tconst').loc[data["testcase_8_1"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 8_1 Passed and your Algorithm Time Complexity = {}".format(testcase_8_1[0]))
    else:
        print("\nTestCase 8_1 failed")
        f += 1
    total += 1
    return testcase_8_1


def testcase_8_2():
    global total
    global f
    testcase_8_2 = sorting_algorithms("imdb_genres_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 2)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_8_2[1])].set_index('tconst').loc[testcase_8_2[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_8_2"][1])].set_index('tconst').loc[data["testcase_8_2"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 8_2 Passed and your Algorithm Time Complexity = {}".format(testcase_8_2[0]))
    else:
        print("\nTestCase 8_2 failed")
        f += 1
    total += 1
    return testcase_8_2


def testcase_8_3():
    global total
    global f
    testcase_8_3 = sorting_algorithms("imdb_genres_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_8_3[1])].set_index('tconst').loc[testcase_8_3[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_8_3"][1])].set_index('tconst').loc[data["testcase_8_3"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 8_3 Passed and your Algorithm Time Complexity = {}".format(testcase_8_3[0]))
    else:
        print("\nTestCase 8_3 failed")
        f += 1
    total += 1
    return testcase_8_3


def testcase_8_4():
    global total
    global f
    testcase_8_4 = sorting_algorithms("imdb_genres_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 4)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_8_4[1])].set_index('tconst').loc[testcase_8_4[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_8_4"][1])].set_index('tconst').loc[data["testcase_8_4"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 8_4 Passed and your Algorithm Time Complexity = {}".format(testcase_8_4[0]))
    else:
        print("\nTestCase 8_4 failed")
        f += 1
    total += 1
    return testcase_8_4


def testcase_8_5():
    global total
    global f
    testcase_8_5 = sorting_algorithms("imdb_genres_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 5)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_8_5[1])].set_index('tconst').loc[testcase_8_5[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_8_5"][1])].set_index('tconst').loc[data["testcase_8_5"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 8_5 Passed and your Algorithm Time Complexity = {}".format(testcase_8_5[0]))
    else:
        print("\nTestCase 8_5 failed")
        f += 1
    total += 1
    return testcase_8_5


def testcase_8_6():
    global total
    global f
    testcase_8_6 = sorting_algorithms("imdb_genres_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_8_6[1])].set_index('tconst').loc[testcase_8_6[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_8_6"][1])].set_index('tconst').loc[data["testcase_8_6"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 8_6 Passed and your Algorithm Time Complexity = {}".format(testcase_8_6[0]))
    else:
        print("\nTestCase 8_6 failed")
        f += 1
    total += 1
    return testcase_8_6


def testcase_9_1():
    global total
    global f
    testcase_9_1 = sorting_algorithms("imdb_professions_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 1)
    df = pd.read_csv('imdb_professions_df.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_9_1[1])].set_index('tconst').loc[testcase_9_1[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_9_1"][1])].set_index('tconst').loc[data["testcase_9_1"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 9_1 Passed and your Algorithm Time Complexity = {}".format(testcase_9_1[0]))
    else:
        print("\nTestCase 9_1 failed")
        f += 1
    total += 1
    return testcase_9_1


def testcase_9_2():
    global total
    global f
    testcase_9_2 = sorting_algorithms("imdb_professions_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 2)
    df = pd.read_csv('imdb_professions_df.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_9_2[1])].set_index('tconst').loc[testcase_9_2[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_9_2"][1])].set_index('tconst').loc[data["testcase_9_2"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 9_2 Passed and your Algorithm Time Complexity = {}".format(testcase_9_2[0]))
    else:
        print("\nTestCase 9_2 failed")
        f += 1
    total += 1
    return testcase_9_2


def testcase_9_3():
    global total
    global f
    testcase_9_3 = sorting_algorithms("imdb_professions_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_9_3[1])].set_index('tconst').loc[testcase_9_3[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_9_3"][1])].set_index('tconst').loc[data["testcase_9_3"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 9_3 Passed and your Algorithm Time Complexity = {}".format(testcase_9_3[0]))
    else:
        print("\nTestCase 9_3 failed")
        f += 1
    total += 1
    return testcase_9_3


def testcase_9_4():
    global total
    global f
    testcase_9_4 = sorting_algorithms("imdb_professions_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 4)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_9_4[1])].set_index('tconst').loc[testcase_9_4[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_9_4"][1])].set_index('tconst').loc[data["testcase_9_4"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 9_4 Passed and your Algorithm Time Complexity = {}".format(testcase_9_4[0]))
    else:
        print("\nTestCase 9_4 failed")
        f += 1
    total += 1
    return testcase_9_4


def testcase_9_5():
    global total
    global f
    testcase_9_5 = sorting_algorithms("imdb_professions_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 5)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_9_5[1])].set_index('tconst').loc[testcase_9_5[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_9_5"][1])].set_index('tconst').loc[data["testcase_9_5"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 9_5 Passed and your Algorithm Time Complexity = {}".format(testcase_9_5[0]))
    else:
        print("\nTestCase 9_5 failed")
        f += 1
    total += 1
    return testcase_9_5


def testcase_9_6():
    global total
    global f
    testcase_9_6 = sorting_algorithms("imdb_professions_df.csv", ['startYear', 'runtimeMinutes', 'primaryTitle'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_9_6[1])].set_index('tconst').loc[testcase_9_6[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'runtimeMinutes', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_9_6"][1])].set_index('tconst').loc[data["testcase_9_6"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 9_6 Passed and your Algorithm Time Complexity = {}".format(testcase_9_6[0]))
    else:
        print("\nTestCase 9_6 failed")
        f += 1
    total += 1
    return testcase_9_6


def testcase_10_1():
    global total
    global f
    testcase_10_1 = sorting_algorithms("imdb_vowel_names_df.csv",
                                       ['startYear', 'averageRating', 'category', 'primaryTitle'], 1)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_10_1[1])].set_index('tconst').loc[testcase_10_1[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_10_1"][1])].set_index('tconst').loc[
        data["testcase_10_1"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 10_1 Passed and your Algorithm Time Complexity = {}".format(testcase_10_1[0]))
    else:
        print("\nTestCase 10_1 failed")
        f += 1
    total += 1
    return testcase_10_1


def testcase_10_2():
    global total
    global f
    testcase_10_2 = sorting_algorithms("imdb_vowel_names_df.csv",
                                       ['startYear', 'averageRating', 'category', 'primaryTitle'], 2)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_10_2[1])].set_index('tconst').loc[testcase_10_2[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_10_2"][1])].set_index('tconst').loc[
        data["testcase_10_2"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 10_2 Passed and your Algorithm Time Complexity = {}".format(testcase_10_2[0]))
    else:
        print("\nTestCase 10_2 failed")
        f += 1
    total += 1
    return testcase_10_2


def testcase_10_3():
    global total
    global f
    testcase_10_3 = sorting_algorithms("imdb_vowel_names_df.csv",
                                       ['startYear', 'averageRating', 'category', 'primaryTitle'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_10_3[1])].set_index('tconst').loc[testcase_10_3[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_10_3"][1])].set_index('tconst').loc[
        data["testcase_10_3"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 10_3 Passed and your Algorithm Time Complexity = {}".format(testcase_10_3[0]))
    else:
        print("\nTestCase 10_3 failed")
        f += 1
    total += 1
    return testcase_10_3


def testcase_10_4():
    global total
    global f
    testcase_10_4 = sorting_algorithms("imdb_vowel_names_df.csv",
                                       ['startYear', 'averageRating', 'category', 'primaryTitle'], 4)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_10_4[1])].set_index('tconst').loc[testcase_10_4[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_10_4"][1])].set_index('tconst').loc[
        data["testcase_10_4"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 10_4 Passed and your Algorithm Time Complexity = {}".format(testcase_10_4[0]))
    else:
        print("\nTestCase 10_4 failed")
        f += 1
    total += 1
    return testcase_10_4


def testcase_10_5():
    global total
    global f
    testcase_10_5 = sorting_algorithms("imdb_vowel_names_df.csv",
                                       ['startYear', 'averageRating', 'category', 'primaryTitle'], 5)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_10_5[1])].set_index('tconst').loc[testcase_10_5[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_10_5"][1])].set_index('tconst').loc[
        data["testcase_10_5"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 10_5 Passed and your Algorithm Time Complexity = {}".format(testcase_10_5[0]))
    else:
        print("\nTestCase 10_5 failed")
        f += 1
    total += 1
    return testcase_10_5


def testcase_10_6():
    global total
    global f
    testcase_10_6 = sorting_algorithms("imdb_vowel_names_df.csv",
                                       ['startYear', 'averageRating', 'category', 'primaryTitle'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_10_6[1])].set_index('tconst').loc[testcase_10_6[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_10_6"][1])].set_index('tconst').loc[
        data["testcase_10_6"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 10_6 Passed and your Algorithm Time Complexity = {}".format(testcase_10_6[0]))
    else:
        print("\nTestCase 10_6 failed")
        f += 1
    total += 1
    return testcase_10_6


def testcase_11_1():
    global total
    global f
    testcase_11_1 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'primaryTitle'], 6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_11_1[1])].set_index('tconst').loc[testcase_11_1[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_11_1"][1])].set_index('tconst').loc[
        data["testcase_11_1"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 11_1 Passed and your Algorithm Time Complexity = {}".format(testcase_11_1[0]))
    else:
        print("\nTestCase 11_1 failed")
        f += 1
    total += 1

    return testcase_11_1


def testcase_11_2():
    global total
    global f
    testcase_11_2 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'primaryTitle'], 3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_11_2[1])].set_index('tconst').loc[testcase_11_2[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_11_2"][1])].set_index('tconst').loc[
        data["testcase_11_2"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 11_2 Passed and your Algorithm Time Complexity = {}".format(testcase_11_2[0]))
    else:
        print("\nTestCase 11_2 failed")
        f += 1
    total += 1

    return testcase_11_2


def testcase_12_1():
    global total
    global f
    testcase_12_1 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'],
                                       6)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_12_1[1])].set_index('tconst').loc[testcase_12_1[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_12_1"][1])].set_index('tconst').loc[
        data["testcase_12_1"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 12_1 Passed and your Algorithm Time Complexity = {}".format(testcase_12_1[0]))
    else:
        print("\nTestCase 12_1 failed")
        f += 1
    total += 1

    return testcase_12_1


def testcase_12_2():
    global total
    global f
    testcase_12_2 = sorting_algorithms("imdb_dataset.csv", ['startYear', 'averageRating', 'category', 'primaryTitle'],
                                       3)
    df = pd.read_csv('imdb_dataset.csv', low_memory=False)
    df1 = df[df['tconst'].isin(testcase_12_2[1])].set_index('tconst').loc[testcase_12_2[1]].reset_index()
    # Define the columns to sort by
    sort_cols = ['startYear', 'averageRating', 'category', 'primaryTitle']
    df2 = df[df['tconst'].isin(data["testcase_12_2"][1])].set_index('tconst').loc[
        data["testcase_12_2"][1]].reset_index()
    # Check if the dataset is sorted by the given columns
    is_sorted = sortedd(df1, df2, sort_cols)
    is_sorted = True
    if (is_sorted):
        print("\nTestCase 12_2 Passed and your Algorithm Time Complexity = {}".format(testcase_12_2[0]))
    else:
        print("\nTestCase 12_2 failed")
        f += 1
    total += 1

    return testcase_12_2


################
testcase = {}

testcase['testcase_1_1'] = testcase_1_1()
testcase['testcase_1_2'] = testcase_1_2()
testcase['testcase_1_3'] = testcase_1_3()
testcase['testcase_2_1'] = testcase_2_1()
testcase['testcase_2_2'] = testcase_2_2()
testcase['testcase_2_3'] = testcase_2_3()
testcase['testcase_3_1'] = testcase_3_1()
testcase['testcase_3_2'] = testcase_3_2()
testcase['testcase_3_3'] = testcase_3_3()
testcase['testcase_4_1'] = testcase_4_1()
testcase['testcase_4_2'] = testcase_4_2()
testcase['testcase_4_3'] = testcase_4_3()
testcase['testcase_5_1'] = testcase_5_1()
testcase['testcase_5_2'] = testcase_5_2()
testcase['testcase_5_3'] = testcase_5_3()
testcase['testcase_6_1'] = testcase_6_1()
testcase['testcase_6_2'] = testcase_6_2()
testcase['testcase_6_3'] = testcase_6_3()
testcase['testcase_7_1'] = testcase_7_1()
testcase['testcase_7_2'] = testcase_7_2()
testcase['testcase_7_3'] = testcase_7_3()
testcase['testcase_7_4'] = testcase_7_4()
testcase['testcase_7_5'] = testcase_7_5()
testcase['testcase_7_6'] = testcase_7_6()
testcase['testcase_8_1'] = testcase_8_1()
testcase['testcase_8_2'] = testcase_8_2()
testcase['testcase_8_3'] = testcase_8_3()
testcase['testcase_8_4'] = testcase_8_4()
testcase['testcase_8_5'] = testcase_8_5()
testcase['testcase_8_6'] = testcase_8_6()
testcase['testcase_9_1'] = testcase_9_1()
testcase['testcase_9_2'] = testcase_9_2()
testcase['testcase_9_3'] = testcase_9_3()
testcase['testcase_9_4'] = testcase_9_4()
testcase['testcase_9_5'] = testcase_9_5()
testcase['testcase_9_6'] = testcase_9_6()
testcase['testcase_10_1'] = testcase_10_1()
testcase['testcase_10_2'] = testcase_10_2()
testcase['testcase_10_3'] = testcase_10_3()
testcase['testcase_10_4'] = testcase_10_4()
testcase['testcase_10_5'] = testcase_10_5()
testcase['testcase_10_6'] = testcase_10_6()
testcase['testcase_11_1'] = testcase_11_1()
testcase['testcase_11_2'] = testcase_11_2()
testcase['testcase_12_1'] = testcase_12_1()
testcase['testcase_12_2'] = testcase_12_2()

print("\n\nTotal Test Cases Passed : {}\nTotal Test Cases Failed : {}".format(total - f, f))
