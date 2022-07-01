'''
cron: 5 0 * * *
new Env('安静的锦鲤');
Version=20220617
by Mad Rabbit
log windfgg

入口: 京东首页>领券>锦鲤红包
变量: JD_COOKIE,kois,WindfggJinliToken,Proxy_Url
export Proxy_Url='代理网址 推荐星空 生成选择txt 一次一个'
export WindfggJinliToken="windfgg 锦鲤 token" 
export JD_COOKIE="第1个cookie&第2个cookie"
export kois=" 第1个cookie的pin & 第2个cookie的pin "
环境变量kois中填入需要助力的pt_pin，有多个请用 '@'或'&'或空格 符号连接,不填默认全部账号内部随机助力
脚本内或环境变量填写，优先环境变量
'''
import os
import re
import json
import time
import logging 
import requests
import os.path

if "LOG_DEBUG" in os.environ:  # 判断调试模式变量
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')  # 设置日志为 Debug等级输出
    logger = logging.getLogger(__name__)  # 主模块
    logger.debug("\nDEBUG模式开启!\n")  # 消息输出
else:  # 判断分支
    logging.basicConfig(level=logging.INFO, format='%(message)s')  # Info级日志
    logger = logging.getLogger(__name__)  # 主模块

requests.packages.urllib3.disable_warnings()

sceneid = 'JLHBhPageh5'
startLog=0
endLog=0
#获取log
def get_log(functionId,pin):
    windfgg_token= os.environ.get("WindfggJinliToken", '')
    JinLinHost= os.environ.get("JinLinHost", 'api1.windfgg.cf')
    windfgg_url = f"http://{JinLinHost}/jd/jinli?pin={pin}&token={windfgg_token}"
    for i in range(5):
        try:
            res = requests.post(windfgg_url,timeout=20,verify=False)
            res = res.json()
            if not res["data"]["log"]:
                logger.info("获取log失败： ", res["msg"])
                continue
            resp = res['data']
            times=res['msg']
            logger.info(f'log剩余次数:{times}次')
            return resp["log"], resp["random"], resp["ck"], res['msg']
        except Exception as e:
            logger.info(f"获取log出错 等待十秒 {res}")
            time.sleep(10)
            count=i+1;
            logger.info(f"第{count}次重试")
    else:
        logger.info("5次重试失败，退出程序")
        exit()

#获取代理
def get_proxy(url):
    payload={}
    headers = {}
    for n in range(3):
        try:
            response = requests.request("GET", url, headers=headers, data=payload,verify=False)
            sss=response.text
            proxies = {
                "http": f"http://{sss}",
                'https': f'http://{sss}'
            }
            res = requests.get('https://www.baidu.com', proxies=proxies, timeout=10,verify=False)
            if res.status_code == 200:
                return proxies,sss
        except Exception as e:
            logger.info(f"代理超时或错误 重新获取")
            logger.info(f"第{n}次重试")

#请求
def taskPostUrl(functionId, body, cookie):
    global startLog
    global endLog
    pt_pin=get_pin(cookie)
    pt_key=get_key(cookie)
    proxy_url=os.environ.get("Proxy_Url", '')
    proxies,sss=get_proxy(proxy_url)
    log, randoms, ck, msg = get_log(functionId,pt_pin)
    body.update({"log": log, "random": randoms})
    logger.info(f'[{pt_pin}] {functionId} 使用代理:'+sss)
    if startLog==0:
        startLog=msg
    logger.info("Log剩余次数:"+str(msg))
    endLog = msg
    cookie=f'pt_pin={pt_pin};pt_key={pt_key};'
    url = f'https://api.m.jd.com/api?appid=jinlihongbao&functionId={functionId}&loginType=2&client=jinlihongbao&t={gettimestamp()}&clientVersion=10.1.4&osVersion=-1'
    headers = {
        'Cookie': cookie,
        'Host': 'api.m.jd.com',
        'Connection': 'keep-alive',
        'origin': 'https://happy.m.jd.com',
        'referer': 'https://happy.m.jd.com/babelDiy/zjyw/3ugedFa7yA6NhxLN5gw2L3PF9sQC/index.html?channel=9&un_area=4_134_19915_0',
        'Content-Type': 'application/x-www-form-urlencoded',
        "User-Agent": 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1654650382027%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22EG%3D%3D%22%2C%22ad%22%3A%22CzDuCQGzZNOnEJc5DNS4Dq%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctq%3D%22%2C%22ud%22%3A%22CzDuCQGzZNOnEJc5DNS4Dq%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 9; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046010 Mobile Safari/537.36',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    data = f"body={json.dumps(body)}"
    for n in range(3):
        try:
            res = requests.post(url, headers=headers, proxies=proxies,data=data,verify=False).text
            return res
        except Exception as e:
            if n == 2:
                logger.info('API请求失败，请检查网路重试❗\n')
                
# 13位时间戳
def gettimestamp():
    return str(int(time.time() * 1000))

# 获取pin key
cookie_findall = re.compile(r'pt_pin=(.+?);')
cookie_findall_key = re.compile(r'pt_key=(.+?);')
def get_pin(cookie):
    try:
        return cookie_findall.findall(cookie)[0]
    except:
        logger.info('ck格式不正确，请检查')  
def get_key(cookie):
    try:
        return cookie_findall_key.findall(cookie)[0]
    except:
        logger.info('ck格式不正确，请检查')

# 开启助力
code_findall = re.compile(r'"code":(.*?),')
def h5launch(cookie):
    body = {"followShop": 1, "sceneid": sceneid}
    res = taskPostUrl("h5launch",body, cookie)
    if not res:
        return
    Code = code_findall.findall(res)
    if Code:
        if str(Code[0]) == '0':
            logger.info(f"账号 {get_pin(cookie)} 开启助力码成功\n")
        else:
            logger.info(f"账号 {get_pin(cookie)} 开启助力码失败")
            logger.info(res)
    else:
        logger.info(f"账号 {get_pin(cookie)} 开启助力码失败")
        exit()
        
# 获取助力码
id_findall = re.compile(r'","id":(.+?),"')
def h5activityIndex(cookie):
    h5launch(cookie)
    global inviteCode_list
    body = {"isjdapp": 1}
    res = taskPostUrl("h5activityIndex",body, cookie)
    if not res:
        return
    inviteCode = id_findall.findall(res)
    if inviteCode:
        inviteCode = inviteCode[0]
        # inviteCode_list.append(inviteCode)
        logger.info(f"账号 {get_pin(cookie)} 的锦鲤红包助力码为 {inviteCode}\n")
        return inviteCode
    else:
        logger.info(f"账号 {get_pin(cookie)} 获取助力码失败\n")
        exit()

# 助力
statusDesc_findall = re.compile(r',"statusDesc":"(.+?)"')
def jinli_h5assist(cookie, redPacketId):
    body = {"redPacketId": redPacketId, "followShop": 0, "sceneid": sceneid}
    res = taskPostUrl('jinli_h5assist',body, cookie)
    logger.info(f'账号 {get_pin(cookie)} 去助力{redPacketId}')
    if not res:
        return
    statusDesc = statusDesc_findall.findall(res)
    if statusDesc:
        statusDesc = statusDesc[0]
        logger.info(f"{statusDesc}\n")
        if "TA的助力已满" in statusDesc:
            return True
    else:
        logger.info(f"错误\n{res}\n")

# 开红包
biz_msg_findall = re.compile(r'"biz_msg":"(.*?)"')
discount_findall = re.compile(r'"discount":"(.*?)"')
def h5receiveRedpacketAll(cookie):
    body = {"sceneid": sceneid}
    res = taskPostUrl("h5receiveRedpacketAll", body, cookie)
    logger.info(f'账号 {get_pin(cookie)} 开红包')
    if not res:
        return
    try:
        biz_msg = biz_msg_findall.findall(res)[0]
    except:
        logger.info(res)
        return
    discount = discount_findall.findall(res)
    if discount:
        discount = discount[0]
        logger.info(f"恭喜您，获得红包 {discount}\n")
        return h5receiveRedpacketAll(cookie)
    else:
        logger.info(f"{biz_msg}\n")

# 读取环境变量
def get_env(env):
    try:
        if env in os.environ:
            a = os.environ[env]
        else:
            a = ""
    except:
        a = ''
    return a

def main():
    logger.info('🔔安静的锦鲤，开始！\n')
    windfgg_token= os.environ.get("WindfggJinliToken", '')
    if not windfgg_token:
        logger.info("未配置WindfggJinliToken")
        exit()
    proxy_url=os.environ.get("Proxy_Url", '')
    if not proxy_url:
        logger.info("未配置Proxy_Url")
        exit()
    logger.info(f'WindfggJinliToken: {windfgg_token}')
    logger.info(f'Proxy_Url: \n{proxy_url}')
    try:
        cookie_list = os.environ["JD_COOKIE"].split("&")
    except:
        with open('cklist.txt', 'r') as f:
            cookie_list = f.read().split('\n')
    logger.info(f"共:{len(cookie_list)}个CK")
    if not cookie_list:
        logger.info("没有找到ck")
        exit()
    logger.info(f'====================共{len(cookie_list)}京东个账号Cookie=========\n')

    debug_pin = get_env('kois')
    if debug_pin:
        cookie_list_pin = [cookie for cookie in cookie_list if get_pin(cookie) in debug_pin]
    else:
        cookie_list_pin = cookie_list
    logger.info('*******************助力*******************\n')
    index = 0

    inviteCode = h5activityIndex(cookie_list_pin[index])
    for cookie in cookie_list:
        if cookie.find('app_open')<=0:
            logger.info('*******************当前ck不是appck 跳过助力*******************\n')
            continue
        status = jinli_h5assist(cookie, inviteCode)
        if status:
            logger.info('*************助力满了 开红包*************\n')
            #logger.info('*******************开红包*******************\n')
            h5receiveRedpacketAll(cookie_list_pin[index])
            time.sleep(3)
            index += 1
            if index >= len(cookie_list_pin):
                break
            for i in range(len(cookie_list_pin[index:])):
                index += i
                inviteCode = h5activityIndex(cookie_list_pin[index])
                if inviteCode:
                    break
    else:
        logger.info('*******************开红包*******************\n')
        h5receiveRedpacketAll(cookie_list_pin[index])
        time.sleep(3)
        logger.info('没有需要助力的锦鲤红包助力码\n')

    logCount = (startLog+1)-endLog
    logger.info(f'运行前[{startLog}]次 运行后[{endLog}]次 本次使用[{logCount}]次')

if __name__ == '__main__':
    main()
