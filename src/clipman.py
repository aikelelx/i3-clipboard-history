#!/usr/bin/env python3
import subprocess
import time
import os
import sys
from datetime import datetime

HISTORY_FILE = os.path.expanduser("~/.clipboard_history.txt")
MAX_HISTORY = 500

def save_to_history(text):
    if not text:
        return
    # Читаем существующую историю
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = f.readlines()
    # Проверяем дубликат с последним
    if history and history[-1].split(' | ')[1].strip() == text:
        return
    # Добавляем новую запись
    with open(HISTORY_FILE, 'a') as f:
        f.write(f"{datetime.now()} | {text}\n")
    # Ограничиваем размер истории
    if len(history) >= MAX_HISTORY:
        with open(HISTORY_FILE, 'w') as f:
            f.writelines(history[-MAX_HISTORY:])

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("История пуста")
        return
    with open(HISTORY_FILE, 'r') as f:
        lines = f.readlines()
    if not lines:
        print("История пуста")
        return
    print("\n=== История буфера обмена ===\n")
    for i, line in enumerate(reversed(lines[-20:]), 1):
        parts = line.split(' | ', 1)
        if len(parts) == 2:
            time_str = parts[0]
            content = parts[1].strip()[:80]
            print(f"{i}. [{time_str}] {content}")

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("История очищена")
    else:
        print("История пуста")

def get_clipboard():
    try:
        result = subprocess.run(['xclip', '-selection', 'clipboard', '-o'],
                               capture_output=True, text=True, timeout=1)
        return result.stdout.strip() if result.returncode == 0 else None
    except:
        return None

def daemon_mode():
    print("Clipman демон запущен. Мониторинг буфера обмена...")
    last_content = None
    while True:
        current = get_clipboard()
        if current and current != last_content:
            save_to_history(current)
            print(f"Сохранено: {current[:50]}...")
            last_content = current
        time.sleep(1)

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '--daemon':
            daemon_mode()
        elif arg == '--show':
            show_history()
        elif arg == '--clear':
            clear_history()
        else:
            print("Использование: clipman [--daemon|--show|--clear]")
    else:
        show_history()

if __name__ == "__main__":
    main()
