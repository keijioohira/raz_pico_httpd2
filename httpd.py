def start_page(state):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Pico Web Server</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <h1>Pico LED is {state}</h1>
    <a href="/led/on">Turn ON</a>
    <a href="/led/off">Turn OFF</a>
    <a href="/play">Play Mario</a>
    <a href="/stop">Stop Mario</a>
</body>
</html>"""
    return html
