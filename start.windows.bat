@echo off
chcp 65001 >nul 2>&1
python "%~dp0codelings.py"
if errorlevel 1 (
    echo.
    echo Erro ao iniciar. Verifique se o Python esta instalado e no PATH.
    pause
)
