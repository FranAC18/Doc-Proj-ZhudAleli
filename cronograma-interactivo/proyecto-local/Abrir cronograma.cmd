@echo off
setlocal
title Gestor Tesis Agile - Zhud Aleli
set "DASHBOARD=%~dp0..\index.html"
if not exist "%DASHBOARD%" (
  echo No se encontro el dashboard: "%DASHBOARD%"
  pause
  exit /b 1
)
start "" "%DASHBOARD%"
endlocal
