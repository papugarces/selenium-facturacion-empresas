from selenium.webdriver.common.by import By
from src.testproject.decorator import report_assertion_errors


"""
This pytest test was automatically generated by TestProject
    Project: UNI
    Package: TestProject.Generated.Tests.UNI
    Test: Login
    Generated by: Nicolas Duran (nicolas.duran@atlanticsoft.us)
    Generated on 11/24/2021, 00:49:54
"""


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://facturaciononempresa.herokuapp.com/"
    nombreUsuario = ""
    contrasena = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Iniciar Sesión'
    iniciar_sesi_n = driver.find_element(By.XPATH,
                                         "//a[. = 'Iniciar Sesión']")
    iniciar_sesi_n.click()

    # 3. Click 'nombreUsuario'
    nombreusuario = driver.find_element(By.CSS_SELECTOR,
                                        "[name='nombreUsuario']")
    nombreusuario.click()

    # 4. Type '{nombreUsuario}' in 'nombreUsuario'
    nombreusuario = driver.find_element(By.CSS_SELECTOR,
                                        "[name='nombreUsuario']")
    nombreusuario.send_keys(f'{nombreUsuario}')

    # 5. Click 'contrasena'
    contrasena = driver.find_element(By.CSS_SELECTOR,
                                     "[name='contrasena']")
    contrasena.click()

    # 6. Type '{contrasena}' in 'contrasena'
    contrasena = driver.find_element(By.CSS_SELECTOR,
                                     "[name='contrasena']")
    contrasena.send_keys(f'{contrasena}')

    # 7. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[4]/input")
    input.click()
