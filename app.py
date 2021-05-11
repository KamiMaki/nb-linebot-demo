from flask import Flask, request, abort#,redirect
import json
# import db
# from datetime import datetime
# import pandas  as pd
#%%
# DB = db.constructor_DB()



from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)




# Channel Access Token
# line_bot_api = LineBotApi('QaJ08dNM3i3K5HkfFVlwWlo+ETVqyHnE2XHv/8eAs+FzmgnYAXTnAuRuHHOHXFP58mjJROVD2kPsy/Xju6OZk/jywm8jNa+1TMbk8meDIxlEB4GUnZBpXDOI9d0Kk71Gy5sVBSRy709Vr55Ua1XrgwdB04t89/1O/w1cDnyilFU=')
# # Channel Secret
# handler = WebhookHandler('37ba211752bf5e8d752d3f2d53f89fde')


line_bot_api = LineBotApi('gVAAZUKCAd5iouqJ2n6xIhcTVymqVFJ7QzswyrmfAG/O+HF/cBE9663Bu+OovVaZpA6Set/2c7k4ygjBLpS3Vr3EmcrxdaP6IORZf+IPVQV4gdND+nDJD6LIDrXcgsb3S6izJxnJaErY7Uz50kK+FgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('440c699d9821a8b4bc4c7ff0029c9540')


# def url_convert(url,uid):
#     new_url = f'https://40c8dbd2d1fc.ngrok.io?url={url}&uid={uid}'
#     return new_url

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# @app.route("/redir", methods=['GET'])
# def redir():
#     url = request.args.get('url')
#     uid = request.args.get('uid')
#     now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
#     df = pd.DataFrame([[uid],[url],[now]]).transpose()
#     df.columns = ["UID","Click","Time"]
#     db.insert(DB,'user_record',df)
#     return redirect(url)


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    _id = event.source.user_id
    
    with open('funds_search.json',encoding='utf-8-sig', errors='ignore') as f:
        card = json.loads(f.read())
    with open('critical_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        critical_fund = json.loads(f.read())
    with open('inside_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        inside_fund = json.loads(f.read())
    with open('outside_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        outside_fund = json.loads(f.read())
    with open('asset_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        asset_fund = json.loads(f.read())
    with open('stock_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        stock_fund = json.loads(f.read())
    with open('bond_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        bond_fund = json.loads(f.read())
    with open('multiple_asset_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        multiple_asset_fund = json.loads(f.read())
    with open('risk_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        risk_fund = json.loads(f.read())
    with open('RR2_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        RR2_fund = json.loads(f.read())
    with open('RR3_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        RR3_fund = json.loads(f.read())
    with open('RR4_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        RR4_fund = json.loads(f.read())
    with open('RR5_funds.json',encoding='utf-8-sig', errors='ignore') as f:
        RR5_fund = json.loads(f.read())
    
    with open('latest_news.json',encoding='utf-8-sig', errors='ignore') as f:
        latest_news = json.loads(f.read())
    with open('ESG.json',encoding='utf-8-sig', errors='ignore') as f:
        ESG_news = json.loads(f.read())
    with open('5G.json',encoding='utf-8-sig', errors='ignore') as f:
        news_5G = json.loads(f.read())
    with open('CIO.json',encoding='utf-8-sig', errors='ignore') as f:
        CIO_news = json.loads(f.read())
    with open('future.json',encoding='utf-8-sig', errors='ignore') as f:
        future = json.loads(f.read())
    
    
    card_message = FlexSendMessage('card',card)
    critical_fund_message = FlexSendMessage('critical_fund',critical_fund)
    inside_fund_message = FlexSendMessage('inside_fund',inside_fund)
    outside_fund_message = FlexSendMessage('outside_fund',outside_fund)
    asset_fund_message = FlexSendMessage('asset_fund',asset_fund)
    stock_fund_message = FlexSendMessage('stock_fund',stock_fund)
    bond_fund_message = FlexSendMessage('bond_fund',bond_fund)
    multiple_asset_fund_message = FlexSendMessage('multiple_asset_fund',multiple_asset_fund)
    risk_fund_message = FlexSendMessage('risk_fund',risk_fund)
    RR2_fund_message = FlexSendMessage('RR2_fund',RR2_fund)
    RR3_fund_message = FlexSendMessage('RR3_fund',RR3_fund)
    RR4_fund_message = FlexSendMessage('RR4_fund',RR4_fund)
    RR5_fund_message = FlexSendMessage('RR5_fund',RR5_fund)
    
    latest_news_message = FlexSendMessage('latest_news',latest_news)
    ESG_news_message = FlexSendMessage('ESG_news',ESG_news)
    news_5G_message = FlexSendMessage('5G_news',news_5G)
    CIO_news_message = FlexSendMessage('CIO_news', CIO_news)
    future_message = FlexSendMessage('future',future)
    
    
    defult = TextSendMessage(text='數字「1」或「基金」 ： 基金選擇器\n數字「2」或「觀點」 ： 投資觀點')
    quick_reply = TextSendMessage(text='可透過下方類別了解更多：',quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label="5G", text="5G")), QuickReplyButton(action=MessageAction(label="ESG投資", text="ESG投資")),QuickReplyButton(action=MessageAction(label="CIO每周觀點", text="CIO每周觀點")), QuickReplyButton(action=MessageAction(label="投資展望", text="投資展望"))]))
    if event.message.text == '圖卡' or event.message.text == '1':
        line_bot_api.reply_message(event.reply_token,card_message)
    elif event.message.text == '焦點基金':
        line_bot_api.reply_message(event.reply_token,critical_fund_message)
    elif event.message.text == '境內焦點基金':
        line_bot_api.reply_message(event.reply_token,inside_fund_message)
    elif event.message.text == '境外焦點基金':
        line_bot_api.reply_message(event.reply_token,outside_fund_message)
    elif event.message.text == '資產類別基金':
        line_bot_api.reply_message(event.reply_token,asset_fund_message)
    elif event.message.text == '股票型基金':
        line_bot_api.reply_message(event.reply_token,stock_fund_message)
    elif event.message.text == '債券型基金':
        line_bot_api.reply_message(event.reply_token,bond_fund_message)
    elif event.message.text == '多重資產型基金':
        line_bot_api.reply_message(event.reply_token,multiple_asset_fund_message)
    elif event.message.text == '風險等級基金':
        line_bot_api.reply_message(event.reply_token,risk_fund_message)
    elif event.message.text == 'RR2基金':
        line_bot_api.reply_message(event.reply_token,RR2_fund_message)
    elif event.message.text == 'RR3基金':
        line_bot_api.reply_message(event.reply_token,RR3_fund_message)
    elif event.message.text == 'RR4基金':
        line_bot_api.reply_message(event.reply_token,RR4_fund_message)
    elif event.message.text == 'RR5基金':
        line_bot_api.reply_message(event.reply_token,RR5_fund_message)

    elif event.message.text == '觀點' or event.message.text == '2':
        #line_bot_api.reply_message(event.reply_token,card_message)
        line_bot_api.reply_message(event.reply_token,[CIO_news_message,quick_reply])
    elif event.message.text == 'ESG投資':
        line_bot_api.reply_message(event.reply_token,[ESG_news_message,quick_reply])
    elif event.message.text == '5G':
        line_bot_api.reply_message(event.reply_token,[news_5G_message,quick_reply])
    elif event.message.text == 'CIO每周觀點':
        line_bot_api.reply_message(event.reply_token,[CIO_news_message,quick_reply])
    elif event.message.text == '投資展望':
        line_bot_api.reply_message(event.reply_token,[future_message,quick_reply])

    else:
        line_bot_api.reply_message(event.reply_token,defult)
        #line_bot_api.reply_message(event.reply_token,[card_message,quick_reply])
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
