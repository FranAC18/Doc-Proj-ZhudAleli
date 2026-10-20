@echo off
setlocal
title Gestor Tesis Agile - Zhud Aleli
cd /d "%~dp0"
python servidor.py
if errorlevel 1 (
  echo No se pudo iniciar el servidor local. Comprueba que Python 3.9 o posterior este instalado.
  pause
)
endlocal
