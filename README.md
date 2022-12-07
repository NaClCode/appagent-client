# Appagent-Client

#### 介绍
Appagent的客户端

## 背景

运维绝大多数工作都是重复的Web应用部署和管理。
这些工作主要是拉取仓库、编写部署脚本、添加Nginx配置、添加域名解析，
部署脚本更是要与后端对接了解特定应用技术栈下的部署方法（如Java与C#之别）。
Token的前运维++h便提出使用Docker统一部署工作：后端在仓库中附带Dockerfile，
而运维只需要关心如何将Docker应用运行起来，不需要关心应用许多细节。
如此以来，部署工作便变得机械且重复，易于自动化。
## 功能
调用Appagent的REST API的客户端
## 下一步更新
- 支持dockerapp modify
- 支持Appagent-Server（1.0.1.0的所有REST API）