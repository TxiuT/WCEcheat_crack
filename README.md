# WCE Injector — 我带过的最差一届（Worst Class Ever）核心注入器

> 本项目是游戏《我带过的最差一届》（英文名 **Worst Class Ever**，简称 **WCE**）的自包含核心注入器。
> 补丁 DLL 已内嵌在 exe 中，解压即用。

<!--
SEO 关键词（便于被搜索到）：
我带过的最差一届、最差一届、最差的一届、我带过最差的一届、Worst Class Ever、WCE、
WCEcheat、WCE crack、WCE 注入器、WCE 核心、游戏核心注入、DLL 注入、卡密绕过、
Steam 登录修复、作弊菜单、内挂、开箱即用、最差一届辅助、worst class ever cheat
-->


---

## 🆕 v2.0 — HYDRA 图形化一键注入器（最新版）

新版把注入器做成了 HYDRA 风格的图形菜单，开箱即用：

- **单文件 exe**：`WCE_Loader_release.zip` 内只有一个 `WCE_Loader.exe`，补丁 DLL 已内嵌，无第三方 DLL 依赖。
- **游戏卡片**：菜单里只保留《我带过的最差一届》(Worst Class Ever) 一个游戏，配官方中文介绍与图片。
- **一键注入**：点选卡片 → 点 Load → 自动完成远程注入，弹出「核心已加载并接受初始化」提示。

使用：Steam 启动游戏进主菜单 → 管理员运行 `WCE_Loader.exe` → 点选 `Worst Class Ever` 卡片 → 点 `Load` → 回游戏按 **F2 / Insert** 打开菜单。

> 旧版 `WCE_Injector.exe`（命令行版）仍在 v1.0 Release 中，可按需下载。

## 关于

《我带过的最差一届》（Worst Class Ever，WCE）是一款热门联机游戏。本仓库提供该游戏的核心加载器，
解决卡密验证与 Steam 登录状态问题，并对菜单做了个性化处理。如果你在找
"我带过的最差一届" 的辅助、WCE 核心、Worst Class Ever cheat 或 WCE crack，来这里就对了。

## 功能

- 卡密验证绕过，无需卡密即可使用
- 修复 Steam 登录状态报错，可正常进入房间游玩
- 菜单内置 QQ 群入口（点击跳转加群）
- 公告栏与展示图已个性化

## 使用方法

1. 先启动游戏《我带过的最差一届》（Worst Class Ever），进入主菜单
2. 双击运行 `WCE_Injector.exe`
3. 出现 `核心已加载并接受初始化` 即注入成功
4. 回到游戏，按 **F2**（或 **Insert**）打开菜单

> 游戏若以管理员身份运行，请右键 exe → 以管理员身份运行。
> 需要 Windows 64 位。每次重开游戏后需重新运行一次注入器。

## 菜单按键

| 按键 | 功能 |
| --- | --- |
| F2 / Insert | 打开 / 关闭菜单 |
| F7 ~ F13 | 切换页面 |

## 备用方案

若注入器无法使用，可手动把 `DLL/WorstClassEver.dll` 复制到游戏安装目录（`Worst Class Ever.exe` 所在文件夹），再启动游戏。

## 文件说明

- `WCE_Injector.exe` — 主程序，补丁已内嵌，双击即用
- `DLL/WorstClassEver.dll` — 备用核心 DLL

## 关键词 / Tags

我带过的最差一届 · 最差一届 · Worst Class Ever · WCE · WCEcheat · WCE crack ·
游戏辅助 · 核心注入 · DLL injection · cheat menu
