var sbArticles = document.getElementById('searchArticles');
var sbComments = document.getElementById('searchComments');

let showsb1 = function() {
	sbArticles.classList.toggle("_active");
	sbComments.classList.remove("_active");
}

let showsb2 = function() {
	sbComments.classList.toggle("_active");
	sbArticles.classList.remove("_active");
}