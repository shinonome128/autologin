@ECHO ON


REM ///////////////////////////////////////////////////
REM WOXから叩くと失敗するので代替策
REM ///////////////////////////////////////////////////

start "" "C:\Program Files (x86)\VMware\VMware Horizon View Client\vmware-view.exe"
cd C:\Users\shino\doc\autologin
start get_otp.py

REM ///////////////////////////////////////////////////

