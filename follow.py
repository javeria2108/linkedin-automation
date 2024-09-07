from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login, setup_driver, random_delay, wait_for_internet

def follow_profiles():
    ()
    driver = setup_driver()
    login(driver)
    random_delay()

    with open("admin_profiles.txt", "r") as file:
        profile_urls = file.readlines()

    for profile_url in profile_urls:
        try:
            driver.get(profile_url.strip())
            random_delay()

            followed = False

            try:
                
                follow_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action'))
                )
                if "Follow" in follow_button.text:
                    follow_button.click()
                    followed = True
                    print(f"Followed directly: {profile_url.strip()}")

            except Exception as e:
                print(f"Direct follow button not found for {profile_url.strip()}: {e}")

           
            if not followed:
                try:
                    # Try clicking the "More" button if Follow button not found
                    more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button')))

                    
                    more_button.click()
                    random_delay()

                    # Now try to find the Follow button under the "More" menu
                    follow_button_more = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[3]/div/span'))
                    )
                    follow_button_more.click()
                    print(f"Followed via More button: {profile_url.strip()}")

                except Exception as e:
                    print(f"Failed to follow {profile_url.strip()} via More button: {e}")

            random_delay()

        except Exception as e:
            print(f"Error processing profile {profile_url.strip()}: {e}")

    driver.quit()

if __name__ == "__main__":
    follow_profiles()
