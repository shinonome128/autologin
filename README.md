# autologin   
  
## 目的  
  
パスワード入力がメンドイけど、自動化すると危ない  
だからセミオートでBYODにログイン、VDIにログインしたり  
  
## 参照先  
  
Gmail API  
http://fits.hatenablog.com/entry/2015/06/21/151142  
  
Wox + Everything  
https://syon.github.io/refills/rid/1501413/  
  
  
## GitHub上で管理していないファイル  
  
GmailにOAatuで認証するときのクレデンシャルファイル  
```  
client_id.json  
credentials-gmail.json  
```  
  
## クレデンシャルファイルの作り方  
  
この手順で2ファイルを生成、同一ディレクトリに配置  
http://fits.hatenablog.com/entry/2015/06/21/151142  
  
## 各スクリプト内容  
  
get_otp.py  
Gmailにログインしてワンタイムパスワードを取得  
Gmail APIを利用時にOathを利用  
認証にはクレデンシャルファイル利用  
  
otp.bat  
WoXで呼び出す時のラッパー  
  
get_noswin.py  
ハードコーディングされているNOSWINパスワードを取得  
  
noswin.bat  
WoXで呼び出す時のラッパー  
  
byodlogin.bat  
WoXで呼び出す時のラッパー  
検疫モジュールを起動  
get_noswin.py を叩く  
  
vmlogin.bat  
WoXで呼び出す時のラッパー  
ビュークライアントを起動  
get_otp.py を叩く  
  
## 利用時に変更する部分  
  
get_otp.py  
```  
    # 実際の環境に合わせてPINコードを書き換える  
    PIN = '99999'  
```  
  
get_noswin.py  
```  
    # NOSWIN のパスワード書いておく  
    NOSWIN = 'hogehoge'  
```  
  
以上  
