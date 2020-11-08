let showsb1 = function() {
	let sbArticles = document.getElementById('searchArticles');
	sbArticles.classList.toggle("_active");
	sbComments.classList.remove("_active");
}

let showsb2 = function() {
	let sbComments = document.getElementById('searchComments');
	sbComments.classList.toggle("_active");
	showsb1.sbArticles.classList.remove("_active");
}