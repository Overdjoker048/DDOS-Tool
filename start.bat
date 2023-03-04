@echo off
color a
title DDOS Tool

py -m pip install -r requirements.txt
python.exe -m pip install --upgrade pip

cmd /k py main.py