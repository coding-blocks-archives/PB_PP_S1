from flask import Flask , render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_database.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200) , nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __str__(self):
        return 'Task: {}'.format(self.id)

@app.route('/', methods=['GET' , 'POST'])
def index():
    print('here ', request.method)
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error adding your task'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

