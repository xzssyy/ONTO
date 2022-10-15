import json


def find_id(name, data):
    for attribute in data['classAttribute']:
        if attribute.get('label'):
            if attribute['label'].get('IRI-based'):
                if attribute['label']['IRI-based'] == name:
                    return (int(attribute['id']))
                    break;

    return None


word = open("CSCL.json", encoding="utf-8")
data = json.load(word)
name = 'ds'
print(find_id(name, data))
