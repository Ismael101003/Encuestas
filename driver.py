from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Usa el ChromeDriver adecuado sin necesidad de descargarlo manualmente
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")
driver.quit()
