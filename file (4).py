from flask import Flask, redirect

app = Flask(__name__)
users = []


# create user with unique id
def create_user(name, ID=[0]):
    ID[0] += 1
    return {"ID": str(ID[0]), "name": name}


# returns all users
@app.route("/users")
def get_users():
    return str(users)


# adds user to the list
@app.route("/users/create/<name>")
def add_user(name):
    users.append(create_user(name))
    return redirect("/users")


# removes user from the list
@app.route("/users/remove/<ID>")
def remove_user(ID):
    for i, user in enumerate(users):
        if user["ID"] == ID:
            del users[i]
            break
    return redirect("/users")


# update user from the list
@app.route("/users/update/<ID>/<name>")
def update_user(ID, name):
    for user in users:
        if user["ID"] == ID:
            user["name"] = name
    return redirect("/users")


if __name__ == "__main__":
    app.run()




"/users"
"/users/create/<name>"
"/users/remove/<ID>"
"/users/update/<ID>/<name>"
