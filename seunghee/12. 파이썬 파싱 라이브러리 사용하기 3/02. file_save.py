import urllib.request
url = "https://t1.daumcdn.net/cfile/tisory/213B5437527F8C6311"
mem = urllib.request.urlopen(url).read()
save_img = "python.png"

with open(save_img, mode="wb") as f :
    f.write(mem)
    print("해당 파일이 저장되었습니다.")