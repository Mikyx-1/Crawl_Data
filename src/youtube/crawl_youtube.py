# Url extraction tested but download test was not tested
import scrapetube
import requests
import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--channel_username", type=str, help="Username of that channel")
parser.add_argument("--crawl_type", type=bool, help="all or videos or shorts")

args = parser.parse_args()

def download_video(url):
    subprocess.call(["yt-dlp", "-f", "bestvideo[height<=1080][ext=mp4]", url])

channel_username = args.channel_username # Put the name of the channel hear
option = args.crawl_type


if option == "all" or option == "videos":
    video_urls = scrapetube.get_channel(channel_username=channel_username)
    video_urls = ["https://youtube.com/" + "watch?v=" + video_url["videoId"] for video_url in video_urls]
    for video_url in video_urls:
        download_video(video_url)

if option == "all" or option == "shorts":
    short_urls = scrapetube.get_channel(channel_username=channel_username, content_type="shorts")
    short_urls = ["https://youtube.com/" + "shorts/" + short_url["videoId"] for short_url in short_urls]
    for short_url in short_urls:
        download_video(short_url)



