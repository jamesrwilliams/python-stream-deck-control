import subprocess


def run_apple_script():
    script = '''tell application "System Events" to tell process "FortiClientAgent"
        tell menu bar item 1 of menu bar 2
            click
            
            set message to ""
            
            if exists menu item "Connect to Points" of menu 1 then
                set message to "Connecting..."
            else
                set message to "Disconnecting..."
            end if
            
            click menu item 2 of menu 1
            return message
        end tell
    end tell
    '''

    proc = subprocess.Popen(['osascript', '-'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    stdout_output = proc.communicate(script.encode())

    print(stdout_output)

if __name__ == "__main__":
    run_apple_script()
