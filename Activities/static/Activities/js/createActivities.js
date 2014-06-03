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
					// console.log(response);
					var response_data = JSON.parse(response);
					var business_list = response_data.business_list;
					var lat = response_data.lat;
					var lng = response_data.lng;

					$(".result_item").remove();
					$("#error-message").remove();

					if (business_list != 'No Yelp Results') {
						for (var i = 0; i < business_list.length; i++) {
							var name = business_list[i]["name"];
							var location = business_list[i]["location"];
							var id = business_list[i]["id"];
							$("#result_list").append('<button type="button" value="' + id + '"class="btn result_item list-btn"><li class="list-group-item"> <h5 class="list-group-item-heading">'+ name+'</h5>'+location+'</li></button>');
						};
					}
					else {
						$("#result_list").append('<p id="error-message"> No Yelp results. Please enter location information below. </p>');
					}
					

					$(".result_item").click(function(){
						var choosen_obj = $(this).val();
						data["yelp_name"] = choosen_obj;
						data["lat"] = lat;
						data["lng"] = lng;
						$.ajax({
							type: "POST",
							dataType:"text",
							data:data,
							url:'/activities/fill_in_yelp/',
							success:function(response){
								console.log(response);
								var response_data = JSON.parse(response);
								var name = response_data.business_name,
								address = response_data.address[0],
								city = response_data.city,
								state = response_data.state,
								zipcode = response_data.zipcode;

								$("#location_name").val(name);
								$("#location_address").val(address);
								$("#location_city").val(city);
								$("#location_state").val(state);
								$("#location_zipcode").val(zipcode);

								$("#yelp_label").remove();
								$("#yelp_term").remove();
								$("#yelp_btn").remove();
								$("#result_list").remove();
								$(".result_item").remove();


							},
							error:function(error){
								console.log(error);
							}
						});
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