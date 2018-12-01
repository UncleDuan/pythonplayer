# Voice

主要用到了TKinter模块和baidu-aip
## 学习到：
* 1、利用Tkinter创建基本的界面
* 2、利用百度ai生成接口，主要是三个参数：
```python
        APP_ID='14624722'
        API_KEY='ZIjGS2NA7ksxQsH29rfA538i'
        SECRET_KEY='716BPFUDDsOjHUOKYghRxcLavveyag14'
```
这个可以自己生成。然后调用接口:
```python
client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
这个AipSpeech就在aip.AipSpeech模块中。
```
* 3、playsound
只包含一个playsound函数 \
只需要一个参数：the path to the file with the sound you’d like to play. This may be a local file, or a URL.\
有一个可选参数block,默认为True， Setting it to False makes the function run asynchronously.

## 注意：
需要联网。
Tkinter是内置的，_tkinter是tkinter的扩充
## 遇到的错误：
file文件的名字加上后缀名.mp3，否则会出现UnicodeDecodeError
### 感谢奔跑的鳄鱼及菜鸟学Python