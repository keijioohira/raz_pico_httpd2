def start_page(state):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
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

        <p>温度・湿度測定</p>
        <a href="/measure_start">Measurement Start</a>
        <a href="/measure_stop">Measurement Stop</a>

        <div style="margin-top: 20px;">
            <label for="sensor" style="display:block; margin-bottom: 8px;">sensor data</label>
            <input type="text" id="sensor" name="sensor" rows="30"size="30">
        </div>
    </div>
</body>
</html>"""
    return html
