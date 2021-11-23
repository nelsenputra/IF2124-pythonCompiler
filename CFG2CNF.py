import sys, helper

left, right = 0, 1

K, V, Productions = [],[],[]
variablesJar = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a29', 'a30', 'a31', 'a32', 'a33', 'a34', 'a35', 'a36', 'a37', 'a38', 'a39', 'a40', 'a41', 'a42', 'a43', 'a44', 'a45', 'a46', 'a47', 'a48', 'a49', 'a50', 'a51', 'a52', 'a53', 'a54', 'a55', 'a56', 'a57', 'a58', 'a59', 'a60', 'a61', 'a62', 'a63', 'a64', 'a65', 'a66', 'a67', 'a68', 'a69', 'a70', 'a71', 'a72', 'a73', 'a74', 'a75', 'a76', 'a77', 'a78', 'a79', 'a80', 'a81', 'a82', 'a83', 'a84', 'a85', 'a86', 'a87', 'a88', 'a89', 'a90', 'a91', 'a92', 'a93', 'a94', 'a95', 'a96', 'a97', 'a98', 'a99', 'a100', 'a101', 'a102', 'a103', 'a104', 'a105', 'a106', 'a107', 'a108', 'a109', 'a110', 'a111', 'a112', 'a113', 'a114', 'a115', 'a116', 'a117', 'a118', 'a119', 'a120', 'a121', 'a122', 'a123', 'a124', 'a125', 'a126', 'a127', 'a128', 'a129', 'a130', 'a131', 'a132', 'a133', 'a134', 'a135', 'a136', 'a137', 'a138', 'a139', 'a140', 'a141', 'a142', 'a143', 'a144', 'a145', 'a146', 'a147', 'a148', 'a149', 'a150', 'a151', 'a152', 'a153', 'a154', 'a155', 'a156', 'a157', 'a158', 'a159', 'a160', 'a161', 'a162', 'a163', 'a164', 'a165', 'a166', 'a167', 'a168', 'a169', 'a170', 'a171', 'a172', 'a173', 'a174', 'a175', 'a176', 'a177', 'a178', 'a179', 'a180', 'a181', 'a182', 'a183', 'a184', 'a185', 'a186', 'a187', 'a188', 'a189', 'a190', 'a191', 'a192', 'a193', 'a194', 'a195', 'a196', 'a197', 'a198', 'a199', 'a200', 'a201', 'a202', 'a203', 'a204', 'a205', 'a206', 'a207', 'a208', 'a209', 'a210', 'a211', 'a212', 'a213', 'a214', 'a215', 'a216', 
'a217', 'a218', 'a219', 'a220', 'a221', 'a222', 'a223', 'a224', 'a225', 'a226', 'a227', 'a228', 'a229', 'a230', 'a231', 'a232', 'a233', 'a234', 'a235', 'a236', 'a237', 'a238', 'a239', 'a240', 'a241', 'a242', 'a243', 'a244', 'a245', 'a246', 'a247', 'a248', 'a249', 'a250', 'a251', 'a252', 'a253', 'a254', 'a255', 'a256', 'a257', 'a258', 'a259', 'a260', 'a261', 'a262', 'a263', 'a264', 'a265', 'a266', 'a267', 'a268', 'a269', 'a270', 'a271', 'a272', 'a273', 'a274', 'a275', 'a276', 'a277', 'a278', 'a279', 'a280', 'a281', 'a282', 'a283', 'a284', 'a285', 'a286', 'a287', 'a288', 'a289', 'a290', 'a291', 'a292', 'a293', 'a294', 'a295', 'a296', 'a297', 'a298', 'a299', 'a300', 'a301', 'a302', 'a303', 'a304', 'a305', 'a306', 'a307', 'a308', 'a309', 'a310', 'a311', 'a312', 'a313', 'a314', 'a315', 'a316', 'a317', 'a318', 'a319', 'a320', 'a321', 'a322', 'a323', 'a324', 'a325', 'a326', 'a327', 'a328', 'a329', 'a330', 'a331', 'a332', 'a333', 'a334', 'a335', 'a336', 'a337', 'a338', 'a339', 'a340', 'a341', 'a342', 'a343', 'a344', 'a345', 'a346', 'a347', 'a348', 'a349', 'a350', 'a351', 
'a352', 'a353', 'a354', 'a355', 'a356', 'a357', 'a358', 'a359', 'a360', 'a361', 'a362', 'a363', 'a364', 'a365', 'a366', 'a367', 'a368', 'a369', 'a370', 'a371', 'a372', 'a373', 'a374', 'a375', 'a376', 'a377', 'a378', 'a379', 'a380', 'a381', 'a382', 'a383', 'a384', 'a385', 'a386', 'a387', 'a388', 'a389', 'a390', 'a391', 'a392', 'a393', 'a394', 'a395', 'a396', 'a397', 'a398', 'a399', 'a400', 'a401', 'a402', 'a403', 'a404', 'a405', 'a406', 'a407', 'a408', 'a409', 'a410', 'a411', 'a412', 'a413', 'a414', 'a415', 'a416', 'a417', 'a418', 'a419', 'a420', 'a421', 'a422', 'a423', 'a424', 'a425', 'a426', 'a427', 'a428', 'a429', 'a430', 'a431', 'a432', 'a433', 'a434', 'a435', 'a436', 'a437', 'a438', 'a439', 'a440', 'a441', 'a442', 'a443', 'a444', 'a445', 'a446', 'a447', 'a448', 'a449', 'a450', 'a451', 'a452', 'a453', 'a454', 'a455', 'a456', 'a457', 'a458', 'a459', 'a460', 'a461', 'a462', 'a463', 'a464', 'a465', 'a466', 'a467', 'a468', 'a469', 'a470', 'a471', 'a472', 'a473', 'a474', 'a475', 'a476', 'a477', 'a478', 'a479', 'a480', 'a481', 'a482', 'a483', 'a484', 'a485', 'a486', 
'a487', 'a488', 'a489', 'a490', 'a491', 'a492', 'a493', 'a494', 'a495', 'a496', 'a497', 'a498', 'a499', 'a500', 'a501', 'a502', 'a503', 'a504', 'a505', 'a506', 'a507', 'a508', 'a509', 'a510', 'a511', 'a512', 'a513', 'a514', 'a515', 'a516', 'a517', 'a518', 'a519', 'a520', 'a521', 'a522', 'a523', 'a524', 'a525', 'a526', 'a527', 'a528', 'a529', 'a530', 'a531', 'a532', 'a533', 'a534', 'a535', 'a536', 'a537', 'a538', 'a539', 'a540', 'a541', 'a542', 'a543', 'a544', 'a545', 'a546', 'a547', 'a548', 'a549', 'a550', 'a551', 'a552', 'a553', 'a554', 'a555', 'a556', 'a557', 'a558', 'a559', 'a560', 'a561', 'a562', 'a563', 'a564', 'a565', 'a566', 'a567', 'a568', 'a569', 'a570', 'a571', 'a572', 'a573', 'a574', 'a575', 'a576', 'a577', 'a578', 'a579', 'a580', 'a581', 'a582', 'a583', 'a584', 'a585', 'a586', 'a587', 'a588', 'a589', 'a590', 'a591', 'a592', 'a593', 'a594', 'a595', 'a596', 'a597', 'a598', 'a599', 'a600', 'a601', 'a602', 'a603', 'a604', 'a605', 'a606', 'a607', 'a608', 'a609', 'a610', 'a611', 'a612', 'a613', 'a614', 'a615', 'a616', 'a617', 'a618', 'a619', 'a620', 'a621', 
'a622', 'a623', 'a624', 'a625', 'a626', 'a627', 'a628', 'a629', 'a630', 'a631', 'a632', 'a633', 'a634', 'a635', 'a636', 'a637', 'a638', 'a639', 'a640', 'a641', 'a642', 'a643', 'a644', 'a645', 'a646', 'a647', 'a648', 'a649', 'a650', 'a651', 'a652', 'a653', 'a654', 'a655', 'a656', 'a657', 'a658', 'a659', 'a660', 'a661', 'a662', 'a663', 'a664', 'a665', 'a666', 'a667', 'a668', 'a669', 'a670', 'a671', 'a672', 'a673', 'a674', 'a675', 'a676', 'a677', 'a678', 'a679', 'a680', 'a681', 'a682', 'a683', 'a684', 'a685', 'a686', 'a687', 'a688', 'a689', 'a690', 'a691', 'a692', 'a693', 'a694', 'a695', 'a696', 'a697', 'a698', 'a699', 'a700', 'a701', 'a702', 'a703', 'a704', 'a705', 'a706', 'a707', 'a708', 'a709', 'a710', 'a711', 'a712', 'a713', 'a714', 'a715', 'a716', 'a717', 'a718', 'a719', 'a720', 'a721', 'a722', 'a723', 'a724', 'a725', 'a726', 'a727', 'a728', 'a729', 'a730', 'a731', 'a732', 'a733', 'a734', 'a735', 'a736', 'a737', 'a738', 'a739', 'a740', 'a741', 'a742', 'a743', 'a744', 'a745', 'a746', 'a747', 'a748', 'a749', 'a750', 'a751', 'a752', 'a753', 'a754', 'a755', 'a756', 
'a757', 'a758', 'a759', 'a760', 'a761', 'a762', 'a763', 'a764', 'a765', 'a766', 'a767', 'a768', 'a769', 'a770', 'a771', 'a772', 'a773', 'a774', 'a775', 'a776', 'a777', 'a778', 'a779', 'a780', 'a781', 'a782', 'a783', 'a784', 'a785', 'a786', 'a787', 'a788', 'a789', 'a790', 'a791', 'a792', 'a793', 'a794', 'a795', 'a796', 'a797', 'a798', 'a799', 'a800', 'a801', 'a802', 'a803', 'a804', 'a805', 'a806', 'a807', 'a808', 'a809', 'a810', 'a811', 'a812', 'a813', 'a814', 'a815', 'a816', 'a817', 'a818', 'a819', 'a820', 'a821', 'a822', 'a823', 'a824', 'a825', 'a826', 'a827', 'a828', 'a829', 'a830', 'a831', 'a832', 'a833', 'a834', 'a835', 'a836', 'a837', 'a838', 'a839', 'a840', 'a841', 'a842', 'a843', 'a844', 'a845', 'a846', 'a847', 'a848', 'a849', 'a850', 'a851', 'a852', 'a853', 'a854', 'a855', 'a856', 'a857', 'a858', 'a859', 'a860', 'a861', 'a862', 'a863', 'a864', 'a865', 'a866', 'a867', 'a868', 'a869', 'a870', 'a871', 'a872', 'a873', 'a874', 'a875', 'a876', 'a877', 'a878', 'a879', 'a880', 'a881', 'a882', 'a883', 'a884', 'a885', 'a886', 'a887', 'a888', 'a889', 'a890', 'a891', 
'a892', 'a893', 'a894', 'a895', 'a896', 'a897', 'a898', 'a899', 'a900', 'a901', 'a902', 'a903', 'a904', 'a905', 'a906', 'a907', 'a908', 'a909', 'a910', 'a911', 'a912', 'a913', 'a914', 'a915', 'a916', 'a917', 'a918', 'a919', 'a920', 'a921', 'a922', 'a923', 'a924', 'a925', 'a926', 'a927', 'a928', 'a929', 'a930', 'a931', 'a932', 'a933', 'a934', 'a935', 'a936', 'a937', 'a938', 'a939', 'a940', 'a941', 'a942', 'a943', 'a944', 'a945', 'a946', 'a947', 'a948', 'a949', 'a950', 'a951', 'a952', 'a953', 'a954', 'a955', 'a956', 'a957', 'a958', 'a959', 'a960', 'a961', 'a962', 'a963', 'a964', 'a965', 'a966', 'a967', 'a968', 'a969', 'a970', 'a971', 'a972', 'a973', 'a974', 'a975', 'a976', 'a977', 'a978', 'a979', 'a980', 'a981', 'a982', 'a983', 'a984', 'a985', 'a986', 'a987', 'a988', 'a989', 'a990', 'a991', 'a992', 'a993', 'a994', 'a995', 'a996', 'a997', 'a998', 'a999', 'a1000', 'a1001', 'a1002', 'a1003', 'a1004', 'a1005', 'a1006', 'a1007', 'a1008', 'a1009', 'a1010', 'a1011', 'a1012', 'a1013', 'a1014', 'a1015', 'a1016', 'a1017', 'a1018', 'a1019', 'a1020', 'a1021', 'a1022', 'a1023', 
'a1024', 'a1025', 'a1026', 'a1027', 'a1028', 'a1029', 'a1030', 'a1031', 'a1032', 'a1033', 'a1034', 'a1035', 'a1036', 'a1037', 'a1038', 'a1039', 'a1040', 'a1041', 'a1042', 'a1043', 'a1044', 'a1045', 'a1046', 'a1047', 'a1048', 'a1049', 'a1050', 'a1051', 'a1052', 'a1053', 
'a1054', 'a1055', 'a1056', 'a1057', 'a1058', 'a1059', 'a1060', 'a1061', 'a1062', 'a1063', 'a1064', 'a1065', 'a1066', 'a1067', 'a1068', 'a1069', 'a1070', 'a1071', 'a1072', 'a1073', 'a1074', 'a1075', 'a1076', 'a1077', 'a1078', 'a1079', 'a1080', 'a1081', 'a1082', 'a1083', 
'a1084', 'a1085', 'a1086', 'a1087', 'a1088', 'a1089', 'a1090', 'a1091', 'a1092', 'a1093', 'a1094', 'a1095', 'a1096', 'a1097', 'a1098', 'a1099', 'a1100', 'a1101', 'a1102', 'a1103', 'a1104', 'a1105', 'a1106', 'a1107', 'a1108', 'a1109', 'a1110', 'a1111', 'a1112', 'a1113', 
'a1114', 'a1115', 'a1116', 'a1117', 'a1118', 'a1119', 'a1120', 'a1121', 'a1122', 'a1123', 'a1124', 'a1125', 'a1126', 'a1127', 'a1128', 'a1129', 'a1130', 'a1131', 'a1132', 'a1133', 'a1134', 'a1135', 'a1136', 'a1137', 'a1138', 'a1139', 'a1140', 'a1141', 'a1142', 'a1143', 
'a1144', 'a1145', 'a1146', 'a1147', 'a1148', 'a1149', 'a1150', 'a1151', 'a1152', 'a1153', 'a1154', 'a1155', 'a1156', 'a1157', 'a1158', 'a1159', 'a1160', 'a1161', 'a1162', 'a1163', 'a1164', 'a1165', 'a1166', 'a1167', 'a1168', 'a1169', 'a1170', 'a1171', 'a1172', 'a1173', 
'a1174', 'a1175', 'a1176', 'a1177', 'a1178', 'a1179', 'a1180', 'a1181', 'a1182', 'a1183', 'a1184', 'a1185', 'a1186', 'a1187', 'a1188', 'a1189', 'a1190', 'a1191', 'a1192', 'a1193', 'a1194', 'a1195', 'a1196', 'a1197', 'a1198', 'a1199', 'a1200', 'a1201', 'a1202', 'a1203', 
'a1204', 'a1205', 'a1206', 'a1207', 'a1208', 'a1209', 'a1210', 'a1211', 'a1212', 'a1213', 'a1214', 'a1215', 'a1216', 'a1217', 'a1218', 'a1219', 'a1220', 'a1221', 'a1222', 'a1223', 'a1224', 'a1225', 'a1226', 'a1227', 'a1228', 'a1229', 'a1230', 'a1231', 'a1232', 'a1233', 
'a1234', 'a1235', 'a1236', 'a1237', 'a1238', 'a1239', 'a1240', 'a1241', 'a1242', 'a1243', 'a1244', 'a1245', 'a1246', 'a1247', 'a1248', 'a1249', 'a1250', 'a1251', 'a1252', 'a1253', 'a1254', 'a1255', 'a1256', 'a1257', 'a1258', 'a1259', 'a1260', 'a1261', 'a1262', 'a1263', 
'a1264', 'a1265', 'a1266', 'a1267', 'a1268', 'a1269', 'a1270', 'a1271', 'a1272', 'a1273', 'a1274', 'a1275', 'a1276', 'a1277', 'a1278', 'a1279', 'a1280', 'a1281', 'a1282', 'a1283', 'a1284', 'a1285', 'a1286', 'a1287', 'a1288', 'a1289', 'a1290', 'a1291', 'a1292', 'a1293', 
'a1294', 'a1295', 'a1296', 'a1297', 'a1298', 'a1299', 'a1300', 'a1301', 'a1302', 'a1303', 'a1304', 'a1305', 'a1306', 'a1307', 'a1308', 'a1309', 'a1310', 'a1311', 'a1312', 'a1313', 'a1314', 'a1315', 'a1316', 'a1317', 'a1318', 'a1319', 'a1320', 'a1321', 'a1322', 'a1323', 
'a1324', 'a1325', 'a1326', 'a1327', 'a1328', 'a1329', 'a1330', 'a1331', 'a1332', 'a1333', 'a1334', 'a1335', 'a1336', 'a1337', 'a1338', 'a1339', 'a1340', 'a1341', 'a1342', 'a1343', 'a1344', 'a1345', 'a1346', 'a1347', 'a1348', 'a1349', 'a1350', 'a1351', 'a1352', 'a1353', 
'a1354', 'a1355', 'a1356', 'a1357', 'a1358', 'a1359', 'a1360', 'a1361', 'a1362', 'a1363', 'a1364', 'a1365', 'a1366', 'a1367', 'a1368', 'a1369', 'a1370', 'a1371', 'a1372', 'a1373', 'a1374', 'a1375', 'a1376', 'a1377', 'a1378', 'a1379', 'a1380', 'a1381', 'a1382', 'a1383', 
'a1384', 'a1385', 'a1386', 'a1387', 'a1388', 'a1389', 'a1390', 'a1391', 'a1392', 'a1393', 'a1394', 'a1395', 'a1396', 'a1397', 'a1398', 'a1399', 'a1400', 'a1401', 'a1402', 'a1403', 'a1404', 'a1405', 'a1406', 'a1407', 'a1408', 'a1409', 'a1410', 'a1411', 'a1412', 'a1413', 
'a1414', 'a1415', 'a1416', 'a1417', 'a1418', 'a1419', 'a1420', 'a1421', 'a1422', 'a1423', 'a1424', 'a1425', 'a1426', 'a1427', 'a1428', 'a1429', 'a1430', 'a1431', 'a1432', 'a1433', 'a1434', 'a1435', 'a1436', 'a1437', 'a1438', 'a1439', 'a1440', 'a1441', 'a1442', 'a1443', 
'a1444', 'a1445', 'a1446', 'a1447', 'a1448', 'a1449', 'a1450', 'a1451', 'a1452', 'a1453', 'a1454', 'a1455', 'a1456', 'a1457', 'a1458', 'a1459', 'a1460', 'a1461', 'a1462', 'a1463', 'a1464', 'a1465', 'a1466', 'a1467', 'a1468', 'a1469', 'a1470', 'a1471', 'a1472', 'a1473', 
'a1474', 'a1475', 'a1476', 'a1477', 'a1478', 'a1479', 'a1480', 'a1481', 'a1482', 'a1483', 'a1484', 'a1485', 'a1486', 'a1487', 'a1488', 'a1489', 'a1490', 'a1491', 'a1492', 'a1493', 'a1494', 'a1495', 'a1496', 'a1497', 'a1498', 'a1499', 'a1500', 'a1501', 'a1502', 'a1503', 
'a1504', 'a1505', 'a1506', 'a1507', 'a1508', 'a1509', 'a1510', 'a1511', 'a1512', 'a1513', 'a1514', 'a1515', 'a1516', 'a1517', 'a1518', 'a1519', 'a1520', 'a1521', 'a1522', 'a1523', 'a1524', 'a1525', 'a1526', 'a1527', 'a1528', 'a1529', 'a1530', 'a1531', 'a1532', 'a1533', 
'a1534', 'a1535', 'a1536', 'a1537', 'a1538', 'a1539', 'a1540', 'a1541', 'a1542', 'a1543', 'a1544', 'a1545', 'a1546', 'a1547', 'a1548', 'a1549', 'a1550', 'a1551', 'a1552', 'a1553', 'a1554', 'a1555', 'a1556', 'a1557', 'a1558', 'a1559', 'a1560', 'a1561', 'a1562', 'a1563', 
'a1564', 'a1565', 'a1566', 'a1567', 'a1568', 'a1569', 'a1570', 'a1571', 'a1572', 'a1573', 'a1574', 'a1575', 'a1576', 'a1577', 'a1578', 'a1579', 'a1580', 'a1581', 'a1582', 'a1583', 'a1584', 'a1585', 'a1586', 'a1587', 'a1588', 'a1589', 'a1590', 'a1591', 'a1592', 'a1593', 
'a1594', 'a1595', 'a1596', 'a1597', 'a1598', 'a1599', 'a1600', 'a1601', 'a1602', 'a1603', 'a1604', 'a1605', 'a1606', 'a1607', 'a1608', 'a1609', 'a1610', 'a1611', 'a1612', 'a1613', 'a1614', 'a1615', 'a1616', 'a1617', 'a1618', 'a1619', 'a1620', 'a1621', 'a1622', 'a1623', 
'a1624', 'a1625', 'a1626', 'a1627', 'a1628', 'a1629', 'a1630', 'a1631', 'a1632', 'a1633', 'a1634', 'a1635', 'a1636', 'a1637', 'a1638', 'a1639', 'a1640', 'a1641', 'a1642', 'a1643', 'a1644', 'a1645', 'a1646', 'a1647', 'a1648', 'a1649', 'a1650', 'a1651', 'a1652', 'a1653', 
'a1654', 'a1655', 'a1656', 'a1657', 'a1658', 'a1659', 'a1660', 'a1661', 'a1662', 'a1663', 'a1664', 'a1665', 'a1666', 'a1667', 'a1668', 'a1669', 'a1670', 'a1671', 'a1672', 'a1673', 'a1674', 'a1675', 'a1676', 'a1677', 'a1678', 'a1679', 'a1680', 'a1681', 'a1682', 'a1683', 
'a1684', 'a1685', 'a1686', 'a1687', 'a1688', 'a1689', 'a1690', 'a1691', 'a1692', 'a1693', 'a1694', 'a1695', 'a1696', 'a1697', 'a1698', 'a1699', 'a1700', 'a1701', 'a1702', 'a1703', 'a1704', 'a1705', 'a1706', 'a1707', 'a1708', 'a1709', 'a1710', 'a1711', 'a1712', 'a1713', 
'a1714', 'a1715', 'a1716', 'a1717', 'a1718', 'a1719', 'a1720', 'a1721', 'a1722', 'a1723', 'a1724', 'a1725', 'a1726', 'a1727', 'a1728', 'a1729', 'a1730', 'a1731', 'a1732', 'a1733', 'a1734', 'a1735', 'a1736', 'a1737', 'a1738', 'a1739', 'a1740', 'a1741', 'a1742', 'a1743', 
'a1744', 'a1745', 'a1746', 'a1747', 'a1748', 'a1749', 'a1750', 'a1751', 'a1752', 'a1753', 'a1754', 'a1755', 'a1756', 'a1757', 'a1758', 'a1759', 'a1760', 'a1761', 'a1762', 'a1763', 'a1764', 'a1765', 'a1766', 'a1767', 'a1768', 'a1769', 'a1770', 'a1771', 'a1772', 'a1773', 
'a1774', 'a1775', 'a1776', 'a1777', 'a1778', 'a1779', 'a1780', 'a1781', 'a1782', 'a1783', 'a1784', 'a1785', 'a1786', 'a1787', 'a1788', 'a1789', 'a1790', 'a1791', 'a1792', 'a1793', 'a1794', 'a1795', 'a1796', 'a1797', 'a1798', 'a1799', 'a1800', 'a1801', 'a1802', 'a1803', 
'a1804', 'a1805', 'a1806', 'a1807', 'a1808', 'a1809', 'a1810', 'a1811', 'a1812', 'a1813', 'a1814', 'a1815', 'a1816', 'a1817', 'a1818', 'a1819', 'a1820', 'a1821', 'a1822', 'a1823', 'a1824', 'a1825', 'a1826', 'a1827', 'a1828', 'a1829', 'a1830', 'a1831', 'a1832', 'a1833', 
'a1834', 'a1835', 'a1836', 'a1837', 'a1838', 'a1839', 'a1840', 'a1841', 'a1842', 'a1843', 'a1844', 'a1845', 'a1846', 'a1847', 'a1848', 'a1849', 'a1850', 'a1851', 'a1852', 'a1853', 'a1854', 'a1855', 'a1856', 'a1857', 'a1858', 'a1859', 'a1860', 'a1861', 'a1862', 'a1863', 
'a1864', 'a1865', 'a1866', 'a1867', 'a1868', 'a1869', 'a1870', 'a1871', 'a1872', 'a1873', 'a1874', 'a1875', 'a1876', 'a1877', 'a1878', 'a1879', 'a1880', 'a1881', 'a1882', 'a1883', 'a1884', 'a1885', 'a1886', 'a1887', 'a1888', 'a1889', 'a1890', 'a1891', 'a1892', 'a1893', 
'a1894', 'a1895', 'a1896', 'a1897', 'a1898', 'a1899', 'a1900', 'a1901', 'a1902', 'a1903', 'a1904', 'a1905', 'a1906', 'a1907', 'a1908', 'a1909', 'a1910', 'a1911', 'a1912', 'a1913', 'a1914', 'a1915', 'a1916', 'a1917', 'a1918', 'a1919', 'a1920', 'a1921', 'a1922', 'a1923', 
'a1924', 'a1925', 'a1926', 'a1927', 'a1928', 'a1929', 'a1930', 'a1931', 'a1932', 'a1933', 'a1934', 'a1935', 'a1936', 'a1937', 'a1938', 'a1939', 'a1940', 'a1941', 'a1942', 'a1943', 'a1944', 'a1945', 'a1946', 'a1947', 'a1948', 'a1949', 'a1950', 'a1951', 'a1952', 'a1953', 
'a1954', 'a1955', 'a1956', 'a1957', 'a1958', 'a1959', 'a1960', 'a1961', 'a1962', 'a1963', 'a1964', 'a1965', 'a1966', 'a1967', 'a1968', 'a1969', 'a1970', 'a1971', 'a1972', 'a1973', 'a1974', 'a1975', 'a1976', 'a1977', 'a1978', 'a1979', 'a1980', 'a1981', 'a1982', 'a1983', 
'a1984', 'a1985', 'a1986', 'a1987', 'a1988', 'a1989', 'a1990', 'a1991', 'a1992', 'a1993', 'a1994', 'a1995', 'a1996', 'a1997', 'a1998', 'a1999']


def isUnitary(rule, variables):
	if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
		return True
	return False

def isSimple(rule):
	if rule[left] in V and rule[right][0] in K and len(rule[right]) == 1:
		return True
	return False


for nonTerminal in V:
	if nonTerminal in variablesJar:
		variablesJar.remove(nonTerminal)

#Add S0->S rule––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––START
def START(productions, variables):
	variables.append('S0')
	return [('S0', [variables[0]])] + productions
#Remove rules containing both terms and variables, like A->Bc, replacing by A->BZ and Z->c–––––––––––TERM
def TERM(productions, variables):
	newProductions = []
	for production in productions:
		#check if the production is simple
		if isSimple(production):
			#in that case there is nothing to change
			newProductions.append(production)
		else:
			for term in K:
				for index, value in enumerate(production[right]):
					if term == value:
						#it's created a new production vaiable->term and added to it 
						var = variablesJar.pop(0)

						#Variables set it's updated adding new variable
						V.append(var)
						newProductions.append( (var, [term]) )
						
						production[right][index] = var
			newProductions.append( (production[left], production[right]) )
			
	#merge created set and the introduced rules
	return newProductions

#Eliminate non unitry rules––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––BIN
def BIN(productions, variables):
	result = []
	for production in productions:
		k = len(production[right])
		#newVar = production[left]
		if k <= 2:
			result.append( production )
		else:
			newVar = variablesJar.pop(0)
			variables.append(newVar+'1')
			result.append( (production[left], [production[right][0]]+[newVar+'1']) )
			i = 1
			for i in range(1, k-2 ):
				var, var2 = newVar+str(i), newVar+str(i+1)
				variables.append(var2)
				result.append( (var, [production[right][i], var2]) )
			result.append( (newVar+str(k-2), production[right][k-2:k]) ) 
	return result
	

#Delete non terminal rules–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––DEL
def DEL(productions):
	newSet = []
	#seekAndDestroy throw back in:
	#        – outlaws all left side of productions such that right side is equal to the outlaw
	#        – productions the productions without outlaws 
	outlaws, productions = helper.seekAndDestroy(target='e', productions=productions)
	#add new reformulation of old rules
	for outlaw in outlaws:
		#consider every production: old + new resulting important when more than one outlaws are in the same prod.
		for production in productions + [e for e in newSet if e not in productions]:
			#if outlaw is present in the right side of a rule
			if outlaw in production[right]:
				#the rule is rewrited in all combination of it, rewriting "e" rather than outlaw
				#this cycle prevent to insert duplicate rules
				newSet = newSet + [e for e in  helper.rewrite(outlaw, production) if e not in newSet]

	#add unchanged rules and return
	return newSet + ([productions[i] for i in range(len(productions)) 
							if productions[i] not in newSet])

def unit_routine(rules, variables):
	unitaries, result = [], []
	# Cek apakah rule unary
	for aRule in rules:
		if isUnitary(aRule, variables):
			unitaries.append( (aRule[left], aRule[right][0]) )
		else:
			result.append(aRule)
	# Cek apakah bisa digantikan
	for uni in unitaries:
		for rule in rules:
			if uni[right]==rule[left] and uni[left]!=rule[left]:
				result.append( (uni[left],rule[right]) )
	
	return result

def UNIT(productions, variables):
	i = 0
	result = unit_routine(productions, variables)
	tmp = unit_routine(result, variables)
	while result != tmp and i < 1000:
		result = unit_routine(tmp, variables)
		tmp = unit_routine(result, variables)
		i+=1
	return result


if __name__ == '__main__':
	if len(sys.argv) > 1:
		modelPath = str(sys.argv[1])
	else:
		modelPath = 'cfg.txt'
	
	K, V, Productions = helper.loadModel( modelPath )

	Productions = START(Productions, variables=V)
	Productions = TERM(Productions, variables=V)
	Productions = BIN(Productions, variables=V)
	Productions = DEL(Productions)
	Productions = UNIT(Productions, variables=V)
	
	print( helper.prettyForm(Productions) )
	print( len(Productions) )
	open('cnf.txt', 'w').write(	helper.prettyForm(Productions) )