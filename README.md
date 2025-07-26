# StockDataDownloader

该项目旨在提供一个通用的股票数据下载工具。目前仅实现了中国 A 股数据的下载功能，后续可以扩展到全球其他市场。

## 功能简介

- 使用 [pytdx](https://github.com/rainx/pytdx) 读取通达信软件中的数据文件
- 支持日 K 线和 1 分钟线数据
- 将读取到的数据导出为 CSV 文件

## 使用方法

安装依赖：

```bash
pip install -r requirements.txt
```

导出通达信数据：

```bash
python china/export_tdx.py --tdxdir <通达信目录> --outdir <输出目录>
```

其中 `<通达信目录>` 为本地安装的通达信软件数据目录，例如 `~/tdx`。

## 目录结构

```
.
├── china                # 与中国 A 股相关的脚本
│   └── export_tdx.py    # 从通达信导出数据到 CSV
├── requirements.txt     # 项目依赖
└── LICENSE
```
