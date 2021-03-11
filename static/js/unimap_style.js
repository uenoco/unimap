////////////////////////////////////////////////////////////////////////////
//  表示スタイルの定義
//      タイル地図情報、LineString, Polygon表示形状の定義
//      Wirtten by Y.ISHIZUKA(Code for Nara)
////////////////////////////////////////////////////////////////////////////
////
//  背景地図情報
////
var osmorg = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
});
var osmjp = L.tileLayer('https://tile.openstreetmap.jp/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
});
var GSIstd = L.tileLayer("https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png", {
    minZoom: 2,
    maxZoom: 18,
    attribution: "地理院地図(標準)"
});
var GSIpale = L.tileLayer("https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png", {
    minZoom: 2,
    maxZoom: 18,
    attribution: "地理院地図(淡色)"
});
var GSIhillshademap =L.tileLayer("https://cyberjapandata.gsi.go.jp/xyz/hillshademap/{z}/{x}/{y}.png", {
    minZoom: 2,
    maxNativeZoom: 16,
    maxZoom: 18,
    attribution: "地理院地図(傾斜)"
});
var GSIort =L.tileLayer("https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg", {
    minZoom: 14,
    maxZoom: 18,
    attribution: "地理院地図(オルソ)"
});

// MIERUNE地図mono
var style = "mierune_mono";
var mierune_url = "https://tile.mierune.co.jp/" + style + "/{z}/{x}/{y}.png" ;
var mierune_mono = new L.tileLayer(mierune_url, {
    attribution: "Maptiles by <a href='http://mierune.co.jp/' target='_blank'>MIERUNE</a>, under CC BY. Data by <a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> contributors, under ODbL."
});

// MIERUNE地図color
var style = "mierune";
var mierune_url = "https://tile.mierune.co.jp/" + style + "/{z}/{x}/{y}.png" ;
var mierune_color = new L.tileLayer(mierune_url, {
    attribution: "Maptiles by <a href='http://mierune.co.jp/' target='_blank'>MIERUNE</a>, under CC BY. Data by <a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> contributors, under ODbL."
});

// MIERUNE地図normal
var style = "normal";
var mierune_url = "https://tile.cdn.mierune.co.jp/styles/" + style + "/{z}/{x}/{y}.png" + "?key=" + apikey;
//var mierune_url = "https://tile.mierune.co.jp/" + style + "/{z}/{x}/{y}.png"  + "?key=" + apikey;
var mierune_std = new L.tileLayer(mierune_url, {
    attribution: "Maptiles by <a href='http://mierune.co.jp/' target='_blank'>MIERUNE</a>, under CC BY. Data by <a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> contributors, under ODbL."
});

//  Base TileMap List
var baseMaps = {
    "OpenStreetMap": osmorg,
//    "MIERUNE標準" 　: mierune_std,
//    "日本版ＯＳＭ" : osmjp,
//    "地理院標準"   : GSIstd,
//    "地理院淡色地図" : GSIpale,
//    "地理院傾斜地図" : GSIhillshademap,
    "地理院航空写真" : GSIort,
    "MIERUNEモノ" 　 : mierune_mono,
//    "MIERUNEカラー" : mierune_color,
};

////
//  オブジェクトのスタイル指定
////
//  メインルート
var routeMainStyle = {
  color: "#6356a3",
  opacity: "0.8",
  weight: "4",
  dashArray: "0.8,9"
};

//  オプションメインルート
var routeOptionStyle = {
  color: "#dd811d",
  opacity: 0.8,
  weight: 4,
  dashArray: "0.8,9"
};

//　坂道：ゆるやか
var routeSlopeStyleLv1 = {
  delay: 800,
  weight: 6,
  color: "#ffffff",
  pulseColor: "#008cd6",
  dashArray: "1,50",
};
//　坂道：中
var routeSlopeStyleLv2 = {
  delay: 800,
  weight: 6,
  color: "#ffffff",
  pulseColor: "#0068b7",
  dashArray: "1,25",
};
//　坂道：急
var routeSlopeStyleLv3 = {
  delay: 800,
  weight: 6,
  color: "#ffffff",
  pulseColor: "#004098",
  dashArray: "1,10"
};

//  非表示
var routeDefaultStyle = {
  "color": "#ffffff",
  "opacity": 0,
  "weight": 0,
};


/////////////////////////////////////////////////////////////

//　通行不可エリア
var passImpassableStyle = {
  "color": "#888888",
  "opacity": 1,
  "fillColor": "#888888",
  "fillOpacity": 0.2,
  "weight": 1,
  "fill" : 'url(image/fillpattern3.gif)'
};

//　通行困難場所エリア：車椅子の種類による
var passDifficultyStyle = {
  "color": "#e2530c",
  "opacity": 0.8, 
  "fillColor": "#dd811d",
  "fillOpacity": 0.2,
  "weight": 1,
  "fill" : 'url(image/fillpattern2.gif)'
};

//　通行困難場所エリア：砂利
var passGravelStyle = {
  "color": "#ffffff",
  "opacity": 0.8, 
  "fillColor": "#fffcdb",
  "fillOpacity": 0.2,
  "weight": 3,
  "dashArray": "1,6",
  "fill" : 'url(image/fillpattern1.gif)'
};

//　通行困難場所エリア：交通
var passTrafficStyle = {
  "color": "#777777",
  "opacity": 0.8, 
  "fillColor": "#ffffff",
  "fillOpacity": 0.2,
  "weight": 2,
  "dashArray": "0.5,5",
  "fill" : 'url(image/fillpattern3.gif)'
};

