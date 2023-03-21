import json

from utils import get_filtered_data, get_laste_data, get_formatted_data

def main():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    ex_data = get_filtered_data(data)
    ls_data = get_laste_data(ex_data, 5)
    fr_data = get_formatted_data(ls_data)

    result = '\n'.join(fr_data)
    print(result)

if __name__ == "__main__":
    main()
