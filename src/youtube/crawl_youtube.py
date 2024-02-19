# Url extraction tested but download test was not tested
import scrapetube
import requests
import subprocess
import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("--channel_username", type=str, help="Username of that channel")
parser.add_argument("--crawl_type", type=str, help="all or videos or shorts")
parser.add_argument("--link_file", type=str, help="Link to the channel csv")

args = parser.parse_args()

def download_video(url):
    subprocess.call(["yt-dlp", "-f", "bestvideo[height<=1080][ext=mp4]", url])

channel_username = args.channel_username # Put the name of the channel hear
option = args.crawl_type
link_file = args.link_file


if option == "all" or option == "videos":
    video_urls = scrapetube.get_channel(channel_username=channel_username)
    video_urls = ["https://youtube.com/" + "watch?v=" + video_url["videoId"] for video_url in video_urls]
    for video_url in video_urls:
        download_video(video_url)


if option == "all" or option == "shorts":
    df = pd.read_csv(link_file)
    channel_usernames = [channel_url.split("/")[-2][1:] for channel_url in df.Link.values][:3]
    short_urls = []
    for channel_username in channel_usernames:
        short_urls += scrapetube.get_channel(channel_username=channel_username, content_type="shorts")
    short_urls = ["https://youtube.com/" + "shorts/" + short_url["videoId"] for short_url in short_urls]
    # print(short_urls)
    for short_url in short_urls:
        download_video(short_url)
    
