#!/bin/bash
# Instala UFW si no está instalado
sudo apt install ufw -y
# Habilita UFW
sudo ufw enable
# Permite los puertos necesarios
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 5000
sudo ufw allow 22
# Muestra el estado de UFW
sudo ufw status