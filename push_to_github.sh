#!/bin/bash
#
# 一键推送到GitHub脚本
# 使用前请先在GitHub上创建仓库
#

echo ""
echo "=========================================="
echo "🚀 推送到GitHub"
echo "=========================================="
echo ""

# 检查远程仓库
if ! git remote | grep -q origin; then
    echo "❌ 错误：未配置远程仓库"
    echo "远程仓库已配置为: https://github.com/helloforrestwu/study-abroad-ai-agent.git"
    exit 1
fi

echo "远程仓库: "
git remote -v
echo ""

# 推送
echo "正在推送到GitHub..."
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✅ 成功推送到GitHub！"
    echo "=========================================="
    echo ""
    echo "🌐 仓库地址: https://github.com/helloforrestwu/study-abroad-ai-agent"
    echo ""
    echo "📝 下一步："
    echo "   1. 访问您的仓库查看代码"
    echo "   2. 添加仓库描述和topics"
    echo "   3. 配置GitHub Pages（可选）"
    echo "   4. 邀请协作者（可选）"
    echo ""
else
    echo ""
    echo "=========================================="
    echo "❌ 推送失败"
    echo "=========================================="
    echo ""
    echo "可能的原因："
    echo "1. 仓库尚未在GitHub上创建"
    echo "2. 仓库名称不正确"
    echo "3. 没有推送权限"
    echo ""
    echo "解决方法："
    echo ""
    echo "步骤1: 在GitHub创建仓库"
    echo "   访问: https://github.com/new"
    echo "   仓库名: study-abroad-ai-agent"
    echo "   ⚠️ 不要勾选 README, .gitignore, license"
    echo ""
    echo "步骤2: 创建后再次运行此脚本"
    echo "   ./push_to_github.sh"
    echo ""
fi
