# backend document

---

### 0. setup

1. use mysql, url: `localhost:3306/oj'`
2. python backend env
3. set configuration in `config.py`

```shell
conda create -n webenv python=3.10
conda activate webenv
conda install -c conda-forge flask=2.2.3
conda install -c conda-forge pydantic=1.10.5
pip3 install -r requirements.txt
```

---

### 1. Overview

#### 1.1 Response

返回给前端的类, ==截图仅供参考! 重新在本机测试!==

```js
{
    "data"
:
    self.data,
        // 返回数据
        "status_code"
:
    self.status_code,
        "message"
:
    self.message
    // 表示状态的信息(not found, invalid...)
}
```

#### 1.2 User

1. user拥有三个权限
   level1: ”学生“用户, level2: ”老师“用户, level3: super user
2. username: 用户名, nickname: 用于展示的昵称

#### 1.3 json格式

1. `to_json_lite`: 不带object名, 数组中使用
   ```js
   [
       {
           //obj1...
       },
       {
           //obj2...
       }
   ]
   ```
2. `to_json`: 带object名, 其它情况使用
   ```js
   // 放入 Response message 中的 problem 对象
   "message": {
       "problem": {
           //content...
       }
   }
   ```

#### 1.4 时间格式

使用 `datetime.datetime`, `isoformat()`

---

### 2. Problem

0. 获取题目列表 / 单个题目, 老师创建题目
   contributor: nickname
   start_time: 题目创建时间
   status: 预留值
   tag: 预留标签

1. get all problems
   <img src="./pics/problem1.png" style="zoom:50%;" />
2. get single problem
   <img src="pics/problem2.png" style="zoom:50%;" />
3. create problem
   <img src="pics/problem3.png" style="zoom:50%;" />

---

### 3. Submit (code)

1. create submit
   ![submit1.png](pics%2Fsubmit1.png)
2. get all submit histories
   ![submit2.png](pics%2Fsubmit2.png)
3. get submit histories of somebody
   ![submit3.png](pics%2Fsubmit3.png)
4. get submit histories of specific question
5. get submit histories of specific question of somebody

---

---

---

# Milestone 3 Update (! Important)

### Upload

1. upload 中提供了四个 api: `/upload/assignment`, `/upload/zip`, `/upload/upload_assignment`, `/upload/upload_zip`,
   分别对应assignment/zip上传后更新数据和上传
2. upload返回一个数字, 直接拿这个数字访问资源! 比如返回了2, 资源的
   url 就是: `https://simple-oj.oss-cn-shenzhen.aliyuncs.com/2`, 前缀一直是一样的
   ![upload1.png](pics%2Fupload1.png)
   ![upload2.png](pics%2Fupload2.png)

### Problem Update

1. 注意更改了 problem 表的内容, 简化了 tag -> year, difficulty, derivation, 增添了 oss_id (资源包)
2. 注意创建 problem 时的逻辑顺序: 先创建基本内容, 返回 id 后再拿 oss_id, problem_id 添加资源包

### Competition Update

1. 更改了整体逻辑: competition 和 assignment 共享表, 统称 event, 包含 type 字段(competition/assignment)
2. 












