
"""
必要モジュールをロード
"""
import pyperclip


"""
主処理
"""
def main():

    # NOSWIN のパスワード書いておく
    NOSWIN = 'hogehoge'

    # 取得した NOSWIN をクリップボードにコピー
    pyperclip.copy(NOSWIN)


"""
お作法、他ファイルから呼び出された場合は、このスクリプトは実行されない
"""
if __name__ == "__main__":
    main()
