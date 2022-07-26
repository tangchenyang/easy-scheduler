# easy-scheduler

## Parser
解析配置文件，转换并注册到Metadata
- JsonParser 目前仅支持 JSON 格式配置

## Metadata
元数据管理中心 
- 任务元数据
- 数据元数据

## Submitter
用于提交不同的任务
- Spark
- Python
- Bash
- Hive

## Adapter
从Metadata中获取任务信息，生成调度平台能识别的调度配置文件及脚本
- Airflow 目前仅支持 Airflow
- Oozie
- Azkaban

## Deployer
将 Adapter 生成的调度配置文件以及脚本部署到调度平台中
- Airflow
- Oozie
- Azkaban

