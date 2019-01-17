from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants/')
def showRest():
    return "This shows all my restaurants"


@app.route('/restaurant/new')
def newRest():
    return "This page creates a restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRest(restaurant_id):
    return "This page will edit restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRest(restaurant_id):
    return "This page will delete a restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu')
@app.route('/restaurant/<int:restaurant_id>')
def showMenu(restaurant_id):
    return "This page will show restaurant menus"


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "Create new menu item"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "Edits a menu item {}".format(menu_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "Deletes a menu item {}".format(menu_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
