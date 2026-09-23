import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
from Crypto.Util.Padding import pad
import json


def enc_params(data, key):
    data_json = json.dumps(data)
    iv = "0102030405060708"
    padded_data = pad(data_json.encode("utf-8"), AES.block_size)
    aes = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    bs = aes.encrypt(padded_data)
    return str(b64encode(bs), "utf-8")


def get_params(data):
    fir = enc_params(data, g)
    sec = enc_params(fir, i)
    return sec


def get_encSecKey():
    return "67009abc519f0fe08a8446ade82e188d04988b44b24b671d8328ad2f039099f174891227ba135ba1ad4112db3e3ad6dfc727ac5e972ddc311afad6e73bc71245cb90c0a6fcb1a8b82012eb4fb91ab23437a41be5d0688edf613b9640703e771b665696a9d5a21ef9dd91b4214e208e8275c4d34a239e3629a28883cfc358c38f"


e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "RoBOhrvMfmHO1rPW"
data = {"csrf_token": "fae0aabc3a4a2329f643f7d2e5d95749"
    , "cursor": "-1"
    , "offset": "0"
    , "orderType": "1"
    , "pageNo": "1"
    , "pageSize": "20"
    , "rid": "A_PL_0_2954650550"
    , "threadId": "A_PL_0_2954650550"}

url = "https://music.163.com/weapi/comment/resource/comments/get"
res = requests.post(url, data={"params": get_params(data), "encSecKey": get_encSecKey()})
result = res.json()
with open("comments.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print("已保存 comments.json")

# !function() {
#     function a(a) {
#         var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#         for (d = 0; a > d; d += 1)
#             e = Math.random() * b.length,
#             e = Math.floor(e),
#             c += b.charAt(e);
#         return c
#     }
#     function b(a, b) {
#         var c = CryptoJS.enc.Utf8.parse(b)
#           , d = CryptoJS.enc.Utf8.parse("0102030405060708")
#           , e = CryptoJS.enc.Utf8.parse(a)
#           , f = CryptoJS.AES.encrypt(e, c, {
#             iv: d,
#             mode: CryptoJS.mode.CBC
#         });
#         return f.toString()
#     }
#     function c(a, b, c) {
#         var d, e;
#         return setMaxDigits(131),
#         d = new RSAKeyPair(b,"",c),
#         e = encryptedString(d, a)
#     }
#     function d(d, e, f, g) {  d;就是参数data e:010001 f:根据上f g:0CoJUm6Qyw8W8jud
#         var h = {}
#           , i = a(16);
#         return h.encText = b(d, g),
#         h.encText = b(h.encText, i),     #就是params
#         h.encSecKey = c(i, e, f),
#         h
#     }
#     function e(a, b, d, e) {
#         var f = {};
#         return f.encText = c(a + e, b, d),
#         f
#     }
#     window.asrsea = d,
#     window.ecnonasr = e   #网易云评论爬取
