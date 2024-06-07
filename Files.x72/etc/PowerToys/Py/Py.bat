@echo off

REM Check if .venv or .env directories exist
if not exist ".venv" (
    if not exist ".env" (
        echo Creating virtual environment '.env'
        python -m venv .env

        call .env\Scripts\activate
    )
) else call .venv\Scripts\activate

if /I "%1"=="install" (
    if exist ".venv" .venv\Scripts\activate & pip %*
    if exist ".env" .env\Scripts\activate & pip %*
)

if /I "%1"=="freeze" (
    if exist ".venv" .venv\Scripts\activate & pip freeze>requirements.txt
    if exist ".env" .env\Scripts\activate & pip freeze>requirements.txt
)

if /I "%1"=="list" (
    if exist ".venv" .venv\Scripts\activate & pip list
    if exist ".env" .env\Scripts\activate & pip list
) else (
    if exist ".venv" .venv\Scripts\activate & python %*
    if exist ".env" .env\Scripts\activate & python %*
)
