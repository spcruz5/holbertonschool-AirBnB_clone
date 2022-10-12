#!/usr/bin/python3
"""
Class BaseModel
"""

from datetime import datetime
import uuid
# dtm = dateformat
dtm = "%Y-%m-%dT%H:%M:%S.%f"
value = "2017-06-14T22:31:03.285259"


class BaseModel:
    """Base Model"""
    def __init__(self, *args, **kwargs):
        
            self.created_at = datetime.strptime(value, dtm)
            self.updated_at = datetime.strptime(value, dtm)
            self.id = str(uuid.uuid4)
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns the class name, id and dictionary attrbutes"""
        return "[{}] ({}) {}" .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates public instance attribute update_at with the actual date and hour"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary that contains all the keys / values of instance dictionary"""
        dic = {
            
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.strftime(dtm),
            'id': self.id,
            'created_at': self.created_at.strftime(dtm),
        }
        return dic
