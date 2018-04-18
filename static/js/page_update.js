$(document).ready(function(){
	
	request_update ();
	
	
	function request_update () {
		$.ajax({
			url: "/updatequestions",
			type: "get",
			success: renderQuestionsList
		});		
	}
	
	function renderQuestionsList (data) {
		$("#qustions_list_block").empty();
		var questionTemplate = $('#question_link_tmpl').template(data).appendTo("#qustions_list_block");		
		setTimeout(request_update, 5000);
		
	}
	
});