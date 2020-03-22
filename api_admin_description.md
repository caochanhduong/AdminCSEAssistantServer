
# Server CSE Assistant API Description



___


# `GET /api/server-cse-assistant-admin/activities/:_id`

## Goals
`Trả về 1 bài đăng hoàn chỉnh theo _id`

## Required Header

## Param Request
`
_id: id của bài đăng (size = 24 ,string)
`

`
Example: /api/server-cse-assistant-admin/activities/5e593b0e674aef8330ca6ad4
`

## Body Request

## Success Response
```json
{
    "code": 200,
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
Khi _id không hợp lệ.
`
```json
{
    "code": 400,
    "message": "invalid id"
}
```
`
Khi bài đăng có _id không tồn tại.
`
```json
{
    "code": 404,
    "message": "activity not found"
}
```

___
# `DELETE /api/server-cse-assistant-admin/activities/:_id`

## Goals
`Xóa 1 bài đăng theo _id`

## Required Header

## Param Request
`
_id: id của bài đăng (size = 24 ,string)
`

`
Example: /api/server-cse-assistant-admin/activities/5e593b0e674aef8330ca6ad4
`

## Body Request

## Success Response
```json
{
    "code": 200,
    "message": "delete success"
}
```
## Error Response

`
Khi _id không hợp lệ.
`
```json
{
    "code": 400,
    "message": "invalid id"
}
```
`
Khi bài đăng có _id không tồn tại.
`
```json
{
    "code": 404,
    "message": "activity not found"
}
```

___
# `GET /api/server-cse-assistant-admin/activities`

## Goals
`Trả về danh sách các bài đăng (giới hạn tối đa 10 bài)`

## Required Header

## Param Request

## Body Request

## Success Response
```json
{
    "code": 200,
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
Khi không có bài đăng nào trong database.
`
```json
{
    "code": 404,
    "message": "activities not found"
}
```
___
# `POST /api/server-cse-assistant-admin/activities`

## Goals
Thêm 1 bài đăng.

## Required Header

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
```json
{
    "code": 200,
    "message": "insert success"
}
```
## Error Response

`
Khi thêm thất bại.
`
```json
{
    "code": 400,
    "message": "insert fail"
}
```
`
Khi request không có key "activity"
`
```json
{
    "code": 400,
    "message": "activity can not be None"
}
```

___
# `PUT /api/server-cse-assistant-admin/activities`

## Goals
Cập nhật 1 bài đăng. 

## Required Header

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
```json
{
    "code": 200,
    "message": "update success"
}
```
## Error Response

`
Khi "_id" truyền vào không tồn tại.
`
```json
{
    "code": 400,
    "message": "activity's _id not exist"
}
```
`
Khi request không có key "activity"
`
```json
{
    "code": 400,
    "message": "activity can not be None"
}
```