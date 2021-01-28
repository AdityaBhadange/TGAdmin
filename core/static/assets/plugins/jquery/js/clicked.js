$(function(){
	$(".checkAll").click(function(){
		if (this.checked) {
			$(".checkboxes").prop("checked", true);
		} else {
			$(".checkboxes").prop("checked", false);
		}
	});
});