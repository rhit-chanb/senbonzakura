import json
import os
import sys
import time

def download(yt_url, audioOnly):
    if yt_url == "nodownload":
        return
    if audioOnly :
        os.system(f"yt-dlp -x --audio-format mp3 --force-overwrites {yt_url} -o \"./dl/raw.%(ext)s\"")
        print("done downloading audio only " + yt_url)
    else:
        os.system(f"yt-dlp --force-overwrites -S res,ext:mp4:m4a --recode mp4 {yt_url} -o \"./dl/raw.%(ext)s\"")
        print("done downloading video " + yt_url)
    return
def scatter(audio_only):
    target_filename = "\"./dl/raw.mp4\""
    ext = ".mp4"
    if audio_only:
        target_filename = "\"./dl/raw.mp3\""
        ext = ".mp3"
    with open('data.json', 'r', encoding="utf8") as file:
        data = file.read().rstrip()
        data = json.loads(data)
        tag_num = 1
        for entry in data:
            title = entry["tagName"]
            start = int(entry["tagStartSeconds"])
            end = int(entry["tagEndSeconds"])
            
            start_hms = time.strftime("%H:%M:%S", time.gmtime(start))
            end_hms = time.strftime("%H:%M:%S", time.gmtime(end))
            print(f"ffmpeg -i {target_filename} -ss {start_hms} -to {end_hms} -c copy \"./output/{tag_num} - {title}{ext}\"")
            os.system(f"ffmpeg -i {target_filename} -ss {start_hms} -to {end_hms} -c copy \"./output/{tag_num} - {title}{ext}\"")
            # process_id = os.spawnv(os.P_NOWAIT, "ffmpeg", ["-i", target_filename, "-ss", start_hms, "-to", end_hms, "-c", "copy", f"\"./output/{tag_num} - {title}.{ext}\""])
            tag_num += 1
    return
def main():
    yt_url = sys.argv[1]
    audio_only = True
    if len(sys.argv) > 2 and sys.argv[2] == "-v":
        audio_only = False
    download(yt_url,audio_only)
    scatter(audio_only)
    
    return

if __name__ == "__main__":
    main()