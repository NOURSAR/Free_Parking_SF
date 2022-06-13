
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
           content: document.getElementById('info').innerText= 'lat: ' + event.latLng.lat() +  ' lng: ' + event.latLng.lng(),
       });
       console.log(event.latLng);
      });

       google.maps.event.addListener(map, 'click', function(event){
        infoWindow = new google.maps.InfoWindow({
          content: document.getElementById('info').innerText= 'lat: ' + event.latLng.lat() +  ' lng: ' + event.latLng.lng(),
       });
      infoWindow.open(map, marker);
       let lat, lng;
       google.maps.event.addListener(marker, 'dragend', function(){
          lat = marker.getPosition().lat();
          lng = marker.getPosition().lng();
          
          // $('#lat').val(lat); //Not working why??
          // $('#lng').val(lng); 
          console.log(lat, lng);
       });
      
   });
 }


// google.maps.event.addListener(map, 'click', function(event) {
//   alert("Latitude: " + event.latLng.lat() + " " + ", longitude: " + event.latLng.lng());
// });

// console.log(event);
// google.maps.event.addListener(map, 'click', (event) =>{
// document.getElementById('info').innerHTML= 'lat: ' + event.latLng.lat() +  'lng: ' + event.latLng.lng();
// });
window.initMap = initMap;
