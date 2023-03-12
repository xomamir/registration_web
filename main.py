from models import models


import flask


app: flask.app.Flask = flask.Flask(__name__)
users: list[models.User] = []

@app.route('/reg', methods=['GET','POST'])
def registration() -> flask.Response:
    if flask.request.method == "POST":
        data: dict = flask.request.form
        users.append(
            models.User.create_user(**data, users=users)
        )
        
    return flask.render_template(
        template_name_or_list="index.html"
    )

@app.route('/login', methods=['GET','POST'])
def login() -> flask.Response:
    if flask.request.method == "POST":
        data: dict = flask.request.form
        for i in users:
            if (
                i.login == data.get('login')) and(
                i.password == data.get('password')
            ):
                return "OK"
        
    return flask.render_template(
        template_name_or_list="login.html"
    )



if __name__ == "__main__":
    app.run(
        port=8080,
        debug=True
    )