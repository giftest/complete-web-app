from bottle import route, run, template, get, post, request, response, redirect
import dataset

db = dataset.connect("sqlite:///shopping_list.db")

@route('/')
@route('/list')
def get_list():
    items = [dict(item) for item in db['list'].find()]
    shopping_list = [{"id":item['id'], "desc":item['description']} for item in items]
    return template('shopping_list.tpl', shopping_list=shopping_list)

@get("/add")
def get_add():
    return template('add_item.tpl')

@post("/add")
def post_add():
    description = request.forms.get("description")
    print(f"post was called. description={description}")
    db['list'].insert({"description":description})
    redirect("/")

@route("/delete/<id>")
def get_delete(id):
    db['list'].delete(id=id)
    redirect("/")

@route("/edit/<id>")
def get_edit(id):
    items = [dict(item) for item in db['list'].find(id=id)]
    if len(items) != 1:
        redirect('/')
    item = items[0]
    return template('edit_item.tpl', id=item['id'], description=item['description'])

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    db['list'].update({'id':id, 'description':description},['id'])
    redirect("/list")

run(host='localhost', port=8080)