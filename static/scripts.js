$(document).ready(function(){
    $('#btnL1On').click(function(){

		$.ajax({
			type: 'L1On',
			url: '/ProcessL1On',
			success: function(data){
				alert(data);
			}			
		});
	});
});

$(document).ready(function(){
	$('#btnL1Off').click(function(){

		$.ajax({
			type: 'L1Off',
			url: '/ProcessL1Off',
			success: function(data){
				alert(data);
			}
		});
	});
});
	
$(document).ready(function(){
	$('#btnL2On').click(function(){

		$.ajax({
			type: 'L2On',
			url: '/ProcessL2On',
			success: function(data){
				alert(data);
			}
		});
	});
});

$(document).ready(function(){
	$('#btnL2Off').click(function(){

		$.ajax({
			type: 'L2Off',
			url: '/ProcessL2Off',
			success: function(data){
				alert(data);
			}
		});
	});
});

$(document).ready(function(){
	$('#btnOFF').click(function(){

		$.ajax({
			type: 'SLEEP',
			url: '/ProcessSLEEP',
			success: function(data){
				alert(data);
			}
		});
	});
});

$(document).ready(function(){	
	$('#btnWAKE').click(function(){

		$.ajax({
			type: 'WAKE',
			url: '/ProcessWAKE',
			success: function(data){
				alert(data);
			}
		});
	});
});  