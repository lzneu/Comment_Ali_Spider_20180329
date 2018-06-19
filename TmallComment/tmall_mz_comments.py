# coding=UTF-8
import requests
import json

import random

from Config.Base import *
from toollib.logger_tmall_mz import Logger

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

base_url = 'https://rate.tmall.com/list_detail_rate.htm?order=1&itemId=%s&sellerId=%s&currentPage=%d'  # 评论页面的url（Json数据)


def get_Tmall_comment(product_collection, commentID_list, requestDict, comments_collection, product_index, start_num, maxPage_num_control,
                      log_collection, indexCollection):  # itemId 是商品的id, sellerId是卖家的id

    item_id = str(int(requestDict['original_id']))
    shop_id = str(round(float(requestDict['shop_id'])))
    title = str(requestDict['name'])
    category = str(requestDict['category'])
    # store_type = str(requestDict['store_type'])
    # spider_start_date =str(requestDict['spider_start_date'])
    product_dic = list(product_collection.find({'original_id': item_id}))[0]

    maxPage = get_Max_Page_Nummber(item_id, shop_id, product_index, log_collection)
    time.sleep(2)

    Logger.info('maxPage' + str(maxPage))
    if maxPage == 'Empty':
        maxPage = maxPage_num_control
    if int(maxPage) > 99:
        maxPage = maxPage_num_control

    cunzai_count = 0
    # 增加判断条件呀
    if maxPage < start_num:
        log_dict = {'type': '跳出', 'product_index': product_index, 'current_page': maxPage,
                    'log_time': time.time()}
        log_collection.insert(log_dict)
        # os.system('say "attention please,  your program has Exception  "')
        raise

    for page_num2 in range(start_num, int(maxPage) + 1):  # 最多只能爬取99页评论
        contents = get_one_page_comment(product_dic, commentID_list, item_id, shop_id, title, category, page_num2, comments_collection,
                                        product_index, log_collection, indexCollection)
        Logger.info('商品索引:' + str(product_index))
        Logger.info('页码:' + str(page_num2))
        Logger.info(contents)

        if contents != 'Empty' and len(contents) > 0:
            log_dict = {'type': '成功', 'product_index': product_index, 'current_page': page_num2,
                        'log_time': time.time()}
            log_collection.insert(log_dict)

            if sum(contents) >= 12:

                log_dict = {'type': '已经存在', 'product_index': product_index, 'current_page': page_num2,
                            'log_time': time.time()}
                log_collection.insert(log_dict)
                cunzai_count += 1
                if cunzai_count >= 3:
                    raise
            else:
                cunzai_count = 0

        if contents == 'Empty':
            log_dict = {'type': '跳出', 'product_index': product_index, 'current_page': page_num2,
                        'log_time': time.time()}
            log_collection.insert(log_dict)
            # os.system('say "attention please,  your program has Exception  "')
            raise

        time.sleep(random.randint(5, 10) / 10)  # 休眠片刻


def get_Max_Page_Nummber(item_id, shop_id, file_name, log_collection):
    page_url = base_url % (item_id, shop_id, 1)
    Logger.info(page_url)
    response = requests.request(method='GET', url=page_url, headers=headers)

    try:
        page_data = response.content.decode('gbk', 'ignore')

    except Exception:

        log_dict = {'type': '跳出', 'product_index': file_name, 'current_page': 1, 'log_time': time.time()}
        log_collection.insert(log_dict)

        return 'Empty'

    temp = page_data.split('"rateDetail":')
    if len(temp) > 1:
        page_data_dict = json.loads(temp[1])
        # myPrint(page_data_dict)
        # print('1111111', page_data_dict)
        rate_list = page_data_dict['rateList']

        # myPrint(page_data_dict['paginator'])
        pageinator = page_data_dict['paginator']['lastPage']

        # comments = []
        # for comment_info in rate_list:
        #     comment_info['item_id'] = item_id
        #     insertToMongo(comments_collection,comment_info)
        return pageinator
    else:
        time.sleep(5)
        response = requests.request(method='GET', url=page_url, headers=headers)
        try:
            page_data = response.content.decode('gbk', 'ignore')
            # myPrint(page_data)
            # requests.session()
        except Exception:
            # myPrint('error page:',page_num)
            # os.system('say " error page "')
            log_dict = {'type': '跳出', 'product_index': file_name, 'current_page': 1, 'log_time': time.time()}
            log_collection.insert(log_dict)
            # os.system('say "attention please,  your program has Exception  "')

            return 'Empty'

        temp = page_data.split('"rateDetail":')
        if len(temp) > 1:
            page_data_dict = json.loads(temp[1])
            # myPrint(page_data_dict)
            # print('1111111', page_data_dict)
            rate_list = page_data_dict['rateList']

            myPrint(page_data_dict['paginator'])
            pageinator = page_data_dict['paginator']['lastPage']

            # comments = []
            # for comment_info in rate_list:
            #     comment_info['item_id'] =item_id
            #     insertToMongo(comments_collection,comment_info)
            return pageinator
        else:
            myPrint('max page Nummber failure')
            log_dict = {'type': '跳出', 'product_index': file_name, 'current_page': 1, 'log_time': time.time()}
            log_collection.insert(log_dict)
            # os.system('say "attention please,  最大值获取失败  "')

            return 'Empty'


def get_one_page_comment(product_dic, commentID_list, item_id, shop_id, title, category, page_num, comments_collection, product_index,
                         log_collection, indexCollection):  # 根据item_id，和shop_id获取某一页的评论
    page_url = base_url % (item_id, shop_id, page_num)
    myPrint(page_url)

    response = requests.request(method='GET', url=page_url, headers=headers)

    try:
        page_data = response.content.decode('gbk', 'ignore')
        # myPrint(page_data)
        # requests.session()
    except Exception:
        myPrint('error page:', page_num)

        return 'Empty'
    temp = page_data.split('"rateDetail":')
    if len(temp) > 1:
        page_data_dict = json.loads(temp[1])
        # myPrint(page_data_dict['rateList'])
        rate_list = page_data_dict['rateList']
        pageinator = page_data_dict['paginator']['lastPage']

        comments = []
        for comment_info in rate_list:
            comment_info['product_id'] = item_id
            comment_info['product_title'] = title
            comment_info['category'] = category
            comment_id = comment_info['id']
            comment_info['comment_id'] = comment_id
            comment_info.pop('id')

            content = comment_info['rateContent']
            comment_info['content'] = content
            comment_info.pop('rateContent')

            comment_info['store_id'] = 2
            comment_info['brand_id'] = product_dic['brand_id']
            comment_info['category_id'] = product_dic['category_id']
            comment_info['shop_type'] = product_dic['shop_type']

            score = comment_info['tamllSweetLevel']
            comment_info['score'] = score
            comment_info.pop('tamllSweetLevel')

            insert_result = insertToMongo(commentID_list, comments_collection, comment_info, indexCollection)
            comments.append(insert_result)
        time.sleep(3)

        return comments
    else:
        time.sleep(5)
        response = requests.request(method='GET', url=page_url, headers=headers)
        try:
            page_data = response.content.decode('gbk', 'ignore')
            # myPrint(page_data)
            # requests.session()
        except Exception:
            myPrint('error page:', page_num)
            return 'Empty'
        temp = page_data.split('"rateDetail":')
        if len(temp) > 1:
            page_data_dict = json.loads(temp[1])
            # myPrint(page_data_dict['rateList'])
            rate_list = page_data_dict['rateList']
            pageinator = page_data_dict['paginator']['lastPage']

            comments = []
            for comment_info in rate_list:
                comment_info['product_id'] = item_id
                comment_info['product_title'] = title
                comment_info['category'] = category
                comment_id = comment_info['id']
                comment_info['comment_id'] = comment_id
                comment_info.pop('id')

                content = comment_info['rateContent']
                comment_info['content'] = content
                comment_info.pop('rateContent')

                comment_info['store_id'] = 2
                comment_info['brand_id'] = product_dic['brand_id']
                comment_info['category_id'] = product_dic['category_id']
                comment_info['shop_type'] = product_dic['shop_type']

                score = comment_info['tamllSweetLevel']
                comment_info['score'] = score
                comment_info.pop('tamllSweetLevel')
                # comment_info['spider_start_date'] =spider_start_date
                insert_result = insertToMongo(commentID_list, comments_collection, comment_info, indexCollection)
                comments.append(insert_result)
            time.sleep(3)

            return comments
        else:
            myPrint('error page', page_num)

            myPrint('page_num =', page_num)
            log_dict = {'type': '跳出', 'product_index': product_index, 'current_page': page_num, 'log_time': time.time()}
            log_collection.insert(log_dict)
            # os.system('say "attention please,  your program has Exception  "')

            return 'Empty'


from TimeClass.timeClass import *


def insertToMongo(commentID_list, comments_collection, oneDict, indexCollection):
    if oneDict['comment_id'] not in commentID_list:
        # 该评论不存在 执行插入
        timeStr = oneDict['rateDate']  # 时间转换
        oneDict['created_at'] = convertTimeStringToDateTime(timeStr)
        res = comments_collection.insert(oneDict)
        # 更新comment ID列表
        commentID_list.append(oneDict['comment_id'])
        updateCommentID_list(oneDict['product_id'], commentID_list, indexCollection)
        # myPrint(res)
        return 0
    else:
        # myPrint('已存在')
        return 1


''''frame 转字典
'''''


def convertDataframeToDict(df):
    dict_list = []
    for i in range(len(df)):
        series_row = df.iloc[i]  # 返回第i行数据
        # myPrint(series_row)
        oneDict = dict(zip(series_row.index, series_row.values))
        # myPrint(oneDict)
        dict_list.append(oneDict)
    return dict_list


from Config.config import *
from MongoRelated.mongoConnection import *


def getDataDataFrameFromMongo(db, collection, query):
    frame = read_mongo(db, collection, query)
    # myPrint('data scales',len(frame))
    # print(frame)
    return frame  # [:2000]


import sys


def get_commentID_list(item_id, indexCollection):
    cursors = indexCollection.find({'productID': item_id})
    res = list(cursors)
    if len(res) != 0:
        commentID_list = res[0]['commentID_list']
        cursors.close()
    else:
        commentID_list = []

    return commentID_list


def updateCommentID_list(item_id, commentID_list, indexCollection):
    cursor = indexCollection.find({'productID': item_id})
    if len(list(cursor)) != 0:
        indexCollection.update({'productID': item_id}, {'$set': {'commentID_list': commentID_list}})
    else:
        indexCollection.insert({'productID': item_id, 'commentID_list': commentID_list})
    cursor.close()


def main(log_collection_name, product_index, page_nummber, category_collection_name, target_collexction_name,
         maxPage_num_control, db):
    Test = False
    if (not Test):
        # if len(sys.argv)>2:
        # log_collection_name =sys.argv[1]
        # product_index =int(sys.argv[2])
        # startNum =int(sys.argv[3])
        # category_collection_name =sys.argv[4]
        # target_collexction_name =sys.argv[5]
        # maxPage_num_control =int(sys.argv[6])
        log_collection_name = log_collection_name
        product_index = product_index
        startNum = page_nummber
        category_collection_name = category_collection_name
        target_collexction_name = target_collexction_name
        maxPage_num_control = maxPage_num_control

    log_collection = db[log_collection_name]

    comments_collection = db[target_collexction_name]  # collection

    # 索引集合，用来判重，每个product_id对应一个document ，其中有一个field 是commentID列表
    indexCollection = db['s_index_' + target_collexction_name.replace('s_', '')]

    # 产品集合
    product_collection = db[target_collexction_name.replace('_comments', '')]

    df = getDataDataFrameFromMongo(db, category_collection_name, {'status': {"$in": [0, 1]}})
    df['shop_id'] = df['shop_id'].astype('str')
    df['original_id'] = df['original_id'].astype('str')
    df['name'] = df['name'].astype('str')
    df['category'] = df['category'].astype('str')
    # df['store_type'] = df['store_type'].astype('str')
    # df['spider_start_date'] = df['spider_start_date'].astype('str')

    sellID_list = df['shop_id'].values
    itemID_list = df['original_id'].values
    ptitle_list = df['name'].values
    category_list = df['category'].values
    # store_type_list = df['store_type'].values
    # spider_start_date_list = df['spider_start_date'].values


    target_dict = {}
    # 若索超范围，则从头开始
    try:

        target_dict['shop_id'] = str(sellID_list[product_index])
        target_dict['original_id'] = str(itemID_list[product_index])
        target_dict['name'] = str(ptitle_list[product_index])
        target_dict['category'] = str(category_list[product_index])
    # target_dict['store_type'] = str(store_type_list[product_index])
    # target_dict['spider_start_date'] = str(spider_start_date_list[product_index])
    except IndexError:
        log_dict = {'type': '爬取完毕', 'product_index': product_index, 'current_page': 99, 'log_time': time.time()}
        log_collection.insert(log_dict)
        raise
    commentID_list = get_commentID_list(target_dict['original_id'], indexCollection)
    get_Tmall_comment(product_collection, commentID_list, target_dict, comments_collection, product_index, startNum, maxPage_num_control,
                      log_collection, indexCollection)

    for i in range(product_index + 1, len(df)):  # 73   573     #1073    1577

        target_dict = {}
        target_dict['shop_id'] = str(sellID_list[i])
        target_dict['original_id'] = str(itemID_list[i])
        target_dict['name'] = str(ptitle_list[i])
        target_dict['category'] = str(category_list[i])
        # target_dict['store_type'] = str(store_type_list[i])
        # target_dict['spider_start_date'] = str(spider_start_date_list[i])

        startNum = 1

        commentID_list = get_commentID_list(target_dict['original_id'], indexCollection)
        get_Tmall_comment(product_collection, commentID_list, target_dict, comments_collection, i, startNum, maxPage_num_control, log_collection,
                          indexCollection)
        # 若正常爬取完成 执行更新comment ID列表
        if i == (len(df) - 1):
            log_dict = {'type': '爬取完毕', 'product_index': i, 'current_page': 99, 'log_time': time.time()}
            log_collection.insert(log_dict)
            raise
