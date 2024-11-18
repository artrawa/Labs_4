# TODO решите задачу
import json
from itertools import product

filename = 'input.json'
indent = None  # TODO Подставьте любое целое число
ensure_ascii = True  # TODO Замените на значение True


def task() -> float:
    with open(filename) as file:
        data = json.load(file)
        product = []
        for i in range(len(data)):
           product.append(data[i].get("score") * data[i].get("weight"))
        output = sum(product)
    return(round(output,3))

print(task())
