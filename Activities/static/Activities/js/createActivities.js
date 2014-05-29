var createActivities = (function($){
	var search_yelp = function(data,path){
		$("#yelp_btn").click(function(){
			var search_term = $("#yelp_term").val();
			data["yelp_term"] = search_term;
			$.ajax({
				type: "POST",
				dataType:"text",
				data:data,
				url:path,
				success:function(response){
					$("#yelp_term").addClass("dropdown-toggle sr-only");
					console.log(response);
					var response_data = JSON.parse(response);
					var business_list = response_data.business_list;
					var lat = response_data.lat;
					var lng = response_data.lng;
					for (var i = 0; i < 5; i++) {
						var name = business_list[i]["name"];
						var location = business_list[i]["location"];
						var id = business_list[i]["id"];
						$("#result_list").append('<li role="presentation"><button type="button" value='+id+' class="btn btn-default result_item">'+ name+' '+location+'</button></li>');
					};

					$(".result_item").click(function(lat,lng){
						var choosen_obj = $(this).val();
						data["yelp_id"] = choosen_obj;
						data["lat"] = lat;
						data["lng"] = lng;
						console.log(path);
						// $.ajax({
						// 	type: "POST",
						// 	dataType:"text",
						// 	data:data,
						// 	url:path,
						// 	success:function(response){
						// 		console.log(response);
						// 	},
						// 	error:function(error){
						// 		console.log(error);
						// 	}
						// });
					});
				},
				error:function(error){
					console.log(error);
				}
			});
		});
	}
	return {
		search_yelp:search_yelp
	}
}(jQuery));