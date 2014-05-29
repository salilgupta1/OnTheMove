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
	}, 
	getLocation = function(data,position,path){
		var coords = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
		var lat = coords['k'],
		lng = coords['A'],
		coords = {};
		coords['lat'] = lat;
		coords['lng'] = lng;
		data['coords'] = coords;
		$.ajax({
			type: "POST",
			dataType:"text",
			data:data,
			url:path,
			success:function(response){
				console.log(response);
			},
			error:function(error){
				console.log('error');
			}
		});
	}
	return {
		init: function(pos,act,loc,data,path){
			var map = initialize(pos);
			addActivities(act,loc,map);
			getLocation(data,pos,path);
		}
	};
}(jQuery));



