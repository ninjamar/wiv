# Wiv
A browser made in python using webkit

## Installation
### Debian/Ubuntu
```bash
sudo apt update
sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 gir1.2-webkit2-4.0
pip3 install pycairo pygobject requests
rm -r wiv
git clone https://github.com/ninjamar/wiv --depth 1
sudo echo 'alias wiv="python3 ~/wiv/wiv/wiv.py"' >> ~/.bashrc
source ~/.bashrc
```
To run, execute `wiv`
### Windows (Untested)
Go to [this](https://www.msys2.org/) and download the x86_64 installer. 
Follow the instructions on the page for the setup. 
Run `C:\msys64\mingw64.exe` - a  terminal window should popup.
 
```bash
pacman -Suy 
pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject
pip3 install requests
rm -r wiv
git clone https://github.com/ninjamar/wiv --depth 1
```
To run, execute `python3 C:\wiv\wiv\wiv.py` or add a command to your system using [this](https://stackoverflow.com/questions/20530996/aliases-in-windows-command-prompt)

### MacOS (Untested)
```bash
brew install pygobject3 gtk+3
```
