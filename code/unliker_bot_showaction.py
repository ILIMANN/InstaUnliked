from playwright.sync_api import sync_playwright
import json


def generate_session():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        with open('session.json', 'r') as file:
            data = json.load(file)
        cookies = data["cookies"]
        
        context.add_cookies(cookies)

        print("Navigating to Instagram...")
        page.goto("https://www.instagram.com/your_activity/interactions/likes/")
        
        isCompleted = False
        while(True):
            page.get_by_text("Select").click()
            button = page.get_by_label("Image with button")

            if button.count()==0:
                print("No posts found!")
                isCompleted = True
                break
            
            i=0
            while i<100:
                if i>button.count()-1:
                    print("No more posts to unlike!")
                    isCompleted=True
                    break
                                
                button.nth(i).click()
                i+=1
                page.wait_for_timeout(200)
            
            page.get_by_text("Unlike").click()
            page.get_by_role("button").filter(has_text="Unlike").click()
            
            if isCompleted is True:
                break
        
            page.reload()
            page.wait_for_timeout(5000)
        
        
        print("=================================================================")
        print("Progress Done!")        
        
        browser.close()
        

if __name__ == "__main__":
    generate_session()