from flask import Flask, request
from flask import render_template

app = Flask(__name__)

contacts = {
    # '1': {'id': 1, 'name': 'Dan', 'email': 'vietnamezul@gmail.com', 'phone': '0899592515'},
    # '2': {'id': 1, 'name': 'Bula', 'email': 'bula@gmail.com', 'phone': '0899592515'},
    # '3': {'id': 1, 'name': 'Strula', 'email': 'strula@gmail.com', 'phone': '0899592515'},
    }
the_id = 0
@app.route("/", methods=['GET', 'POST'])

def hello():
    
    global the_id
    if request.method == "POST":
        # This is what the user types
        # name_contact = request.form.get('name_contact')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        contacts[the_id] = {'id': the_id, 'name': name, 'email': email, 'phone': phone}
        the_id += 1
        # contacts.update({'name': name, 'email': email, 'phone': phone})
        # contacts.update({'name_contact': name_contact, 'value_contact': {'name': name, 'email': email, 'phone': phone}})
    return render_template('contacts.html', data=contacts.values())
    
@app.route("/delete", methods=['POST'])
def delete_contact():
    id = int(request.form.get('contact_to_delete'))
    del(contacts[id])
    return render_template('contacts.html', data=contacts.values())
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

