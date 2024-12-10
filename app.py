import logging
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG,  # Уровень логирования
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[
                        logging.StreamHandler()
                    ])

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Asilhonbtw7@ooptest.cpk2g68mgiaf.eu-north-1.rds.amazonaws.com'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

logging.info("Initializing SQLAlchemy...")
try:
    db = SQLAlchemy(app)
    logging.info("SQLAlchemy initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing SQLAlchemy: {e}")

class Course(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    level = db.Column(db.String(20), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Course {self.name}>"

@app.route('/')
def index():
    logging.info("Handling '/' route...")
    try:
        courses = Course.query.all()
        logging.debug(f"Fetched courses: {courses}")
        return render_template('index.html', courses=courses)
    except Exception as e:
        logging.error(f"Error fetching courses: {e}")
        return f"An error occurred: {e}"

if __name__ == '__main__':
    logging.info("Starting Flask application...")
    app.run(debug=True)
