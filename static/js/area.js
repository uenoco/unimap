////
//   Project:      IotView
//   Applicattion: IotView
////

//owindow.onload = function () {
//    ;
//}


// is not define 対策
//$(function() {
window.addEventListener('DOMContentLoaded', function(){
  $("table").tablesorter({
      theme: "bootstrap",

      headers: {
	  0: { sorter: true },
	  1: { sorter: true },
	  2: { sorter: false }, //項目名「状態」をスキップ
	  3: { sorter: true },
	  4: { sorter: true },
	  5: { sorter: true },
	  6: { sorter: true },
      },

      widthFixed: true,

      // widget code contained in the jquery.tablesorter.widgets.js file
      // use the zebra stripe widget if you plan on hiding any rows (filter widget)
      // the uitheme widget is NOT REQUIRED!
      widgets: ["filter", "columns", "zebra"],

      widgetOptions: {
        // using the default zebra striping class name, so it actually isn't included in the theme variable above
        // this is ONLY needed for bootstrap theming if you are using the filter widget, because rows are hidden
        zebra: ["even", "odd"],

        // class names added to columns when sorted
        columns: ["primary", "secondary", "tertiary"],

        // reset filters button
        filter_reset: ".reset",

        // extra css class name (string or array) added to the filter element (input or select)
        filter_cssFilter: [
          'form-control',
          'form-control',
          'form-control custom-select', // select needs custom class names :(
          'form-control',
          'form-control',
          'form-control',
          'form-control'
        ]

      }
    })
/*  ページネーションは未対応
    .tablesorterPager({

      // target the pager markup - see the HTML block below
      container: $(".ts-pager"),

      // target the pager page select dropdown - choose a page
      cssGoto: ".pagenum",

      // remove rows from the table to speed up the sort of large tables.
      // setting this to false, only hides the non-visible rows; needed if you plan to add/remove rows with the pager enabled.
      removeRows: false,

      // output string - default is '{page}/{totalPages}';
      // possible variables: {page}, {totalPages}, {filteredPages}, {startRow}, {endRow}, {filteredRows} and {totalRows}
      output: '{startRow} - {endRow} / {filteredRows} ({totalRows})'

    });
*/
    ;
});
