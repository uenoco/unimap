//////////////////////////////////////////////////////////////////////////////////
//  ポップアップコンテンツ
//////////////////////////////////////////////////////////////////////////////////

////////
//  ポップアップ表示用htmlテンプレート  下記部分のみで文字列の変更が可能
////////

//  多目的トイレ用ポップアップテンプレート
TemplatePopup_Toilet = '<div class="leaflet-popup-content" style="width: 266px;">'
                     + 'TOILET_NAME'              // トイレ名称（TemplateParts_Name）
                     + 'TOILET_PHOTO1'            //  画像（TemplateParts_PhotoL ）
                     + 'TOILET_PHOTO2'            //  画像（TemplateParts_PhotoL ）
                     + '<div class="wc-area clearfix">'
                     + 'TOILET_PROP_ICON'         //  トイレ機能アイコン（TemplateParts_PropIcon）
                     + 'TOILET_360PHOTO'          //  360度画像へのリンク（TemplateParts_360photo）
                     + "</div>\n"
                     + 'TOILET_DESCRIBE'          // トイレの説明（階数など）（TemplateParts_360photo）
                     + 'TOILET_SUMMERY'　         // トイレ説明（TemplateParts_Summry）
//                     + 'TOILET_ROUTE_SEARCH'
                     + "</div>\n";

//  ホテル用ポップアップテンプレート
TemplatePopup_Hotel = '<div class="leaflet-popup-content" style="width: 266px;">'
                     + 'HOTEL_NAME'              // トイレ名称（TemplateParts_Name）
                     + 'HOTEL_PHOTO1'            //  画像（TemplateParts_PhotoL ）
                     + 'HOTEL_PHOTO2'            //  画像（TemplateParts_PhotoL ）
                     + '<table class="popup-item">'
                     + 'HOTEL_TEL'
                     + 'HOTEL_ADDRESS' 
                     + 'HOTEL_ACCESS'
                     + 'HOTEL_SUMMERY'
                     + 'HOTEL_URL'
                     + '</table>'
                     + 'HOTEL_DESC_BTN'          // 詳細情報ボタン
                     + "</div>\n";

//差し替えパラメータ



//  TOILET_ROUTE_SEARCH :ルート検索ボタン

//  おすすめルート上の施設ポップアップ
TemplatePopup_POI = '<div class="leaflet-popup-content" style="width: 266px;">'
                  + 'POI_NAME'           //  地点名所湯
                  + 'POI_BLOCK'          //  画像/説明ブロック(TemplatePopup_BLOCK）
                  + 'POI_ITEMS'          //  詳細情報テーブル(TemplatePopup_ITEMS)
//                  + 'POI_ROUTE_SEARCH'   //  ルート検索ボタン
                  + "<div>\n";

//  画像/説明ブロック
TemplatePopup_BLOCK = '<div class="clearfix">'
                    + 'POI_PHOTO1'         //  画像
                    + 'POI_PHOTO2'         //  画像
                    + 'POI_SUMMERY'       //  説明
                    + 'POI_REMARKS'  　   //  備考
                    + "</div>\n";

//  詳細情報テーブル
TemplatePopup_ITEMS = '<table class="popup-item">'
                    + 'POI_OPENINGTIME'    //  営業時間
                    + 'POI_OPENINGNOTE'    //  営業時間補足
                    + 'POI_HOLIDAY'        //  休日
                    + 'POI_PRICE'          //  入場料金
                    + 'POI_PRICE_NOTE'     //  入場料金補足
                    + 'POI_PRICE_DISCOUNT' //  入場料金割引
                    + 'POI_TEL'     　     //  電話番号
                    + 'POI_FAX'     　     //  FAX番号
                    + 'POI_LINK'     　    //  リンク
                    + "</table>\n";     

//  地点情報用ポップアップテンプレート（注意／警告／バス停／スタート／ゴール）
TemplatePopup_Info = '<div class="leaflet-popup-content" style="width: 266px;">'
                + 'INFO_NAME'              //  地点名称
                + 'INFO_SUMMERY'           //  地点説明（TemplateParts_Summry）
                + 'INFO_PHOTO1'            //  地点画像１（TemplateParts_PhotoL ）
                + 'INFO_PHOTO2'            //  地点画像２（TemplateParts_PhotoL ）
                + 'INFO_DESCRIBE'　　　　  //  詳細説明（Remarks用予備）　　　
                + 'INFO_URL'     　　　　  //  詳細説明（Remarks用予備）　　　
//                + 'INFO_ROUTE_SEARCH'      //  ルート検索ボタン
                + "</div>\n";

//  エリア情報用ポップアップテンプレート（注意／警告／バス停／スタート／ゴール）
TemplatePopup_Area = '<div class="leaflet-popup-content" style="width: 266px;">'
                + 'AREA_NAME'              //  エリア名称
                + 'AREA_SUMMERY'           //  エリア説明
                + 'AREA_PHOTO1'            //  エリア画像１（TemplateParts_PhotoL ）
                + 'AREA_PHOTO2'            //  地点画像２（TemplateParts_PhotoL ）
                + 'AREA_DESCRIBE'　　　　  //  詳細説明（Remarks用予備）　　　
                + "</div>\n";

////
//  テンプレート部品
////
//  名称
TemplateParts_Name     = '<h3 class="popup-title">POPUP_NAME</h3>';
//  サマリ（説明）表示
TemplateParts_Summery  = '<p class="popup-note">POPUP_SUMMERY</p>';
//  トイレサマリ（説明）表示
TemplateParts_ToiletSummery  = '<p>POPUP_SUMMERY</p>';
//  トイレアイコン
TemplateParts_PropIcon  = '<div class="wcicon">POPUP_TOILET_PROP_ICON</div>';
//  トイレ360画像
TemplateParts_360photo  = '<div class="wc360">POPUP_TOILET_360PHOTO</div>';
//  補足表示
TemplateParts_Remarks  = '<p class="popup-note">POPUP_REMARKS</p>';
//  階数表示
TemplateParts_Floor    = '<p>階数：　POPUP_FLOOR_LEVEL</p>';
//  URL
TemplateParts_URL      = '<p>リンク：<a href="POPUP_URLLINK" target="_brank">POPUP_URLTITLE</a>';
//  URLHOTEL
TemplateParts_HotelURL = '<p>リンク：<a href="POPUP_URLLINK" target="_brank">ホテル公式サイトへ</a>';
//  写真部品（標準）
TemplateParts_PhotoL   = '<div class="popup-photo"><img src="POPUP_PHOTO" width="265" height="176"></div>';
//  写真部品（施設）
TemplateParts_PhotoS   = '<div class="popup-photo_shisetu"><img src="POPUP_PHOTO"></div>';
//  写真部品（ホテル）
TemplateParts_PhotoH   = '<div class="popup-photo"><img src="POPUP_PHOTO" width="210" height="140"></div>';
//  URLF21
TemplateParts_HOTELDESC= '<a href="POPUP_URLDESC" class="popup-btn link_blank" target="_brank">バリアフリー情報へ</a>';

//  施設詳細情報
TemplateParts_Link     = '<a href="POPUP_URLLINK" target="_brank">POPUP_URLTITLE</a>';

TemplateItem_OpeningTime = '<tr><th>営業時間：</th><td>POPUP_OPENING_TIME</td></tr>';
TemplateItem_OpeningNote = '<tr><th>※補足</th><td>POPUP_OPENING_NOTE</td></tr>';
TemplateItem_Holiday  = '<tr><th>定休日：</th><td>POPUP_HOLIDAY</td></tr>';
TemplateItem_Price    = '<tr><th>入場料金：</th><td>POPUP_PRICE</td></tr>';
TemplateItem_PriceNote= '<tr><th>※補足</th><td>POPUP_PRICE_NOTE</td></tr>';
TemplateItem_PriceDiscount= '<tr><th>[障]手帳割引：</th><td>POPUP_DISCOUNT</td></tr>';
TemplateItem_TEL      = '<tr><th>電話番号：</th><td>POPUP_TEL</td></tr>';
TemplateItem_FAX      = '<tr><th>ＦＡＸ：</th><td>POPUP_FAX</td></tr>';
TemplateItem_Address  = '<tr><th>住所：</th><td>POPUP_ADDRESS</td></tr>';
TemplateItem_Access   = '<tr><th>アクセス：</th><td>POPUP_ACCESS</td></tr>';
TemplateItem_URL      = '<tr><th>リンク：</th><td>POPUP_LINK</td></tr>';

////
//  TOILET_PROPATY_ICON で利用
////
//  トイレ機能アイコン
TemplateParts_WC_Icon  = '<img src="POPUP_WC_ICON">';

////
//  TOILET_360PHOTO で利用
////
//  ３６０度画像リンク表示
TemplateParts_360Photo = '<div class="wc360"><a href="POPUP_360PHOTO" target="_blank">360°写真</a></div>';

//  ルート検索
TemplateParts_RouteSearch = '<form name="routeSearch"><input class="popup-btn" type="button" name="route" value="車椅子でここに行く" onclick="SearchWheelChairRoute( SEARCH_GEOMETRY_POINT )"></form>'

TemplateParts_DemoSearch= '<form name="routeDemo"><input class="popup-btn" type="button" name="XX" value="ルート検索デモ" onclick="SearchWheelChairRouteDemo( SEARCH_GEOMETRY_POINT )"></form>'  

////////
//  ポップアップ制御関数
////////
function checkProp( item ){
    if ( item == undefined ){
	return false;
    }
    if( item == null ){
	return false;
    }
    if( item == "" ){
	return false;
    }
    return true;
}

		
////
// Popup for WC
// 多目的トイレ
function onEachFeatureWC(feature, layer) {
    popupContent = setPopupContentWC(feature);
    layer.bindPopup(popupContent);
}

//  PopupContent for the WC
function setPopupContentWC(feature){ 
    //  console.log( "setPopupContentWC()" );
    var popupContent = TemplatePopup_Toilet 
    var popupParts = "" ;
    
    if ( feature.properties ){
	//  Name
	if ( feature.properties.Name !== undefined ){
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , feature.properties.Name );
	}else{
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , "No Name" );
	}
	popupContent = popupContent.replace("TOILET_NAME", popupParts );
	
	//  Summery
	if ( feature.properties.Summery !== undefined ){
	    popupParts = TemplateParts_ToiletSummery.replace( "POPUP_SUMMERY" , feature.properties.Summery );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("TOILET_SUMMERY", popupParts );
	
	//  Photo1
	if (( feature.properties.Photo1 !== undefined )&&( feature.properties.Photo1 !== "" )){
	    popupParts = TemplateParts_PhotoL.replace("POPUP_PHOTO", feature.properties.Photo1 );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("TOILET_PHOTO1", popupParts );
	//  Photo2
	if (( feature.properties.Photo2 !== undefined )&&( feature.properties.Photo2 !== "" )){
	    popupParts = TemplateParts_PhotoL.replace("POPUP_PHOTO", feature.properties.Photo2 );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("TOILET_PHOTO2", popupParts );
	
	//  Toilet Property Icon 
	popupParts = "";
	if ( feature.properties.Babyseat === true ){
	    popupParts += TemplateParts_WC_Icon.replace( "POPUP_WC_ICON", IconToiletBabyseat );
	}
	if ( feature.properties.Ostomate === true ){
	    popupParts += TemplateParts_WC_Icon.replace( "POPUP_WC_ICON", IconToiletOstomate );
	}
	if ( feature.properties.Nursingbed === true ){
	    popupParts += TemplateParts_WC_Icon.replace( "POPUP_WC_ICON", IconToiletNursingbed );
	}
	if ( feature.properties.Washlet === true ){
	    popupParts += TemplateParts_WC_Icon.replace( "POPUP_WC_ICON", IconToiletWashlet );
	}
	if ( feature.properties.Rotation === true ){
	    popupParts += TemplateParts_WC_Icon.replace( "POPUP_WC_ICON", IconToiletRotation  );
	}
	if ( feature.properties.Emergencycall === true ){
	    popupParts += TemplateParts_WC_Icon.replace( "POPUP_WC_ICON", IconToiletEmergencycall );
	}
	popupContent = popupContent.replace("TOILET_PROP_ICON",
                                            TemplateParts_PropIcon.replace("POPUP_TOILET_PROP_ICON", popupParts ));  
    
	  //  Toilet 360 Photo
    if (( feature.properties.Photo360 !== undefined ) && ( feature.properties.Photo360 != "" )){
      popupParts = TemplateParts_360Photo.replace( "POPUP_360PHOTO", feature.properties.Photo360 );
	  }else{
      popupParts = "";
    }
    popupContent =  popupContent.replace("TOILET_360PHOTO", popupParts );

	  //  Toilet Describe
		var popupDescribe = "";
    //  FLOOR
    if (( feature.properties.Floor !== undefined ) && ( feature.properties.Floor != "" )){
	    popupDescribe += TemplateParts_Floor.replace( "POPUP_FLOOR_LEVEL" , feature.properties.Floor );
	  }
    popupContent = popupContent.replace("TOILET_DESCRIBE", popupDescribe );

    //  RouteSearch
    var popupRouteSearch = "";
    popupRouteSearch += TemplateParts_RouteSearch.replace( "SERARH_GEOMETRY_POINT", feature.geometry.coordinates  );
    //popupRouteSearch += TemplateParts_DemoSearch.replace( "SERARH_GEOMETRY_POINT", feature.geometry.coordinates  );
    popupContent = popupContent.replace("TOILET_ROUTE_SEARCH", popupRouteSearch );
    }else{
	  popupContent = '<h3>No Data</h3><hr class="full"><p>Sorry</p>';
    }

//  console.log( popupContent );
    return( popupContent );
} 

//  PopupContent for the HOTEL
function onEachFeatureHotel(feature, layer) {
    popupContent = setPopupContentHotel(feature);
    layer.bindPopup(popupContent);
}

//  PopupContent for the HOTEL
function setPopupContentHotel(feature){
    var popupContent = TemplatePopup_Hotel
    var popupParts = "" ;
    
    if ( feature.properties ){
	//  Name
	if ( feature.properties.Name !== undefined ){
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , feature.properties.Name );
	}else{
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , "No Name" );
	}
	popupContent = popupContent.replace("HOTEL_NAME", popupParts );
	
	//  Photo1
	if (( feature.properties.Photo1 !== undefined )&&( feature.properties.Photo1 != "" )){
	    popupParts = TemplateParts_PhotoH.replace("POPUP_PHOTO", feature.properties.Photo1 );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("HOTEL_PHOTO1", popupParts );
	
	//  Photo2
	if (( feature.properties.Photo2 !== undefined )&&( feature.properties.Photo2 != "" )){
	    popupParts = TemplateParts_PhotoL.replace("POPUP_PHOTO", feature.properties.Photo2 );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("HOTEL_PHOTO2", popupParts );
	
	//  Summery
	if (( feature.properties.Summery !== undefined )&&( feature.properties.Summery != "" )){
	    popupParts = TemplateParts_Summery.replace( "POPUP_SUMMERY" , feature.properties.Summery );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("HOTEL_SUMMERY", popupParts );
	
	// TEL
	if ((feature.properties.TEL !== undefined ) && (feature.properties.TEL !== "" ) ){
	    popupParts = TemplateItem_TEL.replace( "POPUP_TEL" , feature.properties.TEL );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("HOTEL_TEL", popupParts );
	
	// ADDRESS
	if ((feature.properties.Address !== undefined ) && (feature.properties.Address !== "" ) ){
	    popupParts = TemplateItem_Address.replace( "POPUP_ADDRESS" , feature.properties.Address  );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("HOTEL_ADDRESS", popupParts );
	
	// ACCESS
	if ((feature.properties.Access !== undefined ) && (feature.properties.Access !== "" ) ){
	    popupParts = TemplateItem_Access.replace( "POPUP_ACCESS" , feature.properties.Access  );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("HOTEL_ACCESS", popupParts );
	
	// HOTEL_URL
	//  URL
	if (( feature.properties.URL !== undefined )&&( feature.properties.URL != "" )){
	    popupParts = TemplateParts_Link.replace( "POPUP_URLLINK" , feature.properties.URL );
	    if (( feature.properties.Urltitle !== undefined )&&( feature.properties.Urltitle !== null )
		&&( feature.properties.Urltitle != "" )){
		popupParts = popupParts.replace( "POPUP_URLTITLE" , feature.properties.Urltitle );
	    }else{
		popupParts = popupParts.replace( "POPUP_URLTITLE" , "ホテルの公式サイトへ" );
	    }
	    popupParts = TemplateItem_URL.replace( "POPUP_LINK" , popupParts );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("HOTEL_URL", popupParts );
	
	// TemplateParts_HOTELDESC
	if ((feature.properties.URL_f21 !== null ) && (feature.properties.URL_f21 !== "" ) ){
	    popupParts = TemplateParts_HOTELDESC.replace( "POPUP_URLDESC" , feature.properties.URL_f21 );
	}
	popupContent = popupContent.replace("HOTEL_DESC_BTN", popupParts );
    }else{
	popupContent = '<h3>No Data</h3><hr class="full"><p>Sorry</p>';
    }
    //console.log( popupContent );
    return( popupContent );
}


////
//  Popup for POI (except WC/Info)
function onEachFeaturePOI(feature, layer) {
  var popupContent = '';
  if( ( feature.properties ) && ( feature.properties.Sort != null )){
    switch( feature.properties.Sort ){
	    case "caution" :
	    case "attention" :
	    case "busstop" :
/*	    case "location" :*/
	    case "start" :
	    case "start_op" :
	    case "goal" : 
	    case "goal_op" : 
	    case "barrguide" :
	    case "roadguide" :
        popupContent = setPopupContentInfo(feature, layer);
		    break;
	    default:
        popupContent = setPopupContentPOI(feature, layer);
		    break;
	  }
  }else{
	  popupContent = '<h3>No Data</h3><hr class="full"><p>Sorry</p>';
  }

//  console.log( "popupContent: "+popupContent );

  //window.alert (popupContent);
  layer.bindPopup(popupContent);
}
 
//  PopupContent for the Information 
function setPopupContentInfo(feature, layer) {
//  console.log( "setPopupContentInfo()" );
    var popupContent=TemplatePopup_Info ;
    var popupParts = "" ;

  //  Place Name
    if ( feature.properties ){
	//  Name
	if (( feature.properties.Name !== undefined )&&( feature.properties.Name != "" )){
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , feature.properties.Name );
	}else{
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , "No Name" );
	}
	popupContent = popupContent.replace("INFO_NAME", popupParts );
	
	  //  Summery
	if (( feature.properties.Summery !== undefined )&&( feature.properties.Summery != "" )){
	    popupParts = TemplateParts_Summery.replace( "POPUP_SUMMERY" , feature.properties.Summery );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("INFO_SUMMERY", popupParts );
	
	//  Photo Image (1)
	if (( feature.properties.Photo1 !== undefined )&&( feature.properties.Photo1 != "" )){
	    popupParts = TemplateParts_PhotoL.replace("POPUP_PHOTO", feature.properties.Photo1 );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("INFO_PHOTO1", popupParts );
	//  Photo Image (2)
	if (( feature.properties.Photo2 !== undefined )&&( feature.properties.Photo2 != "" )){
	    popupParts = TemplateParts_PhotoL.replace("POPUP_PHOTO", feature.properties.Photo2 );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("INFO_PHOTO2", popupParts );
	
	//  Remarks
	if (( feature.properties.Remarks !== undefined )&&( feature.properties.Remarks != "" )){
	    popupParts = TemplateParts_Remarks.replace( "POPUP_REMARKS" , feature.properties.Remarks );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("INFO_DESCRIBE", popupParts );
	
	//  URL
	if (( feature.properties.URL !== undefined )&&( feature.properties.URL != "" )){
	    popupParts = TemplateParts_Link.replace( "POPUP_URLLINK" , feature.properties.URL );
	    if (( feature.properties.Urltitle !== undefined )&&( feature.properties.Urltitle != "" )){
		popupParts = popupParts.replace( "POPUP_URLTITLE" , feature.properties.Urltitle );
	    }else{
		popupParts = popupParts.replace( "POPUP_URLTITLE" , feature.properties.URL );
	    }
	    popupParts = TemplateItem_URL.replace( "POPUP_LINK" , popupParts );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("INFO_URL", popupParts );
	
	//  RouteSearch
	popupParts = TemplateParts_RouteSearch.replace( "SERARH_GEOMETRY_POINT", feature.geometry.coordinates  );
	// popupParts += TemplateParts_DemoSearch.replace( "SERARH_GEOMETRY_POINT", feature.geometry.coordinates  );
	popupContent = popupContent.replace("INFO_ROUTE_SEARCH", popupParts );
    }
    
//  console.log( "kokoInfo : "+ popupContent );
  return( popupContent );
}

//  PopupContent for the POI
//  ルート上地点のポップアップ内容
function setPopupContentPOI(feature, layer) {
//  console.log( "setPopupContentPOI()" );

    var popupContent=TemplatePopup_POI ;
    var popupParts = "" ;
    var popupBlock = "" ;

    //  Place Name
    if ( feature.properties ){
	//  Name
	if ( feature.properties.Name !== undefined ){
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , feature.properties.Name );
	}else{
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , "No Name" );
	}
	popupContent = popupContent.replace("POI_NAME", popupParts );
	
	//  Block
	var popupBlock = TemplatePopup_BLOCK;
	{
	    //  Summery
	    if ( checkProp( feature.properties.Summery ) ){
		popupParts = TemplateParts_Summery.replace( "POPUP_SUMMERY" , feature.properties.Summery );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_SUMMERY", popupParts );
	    //  Remarks
	    if ( checkProp( feature.properties.Remarks ) ){
		popupParts = TemplateParts_Remarks.replace( "POPUP_REMARKS" , feature.properties.Remarks );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_REMARKS", popupParts );
	    //  Photo1
	    //if (( feature.properties.Photo1 !== undefined )&&( feature.properties.Photo1 != "" )){
	    if ( checkProp( feature.properties.Photo1 ) ){
		popupParts = TemplateParts_PhotoS.replace("POPUP_PHOTO", feature.properties.Photo1 );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_PHOTO1", popupParts );
	    //  Photo2
	    //if (( feature.properties.Photo2 !== undefined )&&( feature.properties.Photo2 != "" )){
	    if ( checkProp( feature.properties.Photo2 ) ){
		popupParts = TemplateParts_PhotoS.replace("POPUP_PHOTO", feature.properties.Photo2 );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_PHOTO2", popupParts );
	}
	popupContent = popupContent.replace("POI_BLOCK", popupBlock );
	    
	//  Item Table
	popupBlock = TemplatePopup_ITEMS;
	{
	    // Opening times
	    if (( feature.properties.Open !== undefined ) && (feature.properties.Open !== "" )  ){    		
		if (( feature.properties.Close !== undefined ) && (feature.properties.Close !== "" ) ){    		
		    popupParts = TemplateItem_OpeningTime.replace( "POPUP_OPENING_TIME" , 
								   feature.properties.Open + "～" + feature.properties.Close );
		}else{
		    popupParts = TemplateItem_OpeningTime.replace( "POPUP_OPENING_TIME" , feature.properties.Open  );
		}
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_OPENINGTIME", popupParts );
	    
	    // Opening Note
	    if ((feature.properties.OpeningNote !== undefined ) && (feature.properties.OpeningNote !== "" ) ){    		
		popupParts = TemplateItem_OpeningNote.replace( "POPUP_OPENING_NOTE", feature.properties.OpeningNote  );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_OPENINGNOTE", popupParts );
	    
	    // Holiday
	    if ((feature.properties.Holiday !== undefined ) && (feature.properties.Holiday !== "" ) ){    		
		popupParts = TemplateItem_Holiday.replace( "POPUP_HOLIDAY" , feature.properties.Holiday  );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_HOLIDAY", popupParts );
	    
	    // Price
	    if ((feature.properties.Price !== undefined ) && (feature.properties.Price !== "" ) ){    		
		popupParts = TemplateItem_Price.replace( "POPUP_PRICE" , feature.properties.Price );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_PRICE", popupParts );

	    // Price Note
	    if ((feature.properties.PriceNote !== undefined ) && (feature.properties.PriceNote !== "" ) ){    		
		popupParts = TemplateItem_PriceNote.replace( "POPUP_PRICE_NOTE" , feature.properties.PriceNote );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_PRICE_NOTE", popupParts );
	    
	    // Price Discount
	    if ((feature.properties.Discount !== undefined ) && (feature.properties.Discount !== "" ) ){    		
		popupParts = TemplateItem_PriceDiscount.replace( "POPUP_DISCOUNT" , feature.properties.Discount );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_PRICE_DISCOUNT", popupParts );
	    
	    // TEL
	    if ((feature.properties.TEL !== undefined ) && (feature.properties.TEL !== "" ) ){    		
		popupParts = TemplateItem_TEL.replace( "POPUP_TEL" , feature.properties.TEL  );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_TEL", popupParts );
	    
	    // FAX
	    if ((feature.properties.FAX !== undefined ) && (feature.properties.FAX !== "" ) ){    		
		popupParts = TemplateItem_FAX.replace( "POPUP_FAX" , feature.properties.FAX  );
	    }else{
		popupParts = "";
	    }
	    popupBlock = popupBlock.replace("POI_FAX", popupParts );
	    
	    // LINK
	    if ((feature.properties.URL !== undefined ) && (feature.properties.URL !== "" ) ){    		
		popupParts = TemplateParts_Link.replace( "POPUP_URLLINK" , feature.properties.URL );
		if (( feature.properties.Urltitle !== undefined )&&( feature.properties.Urltitle != "" )){
		    popupParts = popupParts.replace( "POPUP_URLTITLE" , feature.properties.Urltitle );
		}else{
		    popupParts = popupParts.replace( "POPUP_URLTITLE" , feature.properties.URL );
		}
		popupParts = TemplateItem_URL.replace( "POPUP_LINK" , popupParts );
	    }else{
		popup = "";
	    }
	    popupBlock = popupBlock.replace("POI_LINK", popupParts );
	}
	popupContent = popupContent.replace("POI_ITEMS", popupBlock );
	
	//  RouteSearch
	popupParts = TemplateParts_RouteSearch.replace( "SERARH_GEOMETRY_POINT", feature.geometry.coordinates  );
	//popupParts += TemplateParts_DemoSearch.replace( "SERARH_GEOMETRY_POINT", feature.geometry.coordinates  );
	popupContent = popupContent.replace("POI_ROUTE_SEARCH", popupParts );
    }
    
    //  console.log( "kokoPOI; "+ popupContent );
    return( popupContent );
}

//  エリアポップアップ
function onEachFeaturePass(feature, layer) {
    popupContent = setPopupContentPass(feature);
    layer.bindPopup(popupContent);
}

function setPopupContentPass(feature){
//  console.log( "setPopupContentInfo()" );
    var popupContent=TemplatePopup_Area ;
    var popupParts = "" ;

    //  Place Name
    if ( feature.properties ){
	//  Name
	if ( feature.properties.Name !== undefined ){
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , feature.properties.Name );
	}else{
	    popupParts = TemplateParts_Name.replace( "POPUP_NAME" , "No Name" );
	}
	popupContent = popupContent.replace("AREA_NAME", popupParts );
	
	//  Summery
	if ( feature.properties.Summery !== undefined ){
	    popupParts = TemplateParts_Summery.replace( "POPUP_SUMMERY" , feature.properties.Summery );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("AREA_SUMMERY", popupParts );
	
	//  Photo Image
	//  Photo1
	if (( feature.properties.Photo1 !== undefined )&&( feature.properties.Photo1 != "" )){
	    popupParts = TemplateParts_PhotoL.replace("POPUP_PHOTO", feature.properties.Photo1 );
	}else{
	    popupParts = "";
	}
	popupContent = popupContent.replace("AREA_PHOTO1", popupParts );
	//  Photo2
	if (( feature.properties.Photo2 !== undefined )&&( feature.properties.Photo2 != "" )){
	  popupParts = TemplateParts_PhotoL.replace("POPUP_PHOTO", feature.properties.Photo2 );
      }else{
	  popupParts = "";
      }
      popupContent = popupContent.replace("AREA_PHOTO2", popupParts );

      //  Remarks
      if ( feature.properties.Remarks !== undefined ){
	  popupParts = TemplateParts_Remarks.replace( "POPUP_REMARKS" , feature.properties.Remarks );
      }else{
	  popupParts = "";
      }
      popupContent = popupContent.replace("AREA_DESCRIBE", popupParts );
  }

//  console.log( "koko AREA; "+ popupContent );
    return( popupContent );
}



////
//  ルートアイコンポップアップ
function onEachSub_SearchRoute(feature) {
  var popupContent = '<div>';
  popupContent += '<form name="routeSearch"><input class="popup-btn" type="button" name="SEARCH" value="車椅子でここに行く" onClick="SearchWheelChairRoute(';
  popupContent += feature.geometry.coordinates ;
  popupContent += ')">';
  popupContent += '&nbsp;<input class="popup-btn" type="button" name="DEL" value="削除" onClick="SearchWheelChairRoute( [999,999] )">';
  if( DEMO == 1 ){
	  popupContent += '&nbsp;<input class="popup-btn" type="button" name="DEMO" value="デモ" onClick="SearchWheelChairRouteDemo(';
	  popupContent += feature.geometry.coordinates ;
	  popupContent += ')"></form>';
  }
  popupContent += '</div>';
    
  return( popupContent );
}





    

