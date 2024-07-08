from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse

router = APIRouter()

ws_tag = "/ws"

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
# 上記コードに関する自分の理解
'''
var ws = new WebSocket("ws://localhost:8000/ws"); でWebSocketのインスタンスを作成している
ws.onmessage = function(event) でWebSocketのメッセージを受け取る処理を設定している
we.send(input.value) でWebSocketのメッセージを送信している
'''

@router.get("/ws/sample", tags=[ws_tag], name="WebSocketサンプルのページを表示する")
async def get():
    return HTMLResponse(html)

# websocketはopenapiに表示されないのでtagsなどの指定は無意味
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # WebSocket接続を受け入れる
    await websocket.accept()
    # 接続が切断されるまでループを続ける
    while True:
        # メッセージを受け取る
        # ここで例外が発生すると、接続が切断される
        data = await websocket.receive_text()

        # メッセージを送信する
        await websocket.send_text(f"Message text was: {data}")