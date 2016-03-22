#!/usr/local/bin/python3
# -*- coding=utf-8 -*-

import os, io, sys, re, time, json, base64
import webbrowser, urllib.request

ChinaStockIndividualList = ['sz002345', 'sz002021', 'sh000953', 'sz000895', 'sh600518', 'sh600173', 'sh600120',
                            'sz399374', 'sh600969', 'sh600211', 'sh600125', 'sh600123', 'sh600725', 'sz000045',
                            'sh600351', 'sz002193', 'sh600433', 'sz002214', 'sh600241', 'sz000717', 'sh600595',
                            'sh600499', 'sh000036', 'sz000527', 'sh600436', 'sh000925', 'sh600866', 'sz000893',
                            'sz300059', 'sz002178', 'sz399934', 'sz399107', 'sh600793', 'sh600112', 'sh600624',
                            'sh600303', 'sz000650', 'sz000761', 'sz002187', 'sh600893', 'sz002334', 'sz002242',
                            'sh600267', 'sh600182', 'sh600490', 'sh600738', 'sh600771', 'sz002174', 'sh000027',
                            'sz399135', 'sh600603', 'sh600151', 'sz002308', 'sh600992', 'sh600428', 'sh600339',
                            'sh600371', 'sh600875', 'sz000024', 'sh600470', 'sz000800', 'sz002239', 'sh600594',
                            'sh600496', 'sz000011', 'sh600856', 'sh601958', 'sz000596', 'sh600493', 'sh601169',
                            'sz000058', 'sz000006', 'sh600292', 'sz399949', 'sz002034', 'sz300049', 'sh600657',
                            'sz002220', 'sh601888', 'sz002017', 'sh000005', 'sz000985', 'sz002143', 'sh600897',
                            'sz399957', 'sh600302', 'sh600631', 'sh601628', 'sh601398', 'sh600321', 'sz002188',
                            'sh600711', 'sz399943', 'sh600978', 'sh600398', 'sz000667', 'sz002004', 'sz000019',
                            'sz002210', 'sz002216', 'sh600291', 'sh600071', 'sz000903', 'sh600537', 'sh600756',
                            'sh600867', 'sh600466', 'sz000659', 'sh600068', 'sz000826', 'sz399951', 'sz399002',
                            'sz399305', 'sh600993', 'sz002202', 'sh600362', 'sh600373', 'sh601008', 'sz002209',
                            'sz000965', 'sz002081', 'sh600589', 'sh600836', 'sz000428', 'sz300025', 'sh601166',
                            'sz002269', 'sz002287', 'sh600039', 'sh600410', 'sh600685', 'sz000990', 'sz300019',
                            'sh600391', 'sh600741', 'sz002067', 'sz002354', 'sz399310', 'sz002227', 'sh600985',
                            'sh600036', 'sh600439', 'sh600389', 'sz300016', 'sh600790', 'sz000578', 'sh600577',
                            'sh600883', 'sh600894', 'sz002024', 'sz002337', 'sz000519', 'sz000547', 'sh600338',
                            'sz002273', 'sh600309', 'sh600572', 'sz000825', 'sh600839', 'sh600221', 'sz399356',
                            'sh600287', 'sz002228', 'sz000005', 'sz300001', 'sz000159', 'sh600995', 'sz002326',
                            'sh600586', 'sh601899', 'sh600990', 'sz002085', 'sz002182', 'sh600546', 'sh600031',
                            'sh600824', 'sz002038', 'sh600099', 'sz000541', 'sz000755', 'sh600029', 'sz002046',
                            'sh600736', 'sh600353', 'sz000976', 'sz000417', 'sz300014', 'sz002170', 'sz000831',
                            'sz002247', 'sz002003', 'sz002226', 'sh601299', 'sz000563', 'sz002126', 'sz399905',
                            'sz000728', 'sh600528', 'sz000514', 'sz002324', 'sh600560', 'sh600376', 'sz002328',
                            'sh600801', 'sz000029', 'sz000710', 'sz000909', 'sz002150', 'sz300026', 'sh600381',
                            'sh600170', 'sz002229', 'sz000568', 'sz000629', 'sz000630', 'sh600312', 'sh600369',
                            'sz002068', 'sh600086', 'sz000913', 'sh000012', 'sz002259', 'sh600000', 'sz002130',
                            'sz002377', 'sh000062', 'sz000538', 'sz000628', 'sz002149', 'sh600118', 'sh601002',
                            'sh600485', 'sh600865', 'sh600185', 'sh600512', 'sz000679', 'sz300036', 'sz000581',
                            'sh600270', 'sh600573', 'sz399932', 'sh600220', 'sz000900', 'sz000422', 'sh601186',
                            'sz000777', 'sz002050', 'sh600375', 'sz002107', 'sh000300', 'sz000819', 'sh600133',
                            'sh600552', 'sz399960', 'sz002250', 'sh580027', 'sh600967', 'sh600310', 'sh600548',
                            'sh600863', 'sh600165', 'sh600830', 'sh600729', 'sh600634', 'sh600215', 'sh999997',
                            'sz000692', 'sz002278', 'sh600831', 'sz300035', 'sh600810', 'sh600275', 'sh600323',
                            'sz000829', 'sh000002', 'sh600522', 'sz399915', 'sz000716', 'sh601601', 'sz399929',
                            'sh600579', 'sz000611', 'sz002086', 'sz000503', 'sz002051', 'sz002261', 'sz000510',
                            'sz002071', 'sh600246', 'sz002349', 'sz002083', 'sz002096', 'sz000022', 'sz002282',
                            'sz399007', 'sz002183', 'sh600965', 'sh601727', 'sh600051', 'sz002063', 'sz000889',
                            'sz002378', 'sh601518', 'sh600266', 'sz000557', 'sh600370', 'sh600581', 'sz000023',
                            'sz002098', 'sz399001', 'sh600663', 'sz399925', 'sz300004', 'sz002205', 'sz000795',
                            'sz000607', 'sh000043', 'sh601390', 'sz000738', 'sh600704', 'sh600510', 'sz300042',
                            'sh600090', 'sz000899', 'sh600505', 'sz000008', 'sh600677', 'sh600423', 'sh600408',
                            'sh600228', 'sz002039', 'sh600260', 'sh601318', 'sz002127', 'sz002123', 'sh600804',
                            'sz001696', 'sz002342', 'sh600069', 'sz000886', 'sz000736', 'sz000540', 'sh600656',
                            'sz000597', 'sh600489', 'sh000923', 'sz002159', 'sz002031', 'sh000957', 'sh110006',
                            'sz002340', 'sh600300', 'sh600820', 'sh600683', 'sh600726', 'sz000938', 'sh000945',
                            'sh600288', 'sz000910', 'sz000753', 'sh600739', 'sz399926', 'sz399328', 'sz399311',
                            'sh600156', 'sz000927', 'sh600027', 'sh601919', 'sz000685', 'sh600202', 'sh110598',
                            'sh600458', 'sh600237', 'sh600137', 'sz000813', 'sz002357', 'sh600828', 'sz000748',
                            'sz000838', 'sz399139', 'sz300010', 'sz000539', 'sz000615', 'sz000537', 'sz399924',
                            'sz002049', 'sh600706', 'sh600976', 'sz000862', 'sz002106', 'sz399108', 'sh600850',
                            'sh600416', 'sz002079', 'sh600399', 'sh600549', 'sh600064', 'sz002218', 'sz002167',
                            'sh600748', 'sz000905', 'sz000027', 'sh600486', 'sz000666', 'sz000712', 'sz002369',
                            'sh600651', 'sh600171', 'sz002104', 'sz000558', 'sz399351', 'sh000937', 'sh000055',
                            'sz399952', 'sz000767', 'sz002124', 'sz399920', 'sz399908', 'sz002047', 'sh600175',
                            'sz000040', 'sz300029', 'sh000034', 'sz000517', 'sz002290', 'sz000801', 'sh600988',
                            'sz002222', 'sh600961', 'sh600335', 'sz002323', 'sz300054', 'sh600085', 'sh600012',
                            'sh600089', 'sh601168', 'sh600618', 'sh000058', 'sz399902', 'sz002272', 'sh600761',
                            'sz000420', 'sh600213', 'sz002358', 'sz399371', 'sh600833', 'sz002113', 'sh600614',
                            'sz002213', 'sh600783', 'sh600138', 'sh600529', 'sz002044', 'sz002070', 'sh600802',
                            'sh600396', 'sz002211', 'sz002304', 'sh600311', 'sh000902', 'sh600979', 'sz002095',
                            'sz000010', 'sh601991', 'sh600861', 'sz399345', 'sz000930', 'sz399358', 'sh601117',
                            'sz002236', 'sh600690', 'sz399130', 'sz000401', 'sh600319', 'sz000550', 'sh000920',
                            'sh600871', 'sh600540', 'sz002270', 'sh600754', 'sh000037', 'sh600868', 'sz399348',
                            'sh600405', 'sh600435', 'sh600162', 'sh600740', 'sz000504', 'sz000880', 'sz000068',
                            'sz002292', 'sh000914', 'sh600818', 'sh600152', 'sz000570', 'sz399373', 'sz000564',
                            'sh600190', 'sz002311', 'sh600088', 'sz000605', 'sz000892', 'sh600636', 'sz002064',
                            'sz000677', 'sh600268', 'sh600843', 'sh000928', 'sz002189', 'sz000088', 'sh600745',
                            'sh600081', 'sz300062', 'sz002360', 'sz002327', 'sh600276', 'sz000090', 'sz002356',
                            'sz000721', 'sz300034', 'sh601998', 'sz000507', 'sz000413', 'sz002365', 'sh000901',
                            'sh600073', 'sh600225', 'sz300006', 'sh600115', 'sz002241', 'sz002249', 'sz000735',
                            'sh600113', 'sh600075', 'sz002372', 'sh600508', 'sz000876', 'sh600097', 'sh600059',
                            'sz399315', 'sz399950', 'sh600243', 'sz000559', 'sz002310', 'sh600509', 'sh000031',
                            'sh600679', 'sh601107', 'sh600497', 'sh600422', 'sh600769', 'sh600121', 'sh600293',
                            'sh600626', 'sh600582', 'sz399912', 'sz002351', 'sh600553', 'sh600163', 'sz000572',
                            'sz000915', 'sz002175', 'sz000627', 'sh600284', 'sh000940', 'sh600809', 'sh600326',
                            'sh600620', 'sh600348', 'sh600050', 'sz000524', 'sz000897', 'sh600848', 'sh000064',
                            'sh600523', 'sz000928', 'sh600826', 'sz002185', 'sh580026', 'sz002066', 'sz000822',
                            'sz002375', 'sh600350', 'sh600877', 'sz399939', 'sh600169', 'sz000020', 'sh600306',
                            'sz000069', 'sz300047', 'sz300031', 'sh110007', 'sh600271', 'sh600845', 'sz002062',
                            'sz000533', 'sz000070', 'sh600048', 'sh600131', 'sh000021', 'sz002301', 'sh600697',
                            'sh600167', 'sz000593', 'sh000038', 'sz000632', 'sh600768', 'sh000029', 'sz002262',
                            'sz002321', 'sz002299', 'sz399930', 'sz000061', 'sh600588', 'sz002087', 'sh600006',
                            'sh000023', 'sz000923', 'sh600886', 'sh600056', 'sz000782', 'sz000338', 'sz000017',
                            'sz000887', 'sh600329', 'sh600449', 'sh600240', 'sh600596', 'sh600765', 'sz000656',
                            'sz399332', 'sh000944', 'sh600087', 'sh600699', 'sh600892', 'sz000811', 'sz000815',
                            'sz002194', 'sz002207', 'sz002093', 'sz002347', 'sz002322', 'sh600346', 'sz000407',
                            'sz000933', 'sz002153', 'sz399324', 'sz002285', 'sz002325', 'sz399927', 'sz002118',
                            'sh600822', 'sh600290', 'sz000851', 'sh600617', 'sh600187', 'sz002148', 'sh000039',
                            'sz000153', 'sh600661', 'sz125960', 'sz300011', 'sz399330', 'sh600766', 'sz000099',
                            'sz399366', 'sz002343', 'sh600858', 'sh000931', 'sz000949', 'sz000731', 'sh000922',
                            'sz002280', 'sh600889', 'sz000671', 'sz399300', 'sz399928', 'sz002061', 'sh000952',
                            'sz002335', 'sz002161', 'sz000665', 'sh600879', 'sz002155', 'sh600021', 'sh600535',
                            'sh000020', 'sh600857', 'sz399339', 'sh600052', 'sz000301', 'sz399334', 'sh000018',
                            'sh600862', 'sh600721', 'sz000729', 'sz002306', 'sh600531', 'sz000652', 'sz000608',
                            'sh600622', 'sz399901', 'sh600247', 'sh601666', 'sh600420', 'sz000501', 'sz000833',
                            'sh600232', 'sh600481', 'sz000530', 'sz000969', 'sz000623', 'sz000823', 'sh601006',
                            'sh600004', 'sh000028', 'sh600675', 'sh600587', 'sh600297', 'sz002192', 'sh000030',
                            'sh110003', 'sh600511', 'sh600722', 'sz000970', 'sh601808', 'sz000877', 'sz002191',
                            'sh600158', 'sh600387', 'sz002201', 'sh600193', 'sz399903', 'sh601898', 'sz399323',
                            'sz002101', 'sh600707', 'sz002015', 'sz000021', 'sz000860', 'sh600102', 'sz000828',
                            'sh000956', 'sz000968', 'sh601866', 'sz002026', 'sh600718', 'sz002374', 'sh600259',
                            'sh000011', 'sz002053', 'sz002009', 'sz002105', 'sh000063', 'sz000039', 'sz002058',
                            'sz399190', 'sh600074', 'sz399220', 'sh000905', 'sz000725', 'sz399907', 'sh600104',
                            'sz002231', 'sh600602', 'sh600999', 'sh000936', 'sh600567', 'sh600332', 'sz002266',
                            'sz000565', 'sh600590', 'sh000001', 'sh600444', 'sh000947', 'sh600261', 'sh600695',
                            'sz399367', 'sz399132', 'sz000573', 'sh600462', 'sh600078', 'sh600098', 'sz000026',
                            'sz000788', 'sh600650', 'sz002117', 'sh000019', 'sh600787', 'sz002152', 'sh600807',
                            'sz399370', 'sz000790', 'sh000033', 'sh600035', 'sh600400', 'sh601179', 'sh600757',
                            'sz000806', 'sz002198', 'sz000155', 'sz000551', 'sh000016', 'sh600644', 'sz000002',
                            'sh600269', 'sz000050', 'sh600289', 'sh600724', 'sz002172', 'sh600207', 'sh000942',
                            'sz000089', 'sh600197', 'sz002054', 'sz000797', 'sh600533', 'sh600714', 'sz002333',
                            'sz399911', 'sz125709', 'sz002129', 'sz000033', 'sz002232', 'sh600785', 'sh600885',
                            'sz399180', 'sz000049', 'sz300003', 'sh600744', 'sz399338', 'sh600781', 'sh600716',
                            'sh600301', 'sz000048', 'sz300041', 'sz399318', 'sh000951', 'sz000096', 'sz399935',
                            'sh600256', 'sz300022', 'sh600775', 'sz000690', 'sh600693', 'sh600652', 'sz002352',
                            'sh600500', 'sz000700', 'sz000616', 'sz000996', 'sz002300', 'sz300052', 'sz000807',
                            'sh600285', 'sz000820', 'sz000715', 'sz000869', 'sz000960', 'sh600538', 'sz002179',
                            'sz399335', 'sh000061', 'sh600475', 'sz002208', 'sz000861', 'sz002314', 'sh600501',
                            'sh600503', 'sh600114', 'sz000951', 'sh600382', 'sz000766', 'sz399004', 'sh600011',
                            'sz002286', 'sz002295', 'sh600665', 'sz300058', 'sz002074', 'sh600189', 'sh600448',
                            'sz002056', 'sz002302', 'sh600107', 'sh600803', 'sh600498', 'sh600105', 'sz000571',
                            'sz399360', 'sh600403', 'sz000848', 'sh000941', 'sz000796', 'sz002320', 'sz399138',
                            'sh600767', 'sh600630', 'sh000040', 'sz002016', 'sz000661', 'sz000429', 'sz002370',
                            'sz000523', 'sh601111', 'sz000890', 'sz002091', 'sh600613', 'sh600884', 'sh600755',
                            'sh600415', 'sh600468', 'sh600230', 'sh600773', 'sz300063', 'sh600359', 'sz002160',
                            'sh600336', 'sz000513', 'sh601328', 'sz002035', 'sh600066', 'sz002350', 'sh601989',
                            'sh600686', 'sh600063', 'sh600377', 'sh600717', 'sz000967', 'sz399936', 'sh601618',
                            'sh600008', 'sh600096', 'sh601766', 'sz000606', 'sz002140', 'sh000911', 'sz000759',
                            'sz399914', 'sh600609', 'sz000651', 'sz000760', 'sz002122', 'sz000408', 'sh600580',
                            'sh600576', 'sh600566', 'sh000935', 'sh600555', 'sz002042', 'sz002245', 'sh600209',
                            'sz399953', 'sh600676', 'sh600735', 'sz000821', 'sz000043', 'sh600229', 'sz399357',
                            'sz000702', 'sh600891', 'sh600307', 'sh601106', 'sz002180', 'sz002252', 'sz000882',
                            'sh600689', 'sz002013', 'sz002052', 'sz000762', 'sz002133', 'sz000531', 'sz000421',
                            'sz399362', 'sh000921', 'sz002077', 'sh600178', 'sz002215', 'sz000901', 'sh000926',
                            'sh600030', 'sz000673', 'sz002361', 'sz002156', 'sz000885', 'sz399337', 'sz002248',
                            'sz002022', 'sh000010', 'sz000534', 'sh600619', 'sz000709', 'sh000017', 'sh600477',
                            'sz000919', 'sz002114', 'sh600033', 'sz002059', 'sz300012', 'sh000930', 'sz002008',
                            'sz000922', 'sh000906', 'sh600637', 'sz000687', 'sz000993', 'sz000063', 'sz000516',
                            'sh000908', 'sh600874', 'sz300032', 'sh600250', 'sz002223', 'sz002319', 'sh600611',
                            'sh601005', 'sh600330', 'sz002317', 'sh600438', 'sh000950', 'sz000723', 'sh600737',
                            'sz399005', 'sh600233', 'sz002355', 'sh600507', 'sz300061', 'sh600776', 'sz002318',
                            'sz002181', 'sz000158', 'sh000917', 'sh601939', 'sh600333', 'sh600502', 'sh600694',
                            'sz000555', 'sh600621', 'sz000028', 'sh000907', 'sz399320', 'sz002135', 'sz399364',
                            'sz000932', 'sh600219', 'sh600606', 'sh600392', 'sz002238', 'sz002073', 'sz399948',
                            'sh600393', 'sh600806', 'sz002364', 'sz002048', 'sh000924', 'sz000609', 'sz002338',
                            'sh600257', 'sz002225', 'sh600117', 'sh600539', 'sz300027', 'sz002072', 'sh600198',
                            'sh600782', 'sz300048', 'sh600987', 'sz399333', 'sz300037', 'sz000836', 'sh600298',
                            'sh600777', 'sz000554', 'sh600418', 'sh600317', 'sh600135', 'sh600463', 'sz000998',
                            'sz000635', 'sz002146', 'sh000916', 'sh600629', 'sz002256', 'sh601801', 'sh601999',
                            'sz399210', 'sh600598', 'sz000548', 'sh600770', 'sh600823', 'sz300056', 'sz002224',
                            'sh000932', 'sz399910', 'sz000418', 'sz000997', 'sh600616', 'sz002001', 'sh600061',
                            'sz002309', 'sz399942', 'sh000912', 'sz000669', 'sh600203', 'sz000601', 'sh600645',
                            'sh600962', 'sh601699', 'sh600543', 'sz002138', 'sh000026', 'sh600615', 'sz002329',
                            'sh600101', 'sz000929', 'sh600037', 'sh600658', 'sz399481', 'sz002102', 'sh600426',
                            'sh000045', 'sz399944', 'sh600478', 'sz000780', 'sz300045', 'sz002246', 'sz000961',
                            'sh600385', 'sh600083', 'sz000803', 'sz000589', 'sh600255', 'sz002284', 'sh601088',
                            'sh600527', 'sh600565', 'sz399933', 'sh600526', 'sz002115', 'sz000975', 'sh000943',
                            'sh600733', 'sh600592', 'sz002020', 'sh600585', 'sz000600', 'sh999999', 'sz000979',
                            'sz000850', 'sz002330', 'sh600710', 'sh600419', 'sh600183', 'sh600981', 'sh600195',
                            'sz002184', 'sh600082', 'sz000917', 'sz002233', 'sh600732', 'sh600278', 'sh000007',
                            'sh600873', 'sz399336', 'sh600655', 'sh600192', 'sz000756', 'sz000852', 'sh600005',
                            'sh600017', 'sh600980', 'sz000921', 'sz002116', 'sh600388', 'sz399359', 'sz399365',
                            'sh600800', 'sh600895', 'sh600356', 'sh000929', 'sh600825', 'sz002092', 'sz002268',
                            'sz000035', 'sh600847', 'sh600249', 'sh601668', 'sh600649', 'sz000042', 'sz002018',
                            'sz002028', 'sh600145', 'sz000544', 'sh601099', 'sh600053', 'sz399331', 'sh600578',
                            'sz300023', 'sh600026', 'sz000683', 'sh600070', 'sz000065', 'sz399101', 'sh580024',
                            'sz000989', 'sh600116', 'sz002244', 'sh600682', 'sz002293', 'sz000016', 'sz000032',
                            'sh600597', 'sz399352', 'sz399906', 'sh600128', 'sh600191', 'sz300044', 'sz399937',
                            'sz000809', 'sh600811', 'sz002162', 'sz002217', 'sz000818', 'sz000868', 'sh600386',
                            'sz002237', 'sz002339', 'sz000528', 'sh601988', 'sh601918', 'sh600495', 'sh600764',
                            'sh600157', 'sz125969', 'sz000078', 'sh600318', 'sz002373', 'sz399368', 'sz002147',
                            'sz002348', 'sz300033', 'sz000423', 'sz002171', 'sz300066', 'sz002173', 'sh600488',
                            'sh600206', 'sh600639', 'sh600479', 'sh600456', 'sz000582', 'sh600136', 'sz000676',
                            'sz002065', 'sh600746', 'sz300017', 'sh600713', 'sz002276', 'sh600100', 'sh600231',
                            'sz399904', 'sz300043', 'sh600520', 'sh600146', 'sh110008', 'sh600238', 'sh000015',
                            'sh000003', 'sz002069', 'sh000909', 'sh600628', 'sh600212', 'sz002057', 'sz002078',
                            'sh600666', 'sh600308', 'sh600360', 'sh600583', 'sz002298', 'sz399312', 'sz300009',
                            'sz002288', 'sh600432', 'sz002380', 'sh600797', 'sh600460', 'sz002043', 'sz000839',
                            'sz002206', 'sz399317', 'sh600480', 'sh600966', 'sz300046', 'sz000553', 'sh600161',
                            'sh600199', 'sz002379', 'sh600007', 'sh600281', 'sh600584', 'sh600654', 'sh600844',
                            'sh600109', 'sh600641', 'sh600148', 'sz002332', 'sz000506', 'sh600363', 'sz399134',
                            'sz000157', 'sh600239', 'sz000416', 'sh600664', 'sz002367', 'sz002103', 'sz002362',
                            'sh600532', 'sz000680', 'sz002037', 'sh600599', 'sh600680', 'sh600805', 'sh600143',
                            'sh600642', 'sh600062', 'sh000056', 'sh600378', 'sh600406', 'sh600983', 'sh600168',
                            'sh600354', 'sh600593', 'sh000041', 'sh600623', 'sz000056', 'sz399322', 'sh600779',
                            'sh600720', 'sh600272', 'sz000591', 'sz000031', 'sz002040', 'sz002264', 'sz002131',
                            'sh601600', 'sz002341', 'sz000007', 'sz002331', 'sz399954', 'sz000055', 'sz000150',
                            'sz399131', 'sz399150', 'sh600201', 'sz002260', 'sz399372', 'sh600222', 'sz000636',
                            'sz002376', 'sh600608', 'sz002090', 'sz002045', 'sh600816', 'sz002010', 'sz002157',
                            'sz399946', 'sh600673', 'sh600835', 'sz000617', 'sh600837', 'sh600160', 'sz000950',
                            'sh600469', 'sh600355', 'sh600248', 'sz002303', 'sh600759', 'sh600960', 'sh600880',
                            'sh600282', 'sz399369', 'sz000793', 'sh600703', 'sz002032', 'sz000837', 'sh600604',
                            'sh600122', 'sh000949', 'sh000060', 'sz000525', 'sh000927', 'sz002258', 'sz000562',
                            'sz000973', 'sz002371', 'sh600476', 'sz002145', 'sz002197', 'sh600888', 'sh000008',
                            'sz000610', 'sz000655', 'sh600299', 'sh000004', 'sz002219', 'sz399100', 'sz000798',
                            'sz399923', 'sz300053', 'sh600455', 'sz000560', 'sz399363', 'sh600774', 'sh600794',
                            'sz399314', 'sh600019', 'sh600896', 'sh600568', 'sz000543', 'sz000626', 'sz000966',
                            'sh600176', 'sh600358', 'sz300018', 'sh600483', 'sh000046', 'sh600196', 'sh600227',
                            'sh600834', 'sh600446', 'sh600821', 'sz000931', 'sz002281', 'sh600662', 'sh600327',
                            'sz002025', 'sz399120', 'sz000982', 'sz000521', 'sz000682', 'sz002366', 'sz000594',
                            'sz002128', 'sz002230', 'sh600368', 'sz399346', 'sz002363', 'sz000025', 'sh600079',
                            'sh600715', 'sh600067', 'sz399110', 'sz002134', 'sz000511', 'sz002291', 'sz000978',
                            'sz000768', 'sh600320', 'sz399919', 'sz000402', 'sh110005', 'sz000980', 'sz300015',
                            'sz000920', 'sz000906', 'sz002307', 'sz000613', 'sh000915', 'sh600409', 'sz000778',
                            'sh600365', 'sz002142', 'sh600366', 'sh600557', 'sz002112', 'sz000972', 'sz002041',
                            'sz399200', 'sz002060', 'sh600719', 'sh600519', 'sz399313', 'sh600103', 'sz000662',
                            'sz002007', 'sh600108', 'sz002132', 'sh600696', 'sz000726', 'sh600838', 'sz000937',
                            'sh600872', 'sh000025', 'sz002014', 'sz300055', 'sz000925', 'sz000545', 'sz399940',
                            'sz000888', 'sz002055', 'sh600150', 'sz000151', 'sz000999', 'sz399003', 'sz002196',
                            'sh600345', 'sh000065', 'sh600159', 'sh600459', 'sz002271', 'sz000009', 'sh600734',
                            'sz000727', 'sh000955', 'sh000938', 'sz000695', 'sz000959', 'sz002166', 'sz002097',
                            'sz002111', 'sh600841', 'sh600022', 'sh601678', 'sh600791', 'sz399916', 'sz300050',
                            'sh600660', 'sz399361', 'sh600513', 'sh600635', 'sh600796', 'sh600551', 'sz002255',
                            'sz000625', 'sh600265', 'sh600991', 'sh600997', 'sh600172', 'sh600226', 'sz300007',
                            'sh600851', 'sh600280', 'sz399341', 'sz399326', 'sh600545', 'sh000960', 'sz399160',
                            'sh000047', 'sz002315', 'sh110078', 'sz000779', 'sh600778', 'sz000520', 'sz002283',
                            'sz002169', 'sz002195', 'sz399955', 'sz002235', 'sh600028', 'sz002368', 'sh600390',
                            'sh000035', 'sz002296', 'sz000977', 'sh000032', 'sz000776', 'sz000962', 'sz300005',
                            'sz399921', 'sh000042', 'sz399938', 'sh600515', 'sz002120', 'sz000638', 'sh000059',
                            'sz002019', 'sh000022', 'sh600760', 'sh600575', 'sz000953', 'sz002336', 'sz399931',
                            'sh601268', 'sh600986', 'sz000567', 'sh600210', 'sh600601', 'sz399344', 'sh000958',
                            'sh600900', 'sh600251', 'sh000006', 'sz000502', 'sz000988', 'sh600758', 'sz002023',
                            'sz002203', 'sz000619', 'sz000590', 'sz399327', 'sh600343', 'sh600010', 'sh000044',
                            'sz300030', 'sz002005', 'sh600188', 'sh600383', 'sz002089', 'sz300038', 'sh600571',
                            'sh600018', 'sz000425', 'sh600106', 'sh600361', 'sz002121', 'sh600688', 'sz000529',
                            'sz002165', 'sh600798', 'sh600328', 'sh600126', 'sz000918', 'sz300013', 'sz000707',
                            'sz000952', 'sz399917', 'sz399375', 'sz300064', 'sh601188', 'sz000012', 'sz000001',
                            'sh600600', 'sz000592', 'sh600742', 'sz002277', 'sh600832', 'sz002125', 'sh600467',
                            'sh600009', 'sh600429', 'sh600750', 'sz399340', 'sh600536', 'sz000509', 'sz399922',
                            'sh600379', 'sz000936', 'sz300008', 'sh600723', 'sh600380', 'sz002234', 'sh600971',
                            'sz300040', 'sz002088', 'sz000878', 'sz002154', 'sh600829', 'sz000532', 'sz000686',
                            'sz002190', 'sh600200', 'sh600263', 'sh600638', 'sz399945', 'sh600559', 'sz399329',
                            'sz399106', 'sh600184', 'sh000904', 'sh600610', 'sz000792', 'sh600668', 'sz300024',
                            'sz000987', 'sz002275', 'sh601857', 'sz000522', 'sz399136', 'sz399377', 'sz002110',
                            'sz002212', 'sz002158', 'sh000934', 'sz000584', 'sz000668', 'sh600854', 'sh600827',
                            'sz000678', 'sz002274', 'sz399133', 'sh600789', 'sh600491', 'sz000059', 'sz002344',
                            'sz000958', 'sh600846', 'sh600322', 'sz002263', 'sh600060', 'sz399941', 'sh600337',
                            'sh000918', 'sz399355', 'sh601607', 'sh600482', 'sh000939', 'sh600547', 'sz002186',
                            'sz000963', 'sh600236', 'sh600177', 'sh600612', 'sh600855', 'sz002094', 'sz002109',
                            'sz002200', 'sz000911', 'sh600452', 'sh600425', 'sz000602', 'sz002176', 'sh600975',
                            'sh600881', 'sh600521', 'sz399316', 'sz002168', 'sh600605', 'sz000566', 'sz000830',
                            'sh600208', 'sh600080', 'sz000060', 'sz002006', 'sz000783', 'sz000595', 'sz000898',
                            'sh600784', 'sz002027', 'sz000912', 'sz001896', 'sz002099', 'sz002199', 'sh600561',
                            'sh600277', 'sh110004', 'sh600667', 'sz002346', 'sh600110', 'sz399137', 'sz002359',
                            'sz399909', 'sz000698', 'sz000752', 'sh600815', 'sz399347', 'sh600132', 'sh600095',
                            'sh601003', 'sz399230', 'sz000639', 'sz000859', 'sh600731', 'sh600093', 'sh600963',
                            'sh600691', 'sz000701', 'sh600674', 'sz000802', 'sh600563', 'sh600316', 'sz000546',
                            'sh600973', 'sh600853', 'sz000948', 'sh600295', 'sz002144', 'sh600179', 'sz002353',
                            'sh600141', 'sz002297', 'sh000954', 'sh600166', 'sh600315', 'sz000718', 'sh601872',
                            'sh600252', 'sz002253', 'sh600242', 'sh000910', 'sh600795', 'sh600020', 'sh000903',
                            'sh600072', 'sh600869', 'sh600367', 'sh600671', 'sh600569', 'sz300021', 'sh600678',
                            'sz000835', 'sh600808', 'sh600558', 'sz002082', 'sz000883', 'sz399353', 'sz000758',
                            'sh600517', 'sz002080', 'sz000419', 'sh600812', 'sz002151', 'sh000959', 'sz002251',
                            'sh601688', 'sh600876', 'sh000049', 'sz000526', 'sz300002', 'sz002316', 'sh600216',
                            'sz000737', 'sh600730', 'sz000875', 'sz002267', 'sz002036', 'sz000409', 'sz000812',
                            'sz000711', 'sh600882', 'sz000404', 'sz002141', 'sh000913', 'sh600753', 'sh000013',
                            'sz000062', 'sz000791', 'sz000488', 'sz000100', 'sz000789', 'sz002076', 'sz000631',
                            'sz300020', 'sh580022', 'sh600819', 'sh600139', 'sh000948', 'sh600743', 'sz002313',
                            'sz000411', 'sz000916', 'sh600111', 'sh600751', 'sz002119', 'sz002029', 'sh600747',
                            'sh600331', 'sh600487', 'sh000054', 'sh600218', 'sh600262', 'sh600395', 'sz000858',
                            'sz002265', 'sz000957', 'sh601139', 'sh600127', 'sh600643', 'sh600780', 'sh999998',
                            'sz000708', 'sh600570', 'sz000935', 'sz002011', 'sz000014', 'sh600186', 'sz399376',
                            'sz000066', 'sh601001', 'sz002108', 'sz000037', 'sh000946', 'sz002084', 'sz399947',
                            'sz000663', 'sh600525', 'sh600982', 'sh600055', 'sz002100', 'sz000881', 'sh600653',
                            'sh000057', 'sh600687', 'sz000599', 'sz002243', 'sh600792', 'sh000933', 'sh600461',
                            'sz002294', 'sh600283', 'sh600749', 'sh600016', 'sh600305', 'sh600712', 'sz000799',
                            'sz002221', 'sh600091', 'sh600647', 'sh601788', 'sh601007', 'sz002204', 'sz000552',
                            'sh601877', 'sz000046', 'sh600692', 'sz300039', 'sz002240', 'sh600702', 'sh600129',
                            'sh600279', 'sz300028', 'sz000926', 'sz000983', 'sz000733', 'sz399321', 'sz300051',
                            'sz002033', 'sz399319', 'sh600550', 'sz000713', 'sz002305', 'sz002137', 'sh600258',
                            'sh600325', 'sh600516', 'sh600864', 'sz002254', 'sz000785', 'sz000536', 'sh601009',
                            'sz002163', 'sz002136', 'sz399140', 'sh600640', 'sz000410', 'sh600038', 'sz000426',
                            'sh600860', 'sh600223', 'sz000633', 'sz002012', 'sz000971', 'sz000705', 'sz002279',
                            'sz300065', 'sh600054', 'sz300057', 'sz000612', 'sz002164', 'sz002289', 'sh600397',
                            'sh600648', 'sz399170', 'sh600015', 'sh600273', 'sh600970', 'sz002030', 'sh600058',
                            'sh600814', 'sz399956', 'sh600530', 'sh600708', 'sz000816', 'sz002139', 'sh600698',
                            'sh000919', 'sz002177', 'sz399913', 'sz000810', 'sz002312', 'sz000786', 'sh600235',
                            'sh601333', 'sh600153', 'sh601588', 'sh600859', 'sz399918', 'sz000939', 'sh600763',
                            'sh600684', 'sz000739', 'sz000637', 'sh600352', 'sz399325', 'sz000400', 'sh000048',
                            'sh600119']

day = 150


# 国内股票数据：个股
def getChinaStockIndividualInfo(stockCode, day):
    try:
        # exchange = "sh" if (int(stockCode) // 100000 == 6) else "sz"
        dataUrl = "http://hq.sinajs.cn/list=" + stockCode
        stdout = urllib.request.urlopen(dataUrl)
        stdoutInfo = stdout.read().decode('gb2312')
        tempData = re.search('''(")(.+)(")''', stdoutInfo).group(2)
        stockInfo = tempData.split(",")
        stockCode = stockCode
        stockName = stockInfo[0]  # 名称
        # stockStart  = stockInfo[1]  #开盘
        # stockLastEnd= stockInfo[2]  #昨收盘
        stockCur = stockInfo[3]  # 当前
        stockMax = stockInfo[4]  # 最高
        stockMin = stockInfo[5]  # 最低
        # stockUp     = round(float(stockCur) - float(stockLastEnd), 2)       #涨跌
        # stockRange  = round(float(stockUp) / float(stockLastEnd), 4) * 100  #幅度
        # stockVolume = round(float(stockInfo[8]) / (100 * 10000), 2)         #总手
        # stockMoney  = round(float(stockInfo[9]) / (100000000), 2)           #金额
        # stockTime   = stockInfo[31]                                         #更新时间

        # content = "#" + stockName + "#(" + stockCode + ")" + " 开盘:" + stockStart \
        # + ",最新:" + stockCur + ",最高:" + stockMax + ",最低:" + stockMin \
        # + ",涨跌:" + str(stockUp) + ",幅度:" + str(stockRange) + "%" \
        # + ",总手:" + str(stockVolume) + "万" + ",金额:" + str(stockMoney) \
        # + "亿" + ",更新时间:" + stockTime + "  "

        if (os.path.exists('data/' + (stockName + stockCode) + '.txt')):
            f = open('data/' + (stockName + stockCode) + '.txt', 'r+')
            line = f.readlines()
            num = len(line)
            # print(num)
            if (num > day):
                for i in range(0, num - day):
                    line.pop(i)
            f.close()
            f2 = open('data/' + (stockName + stockCode) + '.txt', 'w')
            for i in line:
                f2.writelines(i)
            f2.close()

        f3 = open('data/' + (stockName + stockCode) + '.txt', 'a+')
        f3.write(stockName + "#"+stockCode + "#"+stockMax + "#" + stockMin + "#" + stockCur)
        f3.write('\n')
        f3.close()



        # content =  stockName + "#" + stockCode + "#" + stockMax + "#" + stockMin + "#" + stockCur

        # twitter = {'message': content}

    except Exception as e:
        print(">>>>>> Exception: " + str(e))
    else:
        return
    finally:
        None


def test_china_individual_data():
    for stockCode in ChinaStockIndividualList:
        getChinaStockIndividualInfo(stockCode, day)


# 主函数
def main():
    "main function"
    test_china_individual_data()
    print('ok!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


if __name__ == '__main__':
    main()
