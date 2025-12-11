termux-change-repo
pkg update -y
pkg upgrade -y
pkg install python -y
pip install python-telegram-bot
pip install flask
mkdir starsbot
cd starsbot
nano bot.py
export $(cat.env)
export $(cat .env)
cd bot
nano .env
.
cd ~/aimusicbot
nano requirements.txt
nano Procfile
nano render.yaml
nano bot.py

