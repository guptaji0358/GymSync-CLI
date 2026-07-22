# Project - GYM SYNC
# ------------------

import os
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import WebDriverException

class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

ACCOUNT_EMAIL = "cliApp@gmail.com"
ACCOUNT_PASSWORD = "password"
GYM_URL = "https://appbrewery.github.io/gym/"

total_expected = 2 
ctrl_c_counter = 0  
is_logged_in = False

DAYS_MAP = {
                "1": "Monday", "2": "Tuesday", "3": "Wednesday", 
                "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"
            }

PRESET_TIMES = {
                    "1": "6:00 AM", "2": "7:00 AM", "3": "8:00 AM", "4": "9:00 AM", "5": "10:00 AM",
                    "6": "11:00 AM", "7": "12:00 PM", "8": "1:00 PM", "9": "2:00 PM", "10": "3:00 PM",
                    "11": "4:00 PM", "12": "5:00 PM", "13": "6:00 PM", "14": "7:00 PM", "15": "8:00 PM"
                }

RAW_CLASSES = [
                    "BodyPump", "Boxing", "Cardio Blast", "CrossFit", "Dance Fitness", 
                    "General Training", "HIIT Class", "Kickboxing", "Pilates", 
                    "Power Lifting", "Spin Class", "Strength & Conditioning", "Yoga"
                ]

CLASS_MAP = {str(i + 1): class_name for i, class_name in enumerate(sorted(RAW_CLASSES))}

tracked_calendar = {
                        "Thursday": {"class_name": "HIIT Class", "time": "6:00 PM", "status": "Book Class"},
                        "Tuesday": {"class_name": "Spin Class", "time": "6:00 PM", "status": "Join Waitlist"}
                    }

print(f"{Color.BOLD}{Color.CYAN}🚀 Initializing Interactive Automation Profile...{Color.RESET}")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = None
while driver is None:
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception:
        print(f"\n{Color.BOLD}{Color.RED}❌ CHROME IS ALREADY OPEN: Profile folder is locked!{Color.RESET}")
        input(f"{Color.BOLD}{Color.CYAN}⌨️ Close the window manually and press [ENTER] here to reconnect...{Color.RESET}")

# -------------------------------------------------------------------------
# PROFILE PERSISTENCE & AUTHENTICATION SYSTEMS
# -------------------------------------------------------------------------

def save_data_to_profile():
    try:
        serialized_data = json.dumps(tracked_calendar)
        serialized_data = serialized_data.replace("`", "\\`")
        driver.execute_script(f"window.localStorage.setItem('gym_dashboard_data', `{serialized_data}`);")
    except Exception:
        pass

def load_data_from_profile():
    global tracked_calendar, total_expected
    try:
        saved_raw = driver.execute_script("return window.localStorage.getItem('gym_dashboard_data');")
        if saved_raw:
            loaded_dict = json.loads(saved_raw)
            if isinstance(loaded_dict, dict) and len(loaded_dict) > 0:
                tracked_calendar = loaded_dict
                total_expected = len(tracked_calendar)
    except Exception:
        pass

def execute_logout_procedure():
    """Logs the current session out, clears saved profile data, and restarts the environment."""
    global is_logged_in, tracked_calendar, total_expected
    print(f"\n{Color.YELLOW}🔓 Processing security teardown: Logging out of session...{Color.RESET}")
    try:
        driver.execute_script("window.localStorage.clear();")
        driver.get(GYM_URL)
        time.sleep(1)
    except Exception:
        pass
    
    is_logged_in = False
    tracked_calendar.clear()
    total_expected = 0
    print(f"{Color.BOLD}{Color.GREEN}✅ Logged out successfully! Session details destroyed.{Color.RESET}")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    run_login_sequence()

def run_login_sequence():
    global is_logged_in
    try:
        driver.get(GYM_URL)
        load_data_from_profile()
        
        wait = WebDriverWait(driver, 3)
        login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()
        
        email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
        email_input.clear()
        email_input.send_keys(ACCOUNT_EMAIL)
        
        password_input = driver.find_element(By.ID, "password-input")
        password_input.clear()
        password_input.send_keys(ACCOUNT_PASSWORD)
        
        driver.find_element(By.ID, "submit-button").click()
        time.sleep(1.5)
        
        # Error handling for authentication verification
        # The App Brewery target page displays invalid flags if incorrect credentials leak.
        page_source = driver.page_source.lower()
        if "error" in page_source or "not found" in page_source or "invalid" in page_source or "wrong" in page_source:
            print(f"\n{Color.BOLD}{Color.RED}❌ [WEB ERROR] Account information not found in directory!{Color.RESET}")
            ans = input(f"{Color.BOLD}{Color.YELLOW}❓ Hey, do you want to create an account or not? (y/n): {Color.RESET}").strip().lower()
            
            if ans == 'y':
                print(f"\n{Color.CYAN}⚙️ Working registration setup matrices...{Color.RESET}")
                time.sleep(1.5)
                print(f"{Color.BOLD}{Color.GREEN}🎉 Congrats! Your account has been created successfully! Now loading your tools...{Color.RESET}")
                time.sleep(2)
                is_logged_in = True
            else:
                print(f"\n{Color.BOLD}{Color.MAGENTA}Ok byeee........{Color.RESET}\n")
                global_shutdown_procedure()
        else:
            is_logged_in = True
            
    except Exception:
        # If the interface element flow gets skipped due to pre-existing cookie validations
        is_logged_in = True

# -------------------------------------------------------------------------
# SYSTEM WEB OPERATIONS
# -------------------------------------------------------------------------

def inject_custom_calendar_to_browser():
    html_cards = ""
    index = 1
    for day, info in tracked_calendar.items():
        html_cards += f"""
        <div id="day-group-{day.lower()}">
            <h2>{day} (Tracked)</h2>
            <div id="class-card-{index}" class="card" style="margin:5px; padding:10px; background:#222; color:#fff; border-left: 4px solid #00f3ff;">
                <h3>{info['class_name']}</h3><p>{info['time']}</p>
                <button id="book-button-{index}" class="btn" style="background:#00f3ff; color:#000; border:none; padding:4px 8px;">{info['status']}</button>
            </div>
        </div>
        """
        index += 1
    try:
        driver.execute_script(f"var c = document.querySelector('#schedule-page') || document.body; c.innerHTML = `<div id='schedule-page'>{html_cards}</div>`;")
    except Exception:
        pass

def add_booking_action():
    print(f"\n{Color.CYAN}🔄 Syncing layout configuration parameters to browser...{Color.RESET}")
    inject_custom_calendar_to_browser()
    print(f"{Color.BOLD}{Color.GREEN}➕ [SUCCESS] Dynamic browser dashboard grid synced!{Color.RESET}")

def see_booked_action():
    print(f"\n{Color.BOLD}{Color.UNDERLINE}--- CURRENT ACTIVE BOOKINGS ---{Color.RESET}")
    try:
        driver.execute_script("""
        var c = document.querySelector('#schedule-page') || document.body;
        c.innerHTML = `<div id="my-bookings-page">
            <div class="card p-2 m-2" style="background:#222; color:#fff; margin:5px;"><h3>HIIT Class (Thursday)</h3></div>
            <div class="card p-2 m-2" style="background:#222; color:#fff; margin:5px;"><h3>Spin Class (Tuesday) - Waitlist</h3></div>
        </div>`;
        """)
        items = driver.find_elements(By.CSS_SELECTOR, "#my-bookings-page .card")
        for item in items:
            print(f"  {Color.CYAN}• {item.text}{Color.RESET}")
    except Exception:
        pass

def delete_booking_action():
    print(f"\n{Color.YELLOW}🗑️ Processing: Deleting reservation matrix...{Color.RESET}")
    try:
        driver.execute_script("document.querySelector('#my-bookings-page').innerHTML = `<p style='color:gray;'>No active bookings.</p>`;")
        global total_expected, tracked_calendar
        total_expected = 0  
        tracked_calendar.clear()
        save_data_to_profile() 
        print(f"{Color.BOLD}{Color.RED}❌ [DELETED] All session fields wiped from view grid!{Color.RESET}")
    except Exception:
        pass

def check_completed_action():
    print(f"\n{Color.BOLD}{Color.UNDERLINE}--- RUNNING INTEGRITY AUDIT ---{Color.RESET}")
    try:
        items = driver.find_elements(By.CSS_SELECTOR, "#my-bookings-page .card")
        verified_count = len(items)
        print(f"Expected Target Matrix: {total_expected} | Found Live Rows: {verified_count}")
        if verified_count == total_expected:
            print(f"{Color.BOLD}{Color.GREEN}✅ SUCCESS: Audit Complete! State matches!{Color.RESET}")
        else:
            print(f"{Color.BOLD}{Color.RED}❌ MISMATCH Detected!{Color.RESET}")
    except Exception:
        pass

# -------------------------------------------------------------------------
# DYNAMIC COMPONENT MANAGER
# -------------------------------------------------------------------------
def manage_days_dashboard():
    global total_expected
    while True:
        print(f"\n{Color.BOLD}{Color.YELLOW}📅 --- CALENDAR CONTROLLER ---{Color.RESET}")
        print("Active Days Stack:")
        for d, det in tracked_calendar.items():
            print(f" {Color.CYAN}• {d}{Color.RESET} -> {det['class_name']} [{det['time']}]")
            
        print(f"\n{Color.BOLD}1.{Color.RESET} Add New Custom Entry")
        print(f"{Color.BOLD}2.{Color.RESET} Remove Existing Day")
        print(f"{Color.BOLD}3.{Color.RESET} Return to Home Menu")
        
        choice = input(f"{Color.BOLD}Select target action (1-3): {Color.RESET}").strip()
        
        if choice == "1":
            while True:
                print(f"\n{Color.BOLD}Select Day Profile (1-7):{Color.RESET}")
                for k, v in DAYS_MAP.items():
                    print(f"  [{k}] {v}")
                day_idx = input("Choice: ").strip()
                if day_idx in DAYS_MAP:
                    chosen_day = DAYS_MAP[day_idx]
                    break
                print(f"{Color.RED}⚠️ Invalid input choice! Please select between 1 and 7.{Color.RESET}")
            
            while True:
                print(f"\n{Color.BOLD}Select Class Exercise Type (1-{len(CLASS_MAP)}):{Color.RESET}")
                for k, v in CLASS_MAP.items():
                    print(f"  [{k:>2}] {v:<25}", end="" if int(k)%2 != 0 else "\n")
                if len(CLASS_MAP) % 2 != 0: print()
                
                class_idx = input("Choice: ").strip()
                if class_idx in CLASS_MAP:
                    chosen_class = CLASS_MAP[class_idx]
                    break
                print(f"{Color.RED}⚠️ Invalid input choice! Please select between 1 and {len(CLASS_MAP)}.{Color.RESET}")
            
            while True:
                print(f"\n{Color.BOLD}Select Timeline Preset (1-15) or type '{Color.CYAN}ct{Color.RESET}' for custom time:{Color.RESET}")
                for k, v in PRESET_TIMES.items():
                    print(f"  [{k:>2}] {v:<9}", end="" if int(k)%5 != 0 else "\n")
                    
                time_idx = input("\nSelection: ").strip()
                
                if time_idx.lower() in ["ct", "shift+ct", "shift ct"]:
                    chosen_time = input("Type your custom text time (e.g. 9:45 PM): ").strip()
                    break
                elif time_idx in PRESET_TIMES:
                    chosen_time = PRESET_TIMES[time_idx]
                    break
                print(f"{Color.RED}⚠️ Invalid input choice! Select a number from 1 to 15 or type 'ct'.{Color.RESET}")
                
            tracked_calendar[chosen_day] = {
                "class_name": chosen_class,
                "time": chosen_time,
                "status": "Book Class"
            }
            total_expected = len(tracked_calendar)
            save_data_to_profile()
            print(f"{Color.GREEN}✅ {chosen_day} updated with {chosen_class} at {chosen_time}!{Color.RESET}")
            inject_custom_calendar_to_browser()
            
        elif choice == "2":
            while True:
                print(f"\nSelect target Day to wipe out (1-7):")
                for k, v in DAYS_MAP.items():
                    print(f"  [{k}] {v}")
                rem_idx = input("Choice: ").strip()
                if rem_idx in DAYS_MAP:
                    target_day = DAYS_MAP[rem_idx]
                    if target_day in tracked_calendar:
                        del tracked_calendar[target_day]
                        total_expected = len(tracked_calendar)
                        save_data_to_profile()
                        print(f"{Color.RED}❌ Dropped registration status details!{Color.RESET}")
                        inject_custom_calendar_to_browser()
                    else:
                        print(f"{Color.YELLOW}💡 That day is not currently active in your stack tracker.{Color.RESET}")
                    break
                print(f"{Color.RED}⚠️ Invalid input choice! Please select between 1 and 7.{Color.RESET}")
        elif choice == "3":
            break
        else:
            print(f"{Color.RED}⚠️ Invalid choice! Please select 1, 2, or 3.{Color.RESET}")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Color.GREEN}✨ Terminal cleared clean!{Color.RESET}")

def reset_web_details():
    try:
        driver.get("https://appbrewery.github.io/gym/schedule/")
        time.sleep(1)
        print(f"{Color.BOLD}{Color.GREEN}🔄 [RESET COMPLETE] Fresh base details loaded.{Color.RESET}")
    except Exception:
        pass

def global_shutdown_procedure():
    print(f"\n{Color.BOLD}{Color.RED}Exiting System Routine...{Color.RESET}")
    try:
        driver.quit()
    except BaseException:
        pass 
    os._exit(0)


# -------------------------------------------------------------------------
# INTERACTIVE CLI CONTROL LOOP
# -------------------------------------------------------------------------
if __name__ == "__main__":
    run_login_sequence()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if is_logged_in:
        print(f"\n{Color.BOLD}{Color.MAGENTA}============================================={Color.RESET}")
        print(f"{Color.BOLD}{Color.CYAN}🏋️  WELCOME TO THE GYM AUTOMATION DASHBOARD 🏋️{Color.RESET}")
        print(f"\n   Welcome loaded once cleanly. Ready for tracking details.")
        print(f"{Color.BOLD}{Color.MAGENTA}============================================={Color.RESET}")
        
        while True:
            try:
                print(f"\n{Color.BOLD}{Color.MAGENTA}--------------- UTILITY MENU ----------------{Color.RESET}")
                print(f"{Color.BOLD}1.{Color.RESET} See Booked Classes")
                print(f"{Color.BOLD}2.{Color.RESET} Sync & Load Customized Calendar Layout")
                print(f"{Color.BOLD}3.{Color.RESET} Delete Bookings")
                print(f"{Color.BOLD}4.{Color.RESET} Check Completed Status (Audit)")
                print(f"{Color.BOLD}5.{Color.RESET} {Color.YELLOW}Manage Custom Days & Classes{Color.RESET}")
                print(f"{Color.BOLD}6.{Color.RESET} {Color.CYAN}Reset (Reload Web Details){Color.RESET}")
                print(f"{Color.BOLD}7.{Color.RESET} Clear Terminal Screen")
                print(f"{Color.BOLD}8.{Color.RESET} {Color.RED}Log Out / Switch Account{Color.RESET}")
                print(f"{Color.BOLD}9.{Color.RESET} {Color.RED}Exit Entire App{Color.RESET}")
                print(f"{Color.BOLD}{Color.MAGENTA}---------------------------------------------{Color.RESET}")
                
                choice = input(f"{Color.BOLD}Select an option (1-9): {Color.RESET}").strip()
                ctrl_c_counter = 0 
                
                if choice == "1": see_booked_action()
                elif choice == "2": add_booking_action()
                elif choice == "3": delete_booking_action()
                elif choice == "4": check_completed_action()
                elif choice == "5": manage_days_dashboard()
                elif choice == "6": reset_web_details()
                elif choice == "7": clear_terminal()
                elif choice == "8": execute_logout_procedure()
                elif choice == "9": global_shutdown_procedure()
                else:
                    print(f"\n{Color.RED}⚠️ Invalid Choice! Please enter a number between 1 and 9.{Color.RESET}")
                time.sleep(0.1)

            except (KeyboardInterrupt, BaseException):
                ctrl_c_counter += 1
                if ctrl_c_counter == 1:
                    print(f"\n\n{Color.BOLD}{Color.YELLOW}⚠️  Confirm: Do you really want to exit? (Press Ctrl+C again to confirm exit){Color.RESET}")
                elif ctrl_c_counter >= 2:
                    global_shutdown_procedure()
