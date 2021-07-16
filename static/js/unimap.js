//
//  奈良ユニバーサル観光マップ
//  unimap.js

//  背景地図：初期表示の中心の緯度・経度
var DEF_LAT=34.6850; 
var DEF_LON=135.8380; 
var DEF_ZOOM=15;      //ズームレベル

//  おすすめルート
// WIP:エリア番号の追加が必要
var GEOJSON_ROUTE = '/api/v1/route.geojson'; // ルート
var GEOJSON_POINT = '/api/v1/point.geojson'; // 地点情報

var GEOJSON_TOILET= '/api/v1/toilet.geojson'; // 多目的トイレ
var GEOJSON_HOTEL = '/api/v1/hotel.geojson';  // ホテル
var GEOJSON_ZONE  = '/api/v1/zone.geojson';   // 通行情報

//  坂道レイヤー
var courseSlopeLayer = new L.GeoJSON();
//  ルートレイヤー
var courseRouteLayer = new L.GeoJSON();

// コースとスロープのスタイル設定関数
function onCoordsSlope( feature ) {
    latlngs = []; //  座標列格納変数
    line = feature.geometry.coordinates ;
    line.forEach(function(entry){
	latlngs.push(new L.latLng(entry[1],entry[0]));
    });
    // console.log( "latlngs : " + latlngs );
    popupContent = setPopupContentPass(feature);

    switch ( feature.properties.Sort){
    case 1 :    // おすすめルート
	style = routeMainStyle ;
	L.polyline( latlngs, style ).bindPopup(popupContent).addTo( courseRouteLayer );
	break;
    case 2 :  // オプションルート
	style = routeOptionStyle ;
	L.polyline( latlngs, style ).bindPopup(popupContent).addTo( courseRouteLayer );
	break;
    case 11 :
	style = routeSlopeStyleLv1;
	L.polyline.antPath( latlngs, style ).bindPopup(popupContent).addTo( courseSlopeLayer );
	break;
    case 12 :
	style = routeSlopeStyleLv2;
	L.polyline.antPath( latlngs, style ).bindPopup(popupContent).addTo( courseSlopeLayer );
	break;
    case 13 :
	style = routeSlopeStyleLv3;
	L.polyline.antPath( latlngs, style ).bindPopup(popupContent).addTo( courseSlopeLayer );
	break;
    }
}

function drawMap( mapimg ){
    // console.log( mapimg );

    // osm
    var $maptile = osmorg;
    var map = L.map( 'map', {center: [DEF_LAT, DEF_LON], zoom: DEF_ZOOM, zoomControl: true, layers: [ $maptile ]});

    //  Ajax で JSON(geojson) をゲット
    result = $.ajax({
	type: 'GET', 
	url: GEOJSON_ROUTE,
	dataType: 'json',
    }).done( function(data) {
	//  ファイル読み込み完了後の処理
	// console.log( data );
	var Layer = new L.GeoJSON( data ,{
	    style: routeDefaultStyle ,
	    onEachFeature: function (feature, layer) {
		// コースとスロープのスタイル設定
		onCoordsSlope( feature );
	    }
	});
    }).fail( function(status) {
	//  ファイル読み込み失敗時の処理
	console.log( 'Read ERROR : '+GEOJSON_ROUTE );
	console.log( status );
    });
					       
    /*
    result = $.ajax({ type: 'GET', url: GEOJSON_ROUTE })
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

    //  Disp Point on Route
    var coursePointLayer = new L.GeoJSON.AJAX( GEOJSON_POINT , {
	pointToLayer: function (feature, latlng) {
	    switch ( feature.properties.Sort) {
	    case 2   : return L.marker(latlng, {icon: IconStart, opacity: "0.8"});
	    case 3   : return L.marker(latlng, {icon: IconGoal, opacity: "0.8"});
	    case 4   : return L.marker(latlng, {icon: IconStartOP, opacity: "0.8"});
	    case 5   : return L.marker(latlng, {icon: IconGoalOP, opacity: "0.8"});
	    case 6   : return L.marker(latlng, {icon: IconLocation, opacity: "0.8"});
	    case 7   : return L.marker(latlng, {icon: IconBarrGuide, opacity: "0.8"});
	    case 8   : return L.marker(latlng, {icon: IconAttention, opacity: "0.8"});
	    case 9   : return L.marker(latlng, {icon: IconCaution, opacity: "0.8"});
	    case 10  : return L.marker(latlng, {icon: IconBusstop, opacity: "0.8"});
	    case 'guide'   : return L.marker(latlng, {icon: IconGuide, opacity: "0.8"});
	    case 'roadguide': return L.marker(latlng, {icon: IconRoadGuide, opacity: "0.8"});
	    case 'restaurant': return L.marker(latlng, {icon: IconRestaurant, opacity: "0.8"});
	    case 11    : return L.marker(latlng, {icon: IconShop, opacity: "0.8"});
	    case 1 :
		// Main Cource
		switch ( feature.properties.No ){
		case 1 : return L.marker(latlng, {icon: IconLocateNo01, opacity: "0.8"});
		case 2 : return L.marker(latlng, {icon: IconLocateNo02, opacity: "0.8"});
		case 3 : return L.marker(latlng, {icon: IconLocateNo03, opacity: "0.8"});
		case 4 : return L.marker(latlng, {icon: IconLocateNo04, opacity: "0.8"});
		case 5 : return L.marker(latlng, {icon: IconLocateNo05, opacity: "0.8"});
		case 6 : return L.marker(latlng, {icon: IconLocateNo06, opacity: "0.8"});
		case 7 : return L.marker(latlng, {icon: IconLocateNo07, opacity: "0.8"});
		case 8 : return L.marker(latlng, {icon: IconLocateNo08, opacity: "0.8"});
		case 9 : return L.marker(latlng, {icon: IconLocateNo09, opacity: "0.8"});
		case 10: return L.marker(latlng, {icon: IconLocateNo10, opacity: "0.8"});
		};
	    case 12 :
		// Option Cource
		switch ( feature.properties.No ){
	        case 1 : return L.marker(latlng, {icon: IconLocateOp01, opacity: "0.8"});
	        case 2 : return L.marker(latlng, {icon: IconLocateOp02, opacity: "0.8"});
	        case 3 : return L.marker(latlng, {icon: IconLocateOp03, opacity: "0.8"});
	        case 4 : return L.marker(latlng, {icon: IconLocateOp04, opacity: "0.8"});
	        case 5 : return L.marker(latlng, {icon: IconLocateOp05, opacity: "0.8"});
	        case 6 : return L.marker(latlng, {icon: IconLocateOp06, opacity: "0.8"});
	        case 7 : return L.marker(latlng, {icon: IconLocateOp07, opacity: "0.8"});
	        case 8 : return L.marker(latlng, {icon: IconLocateOp08, opacity: "0.8"});
	        case 9 : return L.marker(latlng, {icon: IconLocateOp09, opacity: "0.8"});
	        case 10: return L.marker(latlng, {icon: IconLocateOp10, opacity: "0.8"});
		}
	    default :
		return L.marker(latlng, {icon: IconDefault, opacity: "0.8"});
            }
	},
	onEachFeature: onEachFeaturePOI 
    });

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

    //  通行情報レイヤー
    var zoneLayer = new L.GeoJSON.AJAX( GEOJSON_ZONE, { 
	style: function(feature) {
	    switch (feature.properties.Sort) {
            case 1 :
		return passGravelStyle;
	    case 2 :
		return passDifficultyStyle;
	    case 3 :
		return passImpassableStyle;
	    case 4 :
		return passTrafficStyle;
	    default :
		console.log( "Invalid feature.properties.Sort in zoneLayer" )
	    }
	},
	onEachFeature: onEachFeaturePass
    });
    
    ////  イラスト地図レイヤー
    var imageUrl = mapimg.url;
    var imageBounds = [[ mapimg.lat1, mapimg.lon1 ] , [ mapimg.lat2, mapimg.lon2 ]];
    var imageLayer = new L.imageOverlay(imageUrl, imageBounds, {opacity:1.0} );

    //  Layer Group
    //  ルートレイヤ：観光コース、坂道情報、ルート地点情報
    //var courseLayer  = L.layerGroup([ courseRouteLayer, courseSlopeLayer, coursePointLayer ]);
    var courseLayer  = L.layerGroup([ courseRouteLayer, coursePointLayer ]);
    //  ルート検索レイヤ：拡張用
    var routeLayer   = L.layerGroup([ ]);

    var overlayMaps = {
	"おすすめコース" : courseLayer,
	"バリアフリーホテル"   : hotelLayer,
	"多目的トイレ"   : toiletLayer,
	"イラストマップ" : imageLayer,
	"通行情報"       : zoneLayer,
	"ルート案内表示" : courseRouteLayer,
	//"ルート案内表示" : routeLayer,
    };

    map.addLayer( courseLayer );
    map.addLayer( hotelLayer );
    map.addLayer( toiletLayer );
    //map.addLayer( routeLayer );
    map.addLayer( imageLayer );
    map.addLayer( zoneLayer );

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

}
