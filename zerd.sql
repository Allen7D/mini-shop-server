/*
 Navicat Premium Data Transfer

 Source Server         : yezi
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : localhost:3306
 Source Schema         : zerd

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : 65001

 Date: 09/04/2019 13:24:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for banner
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
-- Records of banner
-- ----------------------------
BEGIN;
INSERT INTO `banner` VALUES (1, '首页置顶', '首页轮播图', NULL, NULL, 1528938338, 1);
COMMIT;

-- ----------------------------
-- Table structure for banner_item
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
-- Records of banner_item
-- ----------------------------
BEGIN;
INSERT INTO `banner_item` VALUES (1, 65, '6', 1, NULL, 1, NULL, 1528938338, 1);
INSERT INTO `banner_item` VALUES (2, 2, '25', 1, NULL, 1, NULL, 1528938338, 1);
INSERT INTO `banner_item` VALUES (3, 3, '11', 1, NULL, 1, NULL, 1528938338, 1);
INSERT INTO `banner_item` VALUES (5, 1, '10', 1, NULL, 1, NULL, 1528938338, 1);
COMMIT;

-- ----------------------------
-- Table structure for category
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
-- Records of category
-- ----------------------------
BEGIN;
INSERT INTO `category` VALUES (2, '果味', 6, NULL, NULL, NULL, NULL, 1);
INSERT INTO `category` VALUES (3, '蔬菜', 5, NULL, NULL, NULL, NULL, 1);
INSERT INTO `category` VALUES (4, '炒货', 7, NULL, NULL, NULL, NULL, 1);
INSERT INTO `category` VALUES (5, '点心', 4, NULL, NULL, NULL, NULL, 1);
INSERT INTO `category` VALUES (6, '粗茶', 8, NULL, NULL, NULL, NULL, 1);
INSERT INTO `category` VALUES (7, '淡饭', 9, NULL, NULL, NULL, NULL, 1);
COMMIT;

-- ----------------------------
-- Table structure for image
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
-- Records of image
-- ----------------------------
BEGIN;
INSERT INTO `image` VALUES (1, '/banner-1a.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (2, '/banner-2a.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (3, '/banner-3a.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (4, '/category-cake.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (5, '/category-vg.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (6, '/category-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (7, '/category-fry-a.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (8, '/category-tea.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (9, '/category-rice.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (10, '/product-dryfruit@1.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (13, '/product-vg@1.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (14, '/product-rice@6.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (16, '/1@theme.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (17, '/2@theme.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (18, '/3@theme.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (19, '/detail-1@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (20, '/detail-2@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (21, '/detail-3@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (22, '/detail-4@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (23, '/detail-5@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (24, '/detail-6@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (25, '/detail-7@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (26, '/detail-8@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (27, '/detail-9@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (28, '/detail-11@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (29, '/detail-10@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (31, '/product-rice@1.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (32, '/product-tea@1.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (33, '/product-dryfruit@2.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (36, '/product-dryfruit@3.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (37, '/product-dryfruit@4.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (38, '/product-dryfruit@5.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (39, '/product-dryfruit-a@6.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (40, '/product-dryfruit@7.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (41, '/product-rice@2.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (42, '/product-rice@3.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (43, '/product-rice@4.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (44, '/product-fry@1.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (45, '/product-fry@2.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (46, '/product-fry@3.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (47, '/product-tea@2.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (48, '/product-tea@3.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (49, '/1@theme-head.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (50, '/2@theme-head.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (51, '/3@theme-head.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (52, '/product-cake@1.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (53, '/product-cake@2.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (54, '/product-cake-a@3.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (55, '/product-cake-a@4.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (56, '/product-dryfruit@8.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (57, '/product-fry@4.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (58, '/product-fry@5.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (59, '/product-rice@5.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (60, '/product-rice@7.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (62, '/detail-12@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (63, '/detail-13@1-dryfruit.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (65, '/banner-4a.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (66, '/product-vg@4.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (67, '/product-vg@5.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (68, '/product-vg@2.png', 1, NULL, NULL, 1, NULL);
INSERT INTO `image` VALUES (69, '/product-vg@3.png', 1, NULL, NULL, 1, NULL);
COMMIT;

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_no` varchar(20) NOT NULL COMMENT '订单号',
  `user_id` int(11) NOT NULL COMMENT '外键，用户id，注意并不是openid',
  `total_price` decimal(6,2) NOT NULL,
  `order_status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1:未支付 2:已支付 3:已发货 4:已支付，但库存不足 ',
  `snap_img` varchar(255) DEFAULT NULL COMMENT '??????',
  `snap_name` varchar(80) DEFAULT NULL COMMENT '??????',
  `total_count` int(11) NOT NULL DEFAULT '0',
  `snap_items` text COMMENT '?????????json)',
  `snap_address` varchar(500) DEFAULT NULL COMMENT '地址信息',
  `prepay_id` varchar(100) DEFAULT NULL COMMENT '??????????id??????????',
  `create_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `delete_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `order_no` (`order_no`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of order
-- ----------------------------
BEGIN;
INSERT INTO `order` VALUES (16, 'B0X435186095427189', 2, 0.20, 1, '0.0.0.0:8080/static/images/product-vg@1.png', '芹菜 半斤 等', 20, '[{\"id\": 1, \"has_stock\": true, \"count\": 10, \"name\": \"芹菜 半斤\", \"total_price\": 0.1}, {\"id\": 2, \"has_stock\": true, \"count\": 10, \"name\": \"梨花带雨 3个\", \"total_price\": 0.1}]', '{\"city\": \"杭州市\", \"country\": \"和瑞科技园 S1-1302\", \"detail\": \"\", \"id\": 2, \"mobile\": \"13788889999\", \"name\": \"董冬伟\", \"province\": \"浙江省\", \"user_id\": 2}', NULL, 1554271488, NULL, NULL, NULL);
INSERT INTO `order` VALUES (17, 'B0X439892335427188', 2, 0.20, 1, '0.0.0.0:8080/static/images/product-vg@1.png', '芹菜 半斤 等', 20, '[{\"id\": 1, \"has_stock\": true, \"count\": 10, \"name\": \"芹菜 半斤\", \"total_price\": 0.1}, {\"id\": 2, \"has_stock\": true, \"count\": 10, \"name\": \"梨花带雨 3个\", \"total_price\": 0.1}]', '{\"city\": \"杭州市\", \"country\": \"和瑞科技园 S1-1302\", \"detail\": \"\", \"id\": 2, \"mobile\": \"13788889999\", \"name\": \"董冬伟\", \"province\": \"浙江省\", \"user_id\": 2}', NULL, 1554271547, NULL, NULL, NULL);
INSERT INTO `order` VALUES (18, 'B0X433513735427169', 2, 0.20, 1, '0.0.0.0:8080/static/images/product-vg@1.png', '芹菜 半斤 等', 20, '[{\"id\": 1, \"has_stock\": true, \"count\": 10, \"name\": \"芹菜 半斤\", \"total_price\": 0.1}, {\"id\": 2, \"has_stock\": true, \"count\": 10, \"name\": \"梨花带雨 3个\", \"total_price\": 0.1}]', '{\"city\": \"杭州市\", \"country\": \"和瑞科技园 S1-1302\", \"detail\": \"\", \"id\": 2, \"mobile\": \"13788889999\", \"name\": \"董冬伟\", \"province\": \"浙江省\", \"user_id\": 2}', NULL, 1554271599, NULL, NULL, NULL);
INSERT INTO `order` VALUES (19, 'B0X431906695427191', 2, 0.20, 1, '0.0.0.0:8080/static/images/product-vg@1.png', '芹菜 半斤 等', 20, '[{\"id\": 1, \"has_stock\": true, \"count\": 10, \"name\": \"芹菜 半斤\", \"total_price\": 0.1}, {\"id\": 2, \"has_stock\": true, \"count\": 10, \"name\": \"梨花带雨 3个\", \"total_price\": 0.1}]', '{\"city\": \"杭州市\", \"country\": \"和瑞科技园 S1-1302\", \"detail\": \"\", \"id\": 2, \"mobile\": \"13788889999\", \"name\": \"董冬伟\", \"province\": \"浙江省\", \"user_id\": 2}', NULL, 1554271604, NULL, NULL, NULL);
INSERT INTO `order` VALUES (22, 'B0X436611625427134', 2, 0.20, 1, '0.0.0.0:8080/static/images/product-vg@1.png', '芹菜 半斤 等', 20, '[{\"id\": 1, \"has_stock\": true, \"count\": 10, \"name\": \"芹菜 半斤\", \"total_price\": 0.1}, {\"id\": 2, \"has_stock\": true, \"count\": 10, \"name\": \"梨花带雨 3个\", \"total_price\": 0.1}]', '{\"city\": \"杭州市\", \"country\": \"和瑞科技园 S1-1302\", \"detail\": \"\", \"id\": 2, \"mobile\": \"13788889999\", \"name\": \"董冬伟\", \"province\": \"浙江省\", \"user_id\": 2}', NULL, 1554271682, NULL, NULL, NULL);
INSERT INTO `order` VALUES (23, 'B0X434107455427153', 2, 0.20, 1, '0.0.0.0:8080/static/images/product-vg@1.png', '芹菜 半斤 等', 20, '[{\"id\": 1, \"has_stock\": true, \"count\": 10, \"name\": \"芹菜 半斤\", \"total_price\": 0.1}, {\"id\": 2, \"has_stock\": true, \"count\": 10, \"name\": \"梨花带雨 3个\", \"total_price\": 0.1}]', '{\"city\": \"杭州市\", \"country\": \"和瑞科技园 S1-1302\", \"detail\": \"\", \"id\": 2, \"mobile\": \"13788889999\", \"name\": \"董冬伟\", \"province\": \"浙江省\", \"user_id\": 2}', NULL, 1554271784, NULL, NULL, NULL);
INSERT INTO `order` VALUES (24, 'B0X436584155427116', 2, 0.20, 1, '0.0.0.0:8080/static/images/product-vg@1.png', '芹菜 半斤 等', 20, '[{\"id\": 1, \"has_stock\": true, \"count\": 10, \"name\": \"芹菜 半斤\", \"total_price\": 0.1}, {\"id\": 2, \"has_stock\": true, \"count\": 10, \"name\": \"梨花带雨 3个\", \"total_price\": 0.1}]', '{\"city\": \"杭州市\", \"country\": \"和瑞科技园 S1-1302\", \"detail\": \"\", \"id\": 2, \"mobile\": \"13788889999\", \"name\": \"董冬伟\", \"province\": \"浙江省\", \"user_id\": 2}', NULL, 1554271865, NULL, NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for order_product
-- ----------------------------
DROP TABLE IF EXISTS `order_product`;
CREATE TABLE `order_product` (
  `order_id` int(11) NOT NULL COMMENT '联合主键，订单id',
  `product_id` int(11) NOT NULL COMMENT '联合主键，商品id',
  `count` int(11) NOT NULL COMMENT '商品数量',
  `delete_time` int(11) DEFAULT NULL,
  `update_time` int(11) DEFAULT NULL,
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`product_id`,`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of order_product
-- ----------------------------
BEGIN;
INSERT INTO `order_product` VALUES (16, 1, 10, NULL, NULL, 1554271517, 1);
INSERT INTO `order_product` VALUES (17, 1, 10, NULL, NULL, 1554271547, 1);
INSERT INTO `order_product` VALUES (18, 1, 10, NULL, NULL, 1554271599, 1);
INSERT INTO `order_product` VALUES (19, 1, 10, NULL, NULL, 1554271604, 1);
INSERT INTO `order_product` VALUES (22, 1, 10, NULL, NULL, 1554271685, 1);
INSERT INTO `order_product` VALUES (23, 1, 10, NULL, NULL, 1554271784, 1);
INSERT INTO `order_product` VALUES (24, 1, 10, NULL, NULL, 1554271865, 1);
INSERT INTO `order_product` VALUES (16, 2, 10, NULL, NULL, 1554271517, 1);
INSERT INTO `order_product` VALUES (17, 2, 10, NULL, NULL, 1554271547, 1);
INSERT INTO `order_product` VALUES (18, 2, 10, NULL, NULL, 1554271599, 1);
INSERT INTO `order_product` VALUES (19, 2, 10, NULL, NULL, 1554271604, 1);
INSERT INTO `order_product` VALUES (22, 2, 10, NULL, NULL, 1554271685, 1);
INSERT INTO `order_product` VALUES (23, 2, 10, NULL, NULL, 1554271784, 1);
INSERT INTO `order_product` VALUES (24, 2, 10, NULL, NULL, 1554271865, 1);
COMMIT;

-- ----------------------------
-- Table structure for product
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
-- Records of product
-- ----------------------------
BEGIN;
INSERT INTO `product` VALUES (1, '芹菜 半斤', 0.01, 998, NULL, 3, '/product-vg@1.png', 1, 1528938338, NULL, NULL, 13, 1);
INSERT INTO `product` VALUES (2, '梨花带雨 3个', 0.01, 984, NULL, 2, '/product-dryfruit@1.png', 1, 1528938339, NULL, NULL, 10, 1);
INSERT INTO `product` VALUES (3, '素米 327克', 0.01, 996, NULL, 7, '/product-rice@1.png', 1, 1528938340, NULL, NULL, 31, 1);
INSERT INTO `product` VALUES (4, '红袖枸杞 6克*3袋', 0.01, 998, NULL, 6, '/product-tea@1.png', 1, 1528938341, NULL, NULL, 32, 1);
INSERT INTO `product` VALUES (5, '春生龙眼 500克', 0.01, 995, NULL, 2, '/product-dryfruit@2.png', 1, 1528938342, NULL, NULL, 33, 1);
INSERT INTO `product` VALUES (6, '小红的猪耳朵 120克', 0.01, 997, NULL, 5, '/product-cake@2.png', 1, 1528938343, NULL, NULL, 53, 1);
INSERT INTO `product` VALUES (7, '泥蒿 半斤', 0.01, 998, NULL, 3, '/product-vg@2.png', 1, 1528938344, NULL, NULL, 68, 1);
INSERT INTO `product` VALUES (8, '夏日芒果 3个', 0.01, 995, NULL, 2, '/product-dryfruit@3.png', 1, 1528938345, NULL, NULL, 36, 1);
INSERT INTO `product` VALUES (9, '冬木红枣 500克', 0.01, 996, NULL, 2, '/product-dryfruit@4.png', 1, 1528938346, NULL, NULL, 37, 1);
INSERT INTO `product` VALUES (10, '万紫千凤梨 300克', 0.01, 996, NULL, 2, '/product-dryfruit@5.png', 1, 1528938347, NULL, NULL, 38, 1);
INSERT INTO `product` VALUES (11, '贵妃笑 100克', 0.01, 994, NULL, 2, '/product-dryfruit-a@6.png', 1, 1528938348, NULL, NULL, 39, 1);
INSERT INTO `product` VALUES (12, '珍奇异果 3个', 0.01, 999, NULL, 2, '/product-dryfruit@7.png', 1, 1528938349, NULL, NULL, 40, 1);
INSERT INTO `product` VALUES (13, '绿豆 125克', 0.01, 999, NULL, 7, '/product-rice@2.png', 1, 1528938350, NULL, NULL, 41, 1);
INSERT INTO `product` VALUES (14, '芝麻 50克', 0.01, 999, NULL, 7, '/product-rice@3.png', 1, 1528938351, NULL, NULL, 42, 1);
INSERT INTO `product` VALUES (15, '猴头菇 370克', 0.01, 999, NULL, 7, '/product-rice@4.png', 1, 1528938352, NULL, NULL, 43, 1);
INSERT INTO `product` VALUES (16, '西红柿 1斤', 0.01, 999, NULL, 3, '/product-vg@3.png', 1, 1528938353, NULL, NULL, 69, 1);
INSERT INTO `product` VALUES (17, '油炸花生 300克', 0.01, 999, NULL, 4, '/product-fry@1.png', 1, 1528938354, NULL, NULL, 44, 1);
INSERT INTO `product` VALUES (18, '春泥西瓜子 128克', 0.01, 997, NULL, 4, '/product-fry@2.png', 1, 1528938355, NULL, NULL, 45, 1);
INSERT INTO `product` VALUES (19, '碧水葵花籽 128克', 0.01, 999, NULL, 4, '/product-fry@3.png', 1, 1528938356, NULL, NULL, 46, 1);
INSERT INTO `product` VALUES (20, '碧螺春 12克*3袋', 0.01, 999, NULL, 6, '/product-tea@2.png', 1, 1528938357, NULL, NULL, 47, 1);
INSERT INTO `product` VALUES (21, '西湖龙井 8克*3袋', 0.01, 998, NULL, 6, '/product-tea@3.png', 1, 1528938358, NULL, NULL, 48, 1);
INSERT INTO `product` VALUES (22, '梅兰清花糕 1个', 0.01, 997, NULL, 5, '/product-cake-a@3.png', 1, 1528938359, NULL, NULL, 54, 1);
INSERT INTO `product` VALUES (23, '清凉薄荷糕 1个', 0.01, 998, NULL, 5, '/product-cake-a@4.png', 1, 1528938360, NULL, NULL, 55, 1);
INSERT INTO `product` VALUES (25, '小明的妙脆角 120克', 0.01, 999, NULL, 5, '/product-cake@1.png', 1, 1528938361, NULL, NULL, 52, 1);
INSERT INTO `product` VALUES (26, '红衣青瓜 混搭160克', 0.01, 999, NULL, 2, '/product-dryfruit@8.png', 1, 1528938362, NULL, NULL, 56, 1);
INSERT INTO `product` VALUES (27, '锈色瓜子 100克', 0.01, 998, NULL, 4, '/product-fry@4.png', 1, 1528938363, NULL, NULL, 57, 1);
INSERT INTO `product` VALUES (28, '春泥花生 200克', 0.01, 999, NULL, 4, '/product-fry@5.png', 1, 1528938364, NULL, NULL, 58, 1);
INSERT INTO `product` VALUES (29, '冰心鸡蛋 2个', 0.01, 999, NULL, 7, '/product-rice@5.png', 1, 1528938365, NULL, NULL, 59, 1);
INSERT INTO `product` VALUES (30, '八宝莲子 200克', 0.01, 999, NULL, 7, '/product-rice@6.png', 1, 1528938366, NULL, NULL, 14, 1);
INSERT INTO `product` VALUES (31, '深涧木耳 78克', 0.01, 999, NULL, 7, '/product-rice@7.png', 1, 1528938367, NULL, NULL, 60, 1);
INSERT INTO `product` VALUES (32, '土豆 半斤', 0.01, 999, NULL, 3, '/product-vg@4.png', 1, 1528938368, NULL, NULL, 66, 1);
INSERT INTO `product` VALUES (33, '青椒 半斤', 0.01, 999, NULL, 3, '/product-vg@5.png', 1, 1528938369, NULL, NULL, 67, 1);
COMMIT;

-- ----------------------------
-- Table structure for product_image
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
-- Records of product_image
-- ----------------------------
BEGIN;
INSERT INTO `product_image` VALUES (4, 19, NULL, 1, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (5, 20, NULL, 2, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (6, 21, NULL, 3, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (7, 22, NULL, 4, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (8, 23, NULL, 5, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (9, 24, NULL, 6, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (10, 25, NULL, 7, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (11, 26, NULL, 8, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (12, 27, NULL, 9, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (13, 28, NULL, 11, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (14, 29, NULL, 10, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (18, 62, NULL, 12, 11, NULL, NULL, 1);
INSERT INTO `product_image` VALUES (19, 63, NULL, 13, 11, NULL, NULL, 1);
COMMIT;

-- ----------------------------
-- Table structure for product_property
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
-- Records of product_property
-- ----------------------------
BEGIN;
INSERT INTO `product_property` VALUES (1, '品名', '杨梅', 11, NULL, NULL, NULL, 1);
INSERT INTO `product_property` VALUES (2, '口味', '青梅味 雪梨味 黄桃味 菠萝味', 11, NULL, NULL, NULL, 1);
INSERT INTO `product_property` VALUES (3, '产地', '火星', 11, NULL, NULL, NULL, 1);
INSERT INTO `product_property` VALUES (4, '保质期', '180天', 11, NULL, NULL, NULL, 1);
INSERT INTO `product_property` VALUES (5, '品名', '梨子', 2, NULL, NULL, NULL, 1);
INSERT INTO `product_property` VALUES (6, '产地', '金星', 2, NULL, NULL, NULL, 1);
INSERT INTO `product_property` VALUES (7, '净含量', '100g', 2, NULL, NULL, NULL, 1);
INSERT INTO `product_property` VALUES (8, '保质期', '10天', 2, NULL, NULL, NULL, 1);
COMMIT;

-- ----------------------------
-- Table structure for theme
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
-- Records of theme
-- ----------------------------
BEGIN;
INSERT INTO `theme` VALUES (1, '专题栏位一', '美味水果世界', 16, NULL, 49, NULL, NULL, 1);
INSERT INTO `theme` VALUES (2, '专题栏位二', '新品推荐', 17, NULL, 50, NULL, NULL, 1);
INSERT INTO `theme` VALUES (3, '专题栏位三', '做个干物女', 18, NULL, 51, NULL, NULL, 1);
COMMIT;

-- ----------------------------
-- Table structure for theme_product
-- ----------------------------
DROP TABLE IF EXISTS `theme_product`;
CREATE TABLE `theme_product` (
  `theme_id` int(11) NOT NULL COMMENT '主题外键',
  `product_id` int(11) NOT NULL COMMENT '商品外键',
  PRIMARY KEY (`theme_id`,`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='主题所包含的商品';

-- ----------------------------
-- Records of theme_product
-- ----------------------------
BEGIN;
INSERT INTO `theme_product` VALUES (1, 2);
INSERT INTO `theme_product` VALUES (1, 5);
INSERT INTO `theme_product` VALUES (1, 8);
INSERT INTO `theme_product` VALUES (1, 10);
INSERT INTO `theme_product` VALUES (1, 12);
INSERT INTO `theme_product` VALUES (2, 1);
INSERT INTO `theme_product` VALUES (2, 2);
INSERT INTO `theme_product` VALUES (2, 3);
INSERT INTO `theme_product` VALUES (2, 5);
INSERT INTO `theme_product` VALUES (2, 6);
INSERT INTO `theme_product` VALUES (2, 16);
INSERT INTO `theme_product` VALUES (2, 33);
INSERT INTO `theme_product` VALUES (3, 15);
INSERT INTO `theme_product` VALUES (3, 18);
INSERT INTO `theme_product` VALUES (3, 19);
INSERT INTO `theme_product` VALUES (3, 27);
INSERT INTO `theme_product` VALUES (3, 30);
INSERT INTO `theme_product` VALUES (3, 31);
COMMIT;

-- ----------------------------
-- Table structure for third_app
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
-- Records of third_app
-- ----------------------------
BEGIN;
INSERT INTO `third_app` VALUES (1, 'starcraft', '777*777', 'CMS', '32', 'Super', NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for user
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, 'oYf_s0OnCim9Cx7tCV-AHs_rDWXs', '666@qq.com', 'Admin6', 'pbkdf2:sha256:50000$pCWwi32D$2f51549dc2731b3f5d53c5456a602410ed0f06d2d41226f064312745e20c1dd2', 1, NULL, NULL, 1529895665, NULL, 1);
INSERT INTO `user` VALUES (2, '999', '999@qq.com', 'Super', 'pbkdf2:sha256:50000$pCWwi32D$2f51549dc2731b3f5d53c5456a602410ed0f06d2d41226f064312745e20c1dd2', 2, NULL, NULL, 1536764841, NULL, 1);
INSERT INTO `user` VALUES (3, '777', '777@qq.com', 'Admin7', 'pbkdf2:sha256:50000$YrYmLzfp$981a20fc95c1dfc423866be176c0a66b728a95f9c285d6b731af05349112d2f9', 1, NULL, NULL, 1536764882, NULL, 1);
COMMIT;

-- ----------------------------
-- Table structure for user_address
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user_address
-- ----------------------------
BEGIN;
INSERT INTO `user_address` VALUES (1, '岑黎光', '13788889999', '浙江省', '杭州市', '和瑞科技园 S1-1302', '', NULL, 3, NULL, 1529924323, 1);
INSERT INTO `user_address` VALUES (2, '董冬伟', '13788889999', '浙江省', '杭州市', '和瑞科技园 S1-1302', '', NULL, 2, NULL, 1529924323, 1);
INSERT INTO `user_address` VALUES (3, '段海兵', '13788889999', '浙江省', '杭州市', '和瑞科技园 S1-1302', '', NULL, 1, NULL, 1529924323, 1);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
