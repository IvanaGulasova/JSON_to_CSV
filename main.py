import json
import csv

def main():
    relative_path = "data.json"
    keys_needed = ["category", "difficulty", "question", "correct_answer"]
    json_to_csv(relative_path, keys_needed)

def json_to_csv(rel_path: str, keys_needed: list) -> csv:
    dicts = check_file(rel_path)

    result = []

    for dict in dicts:
        result.append(sort_keys(dict, keys_needed))

    print("A new csv file is created..")
    record_to_csv("questions.csv", result)

def check_file(file_path: str):
    try:
        with open(file_path) as json_f:
            print("Loading the file..")
            return json.load(json_f)

    except FileNotFoundError:
        print(
            "The file does not exist!",
            "The application terminates..",
            sep="\n"
        )
        quit()

def sort_keys(dicts: dict, keys_needed: list) -> dict:
    new_dict = {}

    for key in dicts:
        if key not in keys_needed:
            continue
        new_dict[key] = dicts[key]

    return new_dict

def record_to_csv(new_file_name: str, data: dict ) -> csv:
    with open(new_file_name, "w") as csv_f:
        header = data[0].keys()
        record = csv.DictWriter(csv_f, fieldnames= header, delimiter="/")

        record.writeheader()
        record.writerows(data)

if __name__=="__main__":
    main()