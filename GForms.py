import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fillForms(driver):
    try:
        # Wait until the first button is clickable
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i5"]/div[3]/div')))
        button.click()
        print("First button clicked successfully")


        age_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div'
        agebutton = wait.until(EC.element_to_be_clickable((By.XPATH, age_button_xpath)))
        agebutton.click()
        print("Age button clicked successfully")
        third_button_xpath ='//*[@id="i40"]/div[3]/div'
        third_button = wait.until(EC.element_to_be_clickable((By.XPATH, third_button_xpath)))
        third_button.click()


        fourth_button_xpath ='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'
        fourth_button = wait.until(EC.element_to_be_clickable((By.XPATH, fourth_button_xpath)))
        fourth_button.click()
        time.sleep(2)

        fifth_button_xpath='//*[@id="i54"]/div[3]/div'
        fifth_button = wait.until(EC.element_to_be_clickable((By.XPATH, fifth_button_xpath)))
        fifth_button.click()
        time.sleep(2)

        sixth_button_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div[1]'
        sixth_button = wait.until(EC.element_to_be_clickable((By.XPATH, sixth_button_xpath)))
        sixth_button.click()
        time.sleep(2)

        seventh_button_xpath='//*[@id="i83"]/div[3]/div'
        seventh_button = wait.until(EC.element_to_be_clickable((By.XPATH, seventh_button_xpath)))
        seventh_button.click()

        eight_button_xpath ='//*[@id="i96"]/div[3]/div'
        eight_button = wait.until(EC.element_to_be_clickable((By.XPATH, eight_button_xpath)))
        eight_button.click()
        time.sleep(2)

        ninth_button_xpath='//*[@id="i112"]/div[3]/div'
        ninth_button = wait.until(EC.element_to_be_clickable((By.XPATH, ninth_button_xpath)))
        ninth_button.click()
        time.sleep(2)

        tenth_button_xpath='//*[@id="i128"]/div[3]/div'
        tenth_button = wait.until(EC.element_to_be_clickable((By.XPATH, tenth_button_xpath)))
        tenth_button.click()

        time.sleep(5)

        submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span'
        wait = WebDriverWait(driver, 10)
        submitbutton = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        submitbutton.click()
        print("Form submitted successfully")

    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        url = "https://docs.google.com/forms/d/e/1FAIpQLSd8930TmRR_p-hnMzEXpdKzO4dVYZ-wTlCHGhsSgklb5tCjdg/viewform?usp=sf_link"
        driver.get(url)
        time.sleep(5)
        # fillForms(driver)
        for i in range(10):
            fillForms(driver)
            submit_another_form_xpath = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
            wait = WebDriverWait(driver, 10)
            submitanotherformbutton = wait.until(EC.element_to_be_clickable((By.XPATH, submit_another_form_xpath)))
            submitanotherformbutton.click()
            time.sleep(10)
        time.sleep(10)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
