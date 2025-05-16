#!/bin/bash
sudo mkdir /usrdata/local/chromedriver
sudo chown muszi:muszi /usrdata/local/chromedriver
cd /usrdata/local/chromedriver
wget https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.94/linux64/chrome-linux64.zip
wget https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.94/linux64/chromedriver-linux64.zip
wget https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.94/linux64/chrome-headless-shell-linux64.zip
