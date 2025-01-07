from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 替換為您的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('Channel Access Token')
handler = WebhookHandler('Channel Secret')


@app.route("/callback", methods=['POST'])
def callback():
    # 獲取請求中的 Line 簽名
    signature = request.headers['X-Line-Signature']
    # 獲取請求主體
    body = request.get_data(as_text=True)
    try:
        # 驗證簽名並處理請求
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理文字訊息事件


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_text = "您說了：" + user_message
    # 回覆使用者
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
