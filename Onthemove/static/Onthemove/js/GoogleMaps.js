var GoogleMap = (function($){
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
		for(var i = 0;i<act.length;i++){
			var aLoc = $.parseJSON(loc[i]);
			var url = "activities/details/"+act[i]['fields']['location_id'];
			var infowindow = new google.maps.InfoWindow({
				content: "<div>"+act[i]['fields']['activity_name']+"</div><a href="+url+">View Details</a>"
			});
			var coods = new google.maps.LatLng(aLoc[0]['fields']['latitude'],aLoc[0]['fields']['longitude']);
			console.log(map);
			var marker = new google.maps.Marker({
				position:coods,
				map:map
			});
			marker.setIcon('http://maps.google.com/mapfiles/ms/icons/blue-dot.png');
			google.maps.event.addListener(marker,'click',function(){
				infowindow.open(map,marker);
			});	
		}
	};
	return {
		init: function(pos,act,loc){
			var map = initialize(pos);
			addActivities(act,loc,map);
		}
	};
}(jQuery));