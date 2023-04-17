from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
import pickle
from forms import ModelForm


app = Flask(__name__)
# commented datbase code
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'

# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ip = db.Column(db.String(200), nullable=False)
#     browser = db.Column(db.String(500), nullable=False)
#     visited_at = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<User %r>' % self.id

# class Feature(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     x1 = db.Column(db.Float, nullable=False)
#     x2 = db.Column(db.Float, nullable=False)
#     x3 = db.Column(db.Float, nullable=False)
#     y_predicted = db.Column(db.Float, nullable=False)
#     y_actual = db.Column(db.Float, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Feature %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():    
    form = ModelForm()
    if form.validate_on_submit():
        with open('notebooks/y_x1_x2_x3_model.pkl', 'rb') as file:
            model = pickle.load(file)        
        x1 = form.x1.data
        x2 = form.x2.data
        x3 = form.x3.data
        new_data_point = [[x1, x2, x3]]
        # Make a prediction using the trained model
        y_pred = model.predict(new_data_point)        
        y_predicted = y_pred[0]
        y_actual = (x1+x2)*x3
        return render_template('home.html', form=form, y_predicted=y_predicted, y_actual=y_actual)
    return render_template('home.html', form=form)


# not required database
# with app.app_context():
#     db.create_all()


if __name__ == "__main__":    
    app.run(host="0.0.0.0", debug=True)
