from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

mensajes_positivos = [
    "Excelente curso, aprendí mucho.",
    "Muy buena experiencia educativa.",
    "Los instructores son de lo mejor.",
    "Me encantó el contenido.",
    "Aprendizaje garantizado.",
    "Dinámicas muy entretenidas.",
    "Cursos muy bien estructurados.",
    "Recomiendo este curso al 100%.",
    "Perfecto para desarrollar habilidades.",
    "Me siento más preparado.",
    "Gran calidad y profesionalismo.",
    "Súper útil y práctico.",
    "Muy buena atención al alumno.",
    "Excelente metodología de enseñanza.",
    "Contenido actualizado y claro.",
    "Ideal para crecer profesionalmente.",
    "Los temas fueron muy interesantes.",
    "Agradecido por esta oportunidad.",
    "Vale totalmente la pena.",
    "Lo volvería a tomar sin dudar."
]

contador = 0

while True:  
    driver = webdriver.Chrome()
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdVWCsx-wIRVFT6EHRIecRMQ14l3tQcJXoMaOU9DnICbloZyg/viewform?fbzx=-3265877377893098071")
    wait = WebDriverWait(driver, 15)

    try:
        # Paso 1
        siguiente_btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn1.click()
        time.sleep(2)

        # Paso 2
        dropdown1 = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="listbox"]')))
        ActionChains(driver).move_to_element(dropdown1).click().perform()
        time.sleep(1)
        option1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and @data-value="SEMAR"]')))
        driver.execute_script("arguments[0].click();", option1)
        time.sleep(1)

        siguiente_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn2.click()
        time.sleep(2)

        # Paso 3
        dropdown2 = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="listbox"]')))
        ActionChains(driver).move_to_element(dropdown2).click().perform()
        time.sleep(1)
        option2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and @data-value="Liliana Granados Ibañez"]')))
        driver.execute_script("arguments[0].click();", option2)
        time.sleep(1)

        siguiente_btn3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn3.click()
        time.sleep(2)

        # Paso 4
        dropdown3 = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="listbox"]')))
        ActionChains(driver).move_to_element(dropdown3).click().perform()
        time.sleep(1)
        option3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and @data-value="Inclusión Digital"]')))
        driver.execute_script("arguments[0].click();", option3)
        time.sleep(1)

        siguiente_btn4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn4.click()
        time.sleep(2)

        # Paso 5
        dropdown4 = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="listbox"]')))
        ActionChains(driver).move_to_element(dropdown4).click().perform()
        time.sleep(1)
        option4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and @data-value="Explorando la computadora"]')))
        driver.execute_script("arguments[0].click();", option4)
        time.sleep(1)

        siguiente_btn5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn5.click()
        time.sleep(2)

        # Paso 6
        radio_buttons1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@role="radio" and @data-value="1"]')))
        for rb in radio_buttons1[:3]:
            driver.execute_script("arguments[0].click();", rb)
            time.sleep(0.5)

        siguiente_btn6 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn6.click()
        time.sleep(2)

        # Paso 7
        radio_buttons2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@role="radio" and @data-value="1"]')))
        for rb in radio_buttons2[:5]:
            driver.execute_script("arguments[0].click();", rb)
            time.sleep(0.5)

        siguiente_btn7 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn7.click()
        time.sleep(2)

        # Paso 8
        radio_buttons3 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@role="radio" and @data-value="1"]')))
        for rb in radio_buttons3[:3]:
            driver.execute_script("arguments[0].click();", rb)
            time.sleep(0.5)

        siguiente_btn8 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "iguiente")]')))
        siguiente_btn8.click()
        time.sleep(2)

        # Paso 9 - Última página
        radio_buttons4 = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@role="radio" and @data-value="1"]')))
        for rb in radio_buttons4[:1]:
            driver.execute_script("arguments[0].click();", rb)
            time.sleep(0.5)

        mensaje = random.choice(mensajes_positivos)
        input_text = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @class="whsOnd zHQkBf"]')))
        input_text.send_keys(mensaje)
        print(f"✅ Mensaje enviado: {mensaje}")

        enviar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Enviar")]')))
        enviar_btn.click()
        print("➡️ Formulario enviado")

        time.sleep(2)

        enviar_otra_respuesta = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Enviar otra respuesta")]')))
        enviar_otra_respuesta.click()
        print("🔄 Reiniciando para nueva respuesta")

        contador += 1
        print(f"📊 Encuestas contestadas: {contador}")

        time.sleep(2)

    except Exception as e:
        print("❌ Error general:", e)

    finally:
        driver.quit()
        time.sleep(2)
