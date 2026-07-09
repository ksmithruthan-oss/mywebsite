from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if name and email and message:
        return jsonify({'success': True, 'message': 'Message received! Thank you for contacting us.'})
    else:
        return jsonify({'success': False, 'error': 'Please fill in all fields.'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
