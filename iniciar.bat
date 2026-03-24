@echo off
chcp 65001 > nul
title Automação Trello x Excel

echo.
echo ============================================
echo   Automação Trello x Excel
echo ============================================
echo.

cd /d "%~dp0"

python App\main.py

echo.
if %ERRORLEVEL% == 0 (
    echo ============================================
    echo   Concluído com sucesso!
    echo ============================================
) else (
    echo ============================================
    echo   Finalizado com erros. Verifique os logs.
    echo ============================================
)

echo.
pause