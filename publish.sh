#!/bin/bash
# 一键发布到 GitHub：创建仓库 -> 推送代码和tag -> 创建 Release 并上传 zip
# 用法: GH_TOKEN=你的token REPO_NAME=wce-injector ./publish.sh

set -e

GH_TOKEN="${GH_TOKEN:?请设置 GH_TOKEN 环境变量}"
REPO_NAME="${REPO_NAME:-wce-injector}"
OWNER="${OWNER:-}"   # 留空则用 token 对应账号

echo "==> 验证 token"
USER_INFO=$(curl -s -H "Authorization: token $GH_TOKEN" https://api.github.com/user)
LOGIN=$(echo "$USER_INFO" | python3 -c "import sys,json; print(json.load(sys.stdin).get('login',''))" 2>/dev/null)
if [ -z "$LOGIN" ]; then
  echo "token 无效或无 user 权限"; echo "$USER_INFO"; exit 1
fi
echo "账号: $LOGIN"

if [ -n "$OWNER" ]; then OWNER="$OWNER"; else OWNER="$LOGIN"; fi

echo "==> 创建仓库 $OWNER/$REPO_NAME"
curl -s -X POST -H "Authorization: token $GH_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$REPO_NAME\",\"description\":\"WCE Injector - self-contained game core injector\",\"private\":false,\"auto_init\":false}" \
  > /tmp/repo_create.json
grep -q '"full_name"' /tmp/repo_create.json && echo "仓库已创建/已存在" || { cat /tmp/repo_create.json; echo "（若仓库已存在可忽略此错误）"; }

echo "==> 推送代码和 tag"
git remote remove origin 2>/dev/null || true
git remote add origin "https://$GH_TOKEN@github.com/$OWNER/$REPO_NAME.git"
git push -u origin master
git push origin v1.0
git remote set-url origin "https://github.com/$OWNER/$REPO_NAME.git"

echo "==> 创建 Release v1.0"
curl -s -X POST -H "Authorization: token $GH_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/$OWNER/$REPO_NAME/releases" \
  -d '{"tag_name":"v1.0","name":"v1.0 开箱即用版","body":"自包含注入器，解压即用。功能：卡密绕过、Steam 修复、定制菜单。","draft":false,"prerelease":false}' \
  > /tmp/release.json
RELEASE_ID=$(python3 -c "import json; print(json.load(open('/tmp/release.json')).get('id',''))" 2>/dev/null)
if [ -z "$RELEASE_ID" ]; then cat /tmp/release.json; echo "Release 创建失败（可能已存在）"; exit 1; fi

echo "==> 上传 zip 到 Release"
curl -s -X POST -H "Authorization: token $GH_TOKEN" \
  -H "Content-Type: application/zip" \
  --data-binary @WCE_Injector_release.zip \
  "https://uploads.github.com/repos/$OWNER/$REPO_NAME/releases/$RELEASE_ID/assets?name=WCE_Injector_release.zip" \
  > /tmp/asset.json
grep -q '"browser_download_url"' /tmp/asset.json && echo "zip 上传成功" || cat /tmp/asset.json

echo "==> 完成"
echo "仓库地址: https://github.com/$OWNER/$REPO_NAME"
echo "下载地址: https://github.com/$OWNER/$REPO_NAME/releases/tag/v1.0"
