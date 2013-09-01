function listTasksbyClient(data){
	console.log(data);
	output='<ul id="#byClientlistview" data-role="listview" data-filter="true" data-filter-placeholder="Search clients...">';
	$.each(data,function(key, val){
		output+='<li><a href="#showClientTasks" onClick="showTasksbyClient('+key+','+val+');">'+key+'</a></li>';
	});
	output+='</ul><!-- end listview -->';
	output+='</div><!-- end collapsible-set -->';
	
	$('#clientlist').html(output);
	$('#clientlist').trigger('create');
}

function showTasksbyClient(key, val){
    output='<div data-role="collapsible-set">';
    output+='<div data-role="collapsible">';
    output+='<h1>Sample Heading</h1>';
    output+='<ul data-role="listview">';
    output+='<li>'+'task'+'</li>'
    output+='</ul><!-- end listview -->';
    output+='</div><!-- end collapsible -->';
    output+='</div><!-- end collapsible-set -->';
    console.log(key);
    console.log(val);
    $('#clienttaskcontent').html(output);
    $('#clienttaskcontent').trigger('create');
    
}