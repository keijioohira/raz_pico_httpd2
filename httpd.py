def start_page(state):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Pico Web Server</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <div class="container">
        <h1>Pico Operation Page</h1>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
        <a href="/play">Play Mario</a>
        <a href="/stop">Stop Mario</a>
    </div>
</body>
</html>"""
    return html
