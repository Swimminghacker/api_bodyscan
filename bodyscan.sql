/*
 Navicat MySQL Data Transfer

 Source Server         : swm
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : bodyscan

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 08/10/2018 22:29:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for operator
-- ----------------------------
DROP TABLE IF EXISTS `operator`;
CREATE TABLE `operator`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `account` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_time` date NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `receive_num` int(11) NOT NULL DEFAULT 0,
  `process_num` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `wait_num` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `finished_num` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `status` int(10) UNSIGNED NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of operator
-- ----------------------------
INSERT INTO `operator` VALUES (15, '石维民1号', '13129997581', '2018-10-07', '997581', 0, 0, 0, 0, 1);

-- ----------------------------
-- Table structure for organization
-- ----------------------------
DROP TABLE IF EXISTS `organization`;
CREATE TABLE `organization`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_time` date NOT NULL,
  `account` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `belonged_organization` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `task_num` int(11) NOT NULL DEFAULT 0,
  `status` int(10) UNSIGNED NOT NULL DEFAULT 0,
  `id_card` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `gender` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of organization
-- ----------------------------
INSERT INTO `organization` VALUES (2, '超级石维民', '2018-10-07', '13997786596', '786596', '华科法医中心', 'niubi@we.cc', 0, 1, '422801199612250010', '华科韵苑食堂', 'male');
INSERT INTO `organization` VALUES (3, '机构石维民1号', '2018-10-07', '13997786591', '786591', '华科法医中心', 'niubi@we.cc', 0, 1, '422801199612250010', '华科韵苑食堂', 'male');
INSERT INTO `organization` VALUES (4, '机构石维民2号', '2018-10-07', '13997786592', '786592', '华科法医中心', 'niubi@we.cc', 0, 1, '422801199612250010', NULL, 'male');
INSERT INTO `organization` VALUES (5, '超级石维民', '2018-10-08', '13997786597', '786597', '华科法医中心', 'niubi@we.cc', 0, 1, '422801199612250010', '华科韵苑食堂', 'male');

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_time` date NOT NULL,
  `organization` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `measuring_part` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` int(255) NOT NULL DEFAULT 0,
  `organization_operator_id` int(255) UNSIGNED NOT NULL DEFAULT '',
  `operator_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task
-- ----------------------------
INSERT INTO `task` VALUES (14, '张浩然1号', 'male', '2018-10-08', '华科法医中心', '屁屁', 0, 1, NULL);
INSERT INTO `task` VALUES (15, '张浩然2号', 'male', '2018-10-08', '华科法医中心', '屁屁', 1, 1, NULL);
INSERT INTO `task` VALUES (16, '张浩然3号', 'male', '2018-10-08', '华科法医中心', '屁屁', 1, 31, 15);
INSERT INTO `task` VALUES (17, '张浩然4号', 'male', '2018-10-08', '华科法医中心', '屁屁', 1, 3, 11);
INSERT INTO `task` VALUES (18, '张浩然5号', 'male', '2018-10-08', '华科法医中心', '屁屁', 1, 3, 15);

-- ----------------------------
-- Table structure for task_detail
-- ----------------------------
DROP TABLE IF EXISTS `task_detail`;
CREATE TABLE `task_detail`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `target_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `target_gender` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `target_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `measuring_part` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `measuring_method` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `measuring_time` date NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `file_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `report_file_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task_detail
-- ----------------------------
INSERT INTO `task_detail` VALUES (3, 14, '张浩然1号', 'male', '422801199612250010', '屁屁', '拍打法', '2018-09-10', '没啥问题', '123', '222');
INSERT INTO `task_detail` VALUES (4, 15, '张浩然2号', 'male', '422801199612250010', '屁屁', '拍打法', '2018-09-02', '没啥问题', '123', '3');
INSERT INTO `task_detail` VALUES (5, 16, '张浩然3号', 'male', '422801199612250010', '屁屁', '拍打法', '2018-09-03', '没啥问题', '123', NULL);
INSERT INTO `task_detail` VALUES (6, 17, '张浩然4号', 'male', '422801199612250010', '屁屁', '拍打法', '2018-09-04', '没啥问题', '123', NULL);
INSERT INTO `task_detail` VALUES (7, 18, '张浩然5号', 'male', '422801199612250010', '屁屁', '拍打法', '2018-09-05', '没啥问题', '123', NULL);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '默认是手机号码',
  `password` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '初始值设为手机号码后六位',
  `role` int(1) NOT NULL COMMENT '0代表超管、1代表操作员、2代表客户机构',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (2, '13129997584', 'swm', 0);
INSERT INTO `user` VALUES (22, '13129997581', '997581', 1);
INSERT INTO `user` VALUES (24, '13997786596', '786596', 2);
INSERT INTO `user` VALUES (25, '13997786591', '786591', 2);
INSERT INTO `user` VALUES (26, '13997786592', '786592', 2);
INSERT INTO `user` VALUES (27, '13997786597', '786597', 2);

SET FOREIGN_KEY_CHECKS = 1;
