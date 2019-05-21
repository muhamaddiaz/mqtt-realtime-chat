# mqtt-realtime-chat
Implementasi realtime chat dengan menggunakan protokol mqtt

Pastikan python3 telah terinstall pada pc

1. Install virtualenv
https://virtualenvwrapper.readthedocs.io/en/latest/

2. Install Dependency menggunakan pip3 (pastikan pip3)
"pip3 install --no-cache-dir -r requirements.txt "

3. Install redis-server (Windows/Linux)
https://redislabs.com/blog/redis-on-windows-10/

4. Pastikan Redis berjalan 
Check: "systemctl status redis-server.service"
Jalankan: "systemctl start redis-server.service"

5. Jalankan django server (pastikan sudah berada pada folder yang benar)
default ip: "python3 manage.py runserver"
desired ip: "python3 manage.py runserver <IP>:<PORT>"
