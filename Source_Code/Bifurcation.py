import asyncio
import websockets

async def serve(websocket, path):
    # Send the HTML page to the client
    await websocket.send(
        '''<!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <title>Scrolling Banner Text Animation effect</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div class="scrolling">
                <h2>scrolling text (defilement du texte)</h2>
            </div>
        </body>
        </html>'''
    )
    # Send the CSS styles to the client
    await websocket.send(
        '''body {
            margin: 0;
            padding: 0;
            font-family: sans-serif;
            background: #6b6b6b;
        }
        .scrolling {
            position: relative;
            width: 100%;
            height: 50px;
            overflow: hidden;
            margin-top: 50px;
        }
        .scrolling h2 {
            position: absolute;
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            font-size: 4em;
            text-align: center;
            line-height: 50px;
            color: #fff;
            transform: translateX(100%);
            animation: scrolling 15s linear infinite;
        }
        @keyframes scrolling {
            0% {
                transform: translateX(100%);
            }
            100% {
                transform: translateX(-100%);
            }
        }'''
    )

start_server = websockets.serve(serve, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()