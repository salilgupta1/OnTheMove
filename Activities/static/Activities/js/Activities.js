var Activities = (function($){
	var enroll = function(data,path){
		$("#enroll").click(function(){
			$("#loading").show();
			$.ajax({
				type: "POST",
				dataType:"text",
				data:data,
				url:path,
				success:function(response){
					$("#loading").hide();
					$('#enroll-modal').modal('hide');
					$("#enroll-list-group").show();
					$("#enrollSuccess").fadeIn('3000');
					$('#enrollSuccess').delay(3000).fadeOut('3000');
					$('#enroll-btn').hide();
					$('#enrollStatus').html('<p>Your enrollment is pending!</p>');
				},
				error:function(error){
					console.log(error);
				}
			});
		});
	},
	init = function(){
		$("#enroll-list-group").hide();
		$("#loading").hide();
	};
	return {
		enroll:enroll,
		init:init
	};
}(jQuery));