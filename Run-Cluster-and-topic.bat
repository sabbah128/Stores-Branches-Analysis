@echo off
setlocal enabledelayedexpansion


set "script_folder=cluster-scripts"

set "cmd1=0-start-zookeeper.cmd"
set "cmd2=1-start-kafka-server-0.cmd"
set "cmd3=2-start-kafka-server-1.cmd"
set "cmd4=3-start-kafka-server-2.cmd"
set "cmd5=4-create-store-data-topic.cmd"
set "cmd6=5-report-cluster.cmd"

:: Check if the script folder exists
if not exist "%script_folder%" (
    echo Error: %script_folder% folder not found.
    pause
    exit /b 1)

echo Running CMD files in new terminals...

:: Run each CMD file in a new terminal
for %%i in (1 2 3 4 5 6) do (
    call :run_cmd_in_new_terminal %%i
    timeout /t 10 /nobreak >nul)

echo All CMD files have been started.
pause
exit /b 0

:: Function to run a CMD file in a new terminal
:run_cmd_in_new_terminal
set "current_cmd=!cmd%1!"
if exist "%script_folder%\!current_cmd!" (
    echo Starting !current_cmd! in a new terminal...
    start "!current_cmd!" cmd /c "cd /d %cd%\%script_folder% && call !current_cmd! && pause"
) else (
    echo Warning: !current_cmd! not found in %script_folder% folder.
)
goto :eof