from app.extensions import login_manager
from app.models.user import User


"""
here i make the relevant imports for my models to prevent having to make them repeatedly elsewhere
and also set up the user loader
"""

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
