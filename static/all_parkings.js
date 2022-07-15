
allOfMarkers=JSON.parse(allOfMarkers)
console.log(allOfMarkers)

function initMap() {
  var mapOptions = {
        center: new google.maps.LatLng(37.77986, -122.42905),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    //Create and open InfoWindow.
    var infoWindow = new google.maps.InfoWindow();

    for (var i=0; i<allOfMarkers.length;i++){
      var markerObject = allOfMarkers[i]['street'];
      var streetName = markerObject[0];
      var review = markerObject[1];
      var review = markerObject[1];
      var lng = markerObject[3][0];
      var lat = markerObject[3][1];
      var latlng = {lat: lat, lng: lng};
      var address = markerObject[4]
      var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        optimized: false,
        title: address,
        draggable: true,
        content: review,
      });

        //Attach click event to the marker.
        (function (marker, markerObject) {
            google.maps.event.addListener(marker, "click", function (e) {
                infoWindow.setContent( streetName +": "+ marker.content);
                infoWindow.open(map, marker);
            });
        })(marker, markerObject);
    }
}

window.initMap = initMap;