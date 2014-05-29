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
		infowindow = new google.maps.InfoWindow({
			content: "You are here!"
		});
		google.maps.event.addListener(userMarker,'click',function(){
			infowindow.open(mapA,userMarker);
		});
		return mapA;
	},
	addActivities = function(act,loc,map){
		var locl = loc.length;
		for(var i = locl-1;i>=0;i--){
			var aLoc = $.parseJSON(loc[i]);
			var url = "activities/details/"+act[i]['pk'];
			console.log(url);
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
			map = initialize(pos);
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


