# -*- coding: utf-8 -*-
"""Stage the new HYDRA-based WCE loader release into the repo."""
import os, shutil, hashlib
ROOT = r'C:\Users\Administrator\Desktop\WCZ'
REPO = os.path.join(ROOT, 'github_release')
NEWZIP = os.path.join(ROOT, 'WCE_Loader_release.zip')
DSTZIP = os.path.join(REPO, 'WCE_Loader_release.zip')

shutil.copy2(NEWZIP, DSTZIP)

readme = os.path.join(REPO, 'README.md')
txt = open(readme, encoding='utf-8').read()

banner = """
---

## 🆕 v2.0 — HYDRA 图形化一键注入器（最新版）

新版把注入器做成了 HYDRA 风格的图形菜单，开箱即用：

- **单文件 exe**：`WCE_Loader_release.zip` 内只有一个 `WCE_Loader.exe`，补丁 DLL 已内嵌，无第三方 DLL 依赖。
- **游戏卡片**：菜单里只保留《我带过的最差一届》(Worst Class Ever) 一个游戏，配官方中文介绍与图片。
- **一键注入**：点选卡片 → 点 Load → 自动完成远程注入，弹出「核心已加载并接受初始化」提示。

使用：Steam 启动游戏进主菜单 → 管理员运行 `WCE_Loader.exe` → 点选 `Worst Class Ever` 卡片 → 点 `Load` → 回游戏按 **F2 / Insert** 打开菜单。

> 旧版 `WCE_Injector.exe`（命令行版）仍在 v1.0 Release 中，可按需下载。

"""

# insert banner right after the SEO comment block, before "## 关于"
marker = '## 关于'
if 'v2.0 — HYDRA' not in txt:
    txt = txt.replace(marker, banner + marker, 1)
    open(readme, 'w', encoding='utf-8').write(txt)

h = hashlib.sha256(open(DSTZIP, 'rb').read()).hexdigest()
print('COPIED=' + DSTZIP)
print('SIZE=' + str(os.path.getsize(DSTZIP)))
print('SHA256=' + h)
print('README_UPDATED=' + str('v2.0 — HYDRA' in txt))
