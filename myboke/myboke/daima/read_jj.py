import json
def read_jjbo():
    with open("../data/data_wa.json", "r", encoding="utf_8") as f:
        data = json.load(f)
        list_data = []
        for item in data:
            tem = tuple(item.values())
            list_data.append(tem)

    return list_data