from application import db

from application.models import Base, Nimellinen


class RaakaAine(Base, Nimellinen):



    def __init__(self, name):
        self.name = name

