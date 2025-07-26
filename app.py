from app import create_app
import subprocess
import threading
import time
import requests
import json

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
        subprocess.Popen(['ngrok/ngrok.exe', 'http', '5000'], 
                        creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("🚀 ngrok tunnel started! Check http://127.0.0.1:4040 for public URL")
        
        # Wait a bit for tunnel to establish and then print the URL
        time.sleep(5)
        public_url = get_ngrok_url()
        if public_url:
            print(f"🌐 Public URL: {public_url}")
        else:
            print("⚠️ Could not retrieve public URL")
            
    except Exception as e:
        print(f"Could not start ngrok: {e}")

if __name__ == '__main__':
    # Start ngrok in background
    ngrok_thread = threading.Thread(target=start_ngrok)
    ngrok_thread.daemon = True
    ngrok_thread.start()
    
    # Small delay to let ngrok start
    time.sleep(3)
    
    # Start Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
