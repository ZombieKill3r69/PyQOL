import time

# test if the library works
def test() -> str:
    print("This is a test")
 
    # If used to give variable value
    return "This is a test"

def clear():
    # Simply output the unicode escape code for clear screen
    print("\033[2J")

def printslow(text: str, speed: float = 0.3, do_new_line: bool = False):

    if not isinstance(text, str):
        raise ValueError("text input is not a string")
    if not isinstance(speed, (int, float)):
        raise ValueError("speed is not float/int")
    if not isinstance(do_new_line, bool):
        raise ValueError("new line value is not a boolian")

    for char in text:
        print(char, end="", flush=True)

        if do_new_line:
            print()

        time.sleep(speed)
