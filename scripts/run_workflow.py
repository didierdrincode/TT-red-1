import json
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Load campaign links and data
with open("data/campaigns.json", "r") as f:
    data = json.load(f)

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "redroid"
options.udid = "localhost:5555"
options.automation_name = "UiAutomator2"
options.app_package = "com.zhiliaoapp.musically"
options.app_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
options.no_reset = True

print("Connecting to Redroid instance via Appium...")
driver = webdriver.Remote("http://localhost:4723", options=options)

for campaign in data.get("campaigns", []):
    if not campaign.get("enabled", True):
        continue
        
    # Resolve URL or construct it from ID if URL is missing
    video_url = campaign.get("url")
    if not video_url and "id" in campaign:
        video_url = f"https://www.tiktok.com/video/{campaign['id']}"
        
    if video_url:
        print(f"Processing Campaign: {campaign['name']}")
        print(f"Navigating to video: {video_url}")
        
        # Open video deep link inside the emulated TikTok app
        driver.get(video_url)
        time.sleep(10)  # Allow view to register

driver.quit()
print("Automation run completed successfully.")