# 项目名称
netease-comment-crawler

## 项目简介
网易云音乐评论批量爬取

## 技术栈
- Python
- Requests
- 逆向工程
- JavaScript

## 功能说明
- 逆向分析网易云音乐评论接口 `weapi/comment/resource/comments/get`，定位加密参数 `params` 与 `encSecKey` 的生成逻辑
- 还原 JS 加密函数 `window.asrsea`，理解其 AES 加密（CBC 模式）与 RSA 加密的组合流程
- 使用 Python 复现加密逻辑，构造合法请求参数，绕过接口校验
- 实现评论数据的批量抓取，支持指定歌曲 ID 获取评论内容
- 对抓取结果进行本地存储，便于后续数据分析

## 运行方式
1. 安装依赖：`pip install requests`
2. 修改代码中的歌曲 ID 为目标歌曲
3. 运行：`python netease_comment.py`
