from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
      return render_template('index.html')

@app.route('/health')
def health():
      return jsonify({"status": "healthy", "version": "1.0"})

@app.route('/api/users')
def users():
      return jsonify({
          "users": [
              {"id": 1, "name": "Alice", "role": "DevOps Engineer"},
              {"id": 2, "name": "Bob",   "role": "Developer"}
          ]
      })

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000, debug=True)

