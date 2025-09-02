# iptvFilter

一个用于过滤IPTV频道的工具，可以根据播放速度筛选出高质量的直播频道。

## 功能特点

- 自动抓取并解析m3u播放列表
- 测试每个频道的播放速度
- 过滤掉播放速度低于500KB/s的频道
- 按语言对频道进行分组
- 生成优化后的播放列表文件

## 工作原理

1. 从指定URL获取m3u播放列表
2. 解析列表中的每个频道URL
3. 测试每个频道的实际播放速度
4. 保留播放速度大于500KB/s的频道
5. 根据频道的语言信息重新分组
6. 生成新的优化播放列表

## 安装依赖
```
pip install uv
uv sync
```

## 播放连接

### 科学上网
**https://raw.githubusercontent.com/DGxg9420/iptvFilter/refs/heads/master/group_channels.m3u8**

### 镜像代理
**https://ghfast.top/https://raw.githubusercontent.com/DGxg9420/iptvFilter/refs/heads/master/group_channels.m3u8**



