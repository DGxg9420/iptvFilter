# coding:utf-8

import os
import re
import queue
from concurrent.futures import ThreadPoolExecutor

def reWrite(file_path, lines_content_queue):
    with open(file_path, "w", encoding="utf-8") as f:
        while True:
            line = lines_content_queue.get()
            if line == "StopHere":
                break
            f.write(line)

def replace_group_title(line_content, lines_content_queue):
    result = re.search(r'(group-title=".*?")', line_content)
    group_title = result.group(1) if result else ""
    result = re.search(r'tvg-language="(.*?)"', line_content)
    tvg_language = result.group(1) if result else ""
    if group_title and tvg_language:
        line_content = line_content.replace(group_title, f"group-title=\"{tvg_language}\"")
    lines_content_queue.put(line_content)

def group_m3u8_file(m3u8_file_path):
    lines_content_queue = queue.Queue()
    if not os.path.exists(m3u8_file_path):
        return None
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(reWrite, "group_channels.m3u8", lines_content_queue)
        with open(m3u8_file_path, "r", encoding="utf-8") as f:
            whole_channel_info = ""
            while True:
                line = f.readline()
                if not line:
                    break
                elif line.startswith("#EXTINF"):
                    whole_channel_info += line
                    whole_channel_info += f.readline()
                    executor.submit(replace_group_title, whole_channel_info, lines_content_queue)
                    whole_channel_info = ""
                else:
                    lines_content_queue.put(line)
            lines_content_queue.put("StopHere")


if __name__ == "__main__":
    group_m3u8_file("test_channels_all_new.m3u8")

