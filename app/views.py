from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView
from flask_appbuilder.widgets import ListBlock, ShowBlockWidget
from wtforms.validators import NumberRange
import datetime

from . import appbuilder, db
from .models import Product, ProductType


class ProductPubView(ModelView):
    datamodel = SQLAInterface(Product)
    base_permissions = ["can_list", "can_show"]
    list_widget = ListBlock
    show_widget = ShowBlockWidget

    list_columns = ["id", "name", "birth"]
    search_columns = ["id", "name", "birth"]


class PersonView(ModelView):
    datamodel = SQLAInterface(Product)
    validators_columns = {
        "birth": [NumberRange(min=1900, max=datetime.date.year, message="year not specified")]
    }


db.create_all()
appbuilder.add_view(ProductPubView, "Our people", icon="fa-folder-open-o")
appbuilder.add_view(
    PersonView, "people", icon="fa-folder-open-o", category="Management"
)
