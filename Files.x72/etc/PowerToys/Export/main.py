import ctypes, ctypes.wintypes, sys

# Constants
STD_OUTPUT_HANDLE = -11

# Get the handle to the console output
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# Define the console screen buffer info structure
class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.wintypes._COORD),
        ("dwCursorPosition", ctypes.wintypes._COORD),
        ("wAttributes", ctypes.wintypes.WORD),
        ("srWindow", ctypes.wintypes.SMALL_RECT),
        ("dwMaximumWindowSize", ctypes.wintypes._COORD),
    ]

# Get the console screen buffer info
csbi = CONSOLE_SCREEN_BUFFER_INFO()
ctypes.windll.kernel32.GetConsoleScreenBufferInfo(std_out_handle, ctypes.byref(csbi))

# Calculate the size of the console window
console_size = csbi.dwSize.X * csbi.dwSize.Y

# Create a buffer to store the console output
buffer = ctypes.create_string_buffer(console_size)

# Read the console screen buffer
ctypes.windll.kernel32.ReadConsoleOutputCharacterA(
    std_out_handle,
    buffer,
    console_size,
    ctypes.wintypes._COORD(0, 0),
    ctypes.byref(ctypes.wintypes.DWORD())
)

# Convert buffer to string
raw_output = buffer.value.decode('utf-8', errors='ignore')

# Get console width
console_width = csbi.dwSize.X

# Process the raw output to remove extra spaces and add new lines
processed_output = ""
for i in range(0, len(raw_output), console_width):
    line = raw_output[i:i + console_width].rstrip()
    processed_output += line + '\n'

processed_output = processed_output.strip()

# Save the processed output to a file
with open(sys.argv[1], 'w', encoding='utf-8') as f:
    f.write(processed_output + "\n")
