// create empty chat object
chat_object = {"done":false};
console.log(chat_object);
var my_function = function(){
	// get the sentence the user typed
	user_input = $("#chat_text").val();
	chat_object["chat_text"] = user_input;
	console.log(chat_object)
	// if we need a field, add it to the chat object
	if ("needs" in chat_object){
		chat_object[chat_object["needs"]] = user_input;
	}
	//make request
	$.get({
		url: "/get_response/",
		data: JSON.stringify(chat_object),
		dataType: 'json',
		method: 'post',
		success:function(data){
			chat_object = data;
			console.log(chat_object);
			$("#mainChat").append("<p>"+chat_object["chat_text"]+"</p>");
			$("#mainChat").append("<p>"+chat_object["response"]+"</p>");
			
			if(data["done"] == 'true'){
				console.log("adding this object");
				chat_object = {"done":false}
			}
		}
	});
	return false;
}