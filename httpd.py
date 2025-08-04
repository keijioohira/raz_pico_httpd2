def start_page(log_text=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pico Web Server</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <div class="container">
        <h1>Pico Operation Page</h1>

        <div class="button-group">
            <a href="/led/on">LED ON</a>
            <a href="/led/off">LED OFF</a>
            <a href="/play">Play Mario</a>
            <a href="/stop">Stop Mario</a>
        </div>
        <p>温度・湿度測定</p>
        <div class="button-group">
            <a href="/measure_start">Measurement Start</a>
            <a href="/measure_stop">Measurement Stop</a>
        </div>

        <div class="sensor-block">
            <p>sensor data</p>
            <textarea id="sensor" name="sensor" rows="10" cols="40" readonly>{log_text}</textarea>
        </div>
    </div>
</body>
</html>"""
    return html



