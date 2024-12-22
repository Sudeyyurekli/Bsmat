Sanal makine kurulumu yapıldı ve işletim sistemi tipi Ubuntu olarak ayarlandı.

sudo apt update && sudo apt upgrade -y komutu ile sistem güncellemesi yapıldı.

sudo apt install python3 python3-pip -y Komutu ile Python kurulumu yapıldı.

mkdir -p /home/ubuntu/bsm/logs komutu ile log dosyasının saklanacağı dizin oluşturuldu.(değişikliklerin kaydedileceği changes.json dosyasını içerecektir.)

pip install watchdog (Değişikliklerin izlenebilmesi için watchdog kütüphanesinin kurulumu yapıldı.)

Script kodu yazıldı

sudo nano /etc/systemd/system/directory_watcher.service Komutu ile servis dosyası oluşturuldu.

sudo systemctl daemon-reload
sudo systemctl enable directory_watcher.service
sudo systemctl start directory_watcher.service
sudo systemctl status directory_watcher.service

Servis ayarları tamamlandı.







