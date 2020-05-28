import requests
import json


# https://360bxy.zkydib.com/#/login 登录页面
# 需要采集的url
url ='https://360bxy.zkydib.com/saasapi/order/orderList'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '103',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '你的cookie',
    'Host': '360bxy.zkydib.com',
    'Origin': 'https://360bxy.zkydib.com',
    'Referer': 'https://360bxy.zkydib.com/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',


}

# 采集所有页面数据
for pag in range(1, 163):
    pag = pag
    data = {
        'page': f'{pag}',
        'page_size': '5',
        'inc_cont_no': '',
        'product_name': '',
        'status': '',
        'a_cn_name': '',
        'cn_name': '',
        'first_pay_time': '',
        'end_pay_time': '',

    }

    response = requests.post(url=url, headers=headers, data=data)
    json_data = json.loads(response.text)
    data = json_data['data']['info']
    for dat in data:
        inc_cont_no = dat.get('inc_cont_no')
        create_time = dat.get('create_time')
        product_name = dat.get('product_name')
        i_user_name = dat.get('i_user_name')
        a_cn_name = dat.get('a_cn_name')
        pay_amount = dat.get('pay_amount')
        status = dat.get('status')
        fee = dat.get('fee')
        with open('user.csv', 'a', encoding='utf-8') as fp:
            text = f'{"’"}{inc_cont_no},{create_time},{product_name},{i_user_name},{a_cn_name},{pay_amount},{status},{fee}'
            fp.write(text)
            fp.write('\n')
            # fp.write('保单号')
            # fp.write(inc_cont_no)
            # fp.write('下单时间')
            # fp.write(create_time)
            # fp.write('产品名称')
            # fp.write(product_name)
            # fp.write('投保人姓名')
            # fp.write(i_user_name)
            # fp.write('被保人姓名')
            # fp.write(a_cn_name)
            # fp.write('付款金额')
            # fp.write(pay_amount)
            # fp.write('保单状态')
            # fp.write(status)
            # fp.write('服务费')
            # fp.write(fee)
            # fp.write('\n')

        # print('保单号', inc_cont_no)
        # print('下单时间', create_time)
        # print('产品名称', product_name)
        # print('投保人姓名', i_user_name)
        # print('被保人姓名', a_cn_name)
        # print('付款金额', pay_amount)
        # print('保单状态', status)
        # print('服务金额', fee)

        # 个人保单服务页数据
        url1 = 'https://360bxy.zkydib.com/saasapi/order/orderInfo'
        data1 = {
            'com_id': '',
            'inc_cont_no': inc_cont_no,
        }

        res = requests.post(url=url1, headers=headers, data=data1)
        json_data1 = json.loads(res.text)
        data1 = json_data1['data']['info']
        for ddmseg in data1:
            l = ddmseg['list']
            ti = ddmseg.get('title')
            for x in l:
                ti = ddmseg.get('title')
                # print(x.get('title')+x.get('value'))
                # print(ti)
            with open('cs.csv', 'a', encoding='utf-8') as f:

                # ti = ddmseg.get('title')
                # f.write(ti+':')
                f.write('订单号'+inc_cont_no +",")
                for x in l:
                    # f.write(x.get('title')+x.get('value'))
                    # f.write(x.get('value'))

                    title = x.get('title')
                    value = x.get('value')
                    print(title)
                    print(value)
                    te = f'{ti},{title},{value},{","}'
                    f.write(te)
                f.write('\n')
 


