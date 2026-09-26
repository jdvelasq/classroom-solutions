@echo off

REM Los mismos objetivos permiten practicar automatización también en Windows.

if "%1"=="report" py -3 src/main.py
if "%1"=="test" py -3 -m pytest tests/test_activity.py
