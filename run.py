from app import create_app, db

app = create_app('development')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')