from application import app

@app.route('/')
def check_status():
    return "Everything is OK"
