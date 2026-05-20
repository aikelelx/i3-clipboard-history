#!/usr/bin/env python3
import subprocess
import time
import os
import sys
from datetime import datetime

HISTORY_FILE = os.path.expanduser("~/.clipboard_history.txt")

def save_to_history(text):
    if not text:
        return
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = f.readlines()
    if len(history) > 0:
        last_line = history[-1].strip()
        if '|' in last_line:
            last_text = last_line.split('|')[1].strip()
        else:
            last_text = last_line
        if last_text == text:
            return
    with open(HISTORY_FILE, 'a') as f:
        f.write(f"{datetime.now()} | {text}\n")

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("История пуста")
        return
    with open(HISTORY_FILE, 'r') as f:
        lines = f.readlines()
    if not lines:
        print("История пуста")
        return
    print("\n=== ИСТОРИЯ БУФЕРА ОБМЕНА ===\n")
    for i, line in enumerate(reversed(lines[-20:]), 1):
        print(f"{i}. {line.strip()}")

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
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except:
        pass
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
        if sys.argv[1] == '--daemon':
            daemon_mode()
        elif sys.argv[1] == '--show':
            show_history()
        elif sys.argv[1] == '--clear':
            clear_history()
        else:
            print("Использование: clipman [--daemon|--show|--clear]")
    else:
        show_history()

if __name__ == "__main__":
    main()
