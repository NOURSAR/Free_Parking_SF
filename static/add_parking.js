
// it does not load due to Jquery issues 
function initMap() {
  var mapOptions = {
      center: new google.maps.LatLng(37.77986, -122.42905),
      zoom: 13,
      mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map"), mapOptions);

  //Attach click event handler to the map.
  google.maps.event.addListener(map, 'click', function (e) {

      //Determine the location where the user has clicked.
      var location = e.latLng;

      //Create a marker and placed it on the map.
      var marker = new google.maps.Marker({
          position: location,
          map: map
      });

      let lat = marker.getPosition().lat()
      let lng = marker.getPosition().lng()
      let contentAddress = ""
      let street= ""

      $.ajax({
      method:'POST',
      url:`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&key=AIzaSyDCLPu50m8qU4eQpqj7rm8U7i1gTa-s5TY`,
      success:function(data){
        console.log(data)
        contentAddress = data.results[0].formatted_address
        street = data.results[0].address_components[1].long_name
        console.log(street)
     }
  }) 
      //Attach click event handler to the marker.
      google.maps.event.addListener(marker, "click", function (e) {
          var infoWindow = new google.maps.InfoWindow({
              content: contentAddress + " " + lat + " , "+ lng
          });

          infoWindow.open(map, marker);
          document.getElementById('info_lat').value=lat;
          document.getElementById('info_lng').value=lng;
          document.getElementById('info_address').value=contentAddress;
          document.getElementById('info_street').value=street;


      });
      // document.getElementById('info_lat').value=lat;
      // document.getElementById('info_lng').value=lng;
  });
};
window.initMap = initMap;

// function initMap() {
//        var map = new google.maps.Map(document.getElementById("map"), {
//        zoom: 13,
//        center: { lat:37.77986, lng:-122.42905},
//        mapTypeId: "terrain",
//      });
//      let marker, infoWindow;
//      google.maps.event.addListener(map, 'click', function (event) {
//         var location = event.latLng
//         marker = new google.maps.Marker({
//            position: location,
//            map: map,
//            optimized: false,
//            title: "Parking",
//            draggable: true,
//        });
//        let lat = marker.getPosition().lat();
//        let lng = marker.getPosition().lng();
//        console.log(lat, lng);
//        let contentAdd = ""
//        $.ajax({
//         method:'POST',
//         url:`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&sensor=true&key=AIzaSyDCLPu50m8qU4eQpqj7rm8U7i1gTa-s5TY`,
//         success:function(data){
//             console.log(data)
//             contentAdd = data.results[0].formatted_address
//         }
//     })
//       });
//       google.maps.event.addListener(map, 'click', function(event){
//         infoWindow = new google.maps.InfoWindow({
//           // content: document.getElementById('info').innerText=event.latLng.lat() + " , " + event.latLng.lng()  ,
//           content: event.latLng.lat() + " , " +  event.latLng.lng(),

//        });
//        document.getElementById('info_lat').value=event.latLng.lat();
//        document.getElementById('info_lng').value=event.latLng.lng();

//        infoWindow.open(map, marker);
//       //  let lat, lng;
//       //  google.maps.event.addListener(marker, 'dragend', function(){
//       //     lat = marker.getPosition().lat();
//       //     lng = marker.getPosition().lng();
      
          
//           // $('#lat').val(lat); //Not working why??
//           // $('#lng').val(lng); 
//           // console.log(lat, lng);
//           infoWindow.open(map, marker)
//        });
      
//   //  });
//   //  i started testing radius here//
// //   function arePointsNear(checkPoint, centerPoint, km) {
// //     var ky = 40000 / 360;
// //     var kx = Math.cos(Math.PI * centerPoint.lat / 180.0) * ky;
// //     var dx = Math.abs(centerPoint.lng - checkPoint.lng) * kx;
// //     var dy = Math.abs(centerPoint.lat - checkPoint.lat) * ky;
// //     return Math.sqrt(dx * dx + dy * dy) <= km;
// // }

// // var center = { lat: 37.78291264858861, lng:-122.44278291015624};
// // var stockholm = { lat: 37.7871635357456, lng: 37.7871635357456};
// // console.log(center, stockholm)
// // var n = arePointsNear(center, stockholm, 10);

// // console.log(n);

//  }


// // google.maps.event.addListener(map, 'click', function(event) {
// //   alert("Latitude: " + event.latLng.lat() + " " + ", longitude: " + event.latLng.lng());
// // });

// // console.log(event);
// // google.maps.event.addListener(map, 'click', (event) =>{
// // document.getElementById('info').innerHTML= 'lat: ' + event.latLng.lat() +  'lng: ' + event.latLng.lng();
// // });
// window.initMap = initMap;
