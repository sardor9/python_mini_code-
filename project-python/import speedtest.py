#pip install speedtest-cli
import speedtest
test = speedtest.Speedtest()
down = test.download()
upload = test.upload()
print(f"Download speed: {down}")
print(f"Download speed:{upload}")