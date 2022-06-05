coords=JSON.parse(coords)

// const latlng= {lat:37.7765572, lng:-122.4178417}
// // const ll= { lat: 37.7763661, lng: -122.419587}
// const latln= {lat:37.7763853, lng:-122.4194349}
// const l= { lat: 37.7765628, lng:-122.4179689}
// const n= {lng:-122.417533, lat: 37.7765378}
// const m = {lng: -122.4194349, lat: 37.7763853}
// const k = {lng: -122.419618, lat: 37.7773095}
// console.log(latlng)
let map;
 function initMap() {
    // const location =  { lat:37.77986, lng:-122.42905};
    //     map = new google.maps.Map(document.getElementById("map"), {
    //     zoom: 13,
    //     center: location,
    // });
        map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: { lat:37.77986, lng:-122.42905},
        mapTypeId: "terrain",
      });
    const poly =[]
    for (var i=0; i<coords.length; i++){
            var lng = coords[i][0]
            var lat = coords[i][1]
            var latlng = {lat: lat, lng: lng}
            poly.push(latlng)
            // console.log(latlng)
            line = new google.maps.Polyline({
            path: poly,
            geodesic: true,
            strokeColor: "#" + Math.floor(Math.random()*16777215).toString(16),
            strokeOpacity: 1.0,
            strokeWeight: 2,
            });   
            line.setMap(map);         
        }
        console.log(poly)

     
}
 
window.initMap = initMap;
// fell street

// [[-122.4194349, 37.7763853], [-122.4179689, 37.7765628],
// [-122.4179054, 37.7765649], [-122.4178417, 37.7765572],
//  [-122.417533, 37.7765378]],
// [-122.4194349, 37.7763853],[-122.419618, 37.7773095]]