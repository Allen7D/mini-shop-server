/*
 Navicat Premium Data Transfer

 Source Server         : yezi
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : localhost
 Source Database       : zerd

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : utf-8

 Date: 06/26/2018 14:18:12 PM
*/

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `banner`
-- ----------------------------
DROP TABLE IF EXISTS `banner`;
CREATE TABLE `banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL COMMENT 'Banner名称，通常作为标识',
  `description` varchar(255) DEFAULT NULL COMMENT 'Banner描述',
  `delete_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='banner管理表';

-- ----------------------------
--  Records of `banner`
-- ----------------------------
BEGIN;
INSERT INTO `banner` VALUES ('1', '首页置顶', '首页轮播图', null, null, '1528938338', '1');
COMMIT;

-- ----------------------------
--  Table structure for `banner_item`
-- ----------------------------
DROP TABLE IF EXISTS `banner_item`;
CREATE TABLE `banner_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_id` int(11) NOT NULL COMMENT '外键，关联image表',
  `key_word` varchar(100) NOT NULL COMMENT '执行关键字，根据不同的type含义不同',
  `type` tinyint(4) NOT NULL DEFAULT '1' COMMENT '跳转类型，可能导向商品，可能导向专题，可能导向其他。0，无导向；1：导向商品;2:导向专题',
  `delete_time` int(11) DEFAULT NULL,
  `banner_id` int(11) NOT NULL COMMENT '外键，关联banner表',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COMMENT='banner子项表';

-- ----------------------------
--  Records of `banner_item`
-- ----------------------------
BEGIN;
INSERT INTO `banner_item` VALUES ('1', '65', '6', '1', null, '1', null, '1528938338', '1'), ('2', '2', '25', '1', null, '1', null, '1528938338', '1'), ('3', '3', '11', '1', null, '1', null, '1528938338', '1'), ('5', '1', '10', '1', null, '1', null, '1528938338', '1');
COMMIT;

-- ----------------------------
--  Table structure for `book`
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `author` varchar(30) DEFAULT NULL,
  `binding` varchar(20) DEFAULT NULL,
  `publisher` varchar(50) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  `pages` int(11) DEFAULT NULL,
  `pubdate` varchar(20) DEFAULT NULL,
  `isbn` varchar(15) NOT NULL,
  `summary` varchar(1000) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL COMMENT '分类名称',
  `topic_img_id` int(11) DEFAULT NULL COMMENT '外键，关联image表',
  `delete_time` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL COMMENT '描述',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COMMENT='商品类目';

-- ----------------------------
--  Records of `category`
-- ----------------------------
BEGIN;
INSERT INTO `category` VALUES ('2', '果味', '6', null, null, null, null, '1'), ('3', '蔬菜', '5', null, null, null, null, '1'), ('4', '炒货', '7', null, null, null, null, '1'), ('5', '点心', '4', null, null, null, null, '1'), ('6', '粗茶', '8', null, null, null, null, '1'), ('7', '淡饭', '9', null, null, null, null, '1');
COMMIT;

-- ----------------------------
--  Table structure for `gift`
-- ----------------------------
DROP TABLE IF EXISTS `gift`;
CREATE TABLE `gift` (
  `create_time` int(11) DEFAULT NULL,
  `delete_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `isbn` varchar(15) NOT NULL,
  `launched` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `gift_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `image`
-- ----------------------------
DROP TABLE IF EXISTS `image`;
CREATE TABLE `image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL COMMENT '图片路径',
  `from` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1 来自本地，2 来自公网',
  `delete_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT '1',
  `create_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COMMENT='图片总表';

-- ----------------------------
--  Records of `image`
-- ----------------------------
BEGIN;
INSERT INTO `image` VALUES ('1', '/banner-1a.png', '1', null, null, '1', null), ('2', '/banner-2a.png', '1', null, null, '1', null), ('3', '/banner-3a.png', '1', null, null, '1', null), ('4', '/category-cake.png', '1', null, null, '1', null), ('5', '/category-vg.png', '1', null, null, '1', null), ('6', '/category-dryfruit.png', '1', null, null, '1', null), ('7', '/category-fry-a.png', '1', null, null, '1', null), ('8', '/category-tea.png', '1', null, null, '1', null), ('9', '/category-rice.png', '1', null, null, '1', null), ('10', '/product-dryfruit@1.png', '1', null, null, '1', null), ('13', '/product-vg@1.png', '1', null, null, '1', null), ('14', '/product-rice@6.png', '1', null, null, '1', null), ('16', '/1@theme.png', '1', null, null, '1', null), ('17', '/2@theme.png', '1', null, null, '1', null), ('18', '/3@theme.png', '1', null, null, '1', null), ('19', '/detail-1@1-dryfruit.png', '1', null, null, '1', null), ('20', '/detail-2@1-dryfruit.png', '1', null, null, '1', null), ('21', '/detail-3@1-dryfruit.png', '1', null, null, '1', null), ('22', '/detail-4@1-dryfruit.png', '1', null, null, '1', null), ('23', '/detail-5@1-dryfruit.png', '1', null, null, '1', null), ('24', '/detail-6@1-dryfruit.png', '1', null, null, '1', null), ('25', '/detail-7@1-dryfruit.png', '1', null, null, '1', null), ('26', '/detail-8@1-dryfruit.png', '1', null, null, '1', null), ('27', '/detail-9@1-dryfruit.png', '1', null, null, '1', null), ('28', '/detail-11@1-dryfruit.png', '1', null, null, '1', null), ('29', '/detail-10@1-dryfruit.png', '1', null, null, '1', null), ('31', '/product-rice@1.png', '1', null, null, '1', null), ('32', '/product-tea@1.png', '1', null, null, '1', null), ('33', '/product-dryfruit@2.png', '1', null, null, '1', null), ('36', '/product-dryfruit@3.png', '1', null, null, '1', null), ('37', '/product-dryfruit@4.png', '1', null, null, '1', null), ('38', '/product-dryfruit@5.png', '1', null, null, '1', null), ('39', '/product-dryfruit-a@6.png', '1', null, null, '1', null), ('40', '/product-dryfruit@7.png', '1', null, null, '1', null), ('41', '/product-rice@2.png', '1', null, null, '1', null), ('42', '/product-rice@3.png', '1', null, null, '1', null), ('43', '/product-rice@4.png', '1', null, null, '1', null), ('44', '/product-fry@1.png', '1', null, null, '1', null), ('45', '/product-fry@2.png', '1', null, null, '1', null), ('46', '/product-fry@3.png', '1', null, null, '1', null), ('47', '/product-tea@2.png', '1', null, null, '1', null), ('48', '/product-tea@3.png', '1', null, null, '1', null), ('49', '/1@theme-head.png', '1', null, null, '1', null), ('50', '/2@theme-head.png', '1', null, null, '1', null), ('51', '/3@theme-head.png', '1', null, null, '1', null), ('52', '/product-cake@1.png', '1', null, null, '1', null), ('53', '/product-cake@2.png', '1', null, null, '1', null), ('54', '/product-cake-a@3.png', '1', null, null, '1', null), ('55', '/product-cake-a@4.png', '1', null, null, '1', null), ('56', '/product-dryfruit@8.png', '1', null, null, '1', null), ('57', '/product-fry@4.png', '1', null, null, '1', null), ('58', '/product-fry@5.png', '1', null, null, '1', null), ('59', '/product-rice@5.png', '1', null, null, '1', null), ('60', '/product-rice@7.png', '1', null, null, '1', null), ('62', '/detail-12@1-dryfruit.png', '1', null, null, '1', null), ('63', '/detail-13@1-dryfruit.png', '1', null, null, '1', null), ('65', '/banner-4a.png', '1', null, null, '1', null), ('66', '/product-vg@4.png', '1', null, null, '1', null), ('67', '/product-vg@5.png', '1', null, null, '1', null), ('68', '/product-vg@2.png', '1', null, null, '1', null), ('69', '/product-vg@3.png', '1', null, null, '1', null);
COMMIT;

-- ----------------------------
--  Table structure for `order`
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_no` varchar(20) NOT NULL COMMENT '订单号',
  `user_id` int(11) NOT NULL COMMENT '外键，用户id，注意并不是openid',
  `delete_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `total_price` decimal(6,2) NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1:未支付， 2：已支付，3：已发货 , 4: 已支付，但库存不足',
  `snap_img` varchar(255) DEFAULT NULL COMMENT '订单快照图片',
  `snap_name` varchar(80) DEFAULT NULL COMMENT '订单快照名称',
  `total_count` int(11) NOT NULL DEFAULT '0',
  `update_time` int(11) DEFAULT NULL,
  `snap_items` text COMMENT '订单其他信息快照（json)',
  `snap_address` varchar(500) DEFAULT NULL COMMENT '地址快照',
  `prepay_id` varchar(100) DEFAULT NULL COMMENT '订单微信支付的预订单id（用于发送模板消息）',
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_no` (`order_no`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `order_product`
-- ----------------------------
DROP TABLE IF EXISTS `order_product`;
CREATE TABLE `order_product` (
  `order_id` int(11) NOT NULL COMMENT '联合主键，订单id',
  `product_id` int(11) NOT NULL COMMENT '联合主键，商品id',
  `count` int(11) NOT NULL COMMENT '商品数量',
  `delete_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`,`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL COMMENT '商品名称',
  `price` decimal(6,2) NOT NULL COMMENT '价格,单位：分',
  `stock` int(11) NOT NULL DEFAULT '0' COMMENT '库存量',
  `delete_time` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `main_img_url` varchar(255) DEFAULT NULL COMMENT '主图ID号，这是一个反范式设计，有一定的冗余',
  `from` tinyint(4) NOT NULL DEFAULT '1' COMMENT '图片来自 1 本地 ，2公网',
  `create_time` int(11) DEFAULT NULL COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL,
  `summary` varchar(50) DEFAULT NULL COMMENT '摘要',
  `img_id` int(11) DEFAULT NULL COMMENT '图片外键',
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `product`
-- ----------------------------
BEGIN;
INSERT INTO `product` VALUES ('1', '芹菜 半斤', '0.01', '998', null, '3', '/product-vg@1.png', '1', '1528938338', null, null, '13', '1'), ('2', '梨花带雨 3个', '0.01', '984', null, '2', '/product-dryfruit@1.png', '1', '1528938339', null, null, '10', '1'), ('3', '素米 327克', '0.01', '996', null, '7', '/product-rice@1.png', '1', '1528938340', null, null, '31', '1'), ('4', '红袖枸杞 6克*3袋', '0.01', '998', null, '6', '/product-tea@1.png', '1', '1528938341', null, null, '32', '1'), ('5', '春生龙眼 500克', '0.01', '995', null, '2', '/product-dryfruit@2.png', '1', '1528938342', null, null, '33', '1'), ('6', '小红的猪耳朵 120克', '0.01', '997', null, '5', '/product-cake@2.png', '1', '1528938343', null, null, '53', '1'), ('7', '泥蒿 半斤', '0.01', '998', null, '3', '/product-vg@2.png', '1', '1528938344', null, null, '68', '1'), ('8', '夏日芒果 3个', '0.01', '995', null, '2', '/product-dryfruit@3.png', '1', '1528938345', null, null, '36', '1'), ('9', '冬木红枣 500克', '0.01', '996', null, '2', '/product-dryfruit@4.png', '1', '1528938346', null, null, '37', '1'), ('10', '万紫千凤梨 300克', '0.01', '996', null, '2', '/product-dryfruit@5.png', '1', '1528938347', null, null, '38', '1'), ('11', '贵妃笑 100克', '0.01', '994', null, '2', '/product-dryfruit-a@6.png', '1', '1528938348', null, null, '39', '1'), ('12', '珍奇异果 3个', '0.01', '999', null, '2', '/product-dryfruit@7.png', '1', '1528938349', null, null, '40', '1'), ('13', '绿豆 125克', '0.01', '999', null, '7', '/product-rice@2.png', '1', '1528938350', null, null, '41', '1'), ('14', '芝麻 50克', '0.01', '999', null, '7', '/product-rice@3.png', '1', '1528938351', null, null, '42', '1'), ('15', '猴头菇 370克', '0.01', '999', null, '7', '/product-rice@4.png', '1', '1528938352', null, null, '43', '1'), ('16', '西红柿 1斤', '0.01', '999', null, '3', '/product-vg@3.png', '1', '1528938353', null, null, '69', '1'), ('17', '油炸花生 300克', '0.01', '999', null, '4', '/product-fry@1.png', '1', '1528938354', null, null, '44', '1'), ('18', '春泥西瓜子 128克', '0.01', '997', null, '4', '/product-fry@2.png', '1', '1528938355', null, null, '45', '1'), ('19', '碧水葵花籽 128克', '0.01', '999', null, '4', '/product-fry@3.png', '1', '1528938356', null, null, '46', '1'), ('20', '碧螺春 12克*3袋', '0.01', '999', null, '6', '/product-tea@2.png', '1', '1528938357', null, null, '47', '1'), ('21', '西湖龙井 8克*3袋', '0.01', '998', null, '6', '/product-tea@3.png', '1', '1528938358', null, null, '48', '1'), ('22', '梅兰清花糕 1个', '0.01', '997', null, '5', '/product-cake-a@3.png', '1', '1528938359', null, null, '54', '1'), ('23', '清凉薄荷糕 1个', '0.01', '998', null, '5', '/product-cake-a@4.png', '1', '1528938360', null, null, '55', '1'), ('25', '小明的妙脆角 120克', '0.01', '999', null, '5', '/product-cake@1.png', '1', '1528938361', null, null, '52', '1'), ('26', '红衣青瓜 混搭160克', '0.01', '999', null, '2', '/product-dryfruit@8.png', '1', '1528938362', null, null, '56', '1'), ('27', '锈色瓜子 100克', '0.01', '998', null, '4', '/product-fry@4.png', '1', '1528938363', null, null, '57', '1'), ('28', '春泥花生 200克', '0.01', '999', null, '4', '/product-fry@5.png', '1', '1528938364', null, null, '58', '1'), ('29', '冰心鸡蛋 2个', '0.01', '999', null, '7', '/product-rice@5.png', '1', '1528938365', null, null, '59', '1'), ('30', '八宝莲子 200克', '0.01', '999', null, '7', '/product-rice@6.png', '1', '1528938366', null, null, '14', '1'), ('31', '深涧木耳 78克', '0.01', '999', null, '7', '/product-rice@7.png', '1', '1528938367', null, null, '60', '1'), ('32', '土豆 半斤', '0.01', '999', null, '3', '/product-vg@4.png', '1', '1528938368', null, null, '66', '1'), ('33', '青椒 半斤', '0.01', '999', null, '3', '/product-vg@5.png', '1', '1528938369', null, null, '67', '1');
COMMIT;

-- ----------------------------
--  Table structure for `product_image`
-- ----------------------------
DROP TABLE IF EXISTS `product_image`;
CREATE TABLE `product_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_id` int(11) NOT NULL COMMENT '外键，关联图片表',
  `delete_time` int(11) DEFAULT NULL COMMENT '状态，主要表示是否删除，也可以扩展其他状态',
  `order` int(11) NOT NULL DEFAULT '0' COMMENT '图片排序序号',
  `product_id` int(11) NOT NULL COMMENT '商品id，外键',
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `product_image`
-- ----------------------------
BEGIN;
INSERT INTO `product_image` VALUES ('4', '19', null, '1', '11', null, null, '1'), ('5', '20', null, '2', '11', null, null, '1'), ('6', '21', null, '3', '11', null, null, '1'), ('7', '22', null, '4', '11', null, null, '1'), ('8', '23', null, '5', '11', null, null, '1'), ('9', '24', null, '6', '11', null, null, '1'), ('10', '25', null, '7', '11', null, null, '1'), ('11', '26', null, '8', '11', null, null, '1'), ('12', '27', null, '9', '11', null, null, '1'), ('13', '28', null, '11', '11', null, null, '1'), ('14', '29', null, '10', '11', null, null, '1'), ('18', '62', null, '12', '11', null, null, '1'), ('19', '63', null, '13', '11', null, null, '1');
COMMIT;

-- ----------------------------
--  Table structure for `product_property`
-- ----------------------------
DROP TABLE IF EXISTS `product_property`;
CREATE TABLE `product_property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT '' COMMENT '详情属性名称',
  `detail` varchar(255) NOT NULL COMMENT '详情属性',
  `product_id` int(11) NOT NULL COMMENT '商品id，外键',
  `delete_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `product_property`
-- ----------------------------
BEGIN;
INSERT INTO `product_property` VALUES ('1', '品名', '杨梅', '11', null, null, null, '1'), ('2', '口味', '青梅味 雪梨味 黄桃味 菠萝味', '11', null, null, null, '1'), ('3', '产地', '火星', '11', null, null, null, '1'), ('4', '保质期', '180天', '11', null, null, null, '1'), ('5', '品名', '梨子', '2', null, null, null, '1'), ('6', '产地', '金星', '2', null, null, null, '1'), ('7', '净含量', '100g', '2', null, null, null, '1'), ('8', '保质期', '10天', '2', null, null, null, '1');
COMMIT;

-- ----------------------------
--  Table structure for `theme`
-- ----------------------------
DROP TABLE IF EXISTS `theme`;
CREATE TABLE `theme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL COMMENT '专题名称',
  `description` varchar(255) DEFAULT NULL COMMENT '专题描述',
  `topic_img_id` int(11) NOT NULL COMMENT '主题图，外键',
  `delete_time` int(11) DEFAULT NULL,
  `head_img_id` int(11) NOT NULL COMMENT '专题列表页，头图',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COMMENT='主题信息表';

-- ----------------------------
--  Records of `theme`
-- ----------------------------
BEGIN;
INSERT INTO `theme` VALUES ('1', '专题栏位一', '美味水果世界', '16', null, '49', null, null, '1'), ('2', '专题栏位二', '新品推荐', '17', null, '50', null, null, '1'), ('3', '专题栏位三', '做个干物女', '18', null, '51', null, null, '1');
COMMIT;

-- ----------------------------
--  Table structure for `theme_product`
-- ----------------------------
DROP TABLE IF EXISTS `theme_product`;
CREATE TABLE `theme_product` (
  `theme_id` int(11) NOT NULL COMMENT '主题外键',
  `product_id` int(11) NOT NULL COMMENT '商品外键',
  PRIMARY KEY (`theme_id`,`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='主题所包含的商品';

-- ----------------------------
--  Records of `theme_product`
-- ----------------------------
BEGIN;
INSERT INTO `theme_product` VALUES ('1', '2'), ('1', '5'), ('1', '8'), ('1', '10'), ('1', '12'), ('2', '1'), ('2', '2'), ('2', '3'), ('2', '5'), ('2', '6'), ('2', '16'), ('2', '33'), ('3', '15'), ('3', '18'), ('3', '19'), ('3', '27'), ('3', '30'), ('3', '31');
COMMIT;

-- ----------------------------
--  Table structure for `third_app`
-- ----------------------------
DROP TABLE IF EXISTS `third_app`;
CREATE TABLE `third_app` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_id` varchar(64) NOT NULL COMMENT '应用app_id',
  `app_secret` varchar(64) NOT NULL COMMENT '应用secret',
  `app_description` varchar(100) DEFAULT NULL COMMENT '应用程序描述',
  `scope` varchar(20) NOT NULL COMMENT '应用权限',
  `scope_description` varchar(100) DEFAULT NULL COMMENT '权限描述',
  `delete_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='访问API的各应用账号密码表';

-- ----------------------------
--  Records of `third_app`
-- ----------------------------
BEGIN;
INSERT INTO `third_app` VALUES ('1', 'starcraft', '777*777', 'CMS', '32', 'Super', null, null);
COMMIT;

-- ----------------------------
--  Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` varchar(50) NOT NULL,
  `email` varchar(24) DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `auth` smallint(6) DEFAULT NULL,
  `extend` varchar(255) DEFAULT NULL,
  `delete_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL COMMENT '注册时间',
  `update_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `openid` (`openid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `user`
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES ('1', 'oYf_s0OnCim9Cx7tCV-AHs_rDWXs', null, null, null, '1', null, null, '1529895665', null, '1');
COMMIT;

-- ----------------------------
--  Table structure for `user_address`
-- ----------------------------
DROP TABLE IF EXISTS `user_address`;
CREATE TABLE `user_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL COMMENT '收获人姓名',
  `mobile` varchar(20) NOT NULL COMMENT '手机号',
  `province` varchar(20) DEFAULT NULL COMMENT '省',
  `city` varchar(20) DEFAULT NULL COMMENT '市',
  `country` varchar(20) DEFAULT NULL COMMENT '区',
  `detail` varchar(100) DEFAULT NULL COMMENT '详细地址',
  `delete_time` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL COMMENT '外键',
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `user_address`
-- ----------------------------
BEGIN;
INSERT INTO `user_address` VALUES ('1', '???', '13758787058', '???', '???', '????? S1-1301', '', null, '1', null, '1529924323', '1');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
