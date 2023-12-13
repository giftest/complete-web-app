import dataset

db = dataset.connect("sqlite:///shopping_list.db")
items = [dict(item) for item in db['list'].find()]
print(items)

items = [dict(item) for item in db['list'].find(id=3)]
print(items)
