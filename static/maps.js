let map;
function initMap() {
       map = new google.maps.Map(document.getElementById("map"), {
       zoom: 13,
       center: { lat:37.77986, lng:-122.42905},
       mapTypeId: "terrain",
     });
     let marker, infoWindow;
     google.maps.event.addListener(map, 'click', function (event) {
       marker = new google.maps.Marker({
           position: event.latLng,
           map: map,
           optimized: false,
           title: "map",
           draggable: true,
           content: 'lat:',
       });
       console.log(event.latLng);
      });
      google.maps.event.addListener(map, 'click', function(event){
        infoWindow = new google.maps.InfoWindow({
          content: document.getElementById('info').innerText=event.latLng.lat() + " , " + event.latLng.lng()  ,

       });
       document.getElementById('info_lat').value=event.latLng.lat();
       document.getElementById('info_lng').value=event.latLng.lng();

       infoWindow.open(map, marker);
       let lat, lng;
       google.maps.event.addListener(marker, 'dragend', function(){
          lat = marker.getPosition().lat();
          lng = marker.getPosition().lng();
          
          
          // $('#lat').val(lat); //Not working why??
          // $('#lng').val(lng); 
          console.log(lat, lng);
          infoWindow.open(map, marker)
       });
      
   });
  //  i started testing radius here//
  function arePointsNear(checkPoint, centerPoint, km) {
    var ky = 40000 / 360;
    var kx = Math.cos(Math.PI * centerPoint.lat / 180.0) * ky;
    var dx = Math.abs(centerPoint.lng - checkPoint.lng) * kx;
    var dy = Math.abs(centerPoint.lat - checkPoint.lat) * ky;
    return Math.sqrt(dx * dx + dy * dy) <= km;
}

var vasteras = { lat: 37.78291264858861, lng:-122.44278291015624};
var stockholm = { lat: 37.7871635357456, lng: 37.7871635357456};
console.log(vasteras, stockholm)
var n = arePointsNear(vasteras, stockholm, 10);

console.log(n);

 }


// google.maps.event.addListener(map, 'click', function(event) {
//   alert("Latitude: " + event.latLng.lat() + " " + ", longitude: " + event.latLng.lng());
// });

// console.log(event);
// google.maps.event.addListener(map, 'click', (event) =>{
// document.getElementById('info').innerHTML= 'lat: ' + event.latLng.lat() +  'lng: ' + event.latLng.lng();
// });
window.initMap = initMap;
