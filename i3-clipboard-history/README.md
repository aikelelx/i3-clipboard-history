# Clipman - менеджер буфера обмена для i3

## Установка
./scripts/install.sh

## Использование
~/.local/bin/clipman --daemon  # Запуск в фоне
~/.local/bin/clipman --show    # Показать историю
~/.local/bin/clipman --clear   # Очистить историю

## Настройка i3
Добавьте в ~/.config/i3/config:
exec --no-startup-id ~/.local/bin/clipman --daemon
bindsym $mod+h exec ~/.local/bin/clipman --show
