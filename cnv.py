from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller as chromedriver
from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

chromedriver.install()


diccionario_juridica = {
    "Matricula": [],
    "Cuit/Cuil": [],
    "Tipo de Agente": [],
    "Tipo de Persona": [],
    "Apellido - Razon Social": [],
    "Domicilio": [],
    "Contratos": [],
}

driver = start_chrome(
    "https://www.cnv.gov.ar/SitioWeb/RegistrosPublicos/Agentes")

wait = WebDriverWait(driver, 100000)

dropdown_agents = wait.until(
    EC.presence_of_element_located((By.ID, "ListaTiposAgentes")))

select = Select(dropdown_agents)

select.select_by_visible_text(
    'Agentes Productores (Persona Jurídica)')

button_buscar = driver.find_element_by_xpath('//input[@value="BUSCAR"]')
button_buscar.click()


tbody = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="tablaagentes"]/tbody')))

time.sleep(5)

rows = tbody.find_elements_by_xpath(".//tr")

for row in rows:
    cells = row.find_elements_by_xpath(".//td")
    # Aquí puedes hacer algo con las celdas, como imprimir su texto
    cont = 0
    for cell in cells:
        if cont == 0:
            diccionario_juridica["Matricula"].append(cell.text)
        elif cont == 1:
            diccionario_juridica["Cuit/Cuil"].append(cell.text)
        elif cont == 2:
            diccionario_juridica["Tipo de Agente"].append(cell.text)
        elif cont == 3:
            diccionario_juridica["Tipo de Persona"].append(cell.text)
        elif cont == 4:
            diccionario_juridica["Apellido - Razon Social"].append(cell.text)
        elif cont == 5:
            cont = 0
            continue
        cont += 1

    button_mas = wait.until(
        EC.presence_of_element_located((By.ID, 'botonmas')))
    button_mas.click()
    button_domicilio = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="innerheading4"]/h4/a')))
    button_domicilio.click()

    time.sleep(1)

    tr_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="innercollapse4"]/div/div/table/tbody/tr')))
    td_elements = tr_element.find_elements_by_xpath('./td')

    diccionario_juridica_domicilio = {
        "Tipo": td_elements[0].text,
        "Direccion": td_elements[1].text,
        "Localidad": td_elements[2].text,
        "Codigo Postal": td_elements[3].text,
        "Provincia": td_elements[4].text,
        "Pais": td_elements[5].text,
        "Telefono": td_elements[6].text,
    }

    diccionario_juridica["Domicilio"].append(diccionario_juridica_domicilio)

    driver.back()

    time.sleep(5)


print(diccionario_juridica)


# time.sleep(1)

# tr_element = wait.until(EC.presence_of_element_located(
#     (By.XPATH, '//*[@id="innercollapse4"]/div/div/table/tbody/tr')))
# td_elements = tr_element.find_elements_by_xpath('./td')

# diccionario_juridica_domicilio = {
#     "Tipo": td_elements[0].text,
#     "Direccion": td_elements[1].text,
#     "Localidad": td_elements[2].text,
#     "Codigo Postal": td_elements[3].text,
#     "Provincia": td_elements[4].text,
#     "Pais": td_elements[5].text,
#     "Telefono": td_elements[6].text,
# }
# print(diccionario_juridica_domicilio)

# button_informacionFin = wait.until(EC.presence_of_element_located((By.ID, 'col2a')))
# button_informacionFin.click()

# button_publicoInv = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="heading9_2"]/h4/a')))
# button_publicoInv.click()

# button_agentesContratos = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="heading30_2"]/h4/a')))
# button_agentesContratos.click()


# rows = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))


# lista_separada = rows.text.split("\n")

# lista_cortada = [x for x in lista_separada if x != 'Ver mas']

# lista_final = [x.replace('AP PJ JURÍDICA', '') for x in lista_cortada]

# print(lista_final)
