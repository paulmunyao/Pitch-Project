from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Welocome to the Den"