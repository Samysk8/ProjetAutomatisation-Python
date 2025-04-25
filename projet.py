from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configuration pour que les fichiers soient téléchargés automatiquement
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download/directory",  # Remplacez par votre répertoire de téléchargement
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})

# Lancer le navigateur avec les options configurées
driver = webdriver.Chrome(options=chrome_options)

# Aller sur le site ISFO Casa
driver.get("https://www.isfocasa.com/")

# Attendre un peu que la page charge
time.sleep(2)

# Descendre légèrement avec la touche "Page Down"
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN)

# Attendre pour voir l'effet de défilement
time.sleep(2)

# Après le défilement, ouvrir le lien spécifique
driver.get("https://www.isfocasa.com/edt")
print("✅ Accès à la page emploi du temps réussi !")

time.sleep(2)

# Ouvrir un nouvel onglet pour le lien du fichier Google Drive
driver.switch_to.new_window('tab')
driver.get("https://drive.google.com/file/d/1-RJnVpUnBsVnUvq8gshM4e2lcdexnTic/view?usp=drive_web")
print("✅ Accès à la page de l'emploi du temps réussi !")

# Cliquer sur le bouton de téléchargement dans Google Drive
time.sleep(2)
download_button = driver.find_element(By.XPATH, "//div[@aria-label='Télécharger']")
download_button.click()

# Attendre pour que le fichier soit téléchargé
time.sleep(10)

# Fermer le navigateur
driver.quit()