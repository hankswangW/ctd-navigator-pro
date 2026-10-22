# 免费在线版部署

部署包使用 cloud_app.py 作为入口，公开站点不提供 FDA 文件上传/替换。包含完整知识库及 FDA 2026-10 快照。访客清单仅存于独立访问会话，请导出保存；服务休眠、断连或刷新可能丢失。浏览器访问服务会向托管服务器发送查询和编辑内容，本版本没有持久化用户清单，也不提供登录权限管理。

## GitHub 上传

1. 登录 GitHub，新建仓库，例如 ctd-navigator-pro。
2. 解压交付的 ctd-navigator-cloud.zip，将解压目录内的文件及 data、.streamlit、tests 文件夹上传到仓库根目录；不要把 ZIP 本身上传作为程序。
3. 确认仓库根目录能看到 cloud_app.py、app.py、requirements.txt，data 文件夹包含 fda_iid.json。
4. 本部署包没有本地虚拟环境、日志、密钥或公司文件。

## Streamlit Community Cloud

1. 打开 https://share.streamlit.io/ ，使用 GitHub 账号登录并连接目标仓库。
2. 点击 Create app，选择已有应用，从 GitHub 部署。
3. Repository 选择你的仓库；Branch 选 main；Main file path 填 cloud_app.py。
4. Advanced settings 中选择 Python 3.11。本依赖清单按此版本准备，不要直接使用平台默认 Python 版本。
5. 无需填写 Secrets，也不需要购买域名。点击 Deploy。
6. 部署成功后得到 https://你的名称.streamlit.app ，在公司电脑打开测试。

## 部署后核对

- 搜索 SEC、PS80、CAPA 和工艺放大；切换 DS/DP、IND/BLA。
- FDA 辅料库显示 9,076 条记录、1,795 个名称；PS80 匹配 78 条。
- 在线版不应显示 FDA 文件上传控件。
- 下载术语 CSV、筛选 FDA 数据并导出、创建并导出项目清单。
- 两个独立浏览器会话不应互相显示项目选择和责任人。

## 后续更新

在本地使用 app.py 更新 FDA 数据并验证，再把更新的数据与代码提交到 GitHub。云服务文件系统不是持久化数据库，不在公共站点现场替换共享快照。

官方部署说明：https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

本地已验证程序行为及部署包完整性；实际云构建与公司网络可达性需要在创建站点后验证。无需提供 GitHub 密码或访问令牌。
