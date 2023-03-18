
from utils import get_data, get_filtered_data, get_laste_data, get_formatted_data
import json


def main():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    OPEARATOINS_URL = data
    COUNT_LASTE_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data, info = get_data(OPEARATOINS_URL)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_laste_data(data, COUNT_LASTE_VALUES)
    data = get_formatted_data(data)
    for row in data:
        print(row)


if __name__ == "__main__":
    main()
