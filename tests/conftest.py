import pytest
from selenium import webdriver

# Nem src/sel tesztek
@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()

# src/sel tesztek
@pytest.fixture(scope="class")
def driver():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options)
    driver = webdriver.Chrome()
    driver.get("https://em2-teszt.rubin.hu/")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.close()
