"""
主処理
"""
import httplib2, os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient import discovery
import re
import sys
import pyperclip

"""
主処理
"""
def main():

    """
    # 引数チェック、クライアントファイルパス、クレデンシャルファイルパス、OTPのPINコード
    if len(sys.argv) < 4:

        # 警告
        print ("./get_otp.py USER_SECRET_FILE CLIENT_SECRET_FILE SCOPES PIN")

        # 関数から抜ける
        return
    """

    # Gmail権限のスコープを指定
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

    # クライアントファイル
    # CLIENT_SECRET_FILE = sys.argv[1]
    CLIENT_SECRET_FILE = 'client_id.json'

    # クレデンシャルファイル
    # USER_SECRET_FILE = sys.argv[2]
    USER_SECRET_FILE = 'credentials-gmail.json'

    # PINコード
    # PIN = sys.argv[3]
    # 実際の環境に合わせてPINコードを書き換える
    PIN = '99999'

    # 取得した OTP をクリップボードにコピー
    pyperclip.copy(get_otp(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES, PIN))


"""
ユーザー認証データの取得
"""
def gmail_user_auth(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES):

    # ユーザーの認証データの読み取り
    store = Storage(USER_SECRET_FILE)
    credentials = store.get()

    # ユーザーが認証済みか?
    if not credentials or credentials.invalid:

        # 新規で認証する
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = 'Python Gmail API'
        credentials = tools.run_flow(flow, store, None)
        print('認証結果を保存しました:' + USER_SECRET_FILE)

    return credentials


"""
Gmailのサービスを取得
"""
def gmail_get_service(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES):

	# ユーザー認証の取得
	# credentials = gmail_auth.gmail_user_auth()
	credentials = gmail_user_auth(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES)
	http = credentials.authorize(httplib2.Http())

	# GmailのAPIを利用する
	service = discovery.build('gmail', 'v1', http=http)

	return service


"""
メッセージ取得処理
"""
def gmail_get_messages(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES):

	# gmail にアクセス
	service = gmail_get_service(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES)
	messages = service.users().messages()

	# 変数 msg_list に自分宛で直近 10 件の id と threadId を配列で格納
	msg_list = messages.list(userId='me', maxResults=10).execute()
	# import pdb; pdb.set_trace()

	# 変数 msg_list の要素 messages を一個ずづつ取り出し、変数 msg に格納
	for msg in msg_list['messages']:
		# import pdb; pdb.set_trace()
	
		# 変数 msg のから id の要素を取り出し変数 topid に格納
		topid = msg['id']
		# import pdb; pdb.set_trace()

		# 変数 msg に自分宛で、かつ 変数 id に格納されたメッセージを格納
		msg = messages.get(userId='me', id=topid).execute()
		# import pdb; pdb.set_trace()

		line = msg['snippet']
		# import pdb; pdb.set_trace()

		# OTPストリングの場合はラインループ処理を抜ける
		if re.match('^1234567890 [0-9]{10} NOS IT Div\.$', msg['snippet']):
			break

	return line


"""
OTP取得処理
"""
def get_otp(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES, PIN):

    maintext = gmail_get_messages(USER_SECRET_FILE, CLIENT_SECRET_FILE, SCOPES)
    # import pdb; pdb.set_trace()

    # OTPを取得、本文の 12 - 21 文字目が OTP ストリングなので、インデクス指定でスライシング
    line = [maintext[11], maintext[12], maintext[13], maintext[14], maintext[15], maintext[16], maintext[17], maintext[18], maintext[19], maintext[20]]
    # import pdb; pdb.set_trace()

    # 変数 pin の空の配列を作成
    pin = []

    # 変数 pin に文字列 PIN から一文字ずつスライシングして配列を作成
    for i in range(len(PIN)):
        # import pdb; pdb.set_trace()
        pin += PIN[i]

    # 変数 otp の空の配列を作成
    otp = []

    # 変数 pin から インデクス番号と要素(ピン番号)を取り出し、変数 str をピン番号でインデクシングして、変数 otp に格納
    for i, j in enumerate(pin):
        # import pdb; pdb.set_trace()
        otp += line[int(j)]

    # 最後、文字悦に変換
    otp = str(''.join(otp))
    # import pdb; pdb.set_trace()

    return otp


"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
