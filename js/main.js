const formButton = document.querySelector(".button");
const loading = document.querySelector(".loading");

formButton.addEventListener("click", e => {
	e.preventDefault();
	loading.classList.toggle("active");
});
