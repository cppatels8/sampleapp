$(document).ready(function(){

	// Can be used to get form data 
	function getFromData(className){
		var data = $(className).serializeArray(),
			formData = {};
		$.map(data, function(x) {
			formData[x.name] = x.value;
		});
		return formData;
	}
	
	function make_url_params(params){
		var url_params = "?";
		$.each( params, function( key, value ) {
			if (value){
				url_params += key + "=" + value+ "&" ;
			}
		});
		return url_params
	}
	
	$('.submit-mp-data').click(function(e) {
		e.preventDefault();
		var url = window.location.origin + '/api/v1/mpattendence/?format=json',
			header = {"content_types": "application/json"},
			data = getFromData('.create-mp-data-form');
		
		var jqXHR = $.ajax({
				url: url,
				method: "POST",
				data: JSON.stringify(data),
				contentType: "application/json",
				success: function(){
					$('#addMpData').modal('hide');
					alert("Success: Added successfuly");
				},
				error: function(jqXHR){
					$('#addMpData').modal('hide');
					alert("Error: " + jqXHR.status);
				}
		});
	});
	
	$('.mp-data-table').DataTable();

	$(".mp-data-table").on('click', ".delete-mp-data", function(e){
		/*
		 * Write code to delete mp data.
		 * Row will be deleted based on id 
		 * */
		var url = window.location.origin + '/api/v1/mpattendence/'+$(this).data("id")+'?format=json';	
		$.ajax({
			url: url,
			method: "DELETE",
			success: function(){
				alert("Success: Delete successfuly");
				location.reload();
			},
			error: function(jqXHR){
				alert("Error: " + jqXHR.status);
			}
		});
	});
	
	$(".edit-mp-data").click( function(e){
		/*
		 * Write code to edit mp data. 
		 * */
	});
	
	$(".filter-results").submit(function(e) {
		e.preventDefault();
		var	header = {"content_types": "application/json"},
			data = getFromData('.filter-results'),
			url_params = make_url_params(data);
		
		location.assign(window.location.origin + url_params);
	});
	
});