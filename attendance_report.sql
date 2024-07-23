/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 100411 (10.4.11-MariaDB)
 Source Host           : localhost:3306
 Source Schema         : attendance_report

 Target Server Type    : MySQL
 Target Server Version : 100411 (10.4.11-MariaDB)
 File Encoding         : 65001

 Date: 23/07/2024 16:02:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attendance_summary
-- ----------------------------
DROP TABLE IF EXISTS `attendance_summary`;
CREATE TABLE `attendance_summary`  (
  `employee_id` bigint NOT NULL,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `department` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `work_duration_standard` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `work_duration_actual` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `late_times` bigint NULL DEFAULT NULL,
  `late_duration_min` bigint NULL DEFAULT NULL,
  `leave_early_times` bigint NULL DEFAULT NULL,
  `leave_early_duration_min` bigint NULL DEFAULT NULL,
  `overtime_normal` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `overtime_special` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `lack_times` bigint NULL DEFAULT NULL,
  `lack_duration_min` bigint NULL DEFAULT NULL,
  `attendance` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `absent_days` bigint NULL DEFAULT NULL,
  `on_business_days` double NULL DEFAULT NULL,
  `ask_off` double NULL DEFAULT NULL,
  `salary_raise_mark` double NULL DEFAULT NULL,
  `salary_raise_over_time` double NULL DEFAULT NULL,
  `salary_raise_subsidy` double NULL DEFAULT NULL,
  `salary_reduce_late_leave_early` double NULL DEFAULT NULL,
  `salary_reduce_casual_leave` double NULL DEFAULT NULL,
  `salary_reduce_chargeback` double NULL DEFAULT NULL,
  `real_wage` double NULL DEFAULT NULL,
  `remarks` double NULL DEFAULT NULL,
  PRIMARY KEY (`employee_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance_summary
-- ----------------------------
INSERT INTO `attendance_summary` VALUES (1, 'Fryma', 'Production Dept.', '180:00', '11:00', 2, 317, 2, 103, '0:00', '0:00', 0, 0, '20/2', 18, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `attendance_summary` VALUES (2, 'Alfan', 'Production Dept.', '180:00', '0:00', 1, 166, 1, 374, '0:00', '0:00', 0, 0, '20/1', 19, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `attendance_summary` VALUES (3, 'Adit', 'R&D Dept.', '180:00', '0:07', 2, 700, 2, 373, '0:00', '0:00', 1, 540, '20/3', 17, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
