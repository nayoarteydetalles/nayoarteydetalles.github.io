# -*- coding: utf-8 -*-
"""
Servidor local de la web de Nayo.
Uso:  python serve.py
Abre automáticamente http://localhost:8777 en tu navegador.
(Ctrl + C para detener.)
"""
import http.server, socketserver, webbrowser, os, threading

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.mp4': 'video/mp4', '.webp': 'image/webp'}
    def log_message(self, *a): pass  # silencioso

class Server(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    with Server(("127.0.0.1", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("\n  Nayo - Arte & Detalles")
        print("  Sitio web corriendo en:  " + url)
        print("  (Ctrl + C para detener)\n")
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Servidor detenido.")

if __name__ == "__main__":
    main()
