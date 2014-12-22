//document.getElementsByClassName("title_wrap fl_l")[43].outerText
//document.getElementsByClassName("play_btn fl_l")[43].getElementsByTagName("input")[0].value

var patt = /https:.*mp3/

for (var i = 0; i < document.getElementsByClassName("title_wrap fl_l").length; i++) {
	linkk = patt.exec(document.getElementsByClassName("play_btn fl_l")[i].getElementsByTagName("input")[0].value)[0]
	namee = document.getElementsByClassName("title_wrap fl_l")[i].outerText
	console.log(linkk, namee)
}
