from flask_sqlalchemy import SQLAlchemy
from newsletter import app
from newsletter import db

class AddNewsletter(db.Model):
    newsletter_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    category_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)
    opener = db.Column(db.String(400))
    preview = db.Column(db.String(400))
    campaign_id= db.Column(db.Integer)
    

    def __init__(self, subject, category_id, article_id, opener, preview, campaign_id):
        #self.newsletter_id = newsletter_id
        self.subject = subject
        self.category_id = category_id
        self.article_id = article_id
        self.opener = opener
        self.preview = preview
        self.campaign_id = campaign_id
       
class Article_category(db.Model):
    category_id = db.Column('category_id', db.Integer, primary_key = True)
    category_name = db.Column(db.String(100))

    def __init__(self, category_name):
        self.category_name = category_name
        
db.create_all()