let sbArticles = document.getElementById('searchArticles');
let sbComments = document.getElementById('searchComments');


sbArticles.addEventListener("click", 
	(e) => {
	    e.currentTarget.classList.toggle("_active col-md-3");
});

sbComments.addEventListener("click", 
	(e) => {
	    e.currentTarget.classList.toggle("_active col-md-3");
});

console.log(sbArticles);
console.log(sbComments);

/*
document.body.addEventListener("click", 
    (e) =>{
        console.log("Body clicked");
    }
);*/
