import requests

url = 'https://api-uss.danke.com/v3/rooms?cityId=540&pageNumber=1&pageReferrer=3&searchSessionId=91498D9A-0EF3-4CBD-93D5-3F02B604866B&timestamp=1594275808682'


#      https://api-uss.danke.com/v3/rooms/recommendations?cityId=540&execlusions=&is_near_by=1&latlng=31.300710_121.442950&nearBy=5000&pageNumber=1&pageReferrer=3&searchSessionId=300F4548-52B1-4B0F-9632-60D9A2245FD3&searchText=%E5%BE%90%E5%AE%B6%E6%B1%87&timestamp=1594276794903
# 快速找房 https://api-uss.danke.com/v3/rooms?cityId=540&pageNumber=1&pageReferrer=3&searchSessionId=91498D9A-0EF3-4CBD-93D5-3F02B604866B&timestamp=1594275808682
# 搜索地区 https://api-uss.danke.com/v3/rooms/recommendations?cityId=540&execlusions=&is_near_by=1&latlng=31.300710_121.442950&nearBy=5000&pageNumber=1&pageReferrer=3&searchSessionId=300F4548-52B1-4B0F-9632-60D9A2245FD3&searchText=%E5%BE%90%E5%AE%B6%E6%B1%87&timestamp=1594276794903
# 城市    https://api-uss.danke.com/v3/metadata/cities?timestamp=1594277358386
# 详情页  https://api-uss.danke.com/v3/rooms/415793804?cityId=540&rentType=2&shortRent=false&timestamp=1594277672167

# 获取城市ID
def get_cityId():

    url = 'https://api-uss.danke.com/v3/metadata/cities'
    dcityId_response = requests.get(url=url, verify=False).json()
    cityids = dcityId_response["result"]
    for cit in cityids:
        cittyid = cit.get("id")
        name = cit.get("name")
        latitude = cit.get("latitude")
        longitude = cit.get("longitude")

        # 获取城市地区
        area_url = f"https://www.danke.com/pangu-activity/marketing/custom-house-resource/district/{cittyid}"
        area_response = requests.get(url=area_url, verify=False).json()
        areaids = area_response["data"]
        areadict = {}
        for area_name, area_ids in areaids.items():
            areadict[area_ids] = area_name

        # 获取地区街道（没添加）
        for area_id in areaids:
            # print(area_id)
            street_url = f"https://www.danke.com/pangu-activity/marketing/custom-house-resource/block/{area_id}"
            street_response = requests.get(url=street_url, verify=False).json()
            streetids = street_response["data"]

        data = {
            "cittyid": cittyid,
            "areaids": areadict,
            "name": name,
            "latitude": latitude,
            "longitude": longitude
        }
        print(data)
        yield data


# 按照搜索内容抓取数据
def get_data(cityId, searchText):
    search_url = f"https://api-uss.danke.com/v3/rooms/recommendations?cityId={cityId}&execlusions=&is_near_by=1&latlng=31.300710_121.442950&nearBy=5000&pageNumber=1&pageReferrer=3&searchText={searchText}"
    totalPages = requests.get(url=search_url).json()["result"].get("totalPages")
    for pag in range(1, totalPages):
        search_url = f"https://api-uss.danke.com/v3/rooms/recommendations?cityId={cityId}&execlusions=&is_near_by=1&latlng=31.300710_121.442950&nearBy=5000&pageNumber={pag}&pageReferrer=3&searchText={searchText}"
        search_dataes = requests.get(url=search_url).json()["result"].get("content")
        for search_data in search_dataes:
            positionId = search_data.get("positionId")
            roomId = search_data.get("roomId")
            distance = search_data.get("distance")
            name = search_data.get("name")
            communityName= search_data.get("communityName")
            districtName = search_data.get("districtName")
            districtId = search_data.get("districtId")
            blockName = search_data.get("blockName")
            blockId = search_data.get("blockId")
            facing = search_data.get("facing")
            suiteId = search_data.get("suiteId")
            bedroomCount = search_data.get("bedroomCount")
            price = search_data.get("price")
            monthPrice = search_data.get("monthPrice")
            roomPictureUrl = search_data.get("roomPictureUrl")
            danke_data = {positionId: [positionId, roomId, distance, name, communityName, districtName, districtId, blockName, blockId,
                  facing, suiteId, bedroomCount, price, monthPrice, roomPictureUrl]}
            # print(danke_data)
            values = danke_data.values()
            for value in values:
                print(value)
                save_data(str(value))
            # print(positionId, roomId, distance, name, communityName, districtName, districtId, blockName, blockId,
            #       facing, suiteId, bedroomCount, price, monthPrice, roomPictureUrl)

def get_Details(cityId, roomId):
    details_url = f"https://api-uss.danke.com/v3/rooms/{roomId}?cityId={cityId}&rentType=2&shortRent=false&timestamp=1594277672167"
    details_reponse = requests.get(url=details_url)
#     进行数据解析

def save_data(value):
    with open("蛋壳.csv", "a", encoding="utf-8") as f:
        f.write(value)
        f.write("\n")


cityid = get_cityId()
# for c in cityid:
    # print(c.get("cittyid"))
get_data(cityId=1, searchText="朝阳区")