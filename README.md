
# Server CSE Assistant API Description


___


# `GET /auth`

## Goals
`Xác thực`

## Required Header

## Param Request

## Body Request
```json
{
	"username":"duongcc",
	"password":"123"
}

```

## Success Response
`
code: 200
`
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1Mzg1MDMsImlhdCI6MTU4NjUzODIwMywibmJmIjoxNTg2NTM4MjAzLCJpZGVudGl0eSI6MX0.PCpb6f4yrwmTCdKCa0VIp4UexcLCSOIfpBJDwOw9JrQ"
}
```
## Error Response

`
code: 401 (Khi tài khoản không tồn tại).
`

```json
{
    "description": "Invalid credentials",
    "error": "Bad Request",
    "status_code": 401
}
```

___


# `GET /api/server-cse-assistant-admin/activities/:_id`

## Goals
`Trả về 1 bài đăng hoàn chỉnh theo _id`

## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"

## Param Request
`
_id: id của bài đăng (size = 24 ,string)
`

`
Example: /api/server-cse-assistant-admin/activities/5e593b0e674aef8330ca6ad4
`

## Body Request

## Success Response
`
code: 200
`
```json
{
    "message": {
        "_id": "5e593b0e674aef8330ca6ad4",
        "address": [],
        "contact": [],
        "holder": [],
        "joiner": [
            "sinh viên khoa học công nghệ",
            "sinh viên sắp ra trường , mới ra trường hay đang tìm kiếm cho mình một công việc",
            "lo lắng , sợ sệt và nghi ngờ về chính khả năng của bản thân mình",
            "có 1001 vấn đề cùng những câu hỏi không tìm được lời giải đáp về sự khác biệt của giảng đường đại học với môi trường làm việc"
        ],
        "name_activity": [
            "trạm nâng cấp phiên bản 4.0",
            "hcm student forum",
            "hcm student forum"
        ],
        "name_place": [
            "trường đại học công nghệ thông tin tphcm"
        ],
        "register": [
            "đăng ký tham gia ngay"
        ],
        "reward": [
            "50 bạn đến với sự kiện sớm nhất sẽ được nhận ngay 1 quyển sách để làm nên sự nghiệp từ alpha books",
            "cơ hội nghề nghiệp hấp dẫn có 1 - 0 - 2 đặc biệt dành riêng cho sự kiện đến từ các đơn vị đối tác chiến lược , đồng hành như bosch , tictag",
            " \n️ nâng cấp và kết nối kiến thức , kỹ năng chuyên môn với dòng chảy 4.0.",
            "trò chuyện cùng diễn giả và khách mời những người dồi dào kinh nghiệm về nghề nghiệp và có cái nhìn sâu sắc về ảnh hưởng sâu rộng của cách mạng 4.0 đến môi trường lao động",
            " \n️ gặp gỡ và giao lưu kinh nghiệm với các bạn đến từ các trường đại học hàng đầu về khoa học công nghệ trên khắp địa bàn thành phố hồ chí minh",
            "khám phá bất ngờ đến từ gameshow thú vị và giải thưởng hấp dẫn"
        ],
        "time": [
            "27.10.2018"
        ],
        "time_work_place_mapping": [],
        "type_activity": [
            "sự kiện"
        ],
        "works": []
    }
}
```
## Error Response

`
code: 400 (Khi _id không hợp lệ).
`

```json
{
    "message": "invalid id"
}
```
`
code: 404 (Khi bài đăng có _id không tồn tại).
`
```json
{
    
    "message": "activity not found"
}
```

___
# `DELETE /api/server-cse-assistant-admin/activities/:_id`

## Goals
`Xóa 1 bài đăng theo _id`

## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"

## Param Request
`
_id: id của bài đăng (size = 24 ,string)
`

`
Example: /api/server-cse-assistant-admin/activities/5e593b0e674aef8330ca6ad4
`

## Body Request

## Success Response
`
code: 200
`
```json
{
    "message": "delete success"
}
```
## Error Response

`
    code: 400 (Khi _id không hợp lệ).
`
```json
{
    "message": "invalid id"
}
```
`
code: 404 (Khi bài đăng có _id không tồn tại).
`
```json
{
    "message": "activity not found"
}
```

___
# `GET /api/server-cse-assistant-admin/activities`

## Goals
`Trả về danh sách các bài đăng (giới hạn tối đa 10 bài)`

## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"


## Param Request

## Body Request

## Success Response
`
code: 200
`
```json
{
    "message": [
        {
            "_id": "5e593b11674aef8330ca6ad6",
            "address": [],
            "contact": [],
            "holder": [
                "4 đội công tác xã hội trường đh sư phạm kỹ thuật tp . h",
                "do "
            ],
            "joiner": [],
            "name_activity": [
                "đêm vui tất niên tết ấm áp",
                "c đêm vui tất niên tết ấm "
            ],
            "name_place": [
                "i sân cờ việt đ"
            ],
            "register": [],
            "reward": [
                " thắt chặt tình đoàn kết , giao lưu gắn bó giữa mọi người và tạo ra một không khí tết ấm áp vui v",
                "ợc tham gia các trò chơi đầy kịch t",
                "để giảm stress trong những ngày học tập , thi cử căng thẳng vừa qua và đón năm mới với đầy may mắn , bình an bên gia đình , bè ",
                "ng quà lộc đầu năm mang đầy ý ng"
            ],
            "time": [
                "c 17h30 , ngày 15/01/20"
            ],
            "time_work_place_mapping": [],
            "type_activity": [],
            "works": [
                "ng thưởng thức một đêm ca nhạc đậm chất tết , vui vẻ , sôi động do đội dày công dàn d",
                "ức ca hát , nhảy múa cùng mọi ng"
            ]
        }
    ]
}
```
## Error Response

`
code: 404 (Khi không có bài đăng nào trong database).
`
```json
{
    "message": "activities not found"
}
```
___
# `POST /api/server-cse-assistant-admin/activities`

## Goals
Thêm 1 bài đăng.

## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"

## Param Request

## Body Request
```json
{
	"activity":{
            "address": [],
            "contact": [],
            "holder": [],
            "joiner": [
                "sinh viên khoa học công nghệ",
                "sinh viên sắp ra trường , mới ra trường hay đang tìm kiếm cho mình một công việc",
                "lo lắng , sợ sệt và nghi ngờ về chính khả năng của bản thân mình",
                "có 1001 vấn đề cùng những câu hỏi không tìm được lời giải đáp về sự khác biệt của giảng đường đại học với môi trường làm việc"
            ],
            "name_activity": [
                "trạm nâng cấp phiên bản 4.0",
                "hcm student forum",
                "hcm student forum"
            ],
            "name_place": [
                "trường đại học công nghệ thông tin tphcm"
            ],
            "register": [
                "đăng ký tham gia ngay"
            ],
            "reward": [
                "50 bạn đến với sự kiện sớm nhất sẽ được nhận ngay 1 quyển sách để làm nên sự nghiệp từ alpha books",
                "cơ hội nghề nghiệp hấp dẫn có 1 - 0 - 2 đặc biệt dành riêng cho sự kiện đến từ các đơn vị đối tác chiến lược , đồng hành như bosch , tictag",
                " \n️ nâng cấp và kết nối kiến thức , kỹ năng chuyên môn với dòng chảy 4.0.",
                "trò chuyện cùng diễn giả và khách mời những người dồi dào kinh nghiệm về nghề nghiệp và có cái nhìn sâu sắc về ảnh hưởng sâu rộng của cách mạng 4.0 đến môi trường lao động",
                " \n️ gặp gỡ và giao lưu kinh nghiệm với các bạn đến từ các trường đại học hàng đầu về khoa học công nghệ trên khắp địa bàn thành phố hồ chí minh",
                "khám phá bất ngờ đến từ gameshow thú vị và giải thưởng hấp dẫn"
            ],
            "time": [
                "27.10.2018"
            ],
            "time_work_place_mapping": [],
            "type_activity": [
                "sự kiện"
            ],
            "works": []
        }
}
```
## Success Response
`
code: 200
`
```json
{
    "message": "insert success",
    "id":"5e593b11674aef8330ca6ad6"
}
```
`
id: id của bài đăng vừa thêm.
`
## Error Response

`
code: 400 (Khi thêm thất bại).
`
```json
{
    "message": "insert fail"
}
```
`
code: 400 (Khi request không có key "activity")
`
```json
{
    "message": "activity can not be None"
}
```

___
# `PUT /api/server-cse-assistant-admin/activities`

## Goals
Cập nhật 1 bài đăng. 

## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"


## Param Request

## Body Request
```json
{
	"activity":{
            "_id":"5e593b10674aef8330ca6ad5",
            "address": [],
            "contact": [],
            "holder": [],
            "joiner": [
                "sinh viên khoa học công nghệ",
                "sinh viên sắp ra trường , mới ra trường hay đang tìm kiếm cho mình một công việc",
                "lo lắng , sợ sệt và nghi ngờ về chính khả năng của bản thân mình",
                "có 1001 vấn đề cùng những câu hỏi không tìm được lời giải đáp về sự khác biệt của giảng đường đại học với môi trường làm việc"
            ],
            "name_activity": [
                "trạm nâng cấp phiên bản 4.0",
                "hcm student forum",
                "hcm student forum"
            ],
            "name_place": [
                "trường đại học công nghệ thông tin tphcm"
            ],
            "register": [
                "đăng ký tham gia ngay"
            ],
            "reward": [
                "50 bạn đến với sự kiện sớm nhất sẽ được nhận ngay 1 quyển sách để làm nên sự nghiệp từ alpha books",
                "cơ hội nghề nghiệp hấp dẫn có 1 - 0 - 2 đặc biệt dành riêng cho sự kiện đến từ các đơn vị đối tác chiến lược , đồng hành như bosch , tictag",
                " \n️ nâng cấp và kết nối kiến thức , kỹ năng chuyên môn với dòng chảy 4.0.",
                "trò chuyện cùng diễn giả và khách mời những người dồi dào kinh nghiệm về nghề nghiệp và có cái nhìn sâu sắc về ảnh hưởng sâu rộng của cách mạng 4.0 đến môi trường lao động",
                " \n️ gặp gỡ và giao lưu kinh nghiệm với các bạn đến từ các trường đại học hàng đầu về khoa học công nghệ trên khắp địa bàn thành phố hồ chí minh",
                "khám phá bất ngờ đến từ gameshow thú vị và giải thưởng hấp dẫn"
            ],
            "time": [
                "27.10.2018"
            ],
            "time_work_place_mapping": [],
            "type_activity": [
                "sự kiện"
            ],
            "works": []
        }
}
```
`
Lưu ý là cập nhật thì "activity" có "_id" còn insert thì không.
`
## Success Response
`
code: 200
`
```json
{
    "message": "update success"
}
```
## Error Response

`
code: 400 (Khi "_id" truyền vào không tồn tại).
`
```json
{
    "message": "activity's _id not exist"
}
```
`
code: 400 (Khi request không có key "activity").
`
```json
{
    "message": "activity can not be None"
}
```

___
# `GET /api/server-cse-assistant-admin/activities/page/:page`

## Goals
Lấy về các bài đăng theo số trang, mỗi trang 20 bài đăng.

## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"


## Param Request
`
page: số  thứ tự trang (đếm từ 1)
`

`
Example: /api/server-cse-assistant-admin/activities/page/1 (lấy trang 1)
`


## Body Request

## Success Response
`
code: 200
`
```json
{
    "current_page": 2,
    "per_page": 20,
    "total": 923,
    "activities": [
        {
            "_id": "5e593b18674aef8330ca6aea",
            "address": [],
            "contact": [],
            "holder": [
                "đội ctxh",
                "đội ctxh"
            ],
            "joiner": [],
            "name_activity": [
                "ngày cuối tuần của tôi",
                "ngày cuối tuần của tôi",
                "ngày cuối tuần của tôi"
            ],
            "name_place": [],
            "register": [],
            "reward": [
                "biết được mùi hương của bùn đất , vị mặn của mồ hôi , cái lấm lem xi măng của một người thợ xây thực thụ",
                "trải nghiệm bữa cơm của đại gia đình ctxh , đạm bạc , đơn sơ nhưng đầy ắp tình cảm"
            ],
            "time": [],
            "time_work_place_mapping": [],
            "type_activity": [
                "chương trình",
                "chương trình",
                "chương trình"
            ],
            "works": [
                "sinh hoạt sau giờ làm việc"
            ]
        },
        {
            "_id": "5e593b18674aef8330ca6aeb",
            "address": [],
            "contact": [],
            "holder": [],
            "joiner": [
                "tự tin vào vốn kiến thức của bản thân",
                "nghĩ mình có tố chất của một thủ lĩnh"
            ],
            "name_activity": [
                "thủ lĩnh sinh viên 2019",
                "thủ lĩnh sinh viên năm 2019",
                "thủ lĩnh sinh viên năm 2019"
            ],
            "name_place": [],
            "register": [
                "các bài dự thi gửi về email",
                "tiêu đề : thủ lĩnh sv"
            ],
            "reward": [
                "được giấy chứng nhận của hội thi"
            ],
            "time": [],
            "time_work_place_mapping": [],
            "type_activity": [
                "hội thi"
            ],
            "works": []
        }
    ]
}
```
## Error Response

`
code: 404 (Khi không có bài đăng nào trong database).
`
```json
{
    "message": "activity not found"
}
```

___
# `POST /api/server-cse-assistant-admin/activities/filter/page/:page`

## Goals
`
Lọc các bài đăng theo điều kiện chung, giới hạn trả về 20 bài đăng.
`
## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"


## Param Request
`
page: số  thứ tự trang (đếm từ 1)
`
## Body Request
```json
{
	"condition":{
        "name_activity":["đêm vui tất niên tết ấm áp"],
        "name_place":["sân cờ"]
    }
}
```
`
condition: object json chứa key và value của các điều kiện (dạng key: list)
`
## Success Response
`
code: 200
`

```json
{
    "activities": [
        {
            "_id": "5e593b11674aef8330ca6ad6",
            "address": [],
            "contact": [],
            "holder": [
                "4 đội công tác xã hội trường đh sư phạm kỹ thuật tp . h",
                "do "
            ],
            "joiner": [],
            "name_activity": [
                "đêm vui tất niên tết ấm áp",
                "c đêm vui tất niên tết ấm "
            ],
            "name_place": [
                "i sân cờ việt đ"
            ],
            "register": [],
            "reward": [
                " thắt chặt tình đoàn kết , giao lưu gắn bó giữa mọi người và tạo ra một không khí tết ấm áp vui v",
                "ợc tham gia các trò chơi đầy kịch t",
                "để giảm stress trong những ngày học tập , thi cử căng thẳng vừa qua và đón năm mới với đầy may mắn , bình an bên gia đình , bè ",
                "ng quà lộc đầu năm mang đầy ý ng"
            ],
            "time": [
                "c 17h30 , ngày 15/01/20"
            ],
            "time_works_place_address_mapping": [
                {
                    "address": "trần duy hưng",
                    "name_place": "nhà nghỉ",
                    "time": "10h",
                    "works": "cua gái"
                },
                {
                    "address": "lý thường kiệt",
                    "name_place": "hotel",
                    "time": "10h",
                    "works": "cua trai"
                }
            ],
            "type_activity": [],
            "works": [
                "ng thưởng thức một đêm ca nhạc đậm chất tết , vui vẻ , sôi động do đội dày công dàn d",
                "ức ca hát , nhảy múa cùng mọi ng"
            ]
        }
    ],
    "message": "activity found",
    "total":1,
    "per_page":20,
    "current_page":1
}
```
## Error Response

`
code: 404 (Khi không có bài đăng nào trong database thỏa điều kiện).
`
```json
{
  "message": "activity not found"
}
```
___
# `GET /api/server-cse-assistant-admin/valid-token`

## Goals
`
Kiểm tra token có hợp lệ không.
`
## Required Header
`
Authorization : "JWT "+access_token (chuỗi 'JWT' rồi tới 1 khoảng trắng xong tới token)
`


Ví dụ: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODY1MzczMDIsImlhdCI6MTU4NjUzNzAwMiwibmJmIjoxNTg2NTM3MDAyLCJpZGVudGl0eSI6MX0.QmVJ3lOX1Xm7LQCJQXmwVJKwS2_pviviu6nmzDYMhD4"


## Param Request

## Body Request

## Success Response
`
code: 200
`


```json
{
    "message": "token valid"
}
```
## Error Response

`
code: 401 
`

```json
{
    "description": "Signature verification failed",
    "error": "Invalid token",
    "status_code": 401
}
```
(trường hợp token không đúng)

`
code: 401 
`

```json
{
    "description": "Signature has expired",
    "error": "Invalid token",
    "status_code": 401
}
```
(trường hợp token hết hạn)

