//　アイコン設定

//  アイコン格納場所（URI）
DEF_ICON_URI = '/static/icons/';

//  画像格納場所（URI）
DEF_IMAGE_URI = '/static/image/';

//  スタートアイコン
var IconStart    = L.icon({ iconUrl: DEF_ICON_URI+'icon_start.png',
                            iconSize: [59,28], iconAnchor: [30,0], popupAnchor: [0,0] });
//  ゴールアイコン
var IconGoal     = L.icon({ iconUrl: DEF_ICON_URI+'icon_goal.png',
                            iconSize: [49,28], iconAnchor: [25,0], popupAnchor: [0,0] });

//  スタートアイコンOP
var IconStartOP  = L.icon({ iconUrl: DEF_ICON_URI+'icon_start_op.png',
                            iconSize: [59,28], iconAnchor: [30,0], popupAnchor: [0,0] });
//  ゴールアイコンOP
var IconGoalOP   = L.icon({ iconUrl: DEF_ICON_URI+'icon_goal_op.png',
                            iconSize: [49,28], iconAnchor: [25,0], popupAnchor: [0,0] });

//  多目的トイレアイコン
var IconToilet   = L.icon({ iconUrl: DEF_ICON_URI+'icon_toilet.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  ホテルアイコン
var IconHotel    = L.icon({ iconUrl: DEF_ICON_URI+'icon_hotel.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });

//  情報地点（建物等）
var IconLocation  = L.icon({ iconUrl: DEF_ICON_URI+'icon_building.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  注意地点（経路上）
var IconAttention = L.icon({ iconUrl: DEF_ICON_URI+'icon_attention.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  警告地点（経路上）
var IconCaution   = L.icon({ iconUrl: DEF_ICON_URI+'icon_instruction.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  現在位置
var IconCurrent   = L.icon({ iconUrl: DEF_ICON_URI+'icon_here.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  バス停//  バス停
var IconBusstop   = L.icon({ iconUrl: DEF_ICON_URI+'icon_busstop.png',
                            iconSize: [22,34], iconAnchor: [11,34], popupAnchor: [0,-30] });
//  ガイド
var IconBarrGuide = L.icon({ iconUrl: DEF_ICON_URI+'icon_barr_guide.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  ガイド
var IconRoadGuide = L.icon({ iconUrl: DEF_ICON_URI+'icon_road_guide.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  レストラン
var IconRestaurant= L.icon({ iconUrl: DEF_ICON_URI+'icon_restaurant.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
//  ショップ
var IconShop      = L.icon({ iconUrl: DEF_ICON_URI+'icon_shop.png',
                            iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });

//  おすすめルート位置番号
var IconLocateNo01 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no01.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo02 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no02.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo03 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no03.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo04 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no04.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo05 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no05.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo06 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no06.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo07 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no07.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo08 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no08.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo09 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no09.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateNo10 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no10.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });

//  オプションルート位置番号
var IconLocateOp01 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no01_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp02 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no02_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp03 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no03_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp04 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no04_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp05 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no05_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp06 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no06_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp07 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no07_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp08 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no08_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp09 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no09_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });
var IconLocateOp10 = L.icon({ iconUrl: DEF_ICON_URI+'icon_no10_op.png' ,
                              iconSize: [32,38], iconAnchor: [16,38], popupAnchor: [0,-30] });

// デフォルトマーカー（アイコン指定なし）
var IconDefault = DEF_ICON_URI + '../dist/images/maker-icon.png';

// トイレ機能アイコン
var IconToiletBabyseat   = DEF_ICON_URI + 'wc_babyseat.png';
var IconToiletOstomate   = DEF_ICON_URI + 'wc_ostomate.png';
var IconToiletNursingbed = DEF_ICON_URI + 'wc_nursingbed.png';
var IconToiletWashlet    = DEF_ICON_URI + 'wc_washlet.png';
var IconToiletRotation   = DEF_ICON_URI + 'wc_rotation.png';
var IconToiletEmergencycall = DEF_ICON_URI + 'wc_sos.png';

// 画像なし表示
var DEF_NOPHOTO = DEF_IMAGE_URI + 'nophoto.jpg';
