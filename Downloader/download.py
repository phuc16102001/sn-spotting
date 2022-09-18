import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader

directory = input("Directory (d:\git\sn-spotting\Data): ")
password = input("Password (s0cc3rn3t): ")
mySoccerNetDownloader=SoccerNetDownloader(LocalDirectory=directory)
mySoccerNetDownloader.password = password

print("Download label...")
mySoccerNetDownloader.downloadGames(files=["Labels-v2.json"], split=["train","valid","test"])

print("Download HQ version...")
mySoccerNetDownloader.downloadGames(files=["1_720p.mkv", "2_720p.mkv", "video.ini"], split=["train","valid","test","challenge"])

print("Download LQ version...")
mySoccerNetDownloader.downloadGames(files=["1_224p.mkv", "2_224p.mkv"], split=["train","valid","test","challenge"])

print("Download Baidu feature...")
mySoccerNetDownloader.downloadGames(files=["1_baidu_soccer_embeddings.npy", "2_baidu_soccer_embeddings.npy"], split=["train","valid","test","challenge"])
