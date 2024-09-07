from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login, setup_driver, random_delay, wait_for_internet

def connect():
    wait_for_internet()
    driver = setup_driver()
    login(driver)
    random_delay()

    with open("admin_profiles.txt", "r") as file:
        profile_urls = file.readlines()

    for profile_url in profile_urls:
        try:
            driver.get(profile_url.strip())
            random_delay()

            connected = False

            try:
                
                connect_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action'))
                )
                if "Connect" in connect_button.text:
                    connect_button.click()
                    random_delay()
                    try:
                        send_without_note=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]'))
                    )
                        
                        send_without_note.click()
                    except:
                        pass
                    connected = True
                    print(f"Invitation sent: {profile_url.strip()}")

            except Exception as e:
                print(f"Direct connect button not found for {profile_url.strip()}: {e}")

           
            if not connected:
                try:
                    # Try clicking the "More" button if Connect button not found directly
                    more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button')))

                    
                    more_button.click()
                    random_delay()
                   

                    # Now try to find the Connect button under the "More" menu
                    connect_button_more = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[3]/div/span'))
                    )
                    connect_button_more.click()
                    random_delay()
                    try:
                        send_without_note=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]'))
                    )
                        
                        send_without_note.click()
                    except:
                        pass
                    print(f"Connected via More button: {profile_url.strip()}")

                except Exception as e:
                    print(f"Failed to connect {profile_url.strip()} via More button: {e}")

            random_delay()

        except Exception as e:
            print(f"Error processing profile {profile_url.strip()}: {e}")

    driver.quit()

if __name__ == "__main__":
    connect()
