1) navigate to GUI dir in cmd
2) pyinstaller.exe --onefile --windowed --icon=datat_logo.ico --hidden-import babel.numbers --add-data todo.ico;. python_gui.py

add data flag adds the file that was missing without having to be in the same dir
hidden import allows secondary import to pass - this kept throwing errors. to troubleshoot remove window view to see missing modules



https://stackoverflow.com/questions/40716346/windows-pyinstaller-error-failed-to-execute-script-when-app-clicked
also added this resource path function but I don't think it worked

https://stackoverflow.com/questions/25733467/no-module-named-when-using-pyinstaller