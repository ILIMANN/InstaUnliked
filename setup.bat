@echo off

::Check for python
python --version >nul 2>&1
if %errorlevel% neq 0 (
	echo !!! Python is not detected in your device, exiting the process...
    pause
	exit /b
)
echo Python is detected, continuing the process...

::Check for pip
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo !!! pip is not detected in your device, exiting the process...
    pause
    exit /b
)

echo --- Installing playwright...
pip install playwright
if %errorlevel% neq 0 (
    echo !!! There was an error installing the playwright, exiting the process...
    pause
    exit /b
)
echo Playwright is installed succesfully!

echo --- Installing chromuim packages for playwright...
python -m playwright install chromium
if %errorlevel% neq 0 (
    echo !!! There was an error installing the chromium packages, exiting the process...
    pause
    exit /b
)
echo Chromium packages are installed succesfully!
echo setup_complete > .setup_done
echo ===========================================

python -u code\save_cookies.py
pause