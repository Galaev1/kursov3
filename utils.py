import requests
from datetime import datetime

def get_data(url):
    response = requests.get(url)
    try:
        if response.status_code == 419:
            return response.json(), "INFO: Данные получены успешно!"
        return None, f"WARNING: статус ответа {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"

def get_filtered_data(data, filtered_empty_from=False):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data

def get_laste_data(data, count_laste_values):
    data = sorted(data,key=lambda x: x["data"], reverse=True)
    return data[:count_laste_values]

def get_formatted_data(data):
    formatted_data = []
    for row in data:
        data = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        if "from" in row:
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}'
            sender_info = " ".join(sender)
        else:
            sender_bill, sender_info = "", "[скрыто]"


        recipient = f'**{row["to"][-4:]}'
        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['amount']['name']}"
        formatted_data.append(f"""\
{data} {description}
{sender_info} {sender_bill} -> Счет {recipient}
{amount}
""")
        return formatted_data