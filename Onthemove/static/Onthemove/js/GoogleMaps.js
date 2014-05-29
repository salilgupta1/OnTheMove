var GoogleMap = (function($){
	var map,
	markers = [];
	var initialize = function(position){
		var coords = new google.maps.LatLng(position.coords.latitude,position.coords.longitude),
		mapOptions = {
			center:coords,
			zoom:13
		},
		mapA = new google.maps.Map(document.getElementById("googleMap"),mapOptions),
		userMarker = new google.maps.Marker({
			position:coords,
			map:mapA
		}),

  input = (document.getElementById('pac-input'));

  var autocomplete = new google.maps.places.Autocomplete(input);
  autocomplete.bindTo('bounds', mapA);

  var infowindow = new google.maps.InfoWindow();
  var marker = new google.maps.Marker({
    map: mapA,
    anchorPoint: new google.maps.Point(0, -29)
  });

  google.maps.event.addListener(autocomplete, 'place_changed', function() {
    infowindow.close();
    marker.setVisible(false);
    var place = autocomplete.getPlace();
    if (!place.geometry) {
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      mapA.fitBounds(place.geometry.viewport);
    } else {
      mapA.setCenter(place.geometry.location);
      mapA.setZoom(13); 
    }
    marker.setIcon(/** @type {google.maps.Icon} */({
      url: place.icon,
      size: new google.maps.Size(71, 71),
      origin: new google.maps.Point(0, 0),
      anchor: new google.maps.Point(17, 34),
      scaledSize: new google.maps.Size(35, 35)
    }));
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);

    var address = '';
    if (place.address_components) {
      address = [
        (place.address_components[0] && place.address_components[0].short_name || ''),
        (place.address_components[1] && place.address_components[1].short_name || ''),
        (place.address_components[2] && place.address_components[2].short_name || '')
      ].join(' ');
    }

    infowindow.setContent('<div><strong>' + place.name + '</strong><br>' + address);
    infowindow.open(mapA, marker);
  });



		infowindowU = new google.maps.InfoWindow({
			content: "<div><strong>You are here!</strong></div>"
		});
		google.maps.event.addListener(userMarker,'click',function(){
			infowindowU.open(mapA,userMarker);
		});
		return mapA;
	},
	addActivities = function(act,loc,map){
		var locl = loc.length;
		for(var i = locl-1;i>=0;i--){
			var aLoc = $.parseJSON(loc[i]);
			var url = "activities/details/"+act[i]['pk'];
			var content_str = "<div>"+act[i]['fields']['activity_name']+"</div><a href="+url+">View Details</a>";

			var infowindow = new google.maps.InfoWindow({content: content_str});
			// infowindow.setContent(content);
			var coods = new google.maps.LatLng(aLoc[0]['fields']['latitude'],aLoc[0]['fields']['longitude']);
			var marker = new google.maps.Marker({
				position:coods,
				map:map
			});
			marker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png');
			google.maps.event.addListener(marker,'click',(function(marker,content,infowindow){ 
        		return function() {
		        	infowindow.open(map,marker);
		        };
   			})(marker,content,infowindow)); 
		}
	};
	return {
		init: function(pos,act,loc){
			var map = initialize(pos);
			addActivities(act,loc,map);
		},
		redrawActivities: function(pos, act, loc) {
			if(map) {
				addActivities(pos, act, loc);
			} else {
				map = initialize(act, loc, map);
			}
		}
	};
}(jQuery));


