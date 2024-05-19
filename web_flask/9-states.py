#!/usr/bin/python3
""" This script starts a Flask web application """


from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Displays an HTML page that contains a list of
    all State objects present in DBStorage sorted by name
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state_id(id):
    """
    Displays an HTML page that contains the list of all cities
    linked to a state id
    """
    if id:
        key = '{}.{}'.format('State', id)
        state = storage.all(State).get(key)
    return render_template('9-states.html', id=id, state=state)


@app.teardown_appcontext
def removesession(self):
    """
    Removes the current SQLAlchemy Session after
    each request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
