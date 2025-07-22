create table address
(
    id          int auto_increment
        primary key,
    name        varchar(30)  not null comment '收获人姓名',
    mobile      varchar(20)  not null comment '手机号',
    province    varchar(20)  null comment '省',
    city        varchar(20)  null comment '市',
    country     varchar(20)  null comment '区',
    detail      varchar(100) null comment '详细地址',
    user_id     int          not null comment '外键',
    create_time int          null comment '创建时间',
    update_time int          null comment '更新时间',
    delete_time int          null comment '删除时间',
    constraint user_id
        unique (user_id)
);

INSERT INTO zerd.address (id, name, mobile, province, city, country, detail, user_id, create_time, update_time, delete_time) VALUES (1, '巴拿巴', '13799999999', '浙江', '杭州', '滨江', '塞浦路斯9栋7单元101室', 1, null, null, null);
INSERT INTO zerd.address (id, name, mobile, province, city, country, detail, user_id, create_time, update_time, delete_time) VALUES (2, '扫罗', '13788888888', '浙江', '杭州', '萧山', '大马士革7栋1单元701室', 3, null, null, null);
create table article
(
    id          int auto_increment
        primary key,
    author_id   int          not null comment '外键，用户id',
    type        smallint     null comment '文章类型',
    title       varchar(255) null comment '文章标题',
    summary     text         null comment '文章摘要',
    content     text         null comment '文章内容',
    theme       smallint     null comment '文章主题',
    img         varchar(255) null comment '主图路径',
    views       int          null comment '浏览量',
    create_time int          null comment '创建时间',
    update_time int          null comment '更新时间',
    delete_time int          null comment '删除时间',
    constraint article_ibfk_1
        foreign key (author_id) references user (id)
);

create index author_id
    on article (author_id);

INSERT INTO zerd.article (id, author_id, type, title, summary, content, theme, img, views, create_time, update_time, delete_time) VALUES (1, 1, 1, '***', '***', '***', null, null, 8, 1590480321, 1592639188, 1592639188);
INSERT INTO zerd.article (id, author_id, type, title, summary, content, theme, img, views, create_time, update_time, delete_time) VALUES (2, 1, 1, '物耀安全工控安全大数据存储平台', 'AiLPHA大数据智能安全平台能够提供基于大数据技术的多源...', 'AiLPHA大数据智能安全平台能够提供基于大数据技术的多源异构数据收集服务能力，依托于分布式复杂事件处理引擎进行安全建模分析与运营框架编排，实现安全事件攻击溯源与威胁回放并剔除误报，提升安全运维效率。', null, null, 10, 1590483315, 1593587208, null);
INSERT INTO zerd.article (id, author_id, type, title, summary, content, theme, img, views, create_time, update_time, delete_time) VALUES (3, 1, 1, '大数据智能安全解决方案', null, '依托大数据态势感知与智能防控国家地方联合工程研究中心，开展网络安 全、大数据与人工智能的交叉领域的前沿研究与落地。', null, null, 1, 1590483277, 1590483323, null);
INSERT INTO zerd.article (id, author_id, type, title, summary, content, theme, img, views, create_time, update_time, delete_time) VALUES (4, 1, 1, '物耀安全工控安全大数据存储平台研发', 'AiLPHA大数据智能安全平台能够提供基于大数据技术的多源异构数据收集服务能力，依托于分布式复杂事件处理引擎进行安全建模...', 'AiLPHA大数据智能安全平台能够提供基于大数据技术的多源异构数据收集服务能力，依托于分布式复杂事件处理引擎进行安全建模分析与运营框架编排，实现安全事件攻击溯源与威胁回放并剔除误报，提升安全运维效率。', null, null, 4, 1590483439, 1592645411, null);
INSERT INTO zerd.article (id, author_id, type, title, summary, content, theme, img, views, create_time, update_time, delete_time) VALUES (5, 1, 1, '物耀安全工控安全大', '大数据智能安全解决方案', '<h2>大数据智能安全解决方案</h2>
<p>AiLPHA大数据智能安全平台能够提供基于大数据技术的多源异构数据收集服务能力，依托于分布式复杂事件处理引擎进行安全建模分析与运营框架编排，实现安全事件攻击溯源与威胁回放并剔除误报，提升安全运维效率。</p>
<h3>核心功能 FEATURES</h3>
<p><img src="https://www.dbappsecurity.com.cn/uploadfile/2019/06/05/20190605173643gwLZk0.jpg" width="741" height="347" /></p>
<h3>平台优势 ADVANTAGE</h3>
<h4>占据行业制高点</h4>
<p>应用于国家部委、大型央企、省级公安、电信运营商、金融等众多客户(已 服务100+客户)，提供全面智能安全解决方案。</p>
<h4>智能分析引擎</h4>
<p>推出大数据智能复杂安全事件关联分析系统，支持智能安全建模和自动化编 排。从而实现精准告警、未知及高级威胁的检测以及追踪溯源。</p>
<h4>国家地方联合工程研究中心</h4>
<p>依托大数据态势感知与智能防控国家地方联合工程研究中心，开展网络安 全、大数据与人工智能的交叉领域的前沿研究与落地。</p>
<h4>市场份额排名第一</h4>
<p>&ldquo;凭借在网络安全大数据与人工智能等前沿技术领域的产品化转速度，日志审计 产品市场份额排名第一&rdquo; &mdash;&mdash;引自赛迪顾问研究报告</p>
<h4>开放兼容 灵活部署</h4>
<p>致力于为全面大、中、小型政企客户提供基于大数据分析的智能安全解决方案。</p>
<h4>重大活动安保应用实战</h4>
<p>为2016中国杭州G20峰会;连续五届世界互联网大会;2017金砖峰会; 2018青岛上合峰会、上海进博会等提供重要安保技术支撑。</p>
<p>。</p>', null, null, 13, 1590484135, 1592449857, null);
create table auth
(
    id       int(10) auto_increment
        primary key,
    group_id int(10)     not null comment '所属权限组id',
    name     varchar(60) null comment '权限字段',
    module   varchar(50) null comment '权限的模块'
)
    comment '权限';

INSERT INTO zerd.auth (id, group_id, name, module) VALUES (1, 1, '查询用户列表', '用户');
INSERT INTO zerd.auth (id, group_id, name, module) VALUES (2, 1, '更改用户密码', '用户');
INSERT INTO zerd.auth (id, group_id, name, module) VALUES (3, 1, '新增类别', '类别');
create table banner
(
    id          int(10) auto_increment
        primary key,
    name        varchar(50)  null comment 'Banner名称，通常作为标识',
    description varchar(255) null comment 'Banner描述',
    create_time int          null,
    update_time int          null,
    delete_time int          null
)
    comment 'banner管理';

INSERT INTO zerd.banner (id, name, description, create_time, update_time, delete_time) VALUES (1, '首页置顶', '首页轮播图', 1528938338, null, null);
create table banner_item
(
    id          int auto_increment
        primary key,
    banner_id   int          null comment '外键，所属Banner组id',
    img_id      int          null comment '外键，关联image表',
    key_word    varchar(100) null comment '执行关键字，根据不同的type含义不同',
    type        smallint     null comment '跳转类型，可能导向商品，可能导向专题，可能导向其他。0，无导向；1：导向商品;2:导向专题',
    create_time int          null comment '创建时间',
    update_time int          null comment '更新时间',
    delete_time int          null comment '删除时间',
    constraint banner_item_ibfk_1
        foreign key (banner_id) references banner (id),
    constraint banner_item_ibfk_2
        foreign key (img_id) references image (id)
);

create index banner_id
    on banner_item (banner_id);

create index img_id
    on banner_item (img_id);

INSERT INTO zerd.banner_item (id, banner_id, img_id, key_word, type, create_time, update_time, delete_time) VALUES (1, 1, 65, '6', 1, 1528938338, null, null);
INSERT INTO zerd.banner_item (id, banner_id, img_id, key_word, type, create_time, update_time, delete_time) VALUES (2, 1, 2, '25', 1, 1528938338, null, null);
INSERT INTO zerd.banner_item (id, banner_id, img_id, key_word, type, create_time, update_time, delete_time) VALUES (3, 1, 3, '11', 1, 1528938338, null, null);
INSERT INTO zerd.banner_item (id, banner_id, img_id, key_word, type, create_time, update_time, delete_time) VALUES (4, 1, 1, '10', 1, 1528938338, null, null);
create table category
(
    id           int auto_increment
        primary key,
    name         varchar(50)  not null comment '分类名称',
    topic_img_id int          null comment '外键，关联image表',
    description  varchar(100) null comment '描述',
    create_time  int          null comment '创建时间',
    update_time  int          null comment '更新时间',
    delete_time  int          null comment '删除时间'
)
    comment '商品类目';

INSERT INTO zerd.category (id, name, topic_img_id, description, create_time, update_time, delete_time) VALUES (2, '果味', 6, null, null, null, null);
INSERT INTO zerd.category (id, name, topic_img_id, description, create_time, update_time, delete_time) VALUES (3, '蔬菜', 5, null, null, null, null);
INSERT INTO zerd.category (id, name, topic_img_id, description, create_time, update_time, delete_time) VALUES (4, '炒货', 7, null, null, null, null);
INSERT INTO zerd.category (id, name, topic_img_id, description, create_time, update_time, delete_time) VALUES (5, '点心', 4, null, null, null, null);
INSERT INTO zerd.category (id, name, topic_img_id, description, create_time, update_time, delete_time) VALUES (6, '粗茶', 8, null, null, null, null);
INSERT INTO zerd.category (id, name, topic_img_id, description, create_time, update_time, delete_time) VALUES (7, '淡饭', 9, null, null, null, null);
create table config
(
    id     int auto_increment
        primary key,
    name   varchar(64) null comment '名称',
    `key`  varchar(64) null comment '键名',
    value  varchar(64) null comment '键值',
    type   tinyint(1)  null comment '是否系统内置(True是, False否)',
    remark text        null comment '备注'
);

INSERT INTO zerd.config (id, name, `key`, value, type, remark) VALUES (1, '用户管理-账号初始密码', 'sys.user.init_password', '123456', 1, '用户初始化密码: 123456');
INSERT INTO zerd.config (id, name, `key`, value, type, remark) VALUES (2, '页面框架-布局主题', 'sys.layout.theme', 'vertical', 1, '左右布局default，上下布局vertical，T型布局t-type');
INSERT INTO zerd.config (id, name, `key`, value, type, remark) VALUES (3, '分页查询-默认页', 'sys.paginator.page', '1', 1, '默认查询第1页');
INSERT INTO zerd.config (id, name, `key`, value, type, remark) VALUES (4, '分页查询-默认数量', 'sys.paginator.size', '10', 1, '默认每页10条数据');
create table dict
(
    id         int auto_increment
        primary key,
    `order`    int         not null comment '字典排序',
    label      varchar(64) null comment '字典标签',
    value      varchar(64) null comment '字典键值',
    type       varchar(64) null comment '字典类型',
    css_class  varchar(64) null comment '样式属性（其他样式扩展）',
    list_class varchar(64) null comment '表格回显样式',
    is_default tinyint(1)  null comment '是否默认(True是, False否)',
    status     tinyint(1)  null comment '状态(True正常, False停用)',
    remark     text        null comment '备注'
);

INSERT INTO zerd.dict (id, `order`, label, value, type, css_class, list_class, is_default, status, remark) VALUES (1, 1, '男', '0', 'sys_user_sex', null, null, 1, 1, '性别: 男');
INSERT INTO zerd.dict (id, `order`, label, value, type, css_class, list_class, is_default, status, remark) VALUES (2, 2, '女', '1', 'sys_user_sex', null, null, 0, 1, '性别: 女');
INSERT INTO zerd.dict (id, `order`, label, value, type, css_class, list_class, is_default, status, remark) VALUES (4, 1, '显示', '0', 'sys_show_hide', null, 'primary', 1, 1, '显示菜单');
INSERT INTO zerd.dict (id, `order`, label, value, type, css_class, list_class, is_default, status, remark) VALUES (5, 2, '隐藏', '1', 'sys_show_hide', null, 'danger', 0, 1, '隐藏菜单');
create table dict_type
(
    id     int auto_increment
        primary key,
    name   varchar(64) null comment '字典名称',
    type   varchar(64) null comment '字典类型',
    status tinyint(1)  null comment '状态(True正常, False停用)',
    remark text        null comment '备注'
);

INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (1, '用户性别', 'sys_user_sex', 1, '用户性别列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (2, '菜单状态', 'sys_show_hide', 1, '菜单状态列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (3, '系统开关', 'sys_normal_disable', 1, '系统开关列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (4, '任务状态', 'sys_job_status', 1, '任务状态列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (5, '任务分组', 'sys_job_group', 1, '任务分组列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (6, '系统是否', 'sys_yes_no', 1, '系统是否列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (7, '通知类型', 'sys_notice_type', 1, '通知类型列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (8, '通知状态', 'sys_notice_status', 1, '通知状态列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (9, '操作类型', 'sys_oper_type', 1, '操作类型列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (10, '系统状态', 'sys_common_status', 1, '登录状态列表');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (13, '用户性别1', 'sys_user_sex1', 1, '');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (14, '用户性别1', 'sys_user_sex1', 1, '');
INSERT INTO zerd.dict_type (id, name, type, status, remark) VALUES (16, '测试1', 'test', 0, '');
create table element
(
    id       int auto_increment,
    name     varchar(50) null comment '名称',
    sign     varchar(50) null comment '元素标识',
    route_id int         not null,
    primary key (id, route_id),
    constraint element_ibfk_1
        foreign key (route_id) references route (id)
);

create index route_id
    on element (route_id);


create table file
(
    create_time int          null comment '创建时间',
    update_time int          null comment '更新时间',
    delete_time int          null comment '删除时间',
    id          int auto_increment
        primary key,
    parent_id   int          null comment '父级目录id',
    uuid_name   varchar(100) null comment '唯一名称',
    name        varchar(100) not null comment '原始名称',
    path        varchar(500) null comment '路径',
    extension   varchar(50)  null comment '后缀',
    `from`      smallint     null comment '来源: 1 本地，2 公网',
    size        int          null comment '大小',
    md5         varchar(40)  null comment '文件md5值，防止上传重复文件'
);

INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1589786103, 1590398617, null, 1, 0, null, '321', null, null, 1, null, null);
INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1589786103, null, null, 2, 0, null, '图片文件', null, null, 1, null, null);
INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1589786103, 1590386642, null, 3, 0, null, 'pdf文件', null, null, 1, null, null);
INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1589786103, null, null, 5, 2, 'aebdff3a-7bb5-11ea-8007-acbc32924b6f.png', 'virtualmachine2.png', '2020/04/11/aebdff3a-7bb5-11ea-8007-acbc32924b6f.png', 'png', 1, null, null);
INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1590112814, null, null, 8, 1, 'f992de74-9bcf-11ea-97a6-acbc32924b6fpng', 'logo-01.png', '2020/05/22/f992de74-9bcf-11ea-97a6-acbc32924b6fpng', 'png', 1, 39272, '61b2160c5fc09e373a25ca5fa9e95e38');
INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1590398385, 1590398395, null, 13, 0, null, '新建文件夹12', null, null, 1, null, null);
INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1590459173, null, null, 15, 1, null, '新建文件夹', null, null, 1, null, null);
INSERT INTO zerd.file (create_time, update_time, delete_time, id, parent_id, uuid_name, name, path, extension, `from`, size, md5) VALUES (1593586591, null, null, 16, 68, 'fe7d066e-bb67-11ea-86bf-acbc32924b6f.png', '我的.png', '2020/07/01/fe7d066e-bb67-11ea-86bf-acbc32924b6f.png', '.png', 1, 805, 'e8e3153cb3f57175a434ef50bc8b541f');
create table `group`
(
    id   int auto_increment
        primary key,
    name varchar(60)  null comment '权限组名称',
    info varchar(255) null comment '权限组描述'
);

INSERT INTO zerd.`group` (id, name, info) VALUES (1, '系统管理员', '行使超级管理员的相同权限，但不能新增同级的系统管理员');
INSERT INTO zerd.`group` (id, name, info) VALUES (2, '运维管理员', '管理商品上架、下架');
INSERT INTO zerd.`group` (id, name, info) VALUES (3, '物流管理员', '负责订单的发货情况');
INSERT INTO zerd.`group` (id, name, info) VALUES (4, '活动策划员', '策划线上营销活动');
INSERT INTO zerd.`group` (id, name, info) VALUES (6, '测试1', '测试分组');
create table group_2_element
(
    group_id   int not null,
    element_id int not null,
    primary key (group_id, element_id),
    constraint group_2_element_ibfk_1
        foreign key (group_id) references `group` (id),
    constraint group_2_element_ibfk_2
        foreign key (element_id) references element (id)
);

create index element_id
    on group_2_element (element_id);


create table group_element
(
    group_id   int not null,
    element_id int not null,
    primary key (group_id, element_id),
    constraint group_element_ibfk_1
        foreign key (group_id) references `group` (id),
    constraint group_element_ibfk_2
        foreign key (element_id) references element (id)
);

create index element_id
    on group_element (element_id);


create table identity
(
    id          int auto_increment
        primary key,
    user_id     int          not null comment '外键，用户id',
    type        int          not null comment '登录类型',
    identifier  varchar(100) null comment '标识(手机号、邮箱、用户名或第三方应用的唯一标识)',
    credential  varchar(100) null comment '密码凭证(站内的保存密码，站外的不保存或保存token)',
    verified    smallint     null comment '是否已经验证',
    create_time int          null comment '创建时间',
    update_time int          null comment '更新时间',
    delete_time int          null comment '删除时间',
    constraint identifier
        unique (identifier),
    constraint identity_ibfk_1
        foreign key (user_id) references user (id)
);

create index user_id
    on identity (user_id);

INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (1, 3, 101, '666@qq.com', 'pbkdf2:sha256:150000$Oh2TxEHw$e497614a0209566491df406275aca2a15ea45c42c4c5132526c323bbfd530fab', 1, 1586767003, 1587019825, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (2, 3, 200, 'oYf_s0OnCim9Cx7tCV-AHs_rDWXs', null, 1, 1586767003, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (3, 1, 101, '999@qq.com', 'pbkdf2:sha256:150000$0YA1wZOx$028783c07999fd6ed8050c2f831857ac602218bcbc2399072f7f50064a30109e', 1, 1586767003, 1592288770, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (4, 3, 100, 'Allen7D', 'pbkdf2:sha256:150000$dlyAHfD8$691ba12bf1e0183f90f70c489ebb89a93040dbc90a733363871453919e476f6d', 1, 1586767003, 1587019825, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (5, 3, 102, '13758787058', 'pbkdf2:sha256:150000$SQwNb0bE$24f9d9ee1372bdf298f7fe70d41f4fb848991049491cd82aff2e9dd7cecba5da', 1, 1586767003, 1587102577, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (7, 2, 101, '777@qq.com', 'pbkdf2:sha256:50000$YrYmLzfp$981a20fc95c1dfc423866be176c0a66b728a95f9c285d6b731af05349112d2f9', 1, 1586767003, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (8, 27, 100, 'Allen2D', 'pbkdf2:sha256:150000$MVGqTbkT$e48eebef1b43782f262c72b9043b706ff27580619e45dae15437c7f9a51cf280', 0, 1587024948, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (9, 27, 102, '13755555555', 'pbkdf2:sha256:150000$sZdQl4R0$fe697627c25a0407b438a304268ff9a681876772482edfdfb3258a863c4b1151', 0, 1587024948, 1587029097, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (10, 27, 101, '555@qq.com', 'pbkdf2:sha256:150000$Jojx9DNW$1307d58aabc221e8a0d098e48877eb00256ff07dbeec439ce38d30b47d82e6cc', 0, 1587024956, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (14, 30, 100, 'Allen3D', 'pbkdf2:sha256:150000$vHwJolCh$a77780e06b034058a5b0ac2263dd965b9539916464e80ad747bd51a3c5465c73', 1, 1587043791, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (15, 30, 102, '13758787053', 'pbkdf2:sha256:150000$fJpShyPb$e2fe9caae9780a81bc351cc4d289c6be9a2be4b6176dc7ad012b58867580da1a', 0, 1587043792, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (18, 1, 102, '13758787011', 'pbkdf2:sha256:150000$RtZqKtDN$fd2cb930047b2e934a1c65198ab213f79d3fef99f5670e9344e133eee7956e69', 0, 1588134197, 1592288770, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (19, 31, 100, 'Allen1D', 'pbkdf2:sha256:150000$vV7OHnCT$dbb29421d70d1d831c1bd12106ce95c026c143772b45a598f4f0ecc732070c69', 1, 1588134674, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (20, 31, 102, '13758787111', 'pbkdf2:sha256:150000$MIOWaCVV$3ac3e942c60dfa1ecf10bc5b102c396edadf79900b54b457e71709e50147ff33', 0, 1588134675, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (21, 31, 101, '111@qq.com', 'pbkdf2:sha256:150000$9AM9MtIo$487496f19fefe828b62e5297f42165637334e14fade766a36cf95e19cd13f3d8', 0, 1588134675, null, null);
INSERT INTO zerd.identity (id, user_id, type, identifier, credential, verified, create_time, update_time, delete_time) VALUES (24, 1, 100, 'Boss', 'pbkdf2:sha256:150000$pFccHtr1$3d6a5dd99315504c63033347c476ff67d0905b8cc77591616ea75ae89099b366', 0, 1588140875, 1592288770, null);
create table image
(
    id          int auto_increment
        primary key,
    url         varchar(255)      not null comment '图片路径',
    `from`      tinyint default 1 not null comment '1 来自本地，2 来自公网',
    create_time int               null comment '创建时间',
    update_time int               null comment '更新时间',
    delete_time int               null comment '删除时间'
)
    comment '图片总表';

INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (1, '/banner-1a.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (2, '/banner-2a.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (3, '/banner-3a.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (4, '/category-cake.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (5, '/category-vg.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (6, '/category-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (7, '/category-fry-a.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (8, '/category-tea.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (9, '/category-rice.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (10, '/product-dryfruit@1.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (13, '/product-vg@1.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (14, '/product-rice@6.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (16, '/1@theme.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (17, '/2@theme.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (18, '/3@theme.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (19, '/detail-1@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (20, '/detail-2@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (21, '/detail-3@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (22, '/detail-4@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (23, '/detail-5@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (24, '/detail-6@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (25, '/detail-7@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (26, '/detail-8@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (27, '/detail-9@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (28, '/detail-11@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (29, '/detail-10@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (31, '/product-rice@1.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (32, '/product-tea@1.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (33, '/product-dryfruit@2.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (36, '/product-dryfruit@3.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (37, '/product-dryfruit@4.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (38, '/product-dryfruit@5.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (39, '/product-dryfruit-a@6.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (40, '/product-dryfruit@7.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (41, '/product-rice@2.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (42, '/product-rice@3.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (43, '/product-rice@4.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (44, '/product-fry@1.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (45, '/product-fry@2.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (46, '/product-fry@3.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (47, '/product-tea@2.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (48, '/product-tea@3.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (49, '/1@theme-head.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (50, '/2@theme-head.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (51, '/3@theme-head.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (52, '/product-cake@1.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (53, '/product-cake@2.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (54, '/product-cake-a@3.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (55, '/product-cake-a@4.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (56, '/product-dryfruit@8.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (57, '/product-fry@4.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (58, '/product-fry@5.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (59, '/product-rice@5.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (60, '/product-rice@7.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (62, '/detail-12@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (63, '/detail-13@1-dryfruit.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (65, '/banner-4a.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (66, '/product-vg@4.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (67, '/product-vg@5.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (68, '/product-vg@2.png', 1, null, null, null);
INSERT INTO zerd.image (id, url, `from`, create_time, update_time, delete_time) VALUES (69, '/product-vg@3.png', 1, null, null, null);
create table login_log
(
    id          int auto_increment
        primary key,
    user_id     int          not null comment '用户id',
    user_name   varchar(50)  null comment '用户当时的昵称',
    ip_addr     varchar(50)  null comment '登录IP地址',
    location    varchar(255) null comment '登录地点',
    browser     varchar(50)  null comment '浏览器类型',
    os          varchar(50)  null comment '操作系统',
    message     varchar(255) null comment '提示消息',
    status      tinyint(1)   null comment '登录状态(True成功, False失败)',
    create_time int          null comment '访问时间'
);

INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (1, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '', 1, 1592230004);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (2, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '', 1, 1592230619);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (3, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '', 1, 1592231445);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (4, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '', 1, 1592231613);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (5, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '', 1, 1592231618);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (6, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '', 1, 1592231620);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (7, 3, 'Allen7D', '192.168.10.80', '内网IP', 'chrome', 'macos', '', 1, 1592272492);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (8, 3, 'Allen7D', '192.168.10.80', '内网IP', 'chrome', 'macos', '', 1, 1592273245);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (9, 3, 'Allen7D', '192.168.10.80', '内网IP', 'chrome', 'macos', '', 1, 1592273358);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (10, 3, 'Allen7D', '192.168.10.74', '内网IP', 'chrome', 'windows', '', 1, 1592273401);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (11, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '', 1, 1592273564);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (12, 3, 'Allen7D', '192.168.10.74', '内网IP', 'chrome', 'windows', '', 1, 1592273605);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (13, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592275354);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (14, 3, 'Allen7D', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592275592);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (15, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592289190);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (16, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592289200);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (17, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592289426);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (18, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592289589);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (19, 3, 'Allen7D', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592290309);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (20, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592290367);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (21, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592295023);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (22, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592295098);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (23, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592295258);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (24, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592377702);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (25, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592408328);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (26, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592442372);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (27, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592446398);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (28, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592446400);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (29, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592446564);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (30, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592446685);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (31, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592446914);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (32, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592446959);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (33, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592447150);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (34, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592447266);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (35, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592447270);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (36, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592447591);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (37, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592448529);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (38, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592449339);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (39, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592449490);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (40, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592456918);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (41, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457110);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (42, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457314);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (43, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457433);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (44, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457470);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (45, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457498);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (46, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457505);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (47, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457530);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (48, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457539);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (49, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457548);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (50, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457585);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (51, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457651);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (52, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592457654);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (53, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592458175);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (54, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592458198);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (55, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592458237);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (56, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592458350);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (57, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592458352);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (58, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592458355);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (59, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592458453);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (60, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592459710);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (61, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592461445);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (62, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592461726);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (63, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592461733);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (64, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592462383);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (65, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592462391);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (66, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592465345);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (67, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592465509);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (68, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592466956);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (69, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592467189);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (70, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592467488);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (71, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592467543);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (72, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592469118);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (73, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592472363);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (74, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592472461);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (75, 1, 'Boss', '192.168.10.55', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592472581);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (76, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592492589);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (77, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592492594);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (78, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592496350);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (79, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592496354);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (80, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592496358);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (81, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592496362);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (82, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592496831);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (83, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592496834);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (84, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592496854);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (85, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592497135);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (86, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592497147);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (87, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592497199);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (88, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592497648);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (89, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592498901);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (90, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592499975);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (91, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592500128);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (92, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592502048);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (93, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592502103);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (94, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592502201);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (95, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592502638);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (96, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592504253);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (97, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592504305);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (98, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592504311);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (99, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592504324);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (100, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592504853);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (101, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592506638);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (102, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592506731);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (103, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592507621);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (104, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592507656);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (105, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534517);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (106, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534517);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (107, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534571);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (108, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534653);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (109, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534669);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (110, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534741);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (111, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534763);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (112, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592534958);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (113, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592534972);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (114, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535508);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (115, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535712);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (116, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535724);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (117, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535760);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (118, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535823);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (119, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535827);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (120, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535830);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (121, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535937);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (122, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592535973);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (123, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536026);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (124, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536096);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (125, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536109);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (126, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536194);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (127, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536252);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (128, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536302);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (129, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536335);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (130, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536365);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (131, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536406);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (132, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536443);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (133, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536469);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (134, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536531);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (135, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536554);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (136, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536564);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (137, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536573);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (138, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536627);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (139, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536640);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (140, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536647);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (141, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536660);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (142, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536714);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (143, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592536975);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (144, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592537111);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (145, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592537165);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (146, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538017);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (147, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538180);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (148, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538224);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (149, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538227);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (150, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538274);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (151, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538303);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (152, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538454);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (153, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538696);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (154, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538749);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (155, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538765);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (156, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538771);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (157, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538792);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (158, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592538941);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (159, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592539285);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (160, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592539290);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (161, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592539303);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (162, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592638346);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (163, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592638394);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (164, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592638833);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (165, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592639533);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (166, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592639563);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (167, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592639714);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (168, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592639767);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (169, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592639816);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (170, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592640059);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (171, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592640075);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (172, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592640202);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (173, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592640223);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (174, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592640226);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (175, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592640338);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (176, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592640409);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (177, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592642892);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (178, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592643016);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (179, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592643020);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (180, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592643709);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (181, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592643724);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (182, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592643726);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (183, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592643778);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (184, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592648526);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (185, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592649278);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (186, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592657035);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (187, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592657049);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (188, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592657243);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (189, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592657262);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (190, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592657387);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (191, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592657573);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (192, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592657680);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (193, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592658688);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (194, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592658693);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (195, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592658790);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (196, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592658794);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (197, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592658840);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (198, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592659377);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (199, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592660103);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (200, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592660125);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (201, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592660271);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (202, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592661054);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (203, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592661061);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (204, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592661066);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (205, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592661072);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (206, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592661424);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (207, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592662688);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (208, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592719174);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (209, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592719245);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (210, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592720730);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (211, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592722942);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (212, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592879225);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (213, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592879233);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (214, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592880253);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (215, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592892400);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (216, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592892423);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (217, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592892462);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (218, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592892611);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (219, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592892854);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (220, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1592893955);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (221, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1592960984);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (222, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593307243);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (223, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593308587);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (224, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593308609);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (225, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593308626);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (226, 3, 'Allen7D', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593308632);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (227, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593310266);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (228, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593310298);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (229, 1, 'Boss', '192.168.10.59', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593400460);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (230, 1, 'Boss', '192.168.10.59', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593401089);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (231, 1, 'Boss', '192.168.10.59', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593409253);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (232, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593415871);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (233, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593415949);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (234, 1, 'Boss', '192.168.10.80', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593420031);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (235, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'android', '登录成功', 1, 1593420227);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (236, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593420708);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (237, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593483841);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (238, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593487473);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (239, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593487529);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (240, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593494870);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (241, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593503116);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (242, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593503137);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (243, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593503839);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (244, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593568245);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (245, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593570738);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (246, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593581966);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (247, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593581973);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (248, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593583769);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (249, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593655035);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (250, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1593655039);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (251, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1593661429);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (252, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604545322);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (253, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604546073);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (254, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604546081);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (255, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604546086);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (256, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604546092);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (257, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604546164);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (258, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604546318);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (259, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1604546328);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (260, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604557523);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (261, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604561437);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (262, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604561627);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (263, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604561656);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (264, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604561727);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (265, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604561777);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (266, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604561831);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (267, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604561833);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (268, 1, 'Boss', '192.168.10.74', '内网IP', 'chrome', 'windows', '登录成功', 1, 1604562130);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (269, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1606149299);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (270, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1606208378);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (271, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1607739198);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (272, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1607742388);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (273, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1611561798);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (274, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1619591451);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (275, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1628605334);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (276, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1658119664);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (277, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1658119665);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (278, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1658119666);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (279, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1658119667);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (280, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1658119772);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (281, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1658119781);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (282, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746901491);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (283, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746901499);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (284, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746901654);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (285, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746901977);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (286, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746902047);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (287, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746902052);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (288, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746902116);
INSERT INTO zerd.login_log (id, user_id, user_name, ip_addr, location, browser, os, message, status, create_time) VALUES (289, 1, 'Boss', '127.0.0.1', '内网IP', 'chrome', 'macos', '登录成功', 1, 1746902198);
create table menu
(
    group_id int not null comment '外键 权限组ID',
    route_id int not null comment '外键 路由节点ID',
    primary key (group_id, route_id),
    constraint menu_ibfk_1
        foreign key (group_id) references `group` (id),
    constraint menu_ibfk_2
        foreign key (route_id) references route (id)
);

create index route_id
    on menu (route_id);

INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 0);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 1);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 3);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 4);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 5);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 6);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 7);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 8);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 9);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 10);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 11);
INSERT INTO zerd.menu (group_id, route_id) VALUES (1, 12);
create table notice
(
    create_time int         null comment '创建时间',
    update_time int         null comment '更新时间',
    delete_time int         null comment '删除时间',
    id          int auto_increment
        primary key,
    type        smallint    null comment '类型(1通知, 2公告)',
    title       varchar(64) null comment '标题',
    content     text        null comment '内容',
    status      tinyint(1)  null comment '状态(0正常 1关闭)',
    remark      text        null comment '备注',
    create_by   varchar(32) null comment '创建者',
    update_by   varchar(32) null comment '更新者'
);

INSERT INTO zerd.notice (create_time, update_time, delete_time, id, type, title, content, status, remark, create_by, update_by) VALUES (null, 1593311079, null, 1, 2, '温馨提醒：2020-07-01 MiniShop新版本发布啦', '<p>新版本内容</p>', 0, '', '管理员', 'Boss');
INSERT INTO zerd.notice (create_time, update_time, delete_time, id, type, title, content, status, remark, create_by, update_by) VALUES (null, 1593311075, null, 2, 1, '维护通知：2020-07-01 MiniShop系统凌晨0:00维护', '<p>维护内容</p>', 0, '', '管理员', 'Boss');
INSERT INTO zerd.notice (create_time, update_time, delete_time, id, type, title, content, status, remark, create_by, update_by) VALUES (1593309584, 1593310141, 1593310141, 3, 1, '测试', '<p>111</p>', 1, '', 'Boss', '');
INSERT INTO zerd.notice (create_time, update_time, delete_time, id, type, title, content, status, remark, create_by, update_by) VALUES (1593311196, 1593311241, 1593311241, 4, 2, '测试1', '<p>测试1111</p>', 1, '', 'Boss', 'Boss');
INSERT INTO zerd.notice (create_time, update_time, delete_time, id, type, title, content, status, remark, create_by, update_by) VALUES (1593316414, 1593316428, 1593316428, 5, 1, '测试', '<p>111</p>', 1, '', 'Boss', '');
create table oper_log
(
    id             int auto_increment
        primary key,
    module         varchar(20)  null comment '系统模块',
    message        varchar(450) null comment '日志信息',
    user_id        int          not null comment '用户id',
    user_name      varchar(50)  null comment '用户当时的昵称',
    path           varchar(50)  null comment '请求路径',
    request_method varchar(20)  null comment '请求方法',
    request_param  json         null comment '请求参数',
    endpoint       varchar(100) null comment '端点',
    type           smallint     null comment '业务类型',
    auth           varchar(100) null comment '访问哪个权限',
    status_code    int          null comment '请求的http返回码',
    create_time    int          null comment '创建时间'
);

INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (1, null, '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', null, null, 2, '更新用户分组', 201, 1592278649);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (2, null, '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', null, null, 2, '更新用户分组', 201, 1592288761);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (3, null, '更改用户密码', 1, 'Boss', '/cms/user/1/password', 'PUT', null, null, 2, '更改用户密码', 201, 1592288770);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (4, null, '更新用户分组', 1, 'Boss', '/cms/user/4/group', 'PUT', null, null, 2, '更新用户分组', 201, 1592879250);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (5, '用户管理', '更新用户分组', 1, 'Boss', '/cms/user/4/group', 'PUT', null, null, 2, '更新用户分组', 201, 1592880267);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (6, '用户管理', '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', null, null, 2, '更新用户分组', 201, 1592894747);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (7, '用户管理', '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', null, 'cms.user+update_user', 2, '更新用户分组', 201, 1592895003);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (8, '用户管理', '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', null, 'cms.user+update_user', 2, '更新用户分组', 201, 1592898895);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (9, '用户管理', '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', null, 'cms.user+update_user', 2, '更新用户分组', 201, 1592899462);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (10, '用户管理', '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', '{"body": {"group_id": 1}, "path": {"uid": 1}, "query": {}}', 'cms.user+update_user', 2, '更新用户分组', 201, 1592901433);
INSERT INTO zerd.oper_log (id, module, message, user_id, user_name, path, request_method, request_param, endpoint, type, auth, status_code, create_time) VALUES (11, '用户管理', '更新用户分组', 1, 'Boss', '/cms/user/1/group', 'PUT', '{"body": {"group_id": 1}, "path": {"uid": 1}, "query": {}}', 'cms.user+update_user', 2, '更新用户分组', 201, 1592901757);
create table `order`
(
    id           int auto_increment
        primary key,
    order_no     varchar(20)       not null comment '订单号',
    user_id      int               not null comment '外键，用户id，注意并不是openid',
    order_status tinyint default 1 not null comment '1:未支付 2:已支付 3:已发货 4:已支付，但库存不足 ',
    snap_img     varchar(255)      null comment '订单快照·封面',
    snap_name    varchar(80)       null comment '订单快照·别名',
    snap_items   text              null comment '订单快照·详情',
    snap_address varchar(500)      null comment '订单快照·地址信息',
    total_count  int     default 0 not null comment '订单总量',
    total_price  decimal(6, 2)     not null comment '订单总价',
    prepay_id    varchar(100)      null comment '预支付ID',
    create_time  int               null comment '创建时间',
    update_time  int               null comment '更新时间',
    delete_time  int               null comment '删除时间',
    constraint order_no
        unique (order_no)
);

create index user_id
    on `order` (user_id);

INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (1, 'B0X435186095427189', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "和瑞科技园 S1-1302", "detail": "", "id": 2, "mobile": "13788889999", "name": "董小小", "province": "浙江省", "user_id": 2}', 20, 0.20, null, 1588130000, 1628692672, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (2, 'B0X439892335427188', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "和瑞科技园 S1-1302", "detail": "", "id": 2, "mobile": "13788889999", "name": "董小小", "province": "浙江省", "user_id": 2}', 20, 0.20, null, 1588131000, 1628692680, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (18, 'B0X433513735427169', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "和瑞科技园 S1-1302", "detail": "", "id": 2, "mobile": "13788889999", "name": "董小小", "province": "浙江省", "user_id": 2}', 20, 0.20, null, 1588132000, 1628692687, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (19, 'B0X431906695427191', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "和瑞科技园 S1-1302", "detail": "", "id": 2, "mobile": "13788889999", "name": "董小小", "province": "浙江省", "user_id": 2}', 20, 0.20, null, 1588133000, 1628692695, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (22, 'B0X436611625427134', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "和瑞科技园 S1-1302", "detail": "", "id": 2, "mobile": "13788889999", "name": "董小小", "province": "浙江省", "user_id": 2}', 20, 0.20, null, 1588134000, 1628692704, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (23, 'B0X434107455427153', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "和瑞科技园 S1-1302", "detail": "", "id": 2, "mobile": "13788889999", "name": "董小小", "province": "浙江省", "user_id": 2}', 20, 0.20, null, 1588135000, 1628692711, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (24, 'B0X436584155427116', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "和瑞科技园 S1-1302", "detail": "", "id": 2, "mobile": "13788889999", "name": "董小小", "province": "浙江省", "user_id": 2}', 20, 0.20, null, 1588136000, 1628692732, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (25, 'B0XB42397767285726', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 2, "has_stock": true, "count": 10, "name": "梨花带雨 3个", "total_price": 0.1}]', '{"city": "杭州市", "country": "中国", "detail": "和瑞科技园 S1-1302", "mobile": 13788889999, "name": "段兵兵", "province": "浙江省"}', 20, 0.20, null, 1588137000, 1628692744, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (26, 'B0XB43649737285735', 1, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤 等', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}, {"id": 11, "has_stock": true, "count": 10, "name": "贵妃笑 100克", "total_price": 0.1}]', '{"city": "杭州市", "country": "中国", "detail": "和瑞科技园 S1-1302", "mobile": 13788889999, "name": "段兵兵", "province": "浙江省"}', 20, 0.20, null, 1588138000, 1628692723, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (27, 'B0XB40017347285790', 1, 1, '0.0.0.0:8010/static/images/product-rice@1.png', '素米 327克 等', '[{"id": 3, "has_stock": true, "count": 10, "name": "素米 327克", "total_price": 0.1}, {"id": 4, "has_stock": true, "count": 10, "name": "红袖枸杞 6克*3袋", "total_price": 0.1}]', '{"city": "杭州市", "country": "中国", "detail": "和瑞科技园 S1-1302", "mobile": 13788889999, "name": "段兵兵", "province": "浙江省"}', 20, 0.20, null, 1588138500, 1628692664, null);
INSERT INTO zerd.`order` (id, order_no, user_id, order_status, snap_img, snap_name, snap_items, snap_address, total_count, total_price, prepay_id, create_time, update_time, delete_time) VALUES (28, 'C0X4262413568787205', 3, 1, '0.0.0.0:8010/static/images/product-vg@1.png', '芹菜 半斤', '[{"id": 1, "has_stock": true, "count": 10, "name": "芹菜 半斤", "total_price": 0.1}]', '{"city": "杭州", "country": "萧山", "detail": "金地三期2栋2单元701室", "mobile": 13799999999, "name": "董小小", "province": "浙江"}', 10, 0.10, null, 1588139000, 1628692649, null);
create table order_product
(
    order_id    int not null comment '联合主键，订单id',
    product_id  int not null comment '联合主键，商品id',
    count       int not null comment '商品数量',
    create_time int null comment '创建时间',
    update_time int null comment '更新时间',
    delete_time int null comment '删除时间',
    primary key (product_id, order_id)
);

INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (1, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (2, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (18, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (19, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (22, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (23, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (24, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (25, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (26, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (28, 1, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (1, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (2, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (18, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (19, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (22, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (23, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (24, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (25, 2, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (27, 3, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (27, 4, 10, null, null, null);
INSERT INTO zerd.order_product (order_id, product_id, count, create_time, update_time, delete_time) VALUES (26, 11, 10, null, null, null);
create table product
(
    id           int auto_increment
        primary key,
    name         varchar(80)       not null comment '商品名称',
    price        decimal(6, 2)     not null comment '价格,单位：分',
    stock        int     default 0 not null comment '库存量',
    category_id  int               null,
    main_img_url varchar(255)      null comment '主图ID号，这是一个反范式设计，有一定的冗余',
    `from`       tinyint default 1 not null comment '图片来自 1 本地 ，2公网',
    summary      varchar(50)       null comment '摘要',
    img_id       int               null comment '图片外键',
    create_time  int               null comment '创建时间',
    update_time  int               null comment '更新时间',
    delete_time  int               null comment '删除时间'
);

INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (1, '芹菜 半斤', 0.01, 998, 3, '/product-vg@1.png', 1, null, 13, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (2, '梨花带雨 3个', 0.01, 984, 2, '/product-dryfruit@1.png', 1, null, 10, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (3, '素米 327克', 0.01, 996, 7, '/product-rice@1.png', 1, null, 31, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (4, '红袖枸杞 6克*3袋', 0.01, 998, 6, '/product-tea@1.png', 1, null, 32, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (5, '春生龙眼 500克', 0.01, 995, 2, '/product-dryfruit@2.png', 1, null, 33, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (6, '小红的猪耳朵 120克', 0.01, 997, 5, '/product-cake@2.png', 1, null, 53, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (7, '泥蒿 半斤', 0.01, 998, 3, '/product-vg@2.png', 1, null, 68, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (8, '夏日芒果 3个', 0.01, 995, 2, '/product-dryfruit@3.png', 1, null, 36, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (9, '冬木红枣 500克', 0.01, 996, 2, '/product-dryfruit@4.png', 1, null, 37, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (10, '万紫千凤梨 300克', 0.01, 996, 2, '/product-dryfruit@5.png', 1, null, 38, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (11, '贵妃笑 100克', 0.01, 994, 2, '/product-dryfruit-a@6.png', 1, null, 39, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (12, '珍奇异果 3个', 0.01, 999, 2, '/product-dryfruit@7.png', 1, null, 40, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (13, '绿豆 125克', 0.01, 999, 7, '/product-rice@2.png', 1, null, 41, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (14, '芝麻 50克', 0.01, 999, 7, '/product-rice@3.png', 1, null, 42, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (15, '猴头菇 370克', 0.01, 999, 7, '/product-rice@4.png', 1, null, 43, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (16, '西红柿 1斤', 0.01, 999, 3, '/product-vg@3.png', 1, null, 69, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (17, '油炸花生 300克', 0.01, 999, 4, '/product-fry@1.png', 1, null, 44, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (18, '春泥西瓜子 128克', 0.01, 997, 4, '/product-fry@2.png', 1, null, 45, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (19, '碧水葵花籽 128克', 0.01, 999, 4, '/product-fry@3.png', 1, null, 46, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (20, '碧螺春 12克*3袋', 0.01, 999, 6, '/product-tea@2.png', 1, null, 47, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (21, '西湖龙井 8克*3袋', 0.01, 998, 6, '/product-tea@3.png', 1, null, 48, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (22, '梅兰清花糕 1个', 0.01, 997, 5, '/product-cake-a@3.png', 1, null, 54, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (23, '清凉薄荷糕 1个', 0.01, 998, 5, '/product-cake-a@4.png', 1, null, 55, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (25, '小明的妙脆角 120克', 0.01, 999, 5, '/product-cake@1.png', 1, null, 52, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (26, '红衣青瓜 混搭160克', 0.01, 999, 2, '/product-dryfruit@8.png', 1, null, 56, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (27, '锈色瓜子 100克', 0.01, 998, 4, '/product-fry@4.png', 1, null, 57, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (28, '春泥花生 200克', 0.01, 999, 4, '/product-fry@5.png', 1, null, 58, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (29, '冰心鸡蛋 2个', 0.01, 999, 7, '/product-rice@5.png', 1, null, 59, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (30, '八宝莲子 200克', 0.01, 999, 7, '/product-rice@6.png', 1, null, 14, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (31, '深涧木耳 78克', 0.01, 999, 7, '/product-rice@7.png', 1, null, 60, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (32, '土豆 半斤', 0.01, 999, 3, '/product-vg@4.png', 1, null, 66, null, null, null);
INSERT INTO zerd.product (id, name, price, stock, category_id, main_img_url, `from`, summary, img_id, create_time, update_time, delete_time) VALUES (33, '青椒 半斤', 0.01, 999, 3, '/product-vg@5.png', 1, null, 67, null, null, null);
create table product_image
(
    img_id      int           not null comment '外键，关联图片表',
    `order`     int default 0 not null comment '图片排序序号',
    product_id  int           not null comment '商品id，外键',
    create_time int           null comment '创建时间',
    update_time int           null comment '更新时间',
    delete_time int           null comment '删除时间',
    primary key (img_id, `order`)
);

INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (19, 1, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (20, 2, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (21, 3, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (22, 4, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (23, 5, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (24, 6, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (25, 7, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (26, 8, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (27, 9, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (28, 11, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (29, 10, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (62, 12, 11, null, null, null);
INSERT INTO zerd.product_image (img_id, `order`, product_id, create_time, update_time, delete_time) VALUES (63, 13, 11, null, null, null);
create table product_property
(
    id          int auto_increment
        primary key,
    name        varchar(30) default '' null comment '详情属性名称',
    detail      varchar(255)           not null comment '详情属性',
    product_id  int                    not null comment '商品id，外键',
    create_time int                    null comment '创建时间',
    update_time int                    null comment '更新时间',
    delete_time int                    null comment '删除时间'
);

INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (1, '品名', '杨梅', 11, null, null, null);
INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (2, '口味', '青梅味 雪梨味 黄桃味 菠萝味', 11, null, null, null);
INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (3, '产地', '火星', 11, null, null, null);
INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (4, '保质期', '180天', 11, null, null, null);
INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (5, '品名', '梨子', 2, null, null, null);
INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (6, '产地', '金星', 2, null, null, null);
INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (7, '净含量', '100g', 2, null, null, null);
INSERT INTO zerd.product_property (id, name, detail, product_id, create_time, update_time, delete_time) VALUES (8, '保质期', '10天', 2, null, null, null);
create table route
(
    id        int auto_increment comment '路由节点ID'
        primary key,
    parent_id int          not null comment '路由节点父级ID',
    title     varchar(20)  not null comment '路由节点标签',
    name      varchar(20)  null comment '路由节点名',
    icon      varchar(100) null comment '图标',
    path      varchar(100) not null comment '路由节点相对路径',
    component varchar(100) null comment '组件路径',
    hidden    tinyint(1)   not null comment '路由节点是否隐藏',
    `order`   int          null comment '路由顺序',
    constraint name
        unique (name)
);

INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (1, 0, '首页', 'Main', 'fa fa-th-large', '/main', null, 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (3, 1, '主页面', 'Home', 'fa fa-align-justify', '/home', 'home/index', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (4, 1, '规范指南', 'Guide', 'fa fa-align-justify', '/guide', 'guide/index', 0, 1);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (5, 0, '关于', 'About', 'fa fa-info', '/about', null, 0, 1);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (6, 5, '关于', 'AboutIndex', 'fa fa-align-justify', '/about/index', 'about/index', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (7, 0, '系统管理', 'Admin', 'fa fa-cog', '/admin', null, 0, 4);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (8, 7, '用户管理', 'AdminUser', 'fa fa-align-justify', '/admin/user', 'admin/user/index', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (9, 7, '权限管理', 'AdminApi', 'fa fa-align-justify', '/admin/auth', 'admin/auth/index', 0, 1);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (10, 7, '菜单管理', 'AdminMenu', 'fa fa-align-justify', '/admin/menu', 'admin/menu/index', 0, 2);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (11, 0, '文件管理', 'File', 'fa fa-folder-o', '/file', null, 0, 7);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (12, 11, '文件管理', 'FileIndex', 'fa fa-align-justify', '/file/index', 'file/index', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (13, 0, '系统工具', 'Tool', 'fa fa-wrench', '/tool', null, 0, 5);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (14, 16, 'Json格式化', 'JsonView', 'fa fa-edit', '/component/json-view', 'components/json-view', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (15, 13, '表单构建', 'FormBuilder', 'fa fa-list-ul', '/tool/build', 'tools/build/index', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (16, 0, '组件管理', 'ComponentLib', 'fa fa-cogs', '/component', '', 0, 6);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (17, 13, '错误码', 'ErrorCode', 'fa fa-file-word-o', '/tool/error-code', 'tools/error-code/index', 0, 1);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (18, 13, '接口文档', 'Swagger', 'fa fa-book', '/tool/swagger', 'tools/swagger/index', 0, 2);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (19, 0, '文章管理', 'Article', 'fa fa-file-text-o', '/article', null, 0, 8);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (20, 19, '新增文章', 'ArticleAdd', 'fa fa-align-justify', '/article/add', 'article/add', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (21, 19, '文章列表', 'ArticleList', 'fa fa-align-justify', '/article/list', 'article/index', 0, 1);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (22, 19, '编辑文章', 'ArticleEdit', 'fa fa-align-justify', '/article/edit/:id', 'article/edit', 1, 2);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (23, 7, '字典管理', 'AdminDict', 'fa fa-align-justify', '/admin/dict', 'admin/dict/index', 0, 3);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (24, 7, '字典数据', 'AdminDictData', 'fa fa-align-justify', '/admin/dict/data/:id', 'admin/dict/dict-data', 1, 4);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (25, 7, '日志管理', 'AdminLog', 'fa fa-pencil-square-o', '/admin/log', null, 0, 7);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (26, 25, '登录日志', 'LoginLog', 'fa fa-sign-in', '/admin/log/login-log', 'admin/log/login-log', 0, 1);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (27, 25, '操作日志', 'OperLog', 'fa fa-keyboard-o', '/admin/log/oper-log', 'admin/log/oper-log', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (28, 7, '通知管理', 'Notice', 'fa fa-align-justify', '/admin/notice', 'admin/notice/index', 0, 6);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (29, 16, '富文本', 'Tinymce', 'fa fa-edit', '/component/tinymce', 'components/tinymce/index', 0, 1);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (30, 7, '参数管理', 'AdminConfig', 'fa fa-list-ol', '/admin/config', 'admin/config/index', 0, 5);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (31, 0, '类别管理', 'Category', 'fa fa-table', '/category', '', 0, 3);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (32, 31, '类别列表', 'CategoryIndex', 'fa fa-align-justify', '/category/index', 'category/index', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (33, 0, 'Banner管理', 'Banner', 'fa fa-ellipsis-h', '/banner', null, 0, 2);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (34, 33, 'Banner列表', 'BannerIndex', 'fa fa-ellipsis-h', '/banner/index', 'banner/index', 0, 0);
INSERT INTO zerd.route (id, parent_id, title, name, icon, path, component, hidden, `order`) VALUES (36, 16, 'Ueditor', 'Ueditor', 'fa fa-edit', '/component/Ueditor', 'components/ueditor/index', 0, 0);
create table theme
(
    id           int auto_increment
        primary key,
    name         varchar(50)  not null comment '专题名称',
    description  varchar(255) null comment '专题描述',
    topic_img_id int          not null comment '主题图，外键',
    head_img_id  int          not null comment '专题列表页，头图',
    create_time  int          null comment '创建时间',
    update_time  int          null comment '更新时间',
    delete_time  int          null comment '删除时间'
)
    comment '主题信息表';

INSERT INTO zerd.theme (id, name, description, topic_img_id, head_img_id, create_time, update_time, delete_time) VALUES (1, '专题栏位一', '美味水果世界', 16, 49, null, null, null);
INSERT INTO zerd.theme (id, name, description, topic_img_id, head_img_id, create_time, update_time, delete_time) VALUES (2, '专题栏位二', '新品推荐', 17, 50, null, null, null);
INSERT INTO zerd.theme (id, name, description, topic_img_id, head_img_id, create_time, update_time, delete_time) VALUES (3, '专题栏位三', '做个干物女', 18, 51, null, null, null);
create table theme_product
(
    theme_id    int not null comment '主题外键',
    product_id  int not null comment '商品外键',
    create_time int null comment '创建时间',
    update_time int null comment '更新时间',
    delete_time int null comment '删除时间',
    primary key (theme_id, product_id)
)
    comment '主题所包含的商品';

INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (1, 2, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (1, 5, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (1, 8, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (1, 10, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (1, 12, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (2, 1, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (2, 2, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (2, 3, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (2, 5, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (2, 6, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (2, 16, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (2, 33, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (3, 15, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (3, 18, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (3, 19, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (3, 27, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (3, 30, null, null, null);
INSERT INTO zerd.theme_product (theme_id, product_id, create_time, update_time, delete_time) VALUES (3, 31, null, null, null);
create table third_app
(
    id                int auto_increment
        primary key,
    app_id            varchar(64)  not null comment '应用app_id',
    app_secret        varchar(64)  not null comment '应用secret',
    app_description   varchar(100) null comment '应用程序描述',
    scope             varchar(20)  not null comment '应用权限',
    scope_description varchar(100) null comment '权限描述',
    create_time       int          null comment '创建时间',
    update_time       int          null comment '更新时间',
    delete_time       int          null comment '删除时间'
)
    comment '访问API的各应用账号密码表';

INSERT INTO zerd.third_app (id, app_id, app_secret, app_description, scope, scope_description, create_time, update_time, delete_time) VALUES (1, 'starcraft', '777*777', 'CMS', '32', 'Super', null, null, null);
create table user
(
    id          int auto_increment
        primary key,
    nickname    varchar(50)  null comment '昵称',
    auth        smallint     null comment '权限',
    group_id    int          null comment '用户所属的权限组id',
    avatar      varchar(255) null comment '头像URL',
    extend      varchar(255) null comment '额外备注',
    create_time int          null comment '创建时间',
    update_time int          null comment '更新时间',
    delete_time int          null comment '删除时间'
);

create index id
    on user (id);

INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (1, 'Boss', 2, 1, 'http://abc/xzy.jpg', null, 1588138125, 1592674088, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (2, '小叶', 1, 1, null, null, null, 1592674088, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (3, '小董', 1, 1, null, null, 1587102577, 1592674088, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (4, 'Allen7D', 1, 1, null, null, null, 1592879250, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (24, 'Allen9D', 1, 2, null, null, null, null, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (25, 'Allen8D', 1, 2, null, null, null, null, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (27, '笑呵呵', 1, 3, null, null, 1587024920, 1587029097, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (30, '宋仁投', 1, 6, null, null, 1587043791, 1588686249, null);
INSERT INTO zerd.user (id, nickname, auth, group_id, avatar, extend, create_time, update_time, delete_time) VALUES (31, 'Allen1D', 1, 6, null, null, 1588134674, 1588686249, null);