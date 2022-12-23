from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os


def test_validate_translation():
    # Check's parent directory for chrome web-driver and load it from there.
    driver_path = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s)

    # Load targeted website
    driver.get("https://subscribe.stctv.com/")

    # Locate "English Translation" button using ID and click it to check if it's working.
    eng_translation_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'translation-btn')))
    eng_translation_btn.click()

    current_web_title = driver.title
    if current_web_title == "Jawwy TV - Watch Online movies, series & live TV | Enjoy Free Trial":
        print("After translation, current web title is: " + str(current_web_title))
    else:
        assert False


def test_validate_country():
    # Check's parent directory for chrome web-driver and load it from there.
    driver_path = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s)

    # Load targeted website
    driver.get("https://subscribe.stctv.com/")

    # Locate the change country button on website using CLASS NAME and click on it.
    change_country_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, 'arrow')))
    change_country_btn.click()

    # Locate all countries appearing on the country's select dialogue box using CSS SELECTOR.
    select_country = WebDriverWait(driver, 25).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.country-select a')))
    # After locating all available countries from the box, count total numbers of countries found.
    count_countries = len(select_country)
    print("Total countries found to select are : " + str(count_countries))

    # Loop through each country and check validation if changing country works as expected.
    # Looping range is set by total number of countries found on the box above.
    for i in range(int(count_countries)):
        # Locate and select countries 1 by 1 using FOR LOOP, appearing on the dialogue box.
        select_country = WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.country-select a')))[i]
        # Check and Save the URL of each country appearing on the dialogue box.
        selected_country_url = select_country.get_attribute('href')
        select_country.click()

        # Get current URL from the browser for validating later.
        check_current_url = driver.current_url
        print("Current URL: " + check_current_url)
        print("Selected Countries URL: " + selected_country_url)
        # Validate if browser's URL matches, the URL attribute found during selecting the country.
        if check_current_url == selected_country_url:
            print("Selected country has been validated successfully!")
            change_country_btn = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'arrow')))
            change_country_btn.click()
        else:
            assert False


def test_validate_pkg_type():
    # Check's parent directory for chrome web-driver and load it from there.
    driver_path = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s)

    # Load targeted website
    driver.get("https://subscribe.stctv.com/")

    # Locate "English Translation" button and click it in-order to locate element using ID and Class in English.
    eng_translation_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'translation-btn')))
    eng_translation_btn.click()

    # Locate the change country button on website using CLASS NAME and click on it.
    change_country_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, 'arrow')))
    change_country_btn.click()

    # Locate all countries appearing on the country's select dialogue box using CSS SELECTOR.
    select_country = WebDriverWait(driver, 25).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.country-select a')))
    # After locating all available countries from the box, count total numbers of countries found.
    count_countries = len(select_country)
    print("Total countries found to select are : " + str(count_countries))

    # Loop through each country and check validation if changing country works as expected.
    # Looping range is set by total number of countries found on the box above.
    for i in range(int(count_countries)):
        # Locate and select countries 1 by 1 using FOR LOOP, appearing on the dialogue box.
        select_country = WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.country-select a')))[i]
        select_country.click()

        # Locate and get name of current country from the website.
        current_country = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'country-name')))

        # Validate if btn for certain package is clickable, if TIMEOUT EXCEPTION is raised. It should assert false.
        # Same validation method is applied on all the three available packages.
        try:
            lite_pkg_btn = WebDriverWait(driver, 25).until(
                EC.element_to_be_clickable((By.ID, 'lite-selection')))
            print("Lite Package Validation Successfully for country: " + current_country.text)
        except TimeoutException:
            print("Lite Package Validation Failed for country: " + current_country.text)
            assert False

        try:
            classic_pkg_btn = WebDriverWait(driver, 25).until(
                EC.element_to_be_clickable((By.ID, 'classic-selection')))
            print("Classic Package Validation Successfully for country: " + current_country.text)
        except TimeoutException:
            print("Classic Package Validation Failed for country: " + current_country.text)
            assert False

        try:
            premium_pkg_btn = WebDriverWait(driver, 25).until(
                EC.element_to_be_clickable((By.ID, 'premium-selection')))
            print("Premium Package Validation Successfully for country: " + current_country.text)
        except TimeoutException:
            print("Premium Package Validation Failed for country: " + current_country.text)
            assert False

        # Locate and click change country button after validation each package of selected country.
        change_country_btn = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'arrow')))
        change_country_btn.click()


def test_validate_currency():
    # Check's parent directory for chrome web-driver and load it from there.
    driver_path = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(driver_path, 'chromedriver.exe')
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s)

    # Load targeted website
    driver.get("https://subscribe.stctv.com/")

    # Locate "English Translation" button and click it in-order to locate element using ID and Class in English.
    eng_translation_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'translation-btn')))
    eng_translation_btn.click()

    # Locate the change country button on website using CLASS NAME and click on it.
    change_country_btn = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, 'arrow')))
    change_country_btn.click()

    # Locate all countries appearing on the country's select dialogue box using CSS SELECTOR.
    select_country = WebDriverWait(driver, 25).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.country-select a')))
    # After locating all available countries from the box, count total numbers of countries found.
    count_countries = len(select_country)
    print("Total countries found to select are : " + str(count_countries))

    # Loop through each country and check validation if changing country works as expected.
    # Looping range is set by total number of countries found on the box above.
    for i in range(int(count_countries)):
        # Locate and select countries 1 by 1 using FOR LOOP, appearing on the dialogue box.
        select_country = WebDriverWait(driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.country-select a')))[i]
        select_country.click()

        # Locate and get name of current country from the website.
        current_country = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'country-name')))

        # Validate if "Choose Your Plan" box appears on first page,
        # if TIMEOUT EXCEPTION is raised. It should assert false.
        try:
            currency_dialogue_box = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'lined')))
            print("Currency Validated Successfully for country: " + current_country.text)
        except TimeoutException:
            print("Currency Validated Failed for country: " + current_country.text)
            assert False

        # Locate and click change country button after validation each package of selected country.
        change_country_btn = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'arrow')))
        change_country_btn.click()
