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
    "university_name": "华中师范大学"
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
# 预获取验证码(若需要)

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

# 获取验证码(若需要)

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
    "university_name":"string",
    "login_info":{
        "username":"xxxxx",  //大学学号
        "password":"xxxxx",  // 教务处密码
        "verify":"string"   // 若有则填,否则为空
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
    "research_direction":string,
    "photo_url":string,  //可省略，默认为王攀www
    "sex":"男" or "女",
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
.
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
**Response Body**
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
