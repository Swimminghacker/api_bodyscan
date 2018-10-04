### 采用mysql数据库

数据库名：**bodyscan**



#### 账号系统

三个表：**user     operator      institution_operator**



##### user表：

记录所有账号的表

字段：id     account     password        role 

role字段：0代表超管、1代表操作员、2代表客户机构操作员



##### operator表：

操作员的信息表

字段：id  name    account   created_time    password  receive_num   process_num   wait_num finished_num   status 

其中status字段：1代表正常 、2 代表被冻结



##### institution_operator表：

客户机构操作员的表

字段：id    name    created_time    account   password     belonged_institution      mail     task_num     status

其中status字段：1代表正常 、2 代表被冻结

