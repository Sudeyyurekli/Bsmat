import os
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, log_file):
        self.log_file = log_file
      #listelenecek eylemler
    def on_created(self, event):
        if not event.is_directory:
            self.log_change(event, 'created')

    def on_deleted(self, event):
        if not event.is_directory:
            self.log_change(event, 'deleted')

    def on_moved(self, event):
        if not event.is_directory:
            self.log_change(event, 'moved')

    def log_change(self, event, event_type):
        # Olay bilgilerini oluştur
        event_details = {
            'event_type': event_type,
            'src_path': event.src_path,
            'dest_path': getattr(event, 'dest_path', None),  # move olayında dest_path var
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        print(f"Detected {event_type} event:")
        print(json.dumps(event_details, indent=4))  # Konsola daha okunabilir şekilde yazdırma
        
        # JSON log dosyasına yaz
        with open(self.log_file, 'a') as log:
            log.write(json.dumps(event_details) + '\n')

def start_monitoring(path, log_file):
    event_handler = ChangeHandler(log_file)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    log_file = "/home/ubuntu/bsm/logs/changes.json"
    monitor_path = "/home/ubuntu/bsm/test"  # İzlemek istediğiniz dizini burada belirleyin
    start_monitoring(monitor_path, log_file)

