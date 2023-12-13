import dataset

db = dataset.connect("sqlite:///shopping_list.db")

try:
    db.begin()
    db['list'].drop()
    table = db['list']
    items = [
        {"description":"apples", "quantity":12, "variety":"golden delicious" },
        {"description":"broccoli", "quantity":4},
        {"description":"pizza", "quantity":1, "toppings":"cheese, pepperoni"},
        {"description":"tangerine", "quantity":3},
        {"description":"potatoes", "quantity":6},
        ]
    # for item in items:
    #     table.insert(item)
    table.insert_many(items)
    db.commit()
except Exception as e:
    db.rollback()

print("done.")

