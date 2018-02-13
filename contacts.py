from flask import Flask, request
from flask import render_template

app = Flask(__name__)

contacts = {
    'Dan': {'name': 'Dan', 'email': 'vietnamezul@gmail.com', 'phone': '0899592515'},
    'Bula': {'name': 'Bula', 'email': 'bula@gmail.com', 'phone': '0899592515'},
    'Strula': {'name': 'Strula', 'email': 'strula@gmail.com', 'phone': '0899592515'},
    }

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        # This is what the user types
        name_contact = request.form.get('name_contact')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        
        contacts[name] = {'name': name, 'email': email, 'phone': phone}
        
        # contacts.update({'name': name, 'email': email, 'phone': phone})
        # contacts.update({'name_contact': name_contact, 'value_contact': {'name': name, 'email': email, 'phone': phone}})
    return render_template('contacts.html', data=contacts.values())
    
@app.route("/delete", methods=['POST'])
def delete_contact():
    name_to_delete = request.form.get('contact_to_delete')
    del(contacts[name_to_delete])
    return render_template('contacts.html', data=contacts.values())
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

