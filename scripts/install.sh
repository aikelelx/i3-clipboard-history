#!/bin/bash

# Установщик для i3-clipboard-history

set -e

echo "🔧 Установка i3 Clipboard History Manager..."

# Проверка зависимостей
echo "📦 Проверка зависимостей..."

# Установка зависимостей
sudo apt update
sudo apt install -y python3 python3-pip xclip rofi libnotify-bin

# Создание директорий
mkdir -p ~/.local/bin
mkdir -p ~/.config/clipman

# Копирование программы
cp src/clipman.py ~/.local/bin/clipman
chmod +x ~/.local/bin/clipman

echo "✅ Установка завершена!"
echo ""
echo "📝 Добавьте в ~/.config/i3/config:"
echo ""
echo "  exec --no-startup-id ~/.local/bin/clipman --daemon"
echo "  bindsym \$mod+h exec ~/.local/bin/clipman --show"
echo "  bindsym \$mod+Shift+h exec ~/.local/bin/clipman --clear"
