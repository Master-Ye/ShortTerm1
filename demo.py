import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'Referer': 'https://y.qq.com/'
}
data='{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.musicsearch.HotkeyService","method":"GetHotkeyForQQMusicMobile","param":{"searchid":"20766209889116389","remoteplace":"txt.yqq.top","from":"yqqweb"}},"req_2":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"718477","biz_sub_type":0}]}},"req_3":{"module":"music.globalComment.CommentRead","method":"GetNewCommentList","param":{"BizType":1,"BizId":"718477","LastCommentSeqNo":"","PageSize":25,"PageNum":0,"FromCommentId":"","WithHot":1,"PicEnable":1,"LastTotal":0,"LastTotalVer":"0"}},"req_4":{"module":"music.globalComment.CommentRead","method":"GetHotCommentList","param":{"BizType":1,"BizId":"718477","LastCommentSeqNo":"","PageSize":15,"PageNum":0,"HotType":2,"WithAirborne":1,"PicEnable":1}},"req_5":{"module":"music.globalComment.CommentAsset","method":"GetCmBgCard","param":{}},"req_6":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001zMQr71F1Qo8"}}}'
params = {
    '_': "1688204083450",
    'sign': "zzb4ce6fec89nqyx53iwj5nirq8kcmhg5b7f038c",

}
res = requests.post(
    url='https://u.y.qq.com/cgi-bin/musics.fcg',
    params=params,
    headers=headers,
data=data
)

json_data = res.json()

Comments=json_data['req_3']['data']['CommentList']['Comments']
content = [i.get('Content') for i in Comments]
print(len(content))
print(content)

