$(document).ready(function(){
	
	comments_update ();	
	
	function comments_update () {
		var tmp = (location.href).split('/');
		$.ajax({			
			url: "/updatecomments/" + tmp[tmp.length - 1],
			type: "get",
			success: renderCommentsList
		});		
	}
	
	function renderCommentsList (data) {
		$("#comments_list_block").empty();
		var commentTemplate = $('#comment_tmpl').template(data).appendTo("#comments_list_block");		
		setTimeout(comments_update, 5000)		
	}
	
	$(".add_comment_form").on({click: function (e) {
		e.preventDefault();
		var formData = make_dict($(".add_comment_form").serialize());
		var currentUrl = (location.href).split('/');
		$.ajax ({
			url: "/addcomment/" + currentUrl[currentUrl.length - 1],
			data: formData,
			type: "post",
			success: renderCommentsList
		});
		
	}}, "#add_comment_button");
	
	function make_dict(data) {
		console.log(data);
		var lst_tmp = data.split("&");
		var dict = {};
		for (var i in lst_tmp)
		{
			var tmp = lst_tmp[i].split("=");
			dict[tmp[0]] = decodeURIComponent(tmp[1]);
		}
		return dict;
	}
	
});