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
### Running
After installation, you can run the browser using the ```wiv``` command
