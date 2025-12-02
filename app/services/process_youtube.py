from typing import Optional

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.scrapers.youtube import YouTubeScraper
from app.database.repository import Repository #db işlemleri (insert, update, select)


TRANSCRIPT_UNAVAILABLE_MARKER = "__UNAVAILABLE__" #transkripti olmayan videolarda db e bunu yaz. Flag bırakmış oluyorsun.


def process_youtube_transcripts(limit: Optional[int] = None) -> dict:
    scraper = YouTubeScraper()
    repo = Repository() #nesneleri oluşturuyorum
    
    #db de transkripti boş olan yt videolarını bulur.
    videos = repo.get_youtube_videos_without_transcript(limit=limit)
    processed = 0
    unavailable = 0
    failed = 0
    
    for video in videos:
        try: #transkripti bulduysan bu sefer db e kaydet
            transcript_result = scraper.get_transcript(video.video_id)
            if transcript_result:
                repo.update_youtube_video_transcript(video.video_id, transcript_result.text)
                processed += 1
            else: #bulamadıysan unavailable olarak işaretler
                repo.update_youtube_video_transcript(video.video_id, TRANSCRIPT_UNAVAILABLE_MARKER)
                unavailable += 1
        except Exception as e:
            repo.update_youtube_video_transcript(video.video_id, TRANSCRIPT_UNAVAILABLE_MARKER)
            unavailable += 1
            print(f"Error processing video {video.video_id}: {e}")
    
    return {
        "total": len(videos),
        "processed": processed,
        "unavailable": unavailable,
        "failed": failed
    }


if __name__ == "__main__":
    result = process_youtube_transcripts()
    print(f"Total videos: {result['total']}")
    print(f"Processed: {result['processed']}")
    print(f"Unavailable: {result['unavailable']}")
    print(f"Failed: {result['failed']}")