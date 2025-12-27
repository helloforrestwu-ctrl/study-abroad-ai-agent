#!/bin/bash
#
# GitHub仓库设置和推送脚本
# Study Abroad AI Agent System - GitHub Setup Script
#

echo "=========================================="
echo "GitHub 仓库设置向导"
echo "=========================================="
echo ""

# 检查是否已有远程仓库
if git remote | grep -q origin; then
    echo "✓ 检测到已配置的远程仓库："
    git remote -v
    echo ""
    read -p "是否要重新配置？(y/N): " reconfigure
    if [[ ! $reconfigure =~ ^[Yy]$ ]]; then
        echo "保持现有配置，准备推送..."
        git push -u origin main
        exit 0
    fi
    git remote remove origin
fi

echo "请选择设置方式："
echo "1. 我已经在GitHub上创建了仓库（输入仓库URL）"
echo "2. 我需要创建新仓库（提供创建步骤指引）"
echo ""
read -p "请选择 (1/2): " choice

if [ "$choice" = "1" ]; then
    echo ""
    echo "请输入您的GitHub仓库URL："
    echo "格式示例："
    echo "  HTTPS: https://github.com/username/repo-name.git"
    echo "  SSH:   git@github.com:username/repo-name.git"
    echo ""
    read -p "仓库URL: " repo_url

    if [ -z "$repo_url" ]; then
        echo "❌ 错误：仓库URL不能为空"
        exit 1
    fi

    # 添加远程仓库
    echo ""
    echo "正在添加远程仓库..."
    git remote add origin "$repo_url"

    # 推送到GitHub
    echo "正在推送到GitHub..."
    git push -u origin main

    if [ $? -eq 0 ]; then
        echo ""
        echo "=========================================="
        echo "✅ 成功推送到GitHub！"
        echo "=========================================="
        echo ""
        echo "仓库地址: $repo_url"
        echo ""
        git remote -v
    else
        echo ""
        echo "❌ 推送失败，请检查："
        echo "1. 仓库URL是否正确"
        echo "2. 是否有推送权限"
        echo "3. 如使用SSH，是否已配置SSH密钥"
        exit 1
    fi

elif [ "$choice" = "2" ]; then
    echo ""
    echo "=========================================="
    echo "📝 创建GitHub仓库步骤指引"
    echo "=========================================="
    echo ""
    echo "请按以下步骤操作："
    echo ""
    echo "1. 打开浏览器访问: https://github.com/new"
    echo ""
    echo "2. 填写仓库信息："
    echo "   Repository name*: study-abroad-ai-agent"
    echo "   Description: 留学规划AI智能体系统 - 多Agent协作的智能留学咨询系统"
    echo "   Visibility: ○ Public  ● Private (根据需要选择)"
    echo ""
    echo "3. ⚠️ 重要: 不要勾选以下选项（保持未选中状态）："
    echo "   [ ] Add a README file"
    echo "   [ ] Add .gitignore"
    echo "   [ ] Choose a license"
    echo ""
    echo "4. 点击 'Create repository' 按钮"
    echo ""
    echo "5. 创建后，GitHub会显示仓库URL，复制它（HTTPS或SSH）"
    echo "   示例: https://github.com/yourusername/study-abroad-ai-agent.git"
    echo ""
    echo "=========================================="
    echo ""
    read -p "完成上述步骤后，按回车继续..."
    echo ""
    read -p "请粘贴您的仓库URL: " repo_url

    if [ -z "$repo_url" ]; then
        echo "❌ 错误：仓库URL不能为空"
        exit 1
    fi

    # 添加远程仓库
    echo ""
    echo "正在配置远程仓库..."
    git remote add origin "$repo_url"

    # 推送到GitHub
    echo "正在推送到GitHub..."
    git push -u origin main

    if [ $? -eq 0 ]; then
        echo ""
        echo "=========================================="
        echo "🎉 成功推送到GitHub！"
        echo "=========================================="
        echo ""
        echo "您的项目已上传到: $repo_url"
        echo ""
        echo "下一步可以："
        echo "1. 在浏览器中查看您的仓库"
        echo "2. 添加README badges"
        echo "3. 设置GitHub Pages（如需要）"
        echo "4. 邀请协作者"
        echo ""
    else
        echo ""
        echo "❌ 推送失败，请检查："
        echo "1. 仓库URL是否正确"
        echo "2. 是否有推送权限"
        echo "3. 网络连接是否正常"
        echo ""
        echo "如需帮助，请查看: https://docs.github.com/cn"
        exit 1
    fi
else
    echo "❌ 无效选择"
    exit 1
fi

echo ""
echo "远程仓库配置："
git remote -v
echo ""
echo "✅ 完成！"
