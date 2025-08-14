@echo off
set app=csv_wtf_basic.exe
echo Invoking %app% "%1"
echo Please wait for the tool's results to be printed to the terminal.
%HOMEDRIVE%%HOMEPATH%\.local\bin\%app% --input "%1"
pause