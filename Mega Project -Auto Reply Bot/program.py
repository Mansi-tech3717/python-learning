
import pyautogui
import time
import pyperclip

# Step 1: Click on the WhatsApp icon at coordinates (1055, 1054)
pyautogui.click(1055, 1054)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

# Step 2: Drag the mouse from (789 ,152) to (1298 ,903) to select the text
pyautogui.moveTo(789 ,152)
pyautogui.dragTo(1298 ,903, duration=1.0, button='left')  # Drag for 1 second

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)  # Wait for 1 second to ensure the copy command is completed

# Step 4: Retrieve the text from the clipboard and store it in a variable
text = pyperclip.paste()

# Print the copied text to verify
print(text)
