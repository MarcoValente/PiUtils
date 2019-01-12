echo "Updating apt-get packages"
sudo apt-get update
echo ""
echo "Install new apt-get packages"
cat packages.txt | xargs sudo apt-get install
echo ""
echo "Installing python argcomplete"
sudo pip install argcomplete
sudo activate-global-python-argcomplete
