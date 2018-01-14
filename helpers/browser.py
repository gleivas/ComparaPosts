from selenium import webdriver
from selenium.webdriver.common.by import By

#classe usada para realizar as operacoes no navegador
class Navegar:

    #instanciando o navegador para usar o chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    #função para fechar o navegador
    def fechar(self):
        self.driver.quit()

    #função para ir ate um site
    def visitar(self, url):
        self.driver.get(url)

    #função para procurar elementos pelo nome da tag, coloca-los em letra minuscula
    #e se uma parte dele for igual ao do post desejado retornar True
    def acha_post(self, tag, post):
        elemento = self.driver.find_elements(By.TAG_NAME, tag)
        for element in elemento:
            if post in element.text.lower():
                return True
