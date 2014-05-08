function initialize(position){
  var coords = new google.maps.LatLng(position.coords.latitude,position.coords.longitude),
  mapOptions = {
    center:coords,
    zoom:13
  },
  activityMap = new google.maps.Map(document.getElementById("googleMap"),mapOptions),
  userMarker = new google.maps.Marker({
    position:coords,
    map:activityMap,
    title:"You are here!",
  }),
  infowindow = new google.maps.InfoWindow({
    content: "You are here!"
  });
  google.maps.event.addListener(userMarker,'click',function(){
    infowindow.open(activityMap,userMarker);
  });
  addActivities(activityMap);
}
// change later to get all activities close to user
function addActivities(map){
  var infowindow = new google.maps.InfoWindow({
    content: "<div>Tennis Activity</div><a href='activities/details'>View Details</a>"
  });
  var coods = new google.maps.LatLng(42.059647, -87.677517);
  var marker = new google.maps.Marker({
    position:coods,
    map:map,
    title:"Tennis Court",
  });
  marker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png')
  google.maps.event.addListener(marker,'click',function(){
    infowindow.open(map,marker);
  });
}

$(document).ready(function(){
  if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(initialize);
  }
  else{
    error('Geo location is not supported');
  }
});