from app import db

class Feature(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), index=True)
    value = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'{self.key}={self.value}'
