# Ikea-x-Virgil-Abloh
宜家联名预约

官方做得实在简陋，没有任何加密，只需要把抓到的token放在请求头里就可以进行预约。
两道答题也是摆设，前端验证，bot完全可以绕过。。。LMAO
## 城市ID
```Java
{
 "city": [
  {
   "id": 1,
   "city_name": "上海徐汇宜家商场",
   "time": "10.28 11:00",
   "start_time": 1572231600,
   "goods_quantity": 21
  },
  {
   "id": 2,
   "city_name": "北京西红门宜家商场",
   "time": "10.28 13:00",
   "start_time": 1572238800,
   "goods_quantity": 21
  },
  {
   "id": 3,
   "city_name": "成都高新宜家商场",
   "time": "10.28 15:00",
   "start_time": 1572246000,
   "goods_quantity": 21
  },
  {
   "id": 4,
   "city_name": "深圳宜家商场",
   "time": "10.28 17:00",
   "start_time": 1572253200,
   "goods_quantity": 13
  },
  {
   "id": 5,
   "city_name": "苏州宜家商场",
   "time": "10.28 19:00",
   "start_time": 1572260400,
   "goods_quantity": 13
  },
  {
   "id": 6,
   "city_name": "广州天河宜家商场",
   "time": "10.28 19:00",
   "start_time": 1572260400,
   "goods_quantity": 13
  },
  {
   "id": 7,
   "city_name": "西安宜家商场",
   "time": "10.28 19:00",
   "start_time": 1572260400,
   "goods_quantity": 13
  } 
  ],
}
```
## 商品ID
```Java
{
 "goods": [
  {
   "id": 1,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/1.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "搬运袋 大 自然色"
   ],
   "price": "199",
   "item_number": "20451510"
  },
  {
   "id": 2,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/2.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "搬运袋 中 自然色"
   ],
   "price": "149",
   "item_number": "70455822"
  },
  {
   "id": 3,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/3.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "挂钟 42 白色"
   ],
   "price": "99",
   "item_number": "90451535"
  },
  {
   "id": 4,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/4.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "工具17件套 橙色"
   ],
   "price": "79",
   "item_number": "40451533"
  },
  {
   "id": 5,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/5.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "背光工艺品 USB"
   ],
   "price": "499",
   "item_number": "50451537"
  },
  {
   "id": 6,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/6.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "镜子"
   ],
   "price": "1499",
   "item_number": "00451525"
  },
  {
   "id": 7,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/7.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "被套和枕套 150x200/50x80 灰色"
   ],
   "price": "199",
   "item_number": "10454793"
  },
  {
   "id": 8,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/8.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "垫套 40x65 米黄色"
   ],
   "price": "79",
   "item_number": "60455511"
  },
  {
   "id": 9,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/9.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "坐卧床架 80x200 松木",
    "坐卧两用床罩 80x200 米黄色"
   ],
   "price": "2299",
   "item_number": "30451519 / 70451517"
  },
  {
   "id": 10,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/10.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "桌子 170x75 山毛榉/桦木",
    "椅子X4 山毛榉"
   ],
   "price": "5095",
   "item_number": "20451529 / 60451513"
  },
  {
   "id": 11,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/11.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "玻璃门柜 80x80 松木"
   ],
   "price": "1699",
   "item_number": "50451523"
  },
  {
   "id": 12,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/12.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "长绒地毯 133x195 绿色"
   ],
   "price": "1499",
   "item_number": "40434751"
  },
  {
   "id": 13,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/13.jpg",
   "name": "MARKERAD 玛克拉德",
   "details": [
    "短绒地毯 90x200 白色/黑色"
   ],
   "price": "999",
   "item_number": "80434754"
  },
  {
   "id": 14,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/14.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "短绒地毯 灰色 300*200"
   ],
   "price": "1999",
   "item_number": "004.353.71",
   "designer": "Virgil Abloh"
  },
  {
   "id": 15,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/15.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "短绒地毯 多色 240*170"
   ],
   "price": "2999",
   "item_number": "104.353.75",
   "designer": "Chiaozza"
  },
  {
   "id": 16,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/16.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "平织地毯 多色 200*175"
   ],
   "price": "1499",
   "item_number": "304.353.60",
   "designer": "Craig Green"
  },
  {
   "id": 17,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/17.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "短绒地毯 多色 250*165"
   ],
   "price": "2499",
   "item_number": "404.353.74",
   "designer": "Misaki Kawai"
  },
  {
   "id": 18,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/18.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "平织地毯 多色 300*200"
   ],
   "price": "2499",
   "item_number": "504.353.78",
   "designer": "SeulgiLee"
  },
  {
   "id": 19,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/19.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "短绒地毯 黑色/白色 直径：200"
   ],
   "price": "2499",
   "item_number": "704.353.58",
   "designer": "Noah Lyon"
  },
  {
   "id": 20,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/20.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "平织地毯 黑色/白色 195*133"
   ],
   "price": "1499",
   "item_number": "804.353.67",
   "designer": "Filip Pagowski"
  },
  {
   "id": 21,
   "img_url": "https://tc.woaap.com/ikea/limitCollect/img/item/21.jpg",
   "name": "ART EVENT 宜家艺术节2019",
   "details": [
    "短绒地毯 黑色/多色 256*170"
   ],
   "price": "2999",
   "item_number": "904.353.62",
   "designer": "SupaKitch"
  }
 ],
}
```
## 并没有什么卵用的问答
```Java
{
 "subject": [
  {
   "id": "1",
   "title": "请问本次限量系列的合作设计师是？",
   "a": "Virgil",
   "b": "Vrigll",
   "right": "a"
  },
  {
   "id": "2",
   "title": "请问本次限量系列的系列名是？",
   "a": "MARKRED",
   "b": "MARKERAD",
   "right": "b"
  },
  {
   "id": "3",
   "title": "以下哪个商品并不是本次抢购商品？",
   "a": "椅子",
   "b": "玻璃杯",
   "right": "b"
  },
  {
   "id": "4",
   "title": "本次发售的绿色长绒地毯上的字样是？",
   "a": "“WET GRASS”",
   "b": "“WET GLASS”",
   "right": "a"
  },
  {
   "id": "5",
   "title": "设计师Virgil作品的特点是？",
   "a": "字母带有感叹号",
   "b": "字母带有引号",
   "right": "b"
  },
  {
   "id": "6",
   "title": "这是宜家和Virgil设计师的第几次合作？",
   "a": "第一次",
   "b": "第二次",
   "right": "b"
  },
  {
   "id": "7",
   "title": "MARKERAD系列商品的上市时间是？",
   "a": "11月1日",
   "b": "12月1日",
   "right": "a"
  },
  {
   "id": "8",
   "title": "中国第一家宜家商场开在哪个城市？",
   "a": "上海",
   "b": "广州",
   "right": "a"
  },
  {
   "id": "9",
   "title": "宜家是来自哪个国家的品牌？",
   "a": "瑞士",
   "b": "瑞典",
   "right": "b"
  },
  {
   "id": "10",
   "title": "本次发售的包袋上印有的字样是？",
   "a": "“SCULPTURE”",
   "b": "”STRUCTURE“",
   "right": "a"
  }
 ],
 "system_time": 1572257143,
 "type": 2
}
```
