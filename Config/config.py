isLocal = True

# mysql配置
mysql_host = 'localhost'
mysql_username = 'root'
mysql_password = 'lidazhuang'
mysql_db = 'power_monitor'

# 阿里云MySQL
ALIYUN_MYSQL_HOST = 'm-bp13a2a5c1a055b4.petadata.rds.aliyuncs.com'
ALIYUN_MYSQL_PORT = 3306
ALIYUN_MYSQL_DB = 'power_monitor'
ALIYUN_MYSQL_USERNAME = 'pmu_e6yaud'
ALIYUN_MYSQL_PASSWORD = 'gdueyagcdmb'

#mongodb 配置

mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_username = None
mongodb_password = None
mongodb_db = 'power'
# dadad


#阿里云两地址
# 节点1，2 副本集名称
ALIYUN_MONGO_CONN_ADDR1 = 'dds-bp177c8d0d4743d41.mongodb.rds.aliyuncs.com:3717'
ALIYUN_MONGO_CONN_ADDR2 = 'dds-bp177c8d0d4743d42.mongodb.rds.aliyuncs.com:3717'
ALIYUN_MONGO_REPLICAT_SET = 'mgset-4586483'
ALIYUN_USERNAME = 'power_mongo_user'
ALIYUN_PASSWORD = 'Kduqudb18bmBca5'
ALIYUN_DB = 'power'
ALIYUN_HOST = '118.31.116.157'
ALIYUN_PORT = 3717

# 打印日志信息
config = {
        'log_file_name_tmall_xy': 'tmall_xy.log',
        'log_file_name_tmall_xf': 'tmall_xf.log',
        'log_file_name_tmall_hf': 'tmall_hf.log',
        'log_file_name_tmall_mz': 'tmall_mz.log',
        'log_file_name_tmall_my': 'tmall_my.log',
        'log_file_name_tmall_kqhl': 'tmall_kqhl.log',
        'log_file_name_tmall_jydq': 'tmall_jydq.log',
        'log_level': 'info'     # support debug,info, warn
          }

# collection_name_list :
CAT_LIST_XY = [
        '1#845024329602482176#2',
        '1#845024361722458112#2',
        '1#845024420715352064#2',
        '1#845024389304213504#2',
        '1#845024448691351552#2',
        '1#864290600999235584#2'
               ]
COLLECTION_NAME_LIST_XY = [
        's_TM_XY_洗衣液',
        's_TM_XY_洗衣粉',
        's_TM_XY_洗衣皂',
        's_TM_XY_洗衣片',
        's_TM_XY_洗衣凝珠',
        's_TM_XY_衣物护理柔顺剂液'
]
COLLECTION_NAME_LIST_XF = [
        's_TM_XF_洗发水',
        's_TM_XF_护发素乳',
        's_TM_XF_洗护套装',
        's_TM_XF_精华乳油',
        's_TM_XF_发膜',
        's_TM_XF_营养水'
]
COLLECTION_NAME_LIST_HF = [
        's_TM_HF_脸部清洁_洁面皂',
        's_TM_HF_脸部清洁_洁面霜膏',
        's_TM_HF_脸部清洁_其他',
        's_TM_HF_脸部清洁_洁肤啫喱',
        's_TM_HF_脸部清洁_洁面粉',
        's_TM_HF_脸部清洁_洁面泡沫摩丝',
        's_TM_HF_脸部清洁_洁面乳',
        's_TM_HF_面膜_贴片式',
        's_TM_HF_面膜_水洗式',
        's_TM_HF_面膜_撕拉式',
        's_TM_HF_面膜_睡眠免洗式',
        's_TM_HF_水_爽肤水',
        's_TM_HF_脸部精华',
        's_TM_HF_脸部润肤_啫喱凝露',
        's_TM_HF_脸部润肤_乳液面霜',
        's_TM_HF_防晒晒后护理_防晒喷雾',
        's_TM_HF_防晒晒后护理_防晒霜乳液',
        's_TM_HF_防晒晒后护理_防晒啫喱露',
        's_TM_HF_防晒晒后护理_晒后修护',
        's_TM_HF_脸部卸妆_其他',
        's_TM_HF_脸部卸妆_水油分离型卸妆液',
        's_TM_HF_脸部卸妆_卸妆乳',
        's_TM_HF_脸部卸妆_卸妆湿巾',
        's_TM_HF_脸部卸妆_卸妆水液',
        's_TM_HF_脸部卸妆_卸妆油',
        's_TM_HF_脸部卸妆_卸妆啫喱',
        's_TM_HF_身体护理_身体乳霜',
        's_TM_HF_身体清洁_沐浴露液',
        's_TM_HF_身体清洁_香皂',
        's_TM_HF_眼部润肤_眼部精华',
        's_TM_HF_眼部润肤_眼膜',
        's_TM_HF_眼部润肤_眼霜',
        's_TM_HF_身体清洁_搓泥浴宝',
        's_TM_HF_身体清洁_磨砂浴盐',
        's_TM_HF_身体清洁_沐浴啫喱',
        's_TM_HF_身体护理_润肤水喷雾',
        's_TM_HF_身体护理_精油',
        's_TM_HF_身体护理_抑汗香氛',
        's_TM_HF_身体护理_其他'
]
COLLECTION_NAME_LIST_MZ = [
        's_TM_MZ_底妆_粉饼',
        's_TM_MZ_底妆_BB霜CC霜',
        's_TM_MZ_底妆_粉底液膏霜',
        's_TM_MZ_唇妆_唇笔唇线笔',
        's_TM_MZ_唇妆_唇彩唇蜜',
        's_TM_MZ_唇妆_唇膏口红',
        's_TM_MZ_底妆_隔离霜妆前乳',
        's_TM_MZ_眼妆_眉笔',
        's_TM_MZ_眼妆_睫毛膏',
        's_TM_MZ_唇妆_润唇膏啫喱',
        's_TM_MZ_唇妆_唇膜',
        's_TM_MZ_眼妆_眼线',
        's_TM_MZ_眼妆_眼影',
        's_TM_MZ_底妆_遮瑕膏笔',
        's_TM_MZ_底妆_修容高光阴影粉'
]
COLLECTION_NAME_LIST_MY = [
        's_TM_MY_婴幼奶粉',
        's_TM_MY_尿裤湿巾_婴儿尿裤',
        's_TM_MY_尿裤湿巾_婴儿尿片',
        's_TM_MY_尿裤湿巾_拉拉裤成长裤',
        's_TM_MY_尿裤湿巾_婴儿湿巾'
]
COLLECTION_NAME_LIST_JYDQ = [
        's_TM_JYDQ_生活电器_空气净化器',
        's_TM_JYDQ_洗衣机_滚筒洗衣机',
        's_TM_JYDQ_洗衣机_波轮洗衣机',
        's_TM_JYDQ_洗衣机_迷你洗衣机',
        's_TM_JYDQ_洗衣机_双缸洗衣机'
]
COLLECTION_NAME_LIST_KQHL = [
        's_TM_KQHL_牙膏牙粉_牙膏'
]