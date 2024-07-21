# Descripton
Coin feature added to RetroPi.
<br /><br />
User has to enter 3 coins to play a limited amount of time then taken back to "Enter Coins" screen.

## Set Up
Assuming basic linux skills such as editing a file, modifing permissions, chanding directory, ect.
1) First follow the instruction to get RetroPie [https://retropie.org.uk/docs/First-Installation/]. It is recommended use to Raspberry Pi Imager and to add custom name, password, as well as reliable wifi network during setup process (see installation instuctions on given websites). 
Then add games using [https://retropie.org.uk/docs/Transferring-Roms/]. Map a controller in order to navigate the menues.
2)Start by exiting EmulationStation by going to the menue and selecting ```exit>exit EmulationStation```. You will be sent to RetroPi in headless mode to re-enter EmulationStation run ```emulationstation``` in terminal.
3) If wifi network was not set during the installation process then follow [Pi Access Using SSH](#pi-access-using-ssh)
4) From here files can be moved over using scp directly from ssh terminal, copy and paste, or other file transfer methods can be used. Note than Xsession will need to replace original Xsession file.
5) Wire up button to Pi see [Button](#button). Note other hardware such as coin mechanism and arcade box frame is work in progress.
6) Reboot Pi

## Program Flow Chart

![Arcade Machine Diagram](https://github.com/user-attachments/assets/da28ee65-e17c-447b-9bb6-5e33fc3b539d)

## File Locations

#### rc.local
```/etc```
<br /><br />

#### Xsession
```/etc/X11```
<br /><br />

#### coin_counter.py
```/opt/retropie/configs/all/emulationstation/scripts```
<br /><br />

#### A_session_manager.sh
```/opt/retropie/configs/all/emulationstation/scripts/game-start```
<br /><br />

#### session_manager.py
```/opt/retropie/configs/all/emulationstation/scripts/game-start```
<br /><br />

## Pi Access Using SSH
Wifi network can be added during set up or by adding a network in ```/etc/wpa_supplicant/wpa_supplicant.conf``` \(will need sudo to write to file). <br /> <br />
Example of adding networks:
```
network={
ssid="wifi-name-1"
psk="password1"
}
network={
ssid="wifi-name-2"
psk="password2"
}
```
Connect to pi using ssh ```(pi_name)@(ip_address_of_pi)```. You will need the Pi's password

## Button
Button is connected to GPIO pin 17 (pin 11) and the GND (pin 9) pin see image for reference.

![Pi 4 pinout](https://github.com/user-attachments/assets/8ac310e6-6d4a-4ee3-b262-d1d481be0524)

#### Example button wiring (pins are not accurate to this project, follow pins above) !!!
![Example button wiring](https://github.com/user-attachments/assets/3cc4f27e-c6f0-4a4f-af4f-cf8a4293a20d)


## Switching to Kiosk Mode
Switching to Kiosk Mode can prevent user from leaving EmulationStation and tampering with Linux environment. 
To switch to Kiosk mode from Full mode go to ```home/pi/.emulationstation/es_settings.cfg```. Open file and change
```<string name="UIMode" value="Full" />``` Value to Full or Kiosk. See more details on [https://retropie.org.uk/docs/Child-friendly-EmulationStation/]
#### It is recommended to start in Full mode and get fimilar with the system, since getting out of Kiosk mode can be difficult without SSH to modify the es_settings.cfg. 

## Sample Image of Coin Counter GUI
![GUI sample](https://github.com/user-attachments/assets/2fbcf487-c2c4-46ec-a380-2c3dff325593)

## Software Notes
- Xsession framework provides Pi with GUI capabilities which are used to show coin counter GUI. Xsession framework may or may not need to be installed by user (I can't remeber, its been too long. I'll have to verify later).
- Xsession is started using xstart command.
- rc.local runs during boot which is a good time to start Xsession.
- Xsession might still run in background which may be causing input lag during gameplay (I need to verify).
- Session manager will allow user to play for a 4 mininute and 30 second duration then will reboot Pi to send them back to coin counter screen.
