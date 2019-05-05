# CMPE 272 - Enterprise SW Platforms
Progressive Project for CMPE272 
Team Warriors 
Team Members:
* Pradeep 
* Sanjeevi
* Senthil
* Yuva

## LearnFlask 
### Purpose 
Learning to build and deploy Flask based webserver using web example

### Reference
Reference [MicroBlog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - Building a Simple Web Server using Flask

### Built With
* [Flask](https://www.palletsprojects.com/) - The web framework used

### Local Deployment

```
(venv) $ export FLASK_APP=microblog.py
(venv) $ sudo bash
(venv) root $ . venv/bin/activate
(venv) root $ flask run --host=0.0.0.0 --port=80
```

### AWS Instance Deployment:

* Clone git repository to root
    * Ref: https://stackoverflow.com/questions/9443927/git-clone-into-home-directory/9444352
    * Ref: https://datawookie.netlify.com/blog/2017/08/remote-desktop-on-an-ubuntu-ec2-instance/ 
```
$ cd ~/CMPE272
$ git init
$ git remote add origin https://github.com/YuvaAthur/cmpe272.git
$ git pull origin master
```
* Remove Git from root directory ```rm -rf .git```


* Remote connection from VSCode
    * Ref: Search: "running vscode on ec2 ubuntu instance"
    * Ref: https://medium.com/@prtdomingo/editing-files-in-your-linux-virtual-machine-made-a-lot-easier-with-remote-vscode-6bb98d0639a4
    * Ref: (Sublime) http://blog.keyrus.co.uk/editing_files_on_a_remote_server_using_sublime.html 
    * Ref: https://askubuntu.com/questions/812192/installing-visual-studio-code-on-aws 

* Steps for remote VS Code
    * Add Remote VSCode Extension 
        * Implemented by : Rafael Maiolla : Needs to be security checked?
    * Reload VS Code
        * Run ``` >Reload Window ``` from command palette
    * Install rmate on EC2 instance
```
sudo wget -O /usr/local/bin/rmate https://raw.github.com/aurora/rmate/master/rmate
sudo chmod a+x /usr/local/bin/rmate

```
* Execute ``` >Remote: Start Server``` from command palette
* Add Remote access to .ssh/config file
```
RemoteForward 52698 127.0.0.1:52698
```
```
ssh -R 52698:localhost:52698 ec2-54-80-101-121.compute-1.amazonaws.com 
```


# Options to connect to EC2 Instance
## Using Desktop Manager

* Setting up AWS Destop environment
    * Ref: https://comtechies.com/how-to-set-up-gui-on-amazon-ec2-ubuntu-server.html 
    * LXDE
```
$ sudo apt-get update -y   
$ sudo apt-get install lxde -y
$ sudo apt-get install xrdp -y
$ sudo passwd ubuntu 'pass1234'
$ vi /etc/xrdp/xrdp.ini
```
    * Open RDP Port (3389) on AWS inbound ports
```
$ sudo service xrdp restart
```
    * Use startx
```
$ sudo update-alternatives --config x-session-manager
```



* ### Altertnative is to work with VNC server ####
    * Ref: https://stackoverflow.com/questions/25657596/how-to-set-up-gui-on-amazon-ec2-ubuntu-server 
    * Ref: https://www.youtube.com/watch?v=r-lQ1VjY02s 
```
$ sudo useradd -m awsgui
$ sudo passwd awsgui   # 'pass1234'
$ sudo usermod -aG admin awsgui
$ sudo vim /etc/ssh/sshd_config # edit line "PasswordAuthentication" to yes
$ sudo /etc/init.d/ssh restart

$ sudo apt-get update
$ sudo apt-get install ubuntu-desktop
$ sudo apt-get install vnc4server
$ su - awsgui       # ^D to exit
$ vncserver # set password 'pass1234'
$ vncserver -kill :1
$ vim /home/awsgui/.vnc/xstartup 
```
            #!/bin/sh
            
            # Uncomment the following two lines for normal desktop:
            unset SESSION_MANAGER
            exec sh /etc/X11/xinit/xinitrc

            [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
            [ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
            xsetroot -solid grey
            vncconfig -iconic &
            x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
            x-window-manager &
```
$ vncserver
$ sudo iptables -A INPUT -p tcp --dport 5901 -j ACCEPT

```
* MacOSX Client side
    * Install vnc viewer
        * https://www.realvnc.com/en/connect/download/viewer/ 
    




* Ref: https://www.brianlinkletter.com/how-to-run-gui-applications-xfce-on-an-amazon-aws-cloud-server-instance/ 


* Install VSCode
    * Ref: https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-18-04/
```
$ sudo apt update
$ sudo apt install software-properties-common apt-transport-https wget
$ wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
$ sudo apt install code
```
* Run code
    * https://techoverflow.net/2018/06/05/how-to-fix-puppetteer-error-while-loading-shared-libraries-libx11-xcb-so-1-cannot-open-shared-object-file-no-such-file-or-directory/
```
$ sudo apt-get install gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
```

