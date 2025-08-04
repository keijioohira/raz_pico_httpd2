
import dht11
import httpd
import css
import network
import socket
import time
import _thread
import mario

play_flag = {'running': False}
log_buffer = []
auto_reload_flag = {'enabled': False}
thread_flag = {'running': False}

def play_music_thread():
    def should_continue():
        return play_flag['running']
    def music_runner():
        print("[DEBUG] Mario music thread started")
        mario.play(should_continue)
        print("[DEBUG] Mario music thread finished")
        play_flag['running'] = False
    play_flag['running'] = True
    _thread.start_new_thread(music_runner, ())

def stop_music():
    print("[DEBUG] Music stop requested")
    play_flag['running'] = False

def auto_loop():
    thread_flag['running'] = True
    while auto_reload_flag['enabled']:
        result = dht11.read_once()
        log_buffer.append(result)
        print("[DEBUG] Auto Measurement:", result)
        time.sleep(300)
    thread_flag['running'] = False

def handle_request(path):
    global log_buffer

    print(f"[DEBUG] Handling request path: {path}")

    if path == "/":
        body = httpd.start_page("\n".join(log_buffer))
        status = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    elif path == "/measure_start":
        result = dht11.read_once()
        log_buffer.append(result)
        auto_reload_flag['enabled'] = True

        if not thread_flag['running']:
            _thread.start_new_thread(auto_loop, ())
            print("[DEBUG] Started auto_loop thread")
        else:
            print("[DEBUG] auto_loop already running")

        body = httpd.start_page("\n".join(log_buffer))
        status = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    elif path == "/measure_stop":
        auto_reload_flag['enabled'] = False
        print("[DEBUG] Measurement stopped")
        body = httpd.start_page("\n".join(log_buffer))
        status = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    elif path == "/style.css":
        body = css.get_stylesheet()
        status = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n"

    else:
        body = "<html><body><h1>404 Not Found</h1></body></html>"
        status = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"

    return status, body

def wait_for_wifi(wlan, timeout=15):
    print("[DEBUG] Waiting for Wi-Fi to connect...")
    start = time.time()
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
        if time.time() - start > timeout:
            raise RuntimeError("[ERROR] Wi-Fi connection timed out.")
    print(" Connected!")
    print("[DEBUG] IP address:", wlan.ifconfig()[0])

def main():
    SSID = "F660P-dtsh-G"
    PASSWORD = "dyuuuudfx7679"

    print("[DEBUG] Starting Wi-Fi connection")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    time.sleep(2)
    wait_for_wifi(wlan)

    port = 80
    addr = socket.getaddrinfo("0.0.0.0", port)[0][-1]
    server = socket.socket()
    try:
        server.bind(addr)
    except OSError as e:
        if e.errno == 98:
            print(f"[WARN] Port {port} in use. Trying port 8080 instead.")
            port = 8080
            addr = socket.getaddrinfo("0.0.0.0", port)[0][-1]
            server.bind(addr)
        else:
            raise
    server.listen(1)
    print(f"[DEBUG] Server running at http://{wlan.ifconfig()[0]}:{port}")

    while True:
        print("[DEBUG] Waiting for HTTP connection...")
        conn, addr = server.accept()
        print("[DEBUG] Client connected from", addr)
        request = conn.recv(1024).decode()
        print("[DEBUG] Request:", request)

        request_line = request.split('\r\n')[0]
        try:
            method, path, _ = request_line.split()
        except ValueError:
            print("[ERROR] Invalid request line:", request_line)
            conn.close()
            continue

        status, body = handle_request(path)

        conn.send(status)
        conn.send(body)
        conn.close()

if __name__ == "__main__":
    main()
