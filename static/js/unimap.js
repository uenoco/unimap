//
//  奈良ユニバーサル観光マップ
//  unimap.js

//  背景地図：初期表示の中心の緯度・経度
var DEF_LAT=34.6850; 
var DEF_LON=135.8380; 
var DEF_ZOOM=15;      //ズームレベル

//  おすすめルート
var GEOJSON_ROUTE = '/api/v1/route.geojson/'; // ルート
var GEOJSON_POINT = '/api/v1/point.geojson/'; // 地点情報
var GEOJSON_TOILET= '/api/v1/toilet.geojson'; // 多目的トイレ
var GEOJSON_HOTEL = '/api/v1/hotel.geojson';  // ホテル
var GEOJSON_PASS  = '/api/v1/pass.geojson';   // 通行情報

//  イラスト地図ファイル
//var DEF_IMAGEMAP = './map/narapark.png';
//  イラスト地図表示位置の緯度・経度（左上）
//var IMG_LAT1=34.6903;
//var IMG_LON1=135.82725; 
//  イラスト地図表示位置の緯度・経度（右下）
//var IMG_LAT2=34.6816;
//var IMG_LON2=135.84599;

// osm
var $maptile = osmorg;
var map = L.map( 'map', {center: [DEF_LAT, DEF_LON], zoom: DEF_ZOOM, zoomControl: true, layers: [ $maptile ]});

/*
//  Ajax で geojson をゲット
result = 
  $.ajax({ type: 'GET', url: GEOJSON_ROUTE })
   .done(function(geojsonString) {
     //  ファイル読み込み完了後の処理
     var geojson = JSON.parse(geojsonString);
     var Layer = new L.GeoJSON( geojson ,{
       style: routeDefaultStyle ,
       onEachFeature: function (feature, layer) {
         onCoordsSlope( feature );
       }
     });
   });
*/

//  Disp Point
/*
var coursePointLayer = new L.GeoJSON.AJAX( GEOJSON_POINT , {
  pointToLayer: function (feature, latlng) {
    switch ( feature.properties.Sort) {
	    case 'start'   : return L.marker(latlng, {icon: IconStart, opacity: "0.8"});
      case 'goal'    : return L.marker(latlng, {icon: IconGoal, opacity: "0.8"});
	    case 'start_op': return L.marker(latlng, {icon: IconStartOP, opacity: "0.8"});
      case 'goal_op' : return L.marker(latlng, {icon: IconGoalOP, opacity: "0.8"});
      case 'location': return L.marker(latlng, {icon: IconLocation, opacity: "0.8"});
      case 'attention': return L.marker(latlng, {icon: IconAttention, opacity: "0.8"});
      case 'caution' : return L.marker(latlng, {icon: IconCaution, opacity: "0.8"});
      case 'busstop' : return L.marker(latlng, {icon: IconBusstop, opacity: "0.8"});
      case 'guide'   : return L.marker(latlng, {icon: IconGuide, opacity: "0.8"});
      case 'barrguide': return L.marker(latlng, {icon: IconBarrGuide, opacity: "0.8"});
      case 'roadguide': return L.marker(latlng, {icon: IconRoadGuide, opacity: "0.8"});
      case 'restaurant': return L.marker(latlng, {icon: IconRestaurant, opacity: "0.8"});
      case 'shop'    : return L.marker(latlng, {icon: IconShop, opacity: "0.8"});
      case 'route' :
        switch ( feature.properties.No ){
	  case "1" : return L.marker(latlng, {icon: IconLocateNo01, opacity: "0.8"});
	  case '2' : return L.marker(latlng, {icon: IconLocateNo02, opacity: "0.8"});
	  case '3' : return L.marker(latlng, {icon: IconLocateNo03, opacity: "0.8"});
	  case '4' : return L.marker(latlng, {icon: IconLocateNo04, opacity: "0.8"});
	  case '5' : return L.marker(latlng, {icon: IconLocateNo05, opacity: "0.8"});
	  case '6' : return L.marker(latlng, {icon: IconLocateNo06, opacity: "0.8"});
	  case '7' : return L.marker(latlng, {icon: IconLocateNo07, opacity: "0.8"});
	  case '8' : return L.marker(latlng, {icon: IconLocateNo08, opacity: "0.8"});
	  case '9' : return L.marker(latlng, {icon: IconLocateNo09, opacity: "0.8"});
	  case '10': return L.marker(latlng, {icon: IconLocateNo10, opacity: "0.8"});
        };
	case 'option' :
        switch ( feature.properties.No ){
	        case "1" : return L.marker(latlng, {icon: IconLocateOp01, opacity: "0.8"});
	        case '2' : return L.marker(latlng, {icon: IconLocateOp02, opacity: "0.8"});
	        case '3' : return L.marker(latlng, {icon: IconLocateOp03, opacity: "0.8"});
	        case '4' : return L.marker(latlng, {icon: IconLocateOp04, opacity: "0.8"});
	        case '5' : return L.marker(latlng, {icon: IconLocateOp05, opacity: "0.8"});
	        case '6' : return L.marker(latlng, {icon: IconLocateOp06, opacity: "0.8"});
	        case '7' : return L.marker(latlng, {icon: IconLocateOp07, opacity: "0.8"});
	        case '8' : return L.marker(latlng, {icon: IconLocateOp08, opacity: "0.8"});
	        case '9' : return L.marker(latlng, {icon: IconLocateOp09, opacity: "0.8"});
	        case '10': return L.marker(latlng, {icon: IconLocateOp10, opacity: "0.8"});
        }
	    default : return L.marker(latlng, {icon: IconDefault, opacity: "0.8"});
        }
    },
    onEachFeature: onEachFeaturePOI 
});
*/

//  ホテル表示
var hotelLayer = new L.GeoJSON.AJAX( GEOJSON_HOTEL , {
  pointToLayer: function (feature, latlng) {
	  return L.marker(latlng, {icon: IconHotel, opacity: "0.8"});
  },
  onEachFeature: onEachFeatureHotel
});

//  多目的トイレ表示
var toiletLayer = new L.GeoJSON.AJAX( GEOJSON_TOILET , {
  pointToLayer: function (feature, latlng) {
	  return L.marker(latlng, {icon: IconToilet, opacity: "0.8"});
  },
  onEachFeature: onEachFeatureWC
});

/*
//  通行情報レイヤー
var passLayer = new L.GeoJSON.AJAX( GEOJSON_PASS, { 
    style: function(feature) {
      switch (feature.properties.Sort) {
        case 'impassable': return passImpassableStyle;
        case 'difficulty': return passDifficultyStyle;
        case 'gravel':     return passGravelStyle;
        case 'traffic':    return passTrafficStyle;
      }
    },
    onEachFeature: onEachFeaturePass
  }
);

////  イラスト地図レイヤー
var imageUrl = DEF_IMAGEMAP, imageBounds = [[ IMG_LAT1, IMG_LON1 ] , [IMG_LAT2, IMG_LON2]];
var imageLayer = new L.imageOverlay(imageUrl, imageBounds, {opacity:1.0} );

//  Layer Group
//  ルートレイヤ：観光コース、坂道情報、ルート地点情報
var courseLayer  = L.layerGroup([ courseRouteLayer, courseSlopeLayer, coursePointLayer ]);
//  ルート検索レイヤ：拡張用
var routeLayer   = L.layerGroup([ ]);
*/

var overlayMaps = {
  "バリアフリーホテル"   : hotelLayer,
  "多目的トイレ"   : toiletLayer,
//  "おすすめコース" : courseLayer,
//  "イラストマップ" : imageLayer,
//  "通行情報"       : passLayer,
//  "ルート案内表示" : routeLayer,
};

//map.addLayer( courseLayer );
map.addLayer( hotelLayer );
map.addLayer( toiletLayer );
//map.addLayer( routeLayer );
//map.addLayer( imageLayer );
//map.addLayer( passLayer );

L.control.layers( baseMaps, overlayMaps ).addTo(map);

//  GPS位置情報がとれれば中心になるように地図を移動。左下に位置を表示
var infowindow=L.control();
var CurrentMaker=L.marker();

infowindow.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this._div.innerHTML='<div id="Status">GPS Waiting</div>';
    return this._div;
};

// method that we will use to update the control based on feature properties passed
infowindow.update = function (props) { this._div.innerHTML='<div id="Status"></div>';};
infowindow.setPosition('bottomleft');
infowindow.addTo(map);

//  ルート検索
/*
function SearchWheelChairRoute( lon2, lat2 ) {
  map.removeLayer( routeLayer );
  if( (lon2 == 999 ) ||(lat2 == 999) ){ return; }
  var gpx = 'https://route.zukatech.com/gpxroute.php?lon1='+curlon+'&lat1='+curlat+'&lon2='+lon2+'&lat2='+lat2 ;
  var wheelLayer = new L.GPX(gpx, {async: true}).on('loaded', function(e) {
	  map.fitBounds(e.target.getBounds());
  });

  routeLayer = L.layerGroup([wheelLayer] );
  routeLayer.addTo(map);
}
*/

/*
function SearchWheelChairRouteDemo( lon2, lat2 ) {
    map.removeLayer( routeLayer );

    var gpx = 'https://route.zukatech.com/unimap/gpxroute.php?lon1='+DEF_CUR_LON+'&lat1='+DEF_CUR_LAT+'&lon2='+lon2+'&lat2='+lat2 ;
    var wheelLayer = new L.GPX(gpx, {async: true}).on('loaded', function(e) {
	map.fitBounds(e.target.getBounds());
    });
    routeLayer = L.layerGroup([wheelLayer] );
    routeLayer.addTo(map);
}
*/

////  get GPS Location
/*
function onLocationFound(e) {
    var undefined;
    var alt = 0, spd = 0 , dir = 0 , tim = 0 ;
    var acc = e.accuracy / 2;
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;
    curlon=e.latlng.lng;
    curlat=e.latlng.lat;

    if( e.altitude !== undefined ){ alt=e.altitude; }
    if( e.speed    !== undefined ){ spd=e.speed;    }
    if( e.heading  !== undefined ){ dir=e.hedding;  }  
    if( e.timestamp !== undefined){ tim=e.timestamp/1000 - 1356040000;  }
    
    var str = '<DIV>'
    str += '<form name="MOVE"><input type="button" name="CP" value="現在地を表示" onClick="movetoCurrentLocation(';
    str += lat + ", " + lng +')">';
    str += '<input type="button" name="RT" value="コースを表示" onClick="movetoRouteLocation()"></form>';
    str += "<p>(" + lng.toFixed(3) + "," + lat.toFixed(3) + ")</br>";
    str += "ACC: " + acc.toFixed(0);
    if( spd != 0 ){
	str += " S: " + spd.toFixed(0) + " m/sec D:" + dir.toFixed(0) + "</p>"
    }else{
	str += " S: 0 m/sec</p>";
    }
    str += '</DIV>'

    CurrentMaker.setLatLng( e.latlng ).addTo(map);
//    Circle2.setLatLng( e.latlng ).addTo(map);

    document.getElementById('Status').innerHTML = str;
    //movetoLocation( latlng ) {
}
*/

////  move to GPS Location
/*
function movetoCurrentLocation( lat, lng ) {
    var zoomLevel = map.getZoom();
    var latlng = L.latLng( lat, lng);
    map.setView( latlng , zoomLevel );
}
*/

////  move to GPS Location
/*
function movetoRouteLocation() {
  map.fitBounds(courseRouteLayer.getBounds(), {
	  padding: [50, 50]
  });
}
*/

// Watch GPS Location
/*
map.on( 'locationfound', onLocationFound);
map.locate({watch: true});
*/

// Change Layer by ZoomLevel
/*
map.on(
  'zoomend', function () {
    switch( map.getZoom() ){
      case 19:
      case 18:
      case 17:
      case 16:
      case 15:
        map.addLayer(passLayer);
        map.addLayer(courseLayer);
        break;
      case 14:
      case 13:
        map.removeLayer(passLayer);
        map.removeLayer(courseLayer);
        map.addLayer(hotelLayer);
        map.addLayer(toiletLayer);
        break;
      default:
        map.removeLayer(passLayer);
        map.removeLayer(courseLayer);
        map.removeLayer(hotelLayer);
        map.removeLayer(toiletLayer);
        break;
    }
  }
);
*/
