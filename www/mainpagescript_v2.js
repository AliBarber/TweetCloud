var word_list = [];
var word_dictionary = {};
var full_name_lookup = {};

var largest_number = 0;
var smallest_number = 10000;

var cloud_loaded = false;

full_name_lookup['con'] = "<a href=\"https://twitter.com/Conservatives\" target=\"_blank\">Conservatives</a>";
full_name_lookup['lab'] = "<a href=\"https://twitter.com/UKLabour\" target=\"_blank\">Labour</a>";
full_name_lookup['lbd'] = "<a href=\"https://twitter.com/LibDems\" target=\"_blank\">Liberal Democrats</a>";
full_name_lookup['grn'] = "<a href=\"https://twitter.com/TheGreenParty\" target=\"_blank\">Green Party</a>";
full_name_lookup['snp'] = "<a href=\"https://twitter.com/theSNP\" target=\"_blank\">The SNP</a>";
full_name_lookup['ukp'] = "<a href=\"https://twitter.com/UKIP\" target=\"_blank\">UKIP</a>";
// full_name_lookup['me'] =  "<a href=\"https://twitter.com/ali_barber\" target=\"_blank\">Alastair Barber</a>";

var options =
{

// gridSize: Math.round(16 * document.getElementById('wordCanvas').offsetWidth / 800),
hover: function(item,dimension,event){
	if(cloud_loaded)
	{

			
			var div_content = "<span style=\"font-size:28px;\">"+item[0]+"</span><br />Used "+word_dictionary[item[0]][0]+" times<br />"
			+"<table>"
			+"<tr><td>Con:</td><td>"+word_dictionary[item[0]][1]+"</td> <td>Green:</td><td>"+word_dictionary[item[0]][4]+"</td></tr>"
			+"<tr><td>Lab:</td><td>"+word_dictionary[item[0]][2]+"</td> <td>SNP:</td><td>"+word_dictionary[item[0]][5]+"</td></tr>"
			+"<tr><td>LibDem:</td><td>"+word_dictionary[item[0]][3]+"</td> <td>UKIP:</td><td>"+word_dictionary[item[0]][6]+"</td></tr>"
			+"</table>";
			console.log(word_dictionary[item[0]].length);
			if(word_dictionary[item[0]].length > 7)
			{
				// console.log(word_dictionary[item[0]][7]);

				div_content = div_content +"<i>Last tweeted by: </i><b>"+full_name_lookup[word_dictionary[item[0]][7]]+"</b>";
				if(word_dictionary[item[0]].length > 8)
				{
					div_content = div_content +"<br /><i><a href=\"http://twitter.com/statuses/"+word_dictionary[item[0]][8]+"\" target=\"_blank\"><span style=\"font-size:12px;\">"+word_dictionary[item[0]][9]+"</span></a></i>";
				}
			}

			$('#word_info_div').hide();
			$('#word_info_div').css({'top':event.pageY-50,'left':event.pageX});
			$('#word_info_div').html(div_content);
			$('#word_info_div').show();
		}
	}
};

function load_cloud(selection)
{
	// $('#wordCanvas').css("width","100%","height","100%");
	// $('#wordCanvas').width = $('#canvas_div').innerWidth;
	// $('#wordCanvas').height = $('#canvas_div').innerHeight;
	var word_canvas = $('#wordCanvas');
	ctx = word_canvas[0].getContext('2d');
	ctx.canvas.height = $('#canvas_div').innerHeight();
	ctx.canvas.width = $('#canvas_div').innerWidth();
	console.log('canvas height: '+$('#wordCanvas').height);

	var json_path;
	cloud_loaded = false;
	largest_number = 0;
	smallest_number = 10000;
	word_list = [];
	if(selection == 'all') json_path = 'data.json';
	else
	{
		json_path = 'query.php?party='+selection;
	}
	
	$.getJSON(json_path,function(data)
	{
		console.log('success');
		word_count_detail = [];
		word_detail_items = [];
		$.each(data.word_data,function(index,item)
		{
			word_count_detail.push(item.word);
			word_count_detail.push(item.count);
			if(item.count > largest_number)
			{
				largest_number = item.count;
			}
			if(item.count < smallest_number)
			{
				smallest_number = item.count;
			}
			// console.log(item.word);
			word_list.push(word_count_detail);
			word_count_detail = [];

			word_detail_items.push(item.count);
			word_detail_items.push(item.con);
			word_detail_items.push(item.lab);
			word_detail_items.push(item.lbd);
			word_detail_items.push(item.grn);
			word_detail_items.push(item.snp);
			word_detail_items.push(item.ukp);
			if(item.last_tweet_from != null)
			{
				word_detail_items.push(item.last_tweet_from);
				if(item.last_tweet != null)
				{
					word_detail_items.push(item.last_tweet);
					word_detail_items.push(item.last_tweet_text);
				}
			}
			word_dictionary[item.word] = word_detail_items;
			word_detail_items = [];
		});
		// console.log(word_list);
		console.log(smallest_number+","+largest_number);
		$.each(word_list, function(index, value)
		{
			word_list[index][1] = word_list[index][1] - smallest_number + 1;
			word_list[index][1] = (word_list[index][1] / largest_number) * 100;
		});
		options.list = word_list;

			  options.weightFactor = function (size) {
    return Math.pow(size,1.125) * 
document.getElementById('wordCanvas').offsetWidth / 800;
			};

		WordCloud(document.getElementById('wordCanvas'),options);
		cloud_loaded = true;
	}).fail(function( jqxhr, textStatus, error){ var err = textStatus +', '+error; console.log('fail: '+err); cloud_loaded = false;});
}

$( "input" ).on( "click", function() {
  load_cloud($( "input:checked" ).val());
});

$("#right_bar").mouseover(function()
{
		$('#word_info_div').hide();

} );
$("#left_bar").mouseover(function()
{
		$('#word_info_div').hide();

} );
$("#bottom_right").mouseover(function()
{
		$('#word_info_div').hide();

} );
// 	$.each(data,function(key,val)
// 	{
// 		console.log(key);
// 		word_list.push([key,val]);
// 	});
// });

	
//alert(WordCloud.isSupported);
