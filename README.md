# 民营企业政策服务请求的跨部门处置与瓶颈分析

本项目用于整理相关业务资料。CSV 文件采用 UTF-8 编码，首行为字段名，日期使用 ISO 格式；空单元格表示来源未提供。样例记录为合成数据。

## 样例资料

- `requests.csv` 包含样例字段 `request,company,category,created_on,order_ref,impact,state`。
- `departments.csv` 包含样例字段 `department,category,service,period,capacity_hours`。
- `handoffs.csv` 包含样例字段 `handoff,request,from_unit,to_unit,action,created_on,response`。
- `outcomes.csv` 包含样例字段 `outcome,request,company_confirmed,confirmed_on,remaining_issue,source_rev`。

## 运行检查

需要 Python 3.11 或更高版本，无第三方依赖。

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q tests
```
