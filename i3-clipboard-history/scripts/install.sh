#!/bin/bash
echo "Установка Clipman..."
sudo apt update
sudo apt install -y xclip
mkdir -p ~/.local/bin
cp src/clipman.py ~/.local/bin/clipman
chmod +x ~/.local/bin/clipman
echo "Установка завершена!"
echo "Запустите: ~/.local/bin/clipman --daemon"
