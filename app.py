from app import create_app
import subprocess
import threading
import time
import requests
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = create_app()

def get_ngrok_url():
    """Get the public URL from ngrok API"""
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json()
        for tunnel in tunnels['tunnels']:
            if tunnel['proto'] == 'https':
                return tunnel['public_url']
        return None
    except Exception as e:
        print(f"Could not get ngrok URL: {e}")
        return None

def start_ngrok():
    """Start ngrok tunnel in a separate thread"""
    try:
        # Kill any existing ngrok processes
        subprocess.run(['taskkill', '/f', '/im', 'ngrok.exe'], 
                      capture_output=True, shell=True)
        time.sleep(2)
        
        # Start ngrok tunnel with correct path
        if sys.platform == "win32":
            # Windows - start in new console window
            subprocess.Popen(['ngrok/ngrok.exe', 'http', '5000'], 
                            creationflags=0x00000010)  # CREATE_NEW_CONSOLE value
        else:
            # Unix/Linux/Mac - start normally
            subprocess.Popen(['./ngrok/ngrok', 'http', '5000'])
            
        print("🚀 ngrok tunnel started! Check http://127.0.0.1:4040 for public URL")
        
        # Wait a bit for tunnel to establish and then print the URL
        time.sleep(5)
        public_url = get_ngrok_url()
        if public_url:
            print(f"🌐 Public URL: {public_url}")
            notify_ngrok_url()
        else:
            print("⚠️ Could not retrieve public URL")
            
    except Exception as e:
        print(f"Could not start ngrok: {e}")

# Fetch https://ecoshare-backend-api.vercel.app/api/ngrok with a POST request passing the ngrok URL and id from env
def notify_ngrok_url():
    """Notify the backend API with the ngrok URL"""
    public_url = get_ngrok_url()
    ngrok_id = os.getenv('NGROK_ID')
    ngrok_api = os.getenv('NGROK_API')
    
    if not ngrok_id:
        print("⚠️ NGROK_ID not found in environment variables")
        return
    
    if not ngrok_api:
        print("⚠️ NGROK_API not found in environment variables")
        return
        
    if public_url:
        try:
            response = requests.post(ngrok_api, json={"url": public_url, "id": ngrok_id})
            if response.status_code == 200:
                print(f"✅ Successfully notified backend API with ngrok URL")
            else:
                print(f"❌ Failed to notify backend API: {response.status_code}")
        except Exception as e:
            print(f"Could not notify backend API: {e}")
    else:
        print("⚠️ No public URL to notify")

if __name__ == '__main__':
    # Start ngrok in background
    ngrok_thread = threading.Thread(target=start_ngrok)
    ngrok_thread.daemon = True
    ngrok_thread.start()
    
    # Small delay to let ngrok start
    time.sleep(3)
    
    # Start Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
