<?php
	$datafile = fopen("data.json","r") or die("Couldn't open resource file.");
	$json_string = fread($datafile,filesize("data.json"));
	fclose($datafile);

	$data_obj = json_decode($json_string,true);
	//var_dump($data_obj['word_data'][0]['word']);
	
	$party_search = $_GET['party'];

	$output_array = array();
	
	echo("{\"word_data\" : [ ");
	$first_time = true;

	foreach ($data_obj['word_data'] as $word_item) {
		if($word_item[$party_search] > 0)
		{
			if(!$first_time)
			{
				echo(",");
			}
			else
			{
				$first_time = false;
			}
			$word_item['count'] = $word_item[$party_search];
			
			echo(json_encode($word_item));
			//echo("{\"word\" : \"".$word_item['word']."\",\"count\":".$word_item['count'].",\"con\":".$word_item['con'].",\"lab\":".$word_item['lab'].",\"lbd\":".$word_item['lbd'].",\"grn\":".$word_item['grn'].",\"snp\":".$word_item['snp'].",\"last_tweet\":\"".$word_item['last_tweet']."\"");
			

			// if(array_key_exists('last_tweet_from', $word_item))
			// {
			// 	echo(",\"last_tweet_from\" : \"".$word_item['last_tweet_from']."\"");
			// }
			// if(array_key_exists('last_tweet_text', $word_item))
			// {
			// 	echo(",\"last_tweet_text\" : \"".addslashes($word_item['last_tweet_text'])."\"");
			// }
			// echo("},");
			$output_array[] = $word_item;
			// echo($word_item['word']);
		}
	}
	echo("]}")
	

?>
