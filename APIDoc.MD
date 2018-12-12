# API 文档

# 大学列表

| URL | Header | Method |
| ------ | ------ | ------ |
| /api/universities/ | 无 | GET |

**Responses Body**
```
{
    "universities":["CCNU", "WUST", ... ...]
}
```

# 获取登录所需信息


| URL | Header | Method |
| ------ | ------ | ------ |
| /api/universities/schema/ | 无 | POST |


**Request Body**

```
{
    "university_name": "CCNU"
}
```

**Responses Body**

```
{
    "username":"str",
    "password":"passwrod",
    "verify": 1 or 0
}
```
# 预获取验证码(若需要)（目前未实现）

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/universities/pre_verify/|无|POST|

**Request Body**
```
{
    "university_name": "WUST"
}
```

**Response**
```
{
    "msg":"ok"
}
```

# 获取验证码(若需要)（目前未实现）

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/universities/verify/|无|POST|

**Request Body**
```
{
    "university_name": "WUST"
}
```

**Response Data**
图片文件


# 登录
|URL |Header|Method|
| ------ | ------ | ------ |
|/api/login/|无|POST|

**Request Body**
```
{
    "university_name":"string", //CCNU, WUST
    "login_info":{
        "username":"xxxxx",  //大学学号
        "password":"xxxxx",  // 教务处密码
        "verify": int   // 若有则填,否则为空
    }
}
```

**Response**
```
{
    "token": token
}
```
OR
```
{
    "msg":"failed" // 原有用户登录失败
}
```

OR 
```
{
    "msg":"school check failed" // 未通过学校验证
}
```

**Status Code**
200 原有用户登录
201 新建的用户
401 登陆失败

# 添加老师
|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/|Authorization:token|POST|

**Request Body**
```
{
    "teacher_name":string,
    "research_direction":string, //CS, EE and so on
    "photo_url":string,  //可省略，默认为王攀www
    "sex":string, //female OR male
    "birth": int    //年份
}
```

**Response**
201
```
{
    "created": integer   //teacher id
}
```

401
```
{
    "msg":"401 unAuthorization"
}
```

403
```
{
    "msg":"403 Forbidden"
}
```

# 评论老师
|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/`<tid>`/|Authorization:token|POST|

**Request Body**
```
{
    "score": 1到5 integer,
    "content": string
}
```

**Response Body**
Status Code:201
```
{
    "msg":"success"
}
```

Status Code:401
```
{
    "msg":"401 unAuthorization"
}
```
Status Code:403
```
{
    "msg":"403 Forbidden"
}
```

# 获取老师列表
|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/`<schoolname>`/page/`<page_num>`/|无|GET|


schoolname: 例如`华中师范大学`
page_num: 从1开始

**Response Body**
```
{
    "allpages":integer, //总页数
    "teachers":[
        {
            "tid":integer,
            "name":string,
            "photo": string
            "direction": string
            "score": float
        }......
    ]
}
```


# 获取有关老师评论

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/`<tid>`/info/page/`<page_num>`/|无|GET|


tid: 老师id
page_num: 页码从1开始
**response body**
```
    "allpages": integer,
    "teacher":{
        "tid":int,
        "name":string,
        "photo":string,
        "direction":string,
        "score":float,
        "sex":string
    },
    "comments": [
        {
            "score":int,
            "content":string
        }, ... ...
    ]
```

# 按照老师姓名查询

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/name/<teachername>/|无|GET|

teachername: 教师姓名，string

**response body**
```
    "teacher":{
        "tid":int,
        "school":string,
        "name":string,
        "photo":string,
        "direction":string,
        "score":float,
        "sex":string
        "birthday":string
    },
```

**Status Code**
200 查询成功

# 按照老师学校查询（未测，武理无法登陆）

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/school/<teacherschool>/|无|GET|

teacherschool: 教师姓名，可包含空格的字符串

**response body**
```
    "teacher":{
        "tid":int,
        "school":string,
        "name":string,
        "photo":string,
        "direction":string,
        "score":float,
        "sex":string
        "birthday":string
    },
```

**Status Code**
200

# 按照老师学校查询（武理无法登陆，未测）

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/school/<teacherschool>/|无|GET|

teacherschool: 教师学校，目前实现CCNU

**response body**
```
    "teacher":{
        "tid":int,
        "school":string,
        "name":string,
        "photo":string,
        "direction":string,
        "score":float,
        "sex":string
        "birthday":string
    },
```

**Status Code**
200 查询成功

# 按照老师性别查询

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/gender/<gender>/|无|GET|

gender: female OR male

**response body**
```
    "teacher":{
        "tid":int,
        "school":string,
        "name":string,
        "photo":string,
        "direction":string,
        "score":float,
        "sex":string
        "birthday":string
    },
```

**Status Code**
200 查询成功


# 按照老师专业查询

|URL |Header|Method|
| ------ | ------ | ------ |
|/api/teacher/major/<major>/|无|GET|

major: CS EE and so on

**response body**
```
    "teacher":{
        "tid":int,
        "school":string,
        "name":string,
        "photo":string,
        "direction":string,
        "score":float,
        "sex":string
        "birthday":string
    },
```

**Status Code**
200 查询成功
