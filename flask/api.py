# put and delete - http verbs
# working with API's - json

from flask import Flask, jsonify, request

app = Flask(__name__)

# initial dataset in my to do list

items = [
    {'id': 1, 'name': 'item1', 'desc':'this is item1'},
    {'id': 2, 'name': 'item2', 'desc':'this is item2'}
]

@app.route('/')
def home():
    return 'welcome to the sample to do list app'

# get: retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# get: retrieve specific item with using an id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'item not found'})
    return jsonify(item)

# post: create a new tasl - API
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'item not found'})
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'desc': request.json['desc']
    }
    items.append(new_item)
    return jsonify(new_item)

# put - update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error':'item not found'})
    item['name'] = request.json.get('name', item['name'])
    item['desc'] = request.json.get('desc', item['desc'])
    return jsonify(item)

# delete - delete an item with a specific id
@app.route('/items/<int:item_id>', methods=['DELETE'])
def del_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': f'{item_id} item was deleted'})

if __name__ == '__main__':
    app.run(debug = True)