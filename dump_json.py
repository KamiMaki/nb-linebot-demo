# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:47:39 2021

@author: penguin
"""
import json
raw_json = '{ "type": "carousel", "contents": [ { "type": "bubble", "direction": "ltr", "header": { "type": "box", "layout": "vertical", "contents": [ { "type": "filler" } ] }, "hero": { "type": "image", "url": "https://imgur.com/ZuuHu2w.jpg", "align": "center", "size": "full", "aspectRatio": "2:1", "aspectMode": "cover" }, "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "資產配置委員會投資展望", "weight": "bold", "size": "xl", "align": "center", "contents": [] }, { "type": "text", "text": "2021第二季 景氣升溫", "weight": "bold", "size": "lg", "align": "center", "contents": [] }, { "type": "text", "text": "路博邁投資團隊主管齊聚一堂，回顧2020年投資環境的演變，並展望2021年的投資主題。", "align": "start", "margin": "md", "wrap": true, "contents": [] } ] }, "footer": { "type": "box", "layout": "horizontal", "contents": [ { "type": "button", "action": { "type": "uri", "label": "了解更多", "uri": "https://www.nb.com/zh-TW/tw/aac/asset-allocation-committee-outlook-2q2021" } } ] } }, { "type": "bubble", "direction": "ltr", "header": { "type": "box", "layout": "vertical", "contents": [ { "type": "filler" } ] }, "hero": { "type": "image", "url": "https://imgur.com/QvXzBzh.jpg", "align": "center", "gravity": "center", "size": "full", "aspectRatio": "2:1", "aspectMode": "cover" }, "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "固定收益投資展望", "weight": "bold", "size": "xl", "align": "center", "contents": [] }, { "type": "text", "text": "2021年第一季: 通膨風險重現", "weight": "bold", "size": "lg", "align": "center", "contents": [] }, { "type": "text", "text": "即使央行政策維持現狀，但在當前寬鬆的貨幣供給下，經濟復甦也可能重新引發價格壓力。", "align": "start", "margin": "sm", "wrap": true, "contents": [] } ] }, "footer": { "type": "box", "layout": "horizontal", "contents": [ { "type": "button", "action": { "type": "uri", "label": "了解更多", "uri": "https://www.nb.com/zh-TW/tw/fiio/fixed-income-investment-outlook-1q2021" } } ] } }, { "type": "bubble", "direction": "ltr", "header": { "type": "box", "layout": "vertical", "contents": [ { "type": "filler" } ] }, "hero": { "type": "image", "url": "https://imgur.com/DCjnnzq.jpg", "align": "center", "size": "full", "aspectRatio": "2:1", "aspectMode": "cover" }, "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " Solving for 2021", "weight": "bold", "size": "xl", "align": "center", "contents": [] }, { "type": "text", "text": "疫情過後新世界", "weight": "bold", "size": "lg", "align": "center", "contents": [] }, { "type": "text", "text": "路博邁投資團隊主管齊聚一堂，回顧2020年投資環境的演變，並展望2021年的投資主題。", "align": "start", "gravity": "top", "margin": "sm", "wrap": true, "contents": [] } ] }, "footer": { "type": "box", "layout": "horizontal", "contents": [ { "type": "button", "action": { "type": "uri", "label": "了解更多", "uri": "https://www.nb.com/zh-TW/tw/solving/solving-2021" } } ] } } ] }'

raw_json = raw_json.replace('true', 'True')
raw_json = raw_json.replace('false', 'False')

new_json = json.dumps(raw_json)

with open('tmp.json','w') as f:
    f.write(new_json)
    