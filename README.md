# YunFeng_Repo
## 收集整理全网可用脚本 分类整理 去除内置助力码 对加密脚本进行标注

### JD仓库 拉库命令

国外
```shell
ql repo https://github.com/FengYun27/YunFeng_Repo "jd_|jx_|m_|js_" "expire" "ql|sendNotify|utils|USER_AGENTS|jdCookie|TS_USER_AGENTS|sign_graphics_validate"

30 0/15 * * * ? 
```

国内

```shell
ql repo https://github.91chi.fun//https://github.com/FengYun27/YunFeng_Repo.git "jd_|jx_|m_|js_" "expire" "ql|sendNotify|utils|USER_AGENTS|jdCookie|TS_USER_AGENTS|sign_graphics_validate"

30 0/15 * * * ? 
```
### 羊毛仓库 拉库命令

**羊毛仓库属于单独仓库 可以同时和JD仓库一起拉**

国内
```shell
ql repo https://github.91chi.fun//https://github.com/FengYun27/Sheep_Hair.git "" "" "ql|sendNotify"

30 0/15 * * * ? 
```
国外
```shell
ql repo https://github.91chi.fun//https://github.com/FengYun27/Sheep_Hair.git "" "" "ql|sendNotify"

30 0/15 * * * ? 
```
#### 单拉羊毛脚本
- [羊毛脚本列表](https://github.com/FengYun27/Sheep_Hair#羊毛)

国外

```shell
ql raw https://raw.githubusercontent.com/FengYun27/Sheep_Hair/main/<脚本名称>.js
```

国内

```shell
ql raw https://github.91chi.fun//https://raw.githubusercontent.com/FengYun27/Sheep_Hair/main/<脚本名称>.js
```

# 脚本列表

### 加密脚本 安全未知
- 京东极速版_金币 `jd_speed_signfaker.js` (局部加密)

### 需要添加环境变量
- 店铺签到 `jd_dpqd.js` (本地没有时获取云端店铺签到TOKEN 不定时更新)
- 京东试用 `jd_try.js` (添加 JD_TRY=true 环境变量)
- 领现金 `jd_cash_Pande.js` (需要添加环境变量gua_cleancart_PandaToken @pang_da_bot获取)

## 依赖
### NodeJs
- axios
- jsdom
- ts-md5
- moment
- png-js
- date-fns
### Python
- PyExecJS
- json5
- requests
- pycryptodomex

# Special statement
* Any unlocking and decryption analysis scripts involved in the Script project released by this warehouse are only used for testing, learning and research, and are forbidden to be used for commercial purposes. Their legality, accuracy, completeness and effectiveness cannot be guaranteed. Please make your own judgment based on the situation. .

* All resource files in this project are forbidden to be reproduced or published in any form by any official account or self-media.

* This warehouse is not responsible for any script problems, including but not limited to any loss or damage caused by any script errors.

* Any user who indirectly uses the script, including but not limited to establishing a VPS or disseminating it when certain actions violate national/regional laws or related regulations, this warehouse is not responsible for any privacy leakage or other consequences caused by this.

* Do not use any content of the Script project for commercial or illegal purposes, otherwise you will be responsible for the consequences.

* If any unit or individual believes that the script of the project may be suspected of infringing on their rights, they should promptly notify and provide proof of identity and ownership. We will delete the relevant script after receiving the certification document.

* Anyone who views this item in any way or directly or indirectly uses any script of the Script item should read this statement carefully. This warehouse reserves the right to change or supplement this disclaimer at any time. Once you have used and copied any relevant scripts or rules of the Script project, you are deemed to have accepted this disclaimer.

 **You must completely delete the above content from your computer or mobile phone within 24 hours after downloading.**  </br>
> ***You have used or copied any script made by yourself in this warehouse, it is deemed to have accepted this statement, please read it carefully*** 

## 呜谢

以下排名不分先后
- [ccwav](https://github.com/ccwav)
- [Orz-3](https://github.com/Orz-3)
- [shufflewzc](https://github.com/shufflewzc)
- [whyour](https://github.com/whyour)
- ....
