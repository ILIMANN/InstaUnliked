@echo off

set "isBackground=True"
::Verify setup
if not exist ".setup_done" (
    echo !!! Please make sure you have competed setup succesfully. Exiting the process...
    pause
    exit /b
)
if not exist "session.json" (
    echo !!! You are missing the session.json file. Exiting the process...
    pause
    exit /b
)
echo Setup verified. Initializing the process...

if isBackground == True (
    python -u code/unliker_bot_background.py
    pause
) else (
    python -u code/unliker_bot_showaction.py
    pause
)