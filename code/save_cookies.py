from playwright.sync_api import sync_playwright
import os

def generate_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to Instagram...")
        page.goto("https://www.instagram.com/")
        
        print("\n*** ACTION REQUIRED ***")
        print("1. Log into your account in the browser window.")
        print("2. Handle any 2FA or 'Save Info' prompts.")
        input("3. Once you can clearly see your feed, press ENTER in this terminal to continue... ")

        print("Saving session data...")
        context.storage_state(path="session.json")
        
        print("Success! Session saved as 'session.json'.")
        
        browser.close()

if __name__ == "__main__":
    generate_session()