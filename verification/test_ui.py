
import os
import http.server
import socketserver
import threading
from playwright.sync_api import sync_playwright

PORT = 8081

def start_server():
    # Serve the root directory so we can access verification/index.html and verification/resumes.json
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

def verify_ui():
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to the page
        # The browser will look for resumes.json relative to the HTML file.
        # Since we access /verification/index.html, it requests /verification/resumes.json, which exists.
        page.goto(f"http://localhost:{PORT}/verification/index.html")
        
        # Wait for data to load - specific text from the mocked json
        try:
            page.wait_for_selector("text=Backend", timeout=5000)
            page.wait_for_selector("text=Fullstack", timeout=5000)
        except Exception as e:
            print(f"Error waiting for content: {e}")
            page.screenshot(path="verification_error.png", full_page=True)
            raise e
        
        # Take a screenshot
        page.screenshot(path="verification.png", full_page=True)
        print("Screenshot saved to verification.png")
        
        browser.close()

if __name__ == "__main__":
    verify_ui()
