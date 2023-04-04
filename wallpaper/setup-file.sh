#!/bin/bash

# Step 0: Hide the Python script
mv wallpaper-changer.py .wallpaper-changer.py

# Step 1: Create the service file
sudo tee /etc/systemd/system/wallpaper-changer.service > /dev/null << EOF
[Unit]
Description=Wallpaper changer
After=network.target

[Service]
User=$(whoami)
ExecStart=$(pwd)/.wallpaper-changer.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Step 2: Reload the systemd daemon
sudo systemctl daemon-reload

# Step 3: Enable the wallpaper-changer service
sudo systemctl enable wallpaper-changer

# Step 4: Start the wallpaper-changer service
sudo systemctl start wallpaper-changer
clear
echo "Thank you all setup"
