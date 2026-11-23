# -*- coding: utf-8 -*-
"""
一键发布到 GitHub: 创建仓库 -> 推送代码和tag -> 创建 Release -> 上传 zip
用法: python publish.py <TOKEN> [仓库名] [owner]
依赖: 仅 Python 标准库 + 系统 git
"""
import sys, os, json, subprocess, urllib.request, urllib.error

TOKEN = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GH_TOKEN", "")
REPO = sys.argv[2] if len(sys.argv) > 2 else "wce-injector"
OWNER_ARG = sys.argv[3] if len(sys.argv) > 3 else ""

if not TOKEN:
    print("GH_TOKEN missing. usage: python publish.py <TOKEN> [repo] [owner]")
    sys.exit(1)

API = "https://api.github.com"
HDR = {
    "Authorization": "token " + TOKEN,
    "Accept": "application/vnd.github+json",
    "User-Agent": "wce-publisher",
}

def req(url, method="GET", data=None, headers=None, raw=False):
    h = dict(HDR)
    if headers:
        h.update(headers)
    body = None
    if data is not None:
        body = data if raw else json.dumps(data).encode("utf-8")
    r = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            out = resp.read()
            return resp.status, json.loads(out) if out and not raw else out
    except urllib.error.HTTPError as e:
        out = e.read().decode("utf-8", "replace")
        return e.code, out

def run(cmd):
    safe = cmd.replace(TOKEN, "***TOKEN***")
    print("  $", safe)
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if p.returncode != 0:
        print((p.stdout + p.stderr).replace(TOKEN, "***TOKEN***"))
    return p.returncode == 0, (p.stdout + p.stderr).replace(TOKEN, "***TOKEN***")

print("==> verify token")
code, info = req(API + "/user")
if code != 200:
    print("token invalid:", info); sys.exit(1)
login = info.get("login", "")
print("account:", login)
owner = OWNER_ARG or login

print("==> create repo %s/%s" % (owner, REPO))
code, r = req(API + "/user/repos", "POST", {
    "name": REPO,
    "description": "WCE Injector - self-contained game core injector",
    "private": False,
    "auto_init": False,
})
if code == 201:
    print("repo created")
elif code == 422:
    print("repo already exists, continuing")
else:
    print("create repo returned", code, r)

print("==> push code and tag")
run('git remote remove origin 2>nul || true')
ok, _ = run('git remote add origin https://%s@github.com/%s/%s.git' % (TOKEN, owner, REPO))
if not ok:
    run('git remote set-url origin https://%s@github.com/%s/%s.git' % (TOKEN, owner, REPO))
run('git push -u origin master')
run('git push origin v1.0')
run('git remote set-url origin https://github.com/%s/%s.git' % (owner, REPO))

print("==> create release v1.0")
code, rel = req(API + "/repos/%s/%s/releases" % (owner, REPO), "POST", {
    "tag_name": "v1.0",
    "name": "v1.0 开箱即用版",
    "body": "自包含注入器，解压即用。卡密绕过、Steam 修复、定制菜单。",
    "draft": False,
    "prerelease": False,
})
release_id = rel.get("id") if isinstance(rel, dict) else None
if not release_id:
    print("release create returned", code, rel)
    print("(release may already exist; check the repo page)")
else:
    print("==> upload zip")
    zpath = "WCE_Injector_release.zip"
    with open(zpath, "rb") as f:
        zdata = f.read()
    up_url = "https://uploads.github.com/repos/%s/%s/releases/%s/assets?name=%s" % (
        owner, REPO, release_id, zpath)
    code, a = req(up_url, "POST", zdata,
                  headers={"Content-Type": "application/zip"}, raw=True)
    if isinstance(a, bytes):
        try:
            a = json.loads(a)
        except Exception:
            pass
    if isinstance(a, dict) and a.get("browser_download_url"):
        print("uploaded:", a["browser_download_url"])
    else:
        print("upload returned", code, a)

print("==> DONE")
print("repo     : https://github.com/%s/%s" % (owner, REPO))
print("download : https://github.com/%s/%s/releases/tag/v1.0" % (owner, REPO))
