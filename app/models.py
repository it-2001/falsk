from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship


class ProductType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    birth = Column(Integer())

    def __repr__(self):
        return self.name


class Product(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth = Column(Integer(), nullable=False)

    def photo_img(self):
        im = ImageManager()
        productPubViewUrl = url_for("ProductPubView.show", pk=str(self.id))
        if self.photo:
            photoUrl = im.get_url(self.photo)
            return Markup(
                f'<a href="{productPubViewUrl}" class="thumbnail"><img src="{photoUrl}" '
                f'alt="Photo" class="img-rounded img-responsive"></a>'
            )
        else:
            return Markup(
                f'<a href="{productPubViewUrl}"" class="thumbnail"><img src="//:0" '
                f'alt="Photo" class="img-responsive">' '</a>'
            )

    def __repr__(self):
        return self.name


class Client(User):
    __tablename__ = "ab_user"
    extra = Column(String(50), unique=True, nullable=False)
