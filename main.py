import pyperclip as pc
import word_count as wc

if __name__ == "__main__":
    clipboard_text = pc.waitForNewPaste()
    print(f"Word count of text on the clipboard: {wc.word_count(clipboard_text)}")
