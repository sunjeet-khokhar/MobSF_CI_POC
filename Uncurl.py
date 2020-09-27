import requests
import uncurl

def try_uncurl():
    context = uncurl.parse_context("curl  'http://localhost:8000/api/v1/upload' -H 'Authorization:161f75d520f0ec254917dedff97ad41c460ca61da2ef39124f4e829a3aba5260' --data-binary 'file=@/Users/sunjeetkhokhar/Downloads/Code/pivaa/apks/pivaa.apk' ")
    print(context)
    

if __name__ == "__main__":
    try_uncurl()