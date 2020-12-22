from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pickle
####



###################################################################### Início do Crawler no site do nubank!! Atenção ao QR Code.
####### Preparando o webdriver
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\I\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe")

####### Indo ao site do Nubank
driver.get('https://app.nubank.com.br/#/login')

############## Parametros de Login do usuário
cpf = '15744584773'
senha = 'Gmjc873umac1$'

#################### Vasculhando o Xpath e Fazendo Login
xpath_cpf= '/html/body/navigation-base/div[1]/div/main/div[1]/div/div[1]/form/md-input-container[1]/input'
xpath_senha = '/html/body/navigation-base/div[1]/div/main/div[1]/div/div[1]/form/md-input-container[2]/input'
xpath_botao = '/html/body/navigation-base/div[1]/div/main/div[1]/div/div[1]/form/button'
login_cpf = driver.find_element_by_xpath(xpath_cpf)
login_cpf.send_keys(cpf)
login_senha = driver.find_element_by_xpath(xpath_senha)
login_senha.send_keys(senha)
login_senha.send_keys(Keys.ENTER)

#################### Sleep do QR Code. Ficar atento.
time.sleep(15)

#################### Coletando as informações da tabela.
mytable = driver.find_element_by_css_selector('#feedTable')
print(mytable)
#list_rows = []
list_cells = []
for row in mytable.find_elements_by_css_selector('tr'):
    list_rows.append(row.text)
    print(row.text)
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)
        list_cells.append(cell.text)
        print("----")

####### Salvando os resultados em Pickle temporário
with open('parrot4.pkl','wb') as z:
        pickle.dump(list_rows,z)
with open('parrot5.pkl','wb') as x:
        pickle.dump(list_cells,x)

###################################################################### Fim do Crawler ao site do Nubank.
