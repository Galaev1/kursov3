from utils import get_data, get_filtered_data, get_laste_data, get_formatted_data


def main():
    OPEARATOINS_URL = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678990788899&signature=T5o3zc1S8Whs4ihvCoRYOm3p0uzScj6Hm3_VOx6t-Qs&downloadName=operations.json'
    COUNT_LASTE_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data, info = get_data(OPEARATOINS_URL)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = get_filtered_data(data,FILTERED_EMPTY_FROM)
    data = get_laste_data(data, COUNT_LASTE_VALUES)
    data = get_formatted_data(data)
    for row in data:
        print(row)

if __name__ == "__main__":
    main()