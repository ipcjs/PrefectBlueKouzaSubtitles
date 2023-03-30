#!/usr/bin/env python3
# 因为原始文件有问题, 拆分效果并不好
# Power by ChatGPT
import os
import re

# Delete previous output files
for filename in os.listdir():
    if filename.endswith('_chinese.vtt') or filename.endswith('_japanese.vtt'):
        os.remove(filename)

# Process all input files
for filename in os.listdir():
    if filename.endswith('_zh_bilingual.vtt'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split the content into two parts: Chinese and Japanese
        chinese_subs = re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3}\n)(.*?)(?=\n\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3}|\n$)', content, flags=re.DOTALL)
        japanese_subs = re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3}\n)(.*?)(?=\n\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3}|\n$)', content, flags=re.DOTALL)

        # Write the Chinese subtitles to a file
        chinese_filename = re.sub(r'(_zh_bilingual.vtt)$', r'_chinese.vtt', filename)
        with open(chinese_filename, 'w', encoding='utf-8') as f:
            f.write('WEBVTT\n\n')
            for sub in chinese_subs:
                # f.write(sub[0] + sub[1].split('\n', 1)[0] + '\n\n')
                f.write(sub[0] + sub[1].split('\n')[1] + '\n\n')


        # Write the Japanese subtitles to a file
        japanese_filename = re.sub(r'(_zh_bilingual.vtt)$', r'_japanese.vtt', filename)
        with open(japanese_filename, 'w', encoding='utf-8') as f:
            f.write('WEBVTT\n\n')
            for sub in japanese_subs:
                # f.write(sub[0] + sub[1].split('\n', 1)[1] + '\n\n')
                f.write(sub[0] + sub[1].split('\n')[2] + '\n\n')


