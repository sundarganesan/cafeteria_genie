import threading
from config import VIDEO_SOURCES
from utils.video_utils import process_video_feed

def main():
    threads = []
    for source_id, path in VIDEO_SOURCES.items():
        t = threading.Thread(target=process_video_feed, args=(source_id, path))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
