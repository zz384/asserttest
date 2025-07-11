# asserttest
、、项目简介、、
本项目为 TechBlog Hub 技术博客平台 的接口自动化测试项目，基于 Python 的 unittest + requests + parameterized 实现。
主要针对博客系统的登录接口进行了正向、反向、边界、异常等多场景的自动化测试，测试数据与代码分离，断言方法封装，提升了测试效率和代码可维护性。
、、目录结构、、
asserttest/
├── daima/                # 主要测试代码（如断言、请求方法等）
│   ├── duan.py
│   ├── qianzhi.py
│   └── read_jj.py
├── data/                 # 测试数据
│   └── data_wa.json
├── Testboke.py           # 主测试用例入口
├── README.md             # 项目说明文档
、、技术栈、、
Python 3.x
unittest
requests
parameterized
、、功能亮点、、
参数化测试：使用 parameterized 实现多组数据驱动，提升用例复用性
断言封装：统一断言方法，便于维护和扩展
数据分离：测试数据与代码分离，便于批量维护
自动化执行：一键运行所有用例，自动判断结果
