#!/usr/bin/python3
""" This script starts a Flask web application """


from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def removesession():
        """
    Removes the current SQLAlchemy Session after
    each request
    """
            storage.close()


            @app.route('/states_list', strict_slashes=False)
            def states_list():
                    """
    Displays an HTML page that contains a list of
    all State objects present in DBStorage sorted by name
    """
                        obj_dct = storage.all(State)
                            return render_template('7-states_list.html', obj_dct)


                        if __name__ == '__main__':
                                app.run(host='0.0.0.0', port=5000)
