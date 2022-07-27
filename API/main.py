from database import Database
from Controllers import StudentsController
from flask_cors import CORS

app = Database.app
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def register_routes():
    app.register_blueprint(StudentsController.bp)


if __name__ == '__main__':
    register_routes()
    print(app.url_map)
    app.run(port=6000)
