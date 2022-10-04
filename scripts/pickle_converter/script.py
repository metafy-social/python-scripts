import pickle
import pprint
import json


def convert_pickle(pickle_file="sample.pickle", target_file='txt'):
    obj = pickle.load(open(pickle_file, "rb"))

    if target_file == 'txt':
        with open("out.txt", "a") as f:
            pprint.pprint(obj, stream=f)

    elif target_file == 'json':
        json_obj = json.loads(json.dumps(obj, default=str))

        with open('out.json', 'w', encoding='utf-8') as outfile:
            json.dump(json_obj, outfile, ensure_ascii=False, indent=2)

    else:
        print("please enter a valid doc type: 'txt', 'json'")
