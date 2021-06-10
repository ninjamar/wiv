#this file installs wiv and all it's dependencies
#this file currently only works on linux
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac
if [[ $machine == "Linux" ]] 
then
  sudo apt update
  sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 gir1.2-webkit2-4.0
  pip3 install pycairo
  pip3 install pygobject
  git clone https://github.com/ninjamar/wiv --depth 1
  sudo echo 'alias wiv="python3 /wiv/wiv/wiv.py"' >> ~/.bashrc
  source ~/.bashrc
fi
