from src import create_app, db
from src.restaurant.models import Modifier, MenuItem

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'MenuItem': MenuItem, 'Modifier': Modifier}
