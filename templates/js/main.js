function showDiv(number){
	var items = document.getElementById("mainChat").getElementsByTagName("div");
	for (var i = 0; i < items.length; i++){
		items[i].className = (i == number) ? 'shown' : 'hidden';
	}
}
console.log(showDiv);

// var text = ["#startFirst","#startSecond","#startThird","#startFourth"];
// console.log(text);

// var delay = 400;

// function addOneWord(i, j) {
//     $('#console_div').append('<br>' + text[i][j]);
//     if (j+1<text[i].length) {  // next character in the current string
//         setTimeout(function() { addOneChar(i, j+1); }, delay);
//     } else if (i+1<text.length) {   // start the next string in the text[] array
//         setTimeout(function() { addOneChar(i+1, 0); }, delay);
//     } // else quit
// }

// setTimeout(function() { addOneChar(0,0); });