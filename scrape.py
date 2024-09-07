from login import login, setup_driver, random_delay, wait_for_internet
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_admins():
    wait_for_internet()
    driver = setup_driver()
    login(driver)
    random_delay()

    # Click the "Groups" link to go to the Groups page
    try:
        groups_link = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'community-panel-interest-package__header-link')]"))
        )
        groups_link.click()
        random_delay()
    except Exception as e:
        print("Error navigating to Groups page:", e)
        driver.quit()
        return
    
    profile_urls = []

    # Loop to keep clicking the "Show more results" button
   
    # Loop to keep clicking the "Show more results" button until it's no longer available
    while True:
        try:
            show_more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button']"))
            )
            if show_more_button.is_displayed():
                show_more_button.click()
                print("Clicked 'Show more results' button.")
                random_delay()
            else:
                print("No more 'Show more results' button found.")
                break
        except Exception as e:
            print(f"Exception encountered: {e}")
            break  # Exit loop if the button is not found or another exception occurs

    # Now all groups should be loaded, start scraping group admins
    group_xpath = "//a[contains(@class, 'group-listing-item__title-link')]"
    group_elements = driver.find_elements(By.XPATH, group_xpath)
    
    if not group_elements:
        print("No groups found.")
        driver.quit()
        return

    print(f"Found {len(group_elements)} groups.")
    
    for i in range(len(group_elements)):
        try:
            # Re-find the group elements after navigating back
            group_elements = driver.find_elements(By.XPATH, group_xpath)
            group_elements[i].click()
            random_delay()

            while True:
                try:
                    show_more_button = driver.find_element(By.XPATH, "//button[text()='Show more']")
                    show_more_button.click()
                    random_delay(1, 2)
                except:
                    break

            try:
                admin_section = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="group-entity-page"]/div/div/aside/section/div/section/div'))
                )
                
                admin_elements = admin_section.find_elements(By.XPATH, ".//a[contains(@href, '/in/')]")
                
                for admin in admin_elements:
                    profile_url = admin.get_attribute("href")
                    profile_urls.append(profile_url)
                    print(f"Scraped: {profile_url}")
                    
                random_delay()
            except Exception as e:
                print("Error finding admin section:", e)
                continue
            
            # Navigate back to the groups list
            driver.back()
            random_delay()
        except Exception as e:
            print(f"Error scraping group: {e}")
            continue
    
    # Save the scraped profile URLs to a file
    with open("admin_profiles.txt", "w") as file:
        for url in profile_urls:
            file.write(url + "\n")
    
    driver.quit()
    print("Scraping completed. Admin profiles saved to admin_profiles.txt.")

if __name__ == "__main__":
    scrape_admins()
