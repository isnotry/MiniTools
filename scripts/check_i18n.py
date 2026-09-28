#!/usr/bin/env python3
"""静态检查单文件页面里还有哪些中文没进 MAP（不需要浏览器）。

用法: python3 scripts/check_i18n.py <file.html> [更多文件]
输出: text / attr / js 三类里没被 MAP 精确覆盖、也没被 PAIRS 片段覆盖的中文串。
"""
import re
import sys
from html.parser import HTMLParser

CJK = re.compile(r'[\u4e00-\u9fff\uff00-\uffef]')
STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\'|`((?:[^`\\]|\\.)*)`')


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.texts = []
        self.attrs = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.depth += 1
        for k, v in attrs:
            if k in ('placeholder', 'title', 'aria-label') and v and CJK.search(v):
                self.attrs.append((k, v.strip()))

    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            return
        t = ' '.join(data.split())
        if t and CJK.search(t):
            self.texts.append(t)


def extract_map(src):
    m = re.search(r'var\s+MAP\s*=\s*\{(.*?)\n\s*\};', src, re.S)
    keys = set()
    if m:
        for k in re.finditer(r'"((?:[^"\\]|\\.)*)"\s*:', m.group(1)):
            keys.add(k.group(1))
    return keys


def extract_pairs(src):
    m = re.search(r'var\s+PAIRS\s*=\s*\[(.*?)\];', src, re.S)
    pairs = []
    if m:
        for p in re.finditer(r'\[\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\]', m.group(1)):
            pairs.append(p.group(1))
    return pairs


def check(path):
    src = open(path, encoding='utf-8').read()
    keys = extract_map(src)
    pairs = extract_pairs(src)

    p = P()
    p.feed(src)

    scripts = re.findall(r'<script[^>]*>(.*?)</script>', src, re.S)
    js_strings = []
    for s in scripts:
        for m in STR_RE.finditer(s):
            v = m.group(1) or m.group(2) or m.group(3) or ''
            v = ' '.join(v.split())
            if v and CJK.search(v):
                js_strings.append(v)

    def covered(s):
        if s in keys:
            return True
        for frag in pairs:
            if frag and frag in s:
                return True
        return False

    left = {'text': [], 'attr': [], 'js': []}
    for t in dict.fromkeys(p.texts):
        if not covered(t):
            left['text'].append(t)
    for a, v in dict.fromkeys(p.attrs):
        if not covered(v):
            left['attr'].append(f'{a}: {v}')
    for v in dict.fromkeys(js_strings):
        if not covered(v):
            left['js'].append(v)

    total = sum(len(v) for v in left.values())
    print(f'\n== {path}   (MAP {len(keys)} 条, PAIRS {len(pairs)} 条)')
    if not total:
        print('   ✓ 已覆盖')
        return 0
    for kind in ('text', 'attr', 'js'):
        if left[kind]:
            print(f'   未覆盖 {kind} {len(left[kind])} 条:')
            for s in left[kind][:80]:
                print(f'     - {s[:110]}')
            if len(left[kind]) > 80:
                print(f'     …还有 {len(left[kind]) - 80} 条')
    return 1


if __name__ == '__main__':
    bad = 0
    for f in sys.argv[1:]:
        bad |= check(f)
    sys.exit(1 if bad else 0)
