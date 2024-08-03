from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(1024), default='')
    priority = db.Column(db.Integer, default=1)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'description': self.description,
            'priority': self.priority
        }
