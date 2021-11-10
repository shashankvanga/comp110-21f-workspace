"""Utility functions."""

__author__ = "730489843"

# Define your functions below
from csv import DictReader
from typing import final
import matplotlib.pyplot as plt


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a singe column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Returns 'n' number of rows of a table."""
    new_dict: dict[str, list[str]] = {}
    for key in x:
        z: list[str] = []
        
        index: int = y
        if y > len(x[key]):
            index = len(x[key])

        for i in range(index):
            z.append(x[key][i])
        
        new_dict[key] = z

    return new_dict


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Returns a column-based table with specific subset of columns."""
    new_dict: dict[str, list[str]] = {}
    for row in y:
        new_dict[row] = x[row]
        
    return new_dict


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a column-based rable with two column-based tables combined."""
    new_dict: dict[str, list[str]] = {}
    for key in x:
        new_dict[key] = x[key]
    for key in y:
        if key in new_dict:
            for value in y[key]:
                new_dict[key].append(value)
        else:
            new_dict[key] = y[key]
        
    return new_dict


def count(x: list[str]) -> dict[str, int]:
    """Returns a dictionary where each key is a unique value in the list, and each value is the frequency."""
    new_dict: dict[str, int] = {}
    for i in x:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    return new_dict


def filter_data(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    x: list[dict[str, str]] =[]
    for row in rows:
        if row["hours_online_social"] not in ["None", ""]:
            x.append(row)
    return x


def table(x: dict[str, list[str]]) -> dict[str, dict[str, str]]:
    """Returns a dictionary with values that are the frequency of the keys."""
    categories = x["hours_online_social"]
    final_dict = {}
    for i in range(len(x["hours_online_social"])):
        category = x["hours_online_social"][i]
        lesson_time = x["lesson_time"][i]

        if category not in final_dict:
            final_dict[category] = {lesson_time: 1} # first entry for this specific lesson time in this specific category
        
        elif lesson_time not in final_dict[category]:
            final_dict[category][lesson_time] = 1 # adding a new lesson_time to the existing category

        else:
            final_dict[category][lesson_time] += 1

    return final_dict


def scores_dict(x: dict[str, dict[str, str]]) -> dict[str, float]:
    """Returns the proportion of high-pointers (6, 7)."""
    new_dict = {}
    for i in x:
        score_six = x[i]["6"]
        score_seven = x[i]["7"]

        total = 0

        for y in x[i]:
            total += int(x[i][y])

        score = (score_six + score_seven) / total
    
        new_dict[i] = score
    
    return new_dict


def plot_bar_chart(x: dict[str, float]):
    """Plots a bar graph."""
    categories = []
    scores = []

    for key in x:
        categories.append(key) 
        scores.append(x[key])

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(categories, scores)
    
    plt.xlabel("Hours spent on social media")
    plt.ylabel("Proportion of students who marked 6 or 7")
    plt.title("Proportion of students finishing lessons on time (6 or 7) vs hours spent on social media")

    plt.show()


def plot_pie_chart(x: dict[str, dict[str, str]]):
    """Plots a pie chart."""

    for key in x:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        plt.rcParams['text.color'] = 'white'
        scores = [1, 2, 3, 4, 5, 6, 7]
        frequencies = [0, 0, 0, 0, 0, 0, 0]

        for y in x[key]:
            frequencies[int(y) - 1] = x[key][y]
            
        ax.pie(frequencies, labels = scores,autopct='%1.2f%%')
    
        plt.title(f"Frequency of {key}")
    plt.show()