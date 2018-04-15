import json
import os

def save(obj, path, fname):
    if not os.path.exists(path):
        os.mkdir(path)

    with open(os.path.join(path, fname), "w") as f:
        json.dump(obj, f, ensure_ascii=False)

def load(path, fname):
    if not os.path.exists(path):
        return None

    with open(os.path.join(path, fname)) as f:
        return json.load(f)
